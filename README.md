# Swarm Alignment Hackathon

This repository is a workspace for research and project activities during [Apart Research's Swarm Alignment Hackathon](https://apartresearch.com/sprints/swarm-alignment-2026#overview), November 6–8, 2026.

The hackathon explores alignment challenges that emerge when AI agents interact—for example, when they negotiate, trade, or share tools. This workspace is intended to hold the ideas, experiments, code, and findings developed during the event.

## Research direction

This project focuses on **Track 4: Multi-Agent Oversight and Control**. We are
developing participant workflows and tooling to explore covert coordination,
completion claims versus actual state, failure diagnosis from incomplete evidence,
and controls for cooperating agents. Specific investigations will develop through
the work, with room to follow other fruitful questions within this track.

The Chirality Library and Root's nascent observability work provide conceptual
and practical resources. Research conclusions must be supported by their stated
principles, reasoning, and evidence.

## Project status

The owner stopped the hackathon undertaking after formation and proposal design.
This repository is now [preserved as a worked case](docs/WORKED_CASE.md) for
adapting useful assessment practices into Chirality Root. Formation produced
source accounts, candidate designs and examined reviews; no empirical model
study or event submission was completed. The owner explicitly described the
responses as reasonable, so preservation does not assign a failure grade.

The [accepted PRD](docs/PRD.md) and [research decomposition](docs/RESEARCH_DECOMP.md)
remain the historical project basis. See the [project entry](loop/LOOP_INIT.md)
for the actual stopping direction, preservation and source locations.

## Repository checks

Run the same checks used by GitHub Actions from this checkout:

```sh
uv run --python 3.13 tools/checks.py
```

Install [uv](https://docs.astral.sh/uv/) first if needed. The first run downloads
Python dependencies, a separate clean Chirality Library checkout at revision
`897e04e963e4e0eb9ba8126adf92faff36dd5d65`, and Gitleaks 8.30.0 with a recorded
SHA-256 check. The Library is cached outside the project under
`~/.cache/swarm-alignment-checks/` so its deliverables cannot enter project
queries; Gitleaks is cached under ignored `.cache/`. Subsequent runs reuse them. To use an existing clean Library checkout at that revision, add
`--library /path/to/chirality-library`. The active working Library is never reset.

Checks cover native deliverable declarations, SOW_V1 scope structure and boundary
owner references, conflict markers, changed code/config whitespace, credentials
(including compressed captures), and the check runner's focused tests. They scan
tracked and non-ignored untracked files; ignored files are outside the scan.
Historical review artifacts and source captures are excluded from marker and
whitespace checks, but remain in the credential scan. Markdown spacing is left
alone because double spaces encode hard breaks. Findings redact credential values.
These checks do not establish research validity or evaluate dependency conditions;
unknown bindings and conditional cycles remain visible observations.

Use `--base origin/main` to check whitespace changes against the integration
branch. Before publishing previously local history, add `--scan-history` to scan
all commits reachable from HEAD as well as current files. Ordinary runs scan
current files; GitHub runs on PRs, pushes to `main`, and manual dispatch, using
the PR base or prior push revision. No experiment or paid model call runs in CI.
As research code appears, add focused tests with small redistributable fixtures.

Agents must run these checks before committing or publishing changes and resolve
failures before merging. GitHub reports a single **Repository checks** status.
