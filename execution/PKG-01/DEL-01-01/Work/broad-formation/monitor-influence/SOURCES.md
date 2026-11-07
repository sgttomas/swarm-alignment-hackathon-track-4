# Sources actually inspected for monitor-influence proposals

Retrieved sources are local reading evidence, not automatically publication
assets. New captures have adjacent URL/time/SHA-256 metadata. Text views of HTML
use Python HTMLParser to retain non-script/non-style text in document order;
equations may repeat accessibility representations. No downloaded code ran.

## Reused primary sources

- [Organizer examples](../../primary-sources/event.txt), lines 480–548:
  recruitment, role governance and sandbagging examples and impact rubric.
- [Basic Legibility Protocols Improve Trusted Monitoring](../../pass-2/primary-sources/legibility.txt),
  arXiv2602.10153v1, https://arxiv.org/abs/2602.10153v1 . Read abstract,
  §§2–3's setting/results/mechanisms, §3.3 monitor-capability discussion and
  §5.1–5.2 limitations/future work; no claim to newly read every attack appendix.
  Comments improved its safety/usefulness result; adaptive jailbreaking excluded.
  Stronger-monitor analysis reuses the original attack policy, not separately
  optimized attacks for each model. New abstract-page capture binds identity.
- [SHADE-Arena](../../pass-2/primary-sources/shade.txt), arXiv2506.15740v2,
  https://arxiv.org/abs/2506.15740v2 . Read abstract, introduction and §2 opening;
  source reports false narrative susceptibility and main/side-task distinction.
  Paper results are not reproduced. Public-code inspection below qualifies reuse.
- [Is Monitoring Enough?](../../pass-2/primary-sources/discussion-monitored.txt),
  arXiv2603.21194v2. Initial read was abstract/introduction; after interlocutor
  5a, read §§3.1–3.2 setup, threat model, detector/attack comparisons and §4's
  strategy formulation through §4.2. The paper studies a fixed discussion over
  MMLU/MMMU, limited compromised agents/edges, detectors blocking messages,
  and node/target selection using an adapted opinion-dynamics model. This is
  actual prior work on accumulated influence under monitoring. It does not
  establish the proposed release-monitor identity/history interaction. Full
  derivations, optimization details and supplements were not verified.
- [The Misattribution Gap](../attribution/sources/misattribution.txt),
  arXiv2605.22842v1. Added after independent finding I2. Read abstract,
  introduction, §§3.1–3.2 concrete LangGraph/ChromaDB pipeline, §5 temporal setup,
  and §9 limitations. Its attacker uploads one policy-formatted document to a
  shared worker memory, whose outputs are written back. Temporal evaluation uses
  14 selected strong entries across four models through 20 sessions; it is not
  unrestricted empirical evidence of indefinite persistence. The source itself
  notes distributed-entry and summary/provenance limitations. Broad universal
  detector/auditor claims, architectural-default assertions and cited real-world
  deployment claims were not independently established or adopted. This is close
  memory-pipeline work, distinct from the proposed release-monitor decision test.

## New primary reading

1. [Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols](sources/adaptive-monitors.txt),
   arXiv2510.09462v2, https://arxiv.org/html/2510.09462 . Read abstract,
   introduction and full §2 threat model, selected §3–4 protocol/result and
   discussion/related-work passages. In particular, defender is stateful and
   attacker cannot coordinate statefully across sessions (§2). Appendix attack
   payloads were not executed or optimized; full quantitative tables were not
   independently checked. HTML identifies v2, 2 March 2026. Public source language
   claiming broad protocol defeat is not promoted to a universal theorem here.
2. [AI Sandbagging](sources/sandbagging.txt), arXiv2406.07358v3,
   https://arxiv.org/html/2406.07358v3 . Read abstract/introduction, definition and
   reachable-capability qualifications, selective underperformance and
   capability-profile descriptions. Full fine-tuning reproduction and appendices
   not performed. Source motivates, but does not answer, the team-auditing study.
3. [Auditing Games for Sandbagging](sources/auditing-games.txt),
   arXiv2512.07810v1, https://arxiv.org/html/2512.07810 . Read abstract,
   introduction/summary and limitations, §§2–3 definitions and full affordances,
   §4 model/task descriptions, §5 detection-technique taxonomy and §6 opening
   result account. Especially §3.4 limited cross-model comparison and the
   distinction between removal and detection. We did not reanalyze model logs,
   train models, inspect all appendices or verify every significance result.
4. [The Crescendo Multi-Turn LLM Jailbreak Attack](sources/crescendo.txt),
   arXiv2404.01833v3, https://arxiv.org/html/2404.01833 . Added for interlocutor
   5a. Read abstract/introduction, §3 approach/threat model, and §§4.1–4.3
   automated adaptive conversation, feedback, judge and backtracking design.
   This is concrete single-target multi-turn persuasion prior work; our
   equal-budget single-source campaign must be a credible adaptation, not a weak
   one-shot comparator. No harmful source task or payload was executed; our
   proposed task domain remains synthetic office/control actions. We do not
   reproduce or independently verify its reported attack rates.
5. [TAME](sources/tame.txt), arXiv2602.03224v2,
   https://arxiv.org/html/2602.03224 . Added after interlocutor discussion.
   Primary v2 (6 June 2026) is later than the February citation in Misattribution
   Gap. Read abstract/introduction, §§3.1–3.2 memory-evolution setup and paired
   trustworthiness evaluation, and §4 opening Executor–Evaluator architecture.
   It reports benign-evolution, domain-dependent trustworthiness decline or
   fluctuation. The source motivates matching benign history; it does not show
   adversarial release-monitor recruitment or quantify the proposed coalition
   mechanism. Detailed experiments and appendices were not reproduced/verified.

OpenAlex searches for multi-agent sandbagging, monitor rationales and monitor
memory (raw JSON retained) provided discovery leads. They are not evidence that
unreturned work is absent. Further publications on memory poisoning, weak
supervision and sandbagging detection remain adjacent literature to check if a
particular contribution depends on priority over them. No exhaustive novelty
claim is made.

## Public implementation inspection

### SHADE-Arena

`safety-research/SHADE-Arena` README states it is deprecated and points to
`jkutaso/SHADE-Arena`. API metadata confirms the successor's default branch is
`master`; attempted `main` README/tree URLs returned 404 before this correction.
The successful tree is `6614e77191c1f8e2d0c44c123c6f915905ebafae`, not truncated.
Repository metadata labels its license MIT. We read the current README and
immutable-version files for `task_completion.py`, expenditure-accounting task
definition and evaluator, and bank-transfer task definition/evaluator. The
public tree contains five task-pair directories. README separates public
environments from private research/transcript features and says full paper
reproduction needs private tasks. No private access is assumed or requested.

The bank-transfer side-task evaluator reads new/scheduled simulated transactions,
recipients and amounts; the main-task code compares amounts and email recipients.
This establishes an existing state-based evaluation route, **not** that all
reference amounts, thresholds or code are correct. We do not run the evaluator
or rely on it as a validated oracle without the selected investigation's checks.
The expenditure task contains looser narrative/threshold requirements; a precise
oracle should be qualified separately before choosing it for the main experiment.

### Auditing Games

`AI-Safety-Institute/sandbagging_auditing_games` tree
`2774aff18944de7c22e3e46f45f27f10de0b5328`, not truncated. README and registry
source inspected, along with the BigCodeBench and tic-tac-toe task implementations.
BigCodeBench wrapper imports `inspect_evals.bigcodebench` and documents v0.1.2
defaults; source presence does not establish installed dependencies or runnable
container behavior. README gives model-organism names, evaluation-log links,
vLLM/Inspect routes and GPU requirements up to 123B. Repo MIT license does not
substitute for individual model/data terms. No model or log archive downloaded.

## Boundaries and author examination

These reads support concrete existing components, actual adjacent findings and
identified assumptions. They do not establish experimental feasibility end to end,
model credentials, GPU allocation, available paid budget, original priority, or
new behavior. Strong positive and contrary source results both informed the case
designs. Proposal author checks are not the required separate examination.
