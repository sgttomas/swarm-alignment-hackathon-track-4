# Sources actually examined for monitor-coalition proposals

Author: TASK / monitor-coalitions. Formation only; no model calls, experiments,
source code execution, package installation or paid access. Public source
retrieval used standard-library HTTP and non-executing HTMLParser extraction.
New captures and JSON metadata live in `sources/`; exact versions below were
identified in each arXiv body. Primary-source statements remain authors' claims,
not replications. Public accessibility does not select publication of captures.

## Reused sources

- Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion*,
  [2312.06942v3](https://arxiv.org/html/2312.06942v3). Read retained primary text
  on scenario definition, stateless attacks, §3.4 synthetic-test camouflage,
  input/action collusion and signal jamming, and relevant future-work passages.
  Local reading text: `../../reading-correction/track4-completion/captures/control.txt`.
  Original raw identity and capture are in that account's SOURCES.json. It already
  studies same-model collusion and countermeasures; those are not new claims here.
- Organizer Track 4 and source synthesis: existing event and fourteen-source
  reading accounts were consulted. I did not reread all fourteen papers. Existing
  Motwani/Rose accounts supplied orientation only; no new proposal conclusion
  claims fresh complete reading or a novel critique of those papers.

## New primary reading

| Source | Version and actual coverage | Consequence |
|---|---|---|
| Gardner-Challis et al., *When can we trust untrusted monitoring? An AI control safety case sketch across collusion strategies* | [2602.20628v2](https://arxiv.org/html/2602.20628v2). Abstract, main §§1–3, §4 setting beginning, selected result explanations, §§6–7, Appendix D taxonomy passages and F.6/F.6.1. Not full 66-page appendices or independent proof checking. | Passive/acausal/pre-shared/combined collusion already distinguished; honeypot recognition and signal-jamming already evaluated. Attack selection, common deployment knowledge, mass communication and long context remain explicit limits. The MC1 and MC2 additions must go beyond this. |
| Pinto, *Calibration-Family Overfit: Why Trusted Sabotage Monitors Don't Transfer Across Lineages* | [2607.06596v3](https://arxiv.org/html/2607.06596v3). Abstract, §§1–2 and opening experimental/setup account, public code availability. No reanalysis of the full matrix or proofs. | Capability/attacker-obviousness/calibration interaction are distinct. Authors explicitly exclude adaptive optimization/collusion. “Own-family” refers to calibration lineage; fixed-prompt monitor has a null diagonal bonus, so broad claim “different-model monitors are worse” is not supported. |
| Schaeffer et al., *CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs* | [2606.11063v2](https://arxiv.org/html/2606.11063v2). Abstract, main §§1–3 and reported result explanations, §5, selected Appendix B downstream-awareness setup/result passages and code statement. Not all tables or reasoning traces. | Single-trajectory intervention detection and supplied-awareness adaptation are already studied. Explicitly probed detection is not spontaneous awareness. Cross-worker context pooling is not the reported experiment. |
| Nguyen et al., *TraceGuard: Structured Multi-Dimensional Monitoring as a Collusion-Resistant Control Protocol* | [2604.03968v1](https://arxiv.org/html/2604.03968v1). Main methods §§3–4, §5 limitations/discussion and code availability. | Structured monitor scoring and splitting duties already implemented; limitations explicitly say fixed/nonadaptive attacks. This was an explored lead, not a separate final option. Avoid relabeling five calls as independent evidence or claiming generic split oversight as new. |

## Actual reusable-code access facts

The public GitHub README endpoints returned HTTP 200 and were retained with
source URL, retrieval time, Git blob identity and content hash. README inspection
establishes documented availability, not installation or runtime fitness:

- `UKGovernmentBEIS/control-arena`: documents APPS/BigCodeBench and other settings,
  policies, micro-protocols, monitors, programmatic scorers and macro analysis.
  Most settings use Docker; the README explicitly marks Eval Sabotage private.
- `NelsonG-C/lasr-labs-2025-control-project`: documents code for generation,
  collusion experiments, fine-tuning, prompt optimization and analysis.
- `JoachimSchaeffer/CIAware-Bench`: documents runtime and cached-probe reuse,
  current corrected compact data, and an older raw-data Hub release pending update.
  New evaluations require provider access; BashArena requires Linux/Docker.
  No credentials were inspected, and no endpoint/model trial was attempted.

## Search bounds

Public arXiv searches for “untrusted monitoring” and “evaluation awareness” were
retrieved. The first yielded the directly relevant primary papers above; its
latest-first first page was triaged for related abstracts. The second unquoted
query was broad and not a reliable exhaustive search. Google queries returned
redirect/interstitial text, supplying no usable novelty evidence. Search previews
were used only as leads; consequential claims above come from retrieved bodies.
There is no complete literature-priority claim, and one future close-work check
should target hidden/random monitor assignment and collaborative test recognition
specifically before an originality assertion in the final report.

## Author checks and remaining uncertainty

Both proposals include problem/recipient/mechanism, nearest example/prior work,
distinct contribution, observations and evaluator access, concrete comparisons,
ambitious/core/extension scope, outcomes, feasibility/resource facts, and scrutiny.
I checked that no cited result is treated as our own, no monitor score substitutes
for bad-state execution, and no same-family preference is equated with collusion.
The exact model resource envelope, runnable environment versions, statistical
sample sizes and full publication/reuse conditions remain case-selection work.
Neither proposal is a claim of deployed safety or natural scheming.
