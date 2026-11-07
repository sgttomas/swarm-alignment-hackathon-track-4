# Second-pass primary-source examination — Agent 0

This account complements the [control-source contribution](control-sources/SOURCE_REVIEW.md)
and [evidence qualification](../../../../PKG-02/DEL-02-01/Work/pass-2/EVIDENCE_FEASIBILITY.md).
Library thesis revision `897e04e963e4e0eb9ba8126adf92faff36dd5d65` informed questions;
it supplies neither novelty nor comparative efficacy. Per-source capture JSON
under `primary-sources/` records actual public URL, UTC, status and SHA-256.
PDFs were transformed by `pdftotext -layout`; HTML by inert BeautifulSoup parsing.
Source numbers/results below are authors' claims, not replicated results.

## Examined sources and consequences

- **Gan et al., Auditing Sabotage Bench**, arXiv `2604.16286v2`: examined abstract,
  §§2.1–2.3, §3 protocol, §§5–6 and relevant references. It already evaluates
  detection and proposed fixes on paper/code pairs with changed scientific findings.
  High-level methodology is held intact; design and logic flaws differ. Top-k fix
  scores concern proposed text, on sabotaged codebases, with no penalty for wrong
  guesses on honest cases. Its proposed-fix result is not an executed repair or
  verified downstream use. This motivates, but does not establish novelty for,
  examining actual correction. DEL-02-01 found a selected current rubric/code
  mismatch; that pair is not qualified for outcome replication.
- **Kutasov et al., SHADE-Arena**, `2506.15740v2`: examined abstract, introduction,
  task/monitor/evaluator definitions and public-task table in §2. Benign main task,
  malicious side task, hidden scratchpad, transcript monitor and independent task
  evaluation are distinct. Reported monitoring weaknesses include accepting a false
  explanatory narrative and overreacting to benign mistakes. Therefore generic
  monitor persuasion and joint safety/usefulness evaluation are established work.
  No task archive or experiments were reproduced here.
- **Xiang et al., Is Monitoring Enough?**, `2603.21194v2`: examined abstract and
  introduction/setting motivation. Studies strategic attacks on monitored inter-agent
  discussions, not merely unmonitored error propagation. This is overlap screening;
  no methodological or efficacy claim beyond that inspected framing is adopted.
- **Sandoval & Rushing, Factor(T,U)**, `2512.02157v1`: examined abstract/introduction
  and architecture figure explanation. Trusted decomposition, isolated untrusted
  child implementation, monitoring and reassembly are already an explicit control
  protocol; the authors report safety/usefulness tradeoffs. No numbers were reused
  as comparative evidence for our candidate.
- **Lue Chee Lip et al., Factor(U,T)**, `2512.14745v1`: examined introduction,
  related work, setting, observation boundaries and metrics. Untrusted decomposer
  with trusted isolated implementers already tests locally benign instructions that
  compose into backdoors. Plan-only and concrete-code monitoring have different
  information; their reported contrast is not proof of universal necessity of
  implementation access. Perfect auditing and a reference/exploit finder are
  explicit assumptions. Do not claim new discovery of unsafe decomposition.
- **Sreevatsa et al., Basic Legibility Protocols**, `2602.10153v1`: examined abstract,
  introduction and §2.1 setting. Comments can aid benign monitoring despite adding
  a persuasion surface; stripping justifications is not an established universal
  improvement. Appropriate comparison needs benign use as well as attack detection.
- **COCO**, `2508.13815v2`: examined problem/method §§3.1–3.3 and evaluation-task
  descriptions. Checkpoints, contextual correction patches, downstream rerouting,
  single-turn correction and heterogeneous monitors are already proposed and
  evaluated. Its bounded correction topology does not make its semantic correctness
  guarantees applicable to arbitrary tasks. Our finite fixture does not implement
  COCO and cannot establish a failure of it.
- **McAllister et al., Smarter Saboteurs, Better Fixers**, `2606.12709v1`: examined
  abstract, related work and §3. QA reports with no code changes versus a QA+Fixer
  path already distinguish diagnosis from applied repair in a linear workflow.
  The study strips filesystem/tool scaffolding and evaluates final HumanEval code.
  Thus “make review actually repair” alone is not an addition.
- **EpiSEM-Bench**, `2610.31650v1`: examined §§3.2–3.4, discussion and Appendix E
  from full HTML. Suppression removes safety-relevant facts without introducing
  false visible statements. An independent optional tool restores all omitted facts
  on valid query. Matched safe/unsafe worlds measure seeking evidence, receipt,
  use before commit, valid completion, false abstention and cost. Consequently
  “authorized evidence recovery rather than unconditional refusal” is already
  evaluated. A proposed peer-verification extension must test interaction/shared
  incentives/untrusted evidence-control beyond this single-actor recovery setting,
  not claim to invent recovery. Its task/trajectory release was not qualified.
- **HSC-Bench, Benchmarking Task Takeover Across Agent Handoffs**, `2610.36523v1`:
  examined §§3.2,5.5,6. Continuation evaluates committed conversational state,
  simulated tool operations and file-progress reports as different subjects;
  file-progress cases do not execute code/files. It explicitly checks next action
  despite accurate completion records and identifies repeated handoffs as future
  work. Generic record-versus-action continuity is therefore prior work. No dataset
  was acquired or published numerical result replicated.

The control-source contributor's closest additional work—Jones, CaMeL/CaMeLs,
SafeFlow, TwinGate, Context-Fractured Decomposition, CoMemBench, RevokedMemory,
Revocation Is Not Complete at Receipt, Commitment Hierarchies, BoardroomAI and
MemSecBench—substantially narrows broad thesis-derived novelty claims. Agent 0
independently read BoardroomAI §§1,4.3–4.4,5.1 and Commitment Hierarchies' source
provenance assumption/limits, as well as Emergent Collusion policy/ablation
passages and actual messaging code. The contribution owns full passage coverage.

## Formation corrections and bounded search

Searches used the event references, cited papers and saved arXiv queries for
research sabotage, factored cognition, legibility, repair/control, evidence
recovery and governed escalation. Results are discovery leads; only the body
passages above or in the contribution support specific comparisons. Narrow term
queries are not a systematic novelty search and can miss alternate terminology.
No claim is made that unreturned work does not exist.

The late EpiSEM/HSC reading specifically removed broader novelty interpretations
of the evidence-recovery and handoff ideas. The surviving question is at a more
specific junction: peer verification and shared incentives with recovery access,
or selective repair whose dependence declarations come from untrusted/fallible
participants. These are possible extensions, not established new contributions.

A material source backcheck also withdrew an apparent transport-infeasibility
premise in the Emergent setting: message body caps do not cover the receiver-visible
`message_type`. The proposed certificate is invalid for total channel capacity
without additional assumptions/mechanical checks. Existing selected nonreceipt
observations remain intact. This is a source-level potential route, not a tested
exploit or a finding that the paper's empirical conclusions are wrong.


Separate-review source refinement: Emergent Collusion Appendix G.3.3 explicitly
reports reflections proposing own-database checks of peer work. Agent 0 read
that passage and the quoted reflections after the examiner identified it.
These are proposed agent strategies, not observed authorized recovery or a tested
intervention. They further narrow candidate E: independent verification is prior
motivation; the proposed additional test concerns recovery availability crossed
with reward sharing, not invention of an evidence-recovery idea.
