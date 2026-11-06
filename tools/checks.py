# /// script
# requires-python = ">=3.12"
# dependencies = ["PyYAML==6.0.3"]
# ///
"""Run the same repository checks locally and in CI: uv run tools/checks.py."""
from __future__ import annotations

import argparse
import hashlib
import io
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tarfile
import tempfile
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
LIBRARY_REVISION = "897e04e963e4e0eb9ba8126adf92faff36dd5d65"
GITLEAKS_VERSION = "8.30.0"
GITLEAKS_HASHES = {
    "darwin_arm64": "b251ab2bcd4cd8ba9e56ff37698c033ebf38582b477d21ebd86586d927cf87e7",
    "darwin_x64": "ca221d012d247080c2f6f61f4b7a83bffa2453806b0c195c795bbe9a8c775ed5",
    "linux_arm64": "b4cbbb6ddf7d1b2a603088cd03a4e3f7ce48ee7fd449b51f7de6ee2906f5fa2f",
    "linux_x64": "79a3ab579b53f71efd634f3aaf7e04a0fa0cf206b7ed434638d1547a2470a66e",
}


def run(*args: str, capture: bool = False) -> str:
    result = subprocess.run(args, cwd=ROOT, check=True, text=True,
                            stdout=subprocess.PIPE if capture else None)
    return result.stdout.strip() if capture else ""


def library_checkout(selected: str | None) -> Path:
    library = (Path(selected).resolve() if selected else
               Path.home() / ".cache/swarm-alignment-checks" / f"chirality-library-{LIBRARY_REVISION}")
    if not library.exists() and not selected:
        library.parent.mkdir(parents=True, exist_ok=True)
        run("git", "clone", "--no-checkout", "https://github.com/sgttomas/chirality-library.git", str(library))
        run("git", "-C", str(library), "checkout", "--detach", LIBRARY_REVISION)
    revision = run("git", "-C", str(library), "rev-parse", "HEAD", capture=True)
    if revision != LIBRARY_REVISION:
        raise ValueError(f"Library must be at {LIBRARY_REVISION}; found {revision}. Omit --library to use the isolated cache.")
    if run("git", "-C", str(library), "status", "--porcelain", "--untracked-files=normal", capture=True):
        raise ValueError("Library checkout has changes; use a clean checkout for reproducible checks.")
    return library


def gitleaks() -> Path:
    arch = {"aarch64": "arm64", "x86_64": "x64", "AMD64": "x64"}.get(platform.machine(), platform.machine())
    target = f"{platform.system().lower()}_{arch}"
    expected = GITLEAKS_HASHES.get(target)
    if not expected:
        raise ValueError(f"Unsupported Gitleaks platform: {target}")
    cache = ROOT / ".cache" / f"gitleaks-{GITLEAKS_VERSION}-{target}"
    cache.mkdir(parents=True, exist_ok=True)
    archive = cache / "release.tar.gz"
    if not archive.exists():
        url = f"https://github.com/gitleaks/gitleaks/releases/download/v{GITLEAKS_VERSION}/gitleaks_{GITLEAKS_VERSION}_{target}.tar.gz"
        with urllib.request.urlopen(url, timeout=60) as response:
            data = response.read()
        if hashlib.sha256(data).hexdigest() != expected:
            raise ValueError("Gitleaks download checksum mismatch")
        archive.write_bytes(data)
    data = archive.read_bytes()
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError("Cached Gitleaks archive checksum mismatch")
    # Extract only the named executable, never archive paths or links.
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as bundle:
        member = bundle.getmember("gitleaks")
        if not member.isfile():
            raise ValueError("Gitleaks executable is not a regular file")
        source = bundle.extractfile(member)
        assert source is not None
        binary = cache / "gitleaks"
        binary.write_bytes(source.read())
        binary.chmod(0o755)
    return binary


def conflict_lines(data: bytes) -> list[int]:
    if b"\0" in data:
        return []
    return [number for number, line in enumerate(data.decode("utf-8", errors="replace").splitlines(), 1)
            if re.match(r"^(?:<{7,}|={7,}|>{7,}|\|{7,})(?:\s|$)", line)]


def hygiene(base: str, scanner: Path) -> None:
    # Limit whitespace checks to changed material; preserved captures and review
    # diffs keep their exact bytes. Markdown double spaces are valid hard breaks.
    run("git", "-c", "core.whitespace=blank-at-eol,blank-at-eof,space-before-tab",
        "diff", "--check", base, "--", ".", ":(exclude)docs/reviews/**", ":(exclude)docs/sources/**", ":(exclude)*.md")
    paths = subprocess.check_output(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT).split(b"\0")
    failures = []
    with tempfile.TemporaryDirectory(prefix="swarm-secret-scan-") as directory:
        snapshot = Path(directory)
        for raw in paths:
            if not raw:
                continue
            relative = Path(os.fsdecode(raw))
            path = ROOT / relative
            if not path.exists():
                continue  # tracked deletion
            if path.is_symlink():
                raise ValueError(f"Review symlink before scanning: {relative}")
            data = path.read_bytes()
            # Source captures and historical review artifacts may quote markers;
            # they remain in the credential scan, including compressed archives.
            if not relative.is_relative_to("docs/reviews") and not relative.is_relative_to("docs/sources"):
                failures.extend(f"{relative}:{line}: conflict marker" for line in conflict_lines(data))
            destination = snapshot / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
        if failures:
            raise ValueError("\n".join(failures))
        run(str(scanner), "dir", str(snapshot), "--redact=100", "--no-banner", "--max-archive-depth=2")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="HEAD", help="Whitespace diff base; defaults to HEAD for local work")
    parser.add_argument("--library", help="Optional clean Library checkout at the recorded revision")
    parser.add_argument("--scan-history", action="store_true", help="Also scan all commits reachable from HEAD before first publication")
    args = parser.parse_args()
    try:
        library = library_checkout(args.library)
        scanner = gitleaks()
        print("Checking repository hygiene and credentials", flush=True)
        hygiene(args.base, scanner)
        if args.scan_history:
            run(str(scanner), "git", str(ROOT), "--log-opts=HEAD", "--redact=100", "--no-banner", "--max-archive-depth=2")
        print("Checking deliverable declarations", flush=True)
        run(sys.executable, "-B", str(library / "tools/deliverables/cli.py"), "--project", ".", "check")
        metadata = set(ROOT.glob("execution/PKG-*/DEL-*/deliverable.yaml"))
        scopes = set(ROOT.glob("execution/PKG-*/DEL-*/ScopeOfWork.md"))
        if not metadata or {p.parent for p in metadata} != {p.parent for p in scopes}:
            raise ValueError("Each deliverable must have both deliverable.yaml and ScopeOfWork.md")
        for scope in sorted(scopes):
            run(sys.executable, "-B", str(library / "tools/scope_of_work/validate_scope_of_work.py"), str(scope))
        run(sys.executable, "-B", str(library / "tools/scope_of_work/check_boundary_owner_resolution.py"), str(ROOT / "execution"))
        run(sys.executable, "-B", "-m", "unittest", "discover", "-s", "tools/tests", "-v")
        print("Repository checks passed. Research validity and acceptance require substantive examination.")
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"CHECK FAILED: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
