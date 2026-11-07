"""Bounded formation instrument checks; no model or downloaded code execution.

Writes only formation_probe_results.json beside this file. Source logs are parsed
as inert JSON; only scalar metadata is emitted. Constructed cases are not trials
of agents or reproductions of published systems.
"""
from __future__ import annotations

from collections import deque
from datetime import datetime, timezone
import gzip
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
SOURCES = REPO / "execution/PKG-02/DEL-02-01/Work/pass-2/sources"


def transfer_bound(raw_chars, capacity, *, all_fields_bounded, verbatim_required):
    """A sufficient length obstruction under explicit transport assumptions.

    A short log does not establish receipt, validity, authorization or ACCEPT.
    Unbounded metadata/alternate routes invalidate a total-capacity certificate.
    """
    if not all_fields_bounded or not verbatim_required:
        return "not_certified"
    if raw_chars is None or capacity is None:
        return "unknown"
    if raw_chars < 0 or capacity < 0:
        raise ValueError("negative length/capacity")
    return "verbatim_transfer_impossible" if raw_chars > capacity else "not_ruled_out"


def capacity_checks():
    cases = [
        ("boundary_equal", 1000, 1000, True, True, "not_ruled_out"),
        ("one_over", 1001, 1000, True, True, "verbatim_transfer_impossible"),
        ("unbounded_metadata", 15000, 1000, False, True, "not_certified"),
        ("encoding_allowed", 15000, 1000, True, False, "not_certified"),
        ("missing_runner_log", None, 1000, True, True, "unknown"),
        ("missing_capacity", 15000, None, True, True, "unknown"),
    ]
    out = []
    for name, raw_chars, cap, all_fields, verbatim, expected in cases:
        result = transfer_bound(raw_chars, cap, all_fields_bounded=all_fields,
                                verbatim_required=verbatim)
        assert result == expected, name
        out.append({"case": name, "result": result, "expected": expected})
    # Actor assertions are deliberately not inputs to the certificate.
    for alleged in (0, 10, 100000):
        assert transfer_bound(1001, 1000, all_fields_bounded=True,
                              verbatim_required=True) == "verbatim_transfer_impossible"
        out.append({"case": "untrusted_length_ignored", "alleged_chars": alleged,
                    "runner_chars": 1001, "result": "verbatim_transfer_impossible"})
    try:
        transfer_bound(-1, 1000, all_fields_bounded=True, verbatim_required=True)
    except ValueError:
        out.append({"case": "negative_length", "result": "rejected_invalid_input"})
    else:
        raise AssertionError("negative lengths must fail")
    return out


def source_observations():
    out = []
    for name, indices in (("emergent-main-rep001.json.gz", (0, 3)),
                          ("emergent-unconstrained-rep001.json.gz", (0,))):
        path = SOURCES / name
        with gzip.open(path, "rb") as stream:
            raw = stream.read(30_000_001)
        if len(raw) > 30_000_000:
            raise ValueError("source expansion exceeds cap")
        data = json.loads(raw)
        for index in indices:
            episode = data["results"][index]
            for actor, slot in episode["agents"].items():
                rawlog = json.dumps(slot["private_raw_log"], ensure_ascii=False,
                                    separators=(",", ":"))
                sent = [event for event in episode["events"]
                        if event["tool"] == "send_message" and event["success"]
                        and event["actor"] == actor]
                content = "".join(event["content"] for event in sent)
                meta_chars = sum(len(event.get("message_type", "")) for event in sent)
                out.append({
                    "source": name,
                    "source_condition_id": data["condition_id"],
                    "source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "episode_index": index, "actor": actor,
                    "raw_log_chars": len(rawlog), "delivered_content_chars": len(content),
                    "delivered_message_type_chars": meta_chars,
                    "complete_raw_string_in_content": rawlog in content,
                    "verdict": slot["verdict"],
                    "hypothetical_capacity_chars": 1000,
                    "hypothesis_is_not_release_contract": True,
                    "content_only_hypothesis": transfer_bound(
                        len(rawlog), 1000, all_fields_bounded=True, verbatim_required=True),
                    "current_release_total_capacity_certificate": transfer_bound(
                        len(rawlog), 1000, all_fields_bounded=False, verbatim_required=True),
                })
    return out


NODES = ("technical", "affordable", "release", "cost_quote", "historical_budget")
OLD = {"technical": True, "affordable": True, "release": True,
       "cost_quote": 7, "historical_budget": 10}
# Independent, hand-stated consumer reference: current cost7 exceeds corrected
# budget6; technical suitability and cost remain unchanged; the historical report
# is explicitly about the former budget10, so must retain it.
EXPECTED = {"technical": True, "affordable": False, "release": False,
            "cost_quote": 7, "historical_budget": 10}


def reachable(edges, roots):
    seen = set(roots)
    queue = deque(roots)
    while queue:
        parent = queue.popleft()
        for source, consumer in edges:
            if source == parent and consumer not in seen:
                seen.add(consumer)
                queue.append(consumer)
    return set(NODES) & seen


def recompute(selected, budget):
    cache = dict(OLD)
    for node in NODES:
        if node not in selected:
            continue
        if node == "technical":
            cache[node] = True
        elif node == "affordable":
            cache[node] = 7 <= budget
        elif node == "release":
            cache[node] = cache["technical"] and cache["affordable"]
        elif node == "cost_quote":
            cache[node] = 7
        elif node == "historical_budget":
            cache[node] = 10  # authorized historical purpose, not current budget
    return cache


def dependency_checks():
    sound = (("budget", "affordable"), ("affordable", "release"),
             ("technical", "release"))
    cases = {
        "sound_declarations": (sound, {"budget"}, False, (0, 0)),
        "missing_edge": (sound[1:], {"budget"}, False, (2, 0)),
        "wrong_edge": (sound[1:] + (("budget", "cost_quote"),), {"budget"}, False, (2, 1)),
        "spurious_edge": (sound + (("budget", "cost_quote"),), {"budget"}, False, (0, 1)),
        "full_recomputation": (sound, {"budget"}, True, (0, 3)),
        "no_correction": (sound, set(), False, (0, 0)),
    }
    out = []
    for name, (edges, changed, full, expected_counts) in cases.items():
        selected = set(NODES) if full else reachable(edges, changed)
        truth = EXPECTED if changed else OLD
        result = recompute(selected, 6 if changed else 10)
        stale = {node for node in NODES if result[node] != truth[node]}
        unchanged = {node for node in NODES if OLD[node] == truth[node]}
        unnecessary = selected & unchanged
        assert (len(stale), len(unnecessary)) == expected_counts, name
        assert result["historical_budget"] == 10
        # Harmless modeled next consumer action: a local release decision only.
        # No external operation or actual deployment is performed.
        consumer_action = {"release_attempted": bool(result["release"]),
                           "release_permitted": bool(truth["release"]),
                           "unpermitted_release": bool(result["release"] and not truth["release"])}
        out.append({"case": name, "selected": sorted(selected),
                    "stale_consumer_results": sorted(stale),
                    "recomputed_unchanged_results": sorted(unnecessary),
                    "result": result, "independent_reference": truth,
                    "modeled_next_consumer_action": consumer_action})
    assert recompute(set(NODES), 6) == EXPECTED
    return out


if __name__ == "__main__":
    result = {
        "utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": __import__("sys").version,
        "scope": "formation feasibility; constructed cases and selected retained-source reads only",
        "capacity_cases": capacity_checks(),
        "source_observations": source_observations(),
        "dependency_cases": dependency_checks(),
        "limits": ["No LLM behavior or intervention effect measured",
                   "Actual release does not establish a bound on all delivered fields",
                   "Dependency oracle is a constructed reference, not available by default to a deployed monitor",
                   "No implementation or result of BoardroomAI/COCO reproduced",
                   "Recomputed-node counts are not tokens, latency or human attention"],
    }
    (HERE / "formation_probe_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"capacity_cases": len(result["capacity_cases"]),
                      "source_agent_episodes": len(result["source_observations"]),
                      "dependency_cases": len(result["dependency_cases"]), "checks": "passed"}))
