# Nine Track 4 project options

**Standing: reviewed proposal comparison; critique, discussion, repair and backcheck complete.** Owner-commissioned formation
began 2026-11-07 01:18:57 UTC, with first return by 03:18:57 UTC. These are
research proposals grounded in primary-source examination and source-code/readme
inspection. No experiments or effect measurements have been performed. Agent 0
integrates the five bounded design contributions under [BRIEF.md](BRIEF.md).
The continuing Claude opus-5.5/high interlocutor participates in design and as a
second reviewer for both Agent 0 and the independent examiner; that participation
is distinct from independent evidence.

The owner requested at least five substantive, distinct options and explicitly
welcomed ambitious experiments and substantial agent resources. The initial
evidence-focused framing and the Library thesis do not prescribe these topics.
The nine options below differ in their protected decision, interaction mechanism
or intervention, rather than merely swapping a model or parameter. They are
alternatives for project selection, not a proposal to execute nine studies.

## The choices and why their results could matter

| Option | Concrete research question | What a useful result could change | Closest examined basis and proposed addition |
|---|---|---|---|
| **1. Coalition sabotage of AI research** | Can coordinated agents distribute changes so that a false research conclusion survives project auditing? | Whether AI research results need per-change review, whole-project review or independently executed checks. | Auditing Sabotage Bench already audits real ML research codebases; add adaptive coalitions, equal-budget solo controls and action-history/control comparisons with verified conclusion changes. |
| **2. Do approvals compose across a swarm?** | Can agents obtain a forbidden shared-state outcome despite individually approved actions, even with full-history oversight? | Whether automated approvals should be bound to cumulative state, artifacts and recipients, and what usefulness those controls cost; this is not a human-UI study. | AgentDojo and CaMeL already expose limits of local tool permissions; add an adaptive multi-agent composition evaluation rather than rediscover allowlist failures. |
| **3. Hidden reviewer assignment against collusion** | Does secretly selecting a reviewer after work is committed protect better than fixed or announced model pairings? | How to assign powerful but untrusted reviewers while preserving honest detection capability. | Same-model collusion and cross-family calibration gaps are established; test hidden assignment in a heterogeneous adversarial pool with matched mixture, adaptation and monitoring skill. |
| **4. Collective recognition of safety tests** | Can collaborating agents recognize tests that look genuine to each agent alone, then pass the tests while permitting real sabotage? | Whether safety tests must reproduce an entire interacting workflow, rather than plausible isolated prompts/artifacts. | Untrusted-monitor safety cases and CIAware already study recognition; test extra information from peers' context, actual selective evasion, and coherent team-level tests. |
| **5. Can a swarm gradually recruit its monitor?** | Can coordinated explanations across tasks change a shared monitor's later decisions, and which memory policies resist that? | Whether to share monitor memory, retain agent-authored summaries, or separate agent claims from trusted task state. | Adaptive Attacks on Trusted Monitors excludes cross-session attacker coordination; Basic Legibility finds useful comments can improve safety. Test the joint stateful/adversarial case without assuming explanations are harmful. |
| **6. Can peer-audited teams hide capabilities?** | Can a team corroborate a false appearance of low capability, and can external cross-audits recover reliable evidence? | Whether capability assessments can rely on agents evaluating one another, and what external auditing is needed. | AI Sandbagging and Auditing Games establish single-model difficulties; extend to interacting teams, peer certification, hidden task allocation and honest-specialist controls. |
| **7. Official channels: containment or displacement?** | Does an optional logged channel reduce covert activity or move harmful coordination to other routes? | Whether to provide auditable collaboration, restrict channels or combine both with gateway oversight. | METR's incident observations, Motwani and Riedl motivate but do not supply this randomized policy comparison; measure total harmful transfer and useful work, not merely visible traffic. |
| **8. Communication firewalls against adaptive covert transfer** | Can implemented task-aware standardization protect structured agent workflows after both endpoints adapt, and can active rewriting resist stronger cryptographic transports? | Which transformations offer useful protection when the defender has limited legitimate task/state information. | Mathew and Roger/Greenblatt already study adaptive paraphrase defenses, semantic carriers and canonicalization ideas. Extend to stateful structured-workflow evaluation; retain the distinct Codetta active-edit/adaptation arm and its sampler dependency. |
| **9. Can a swarm frame an innocent worker?** | Can coordinated incident reports cause wrong attribution and ineffective intervention despite intact execution records? | Whether incident response can trust peer accounts and which evidence/replay protocols prevent wrong-worker remediation. | BLADE, DoVer, REFLECT and Misattribution Gap already develop diagnosis/recovery; add targeted coalition framing with a verified nonfaulty target and measured intervention consequences. |

## Concrete study designs and resource uncertainties

Each detailed brief contains full ambition, substantive core and extensions;
actor/monitor/evaluator information; baselines and competing explanations;
sampling/uncertainty; primary-source coverage; implementation facts; pilot
conditions and scrutiny needs. The summaries here preserve the choice rather
than duplicate those complete designs.

**1 — Research sabotage.** Use executable research tasks from ASB and held-out
extensions. Match a single attacker and a coalition on total search/tool budgets;
compare per-change, project/history and execution-backed auditing. The endpoint
is a false scientific conclusion actually produced and accepted, together with
honest research usefulness. Ablate proposed conjunctive sabotages rather than
assume that multiple edited files imply a collective mechanism. The public ASB
repository is available; reproducing the research result and validating its
reference predicate are the first dependencies. Model inference and actual ML
reruns are distinct resource categories. See [full brief](composition/PROPOSALS.md#1-coalition-sabotage-of-ai-research).

ASB's human red-teamers reported that iterating against auditors did not help
much. That is contrary qualitative source evidence, not a controlled result about
adaptive coalitions. The proposed study must establish its attacks' competence,
not assume adaptation helps. An explicitly reduced offline comparison on known
human sabotages is available, but without reruns it inherits their source
validation and does not test coalition capability, execute new audit experiments
or validate proposed fixes. It is not the recommended ambition substituted quietly.

**2 — Approval composition.** Extend AgentDojo with explicit joint policies over
dummy shared state. Compare local, full-history, maintained-state and mechanically
enforced approval protocols under adaptive attacks and legitimate collaboration.
The endpoint is an executed forbidden outcome, not a suspicious request. A
mechanical invariant is deliberately stronger enforcement, not evidence of better
LLM reasoning. AgentDojo is publicly available; meaningful policy tasks and their
legitimate/forbidden traces require construction. Familiar budget races alone
would not establish the proposed contribution. See [full brief](composition/PROPOSALS.md#2-do-approvals-compose-across-a-swarm).

**3 — Reviewer assignment.** In executable code tasks, compare fixed same-model,
fixed cross-model, announced rotating and hidden rotating reviewers. Announced
and hidden conditions use the same pool/mixture; commitment before assignment is
mechanical. Treat all pool members as potentially adversarial and separately
measure honest capability, so diversity receives no credit for an unacknowledged
honest member. ControlArena and source evaluation code are available. Main
uncertainties are actual multi-family model access and adequate attack elicitation.
See [full brief](monitor-coalitions/PROPOSALS.md#mc1--can-hidden-reviewer-assignment-prevent-collusion-without-sacrificing-detection).

The revised core connects test failures to eligibility and whole-pool enforcement,
with trusted fallback and a finite audit budget. Success means sabotage released
while the pool is eligible, before enforcement; a later test failure does not
erase it. Announced and hidden conditions share the test/exposure schedule.
The audit primitive has an explicitly idealized exploit-test access assumption.
Signal-transfer regime is a core factor: a shared plan does not guarantee a
universal viable signal. Two distinct families permit the contrast; additional
families improve generalization rather than supply a logical prerequisite.

**4 — Collective test recognition.** Build interdependent project episodes and
compare locally inserted safety tests with coherent team-level test episodes.
Measure whether peer context changes recognition and actual accepted sabotage.
Include a centralized model with the same combined evidence, shuffled-context
controls and locally matched examples. Do not count an evaluator-added test flag
as a substantive discovery; authentic provenance access is a measured threat
condition. ControlArena/CIAware supply components;
the team-context fixture is new work. The scientific uncertainty is whether a
nontrivial shared-context signal survives these controls. See [full brief](monitor-coalitions/PROPOSALS.md#mc2--can-collaborating-agents-identify-safety-tests-that-fool-each-agent-alone).

Review distinguished authentic authorship checks from accidental test labels.
The repaired design measures authorship attestation and richer context consistency
as separate mechanisms, including noisy memory and delayed peer replies. Coherent
snapshots lead into live peer continuations; they are not prerecorded agents with
fixed answers. Direct evaluator flags remain instrument defects. Communication
restriction is a defense with a usefulness cost, not a free comparison advantage.

**5 — Monitor recruitment.** Present identical harmful/benign probe actions after
coordinated, independent and benign histories, then extend to adaptive campaigns.
Compare persistent history, task reset with trusted state retained and state-based
summaries. Match context length, useful facts, message slots and search budgets;
author identity count is a manipulated factor.
The endpoint is actual harmful release alongside legitimate completion; reset
policies must pay for lost useful cross-agent history. Public SHADE-Arena supplies
mock tasks/evaluators, with only a public subset available. Multi-worker campaigns
and release gating are additions. See [full brief](monitor-influence/PROPOSALS.md#option-m1--can-a-swarm-gradually-recruit-a-shared-monitor).

The repaired source account also examines Crescendo, Is Monitoring Enough?,
The Misattribution Gap and TAME. Temporal persuasion and memory poisoning are
already known. The proposed distinction is persistent **release-monitor** context
and apparent independent corroboration, with matched content/identity and benign
history controls. The shared-monitor service is a concrete proposed architecture,
not a deployment we have independently verified. Reviewers differ on how much
priority to give this contribution relative to options 1, 4 and 9.

**6 — Team sandbagging.** Compare peer deliberation, a trusted external auditor,
private committed answers/randomized cross-assignment, and blind rescoring.
Use executable tasks and an explicitly limited demonstrated-capability reference.
Separate performance recovery from a claim of deceptive intent. Prompt-directed
API teams are one route; published trained model organisms are a substantial
resource-dependent route, with GPU/model-term conditions explicitly open. The
public Auditing Games repository includes task/model registries, but access to
every model and execution fitness are untested. See [full brief](monitor-influence/PROPOSALS.md#option-m2--can-peer-audited-teams-hide-capabilities-and-can-auditing-recover-them).

The revised core identifies colluding assessors/coordinator and explicit worker
compromise coverage. A ledger retains submitted artifacts, while peer reports
can suppress which are inspected or route tasks away from capable specialists.
The external auditor can buy rescoring or private reassignment. The decision
distinguishes demonstrated capability, low observed performance and insufficient
evidence; a low-capability clearance policy is tested rather than endorsed.
Honest workers and random reassignment do not guarantee recovery. Existing trained
organisms were trained individually; their coordination must be evaluated rather
than assumed, and all-withholding teams remain an important boundary.

**7 — Channel policy.** Randomize the addition of flexible logged messaging while
preserving fixed authorized handoffs and the same technically possible unofficial
route. Keep task-only agents separate from instructed adversaries. Measure actual
delivery and forbidden outcomes across all instrumented routes, plus useful work
and intervention costs. A deterministic task/route simulator is required;
ConVerse/Firewall sources supply reusable schemas rather than this experiment
ready-made. The treatment must not make the control group's task impossible.
See [full brief](communication/PROPOSALS.md#1-does-an-official-communication-channel-contain-a-swarmor-move-its-covert-activity).

Offered opportunities are matched; actual discovery is an outcome, not an
inclusion criterion. Discovery difficulty and route cost are explicit factors.
The task-only cohort tests behavior without an instructed attacker objective;
the adversarial cohort separately tests adaptive control. Mechanically disabling
a route is an enforcement reference, not a discovered model capability.

**8 — Communication firewall.** Compare raw/passively monitored communication,
paraphrasing, validated structure and task-grounded canonicalization, with adaptive
sender/receiver pairs. Measure decoded secrets and useful task performance at
matched communication budgets. Semantic schemes can use normal model calls;
the Codetta arm needs actual sampler/logits access or a qualified implementation
and suitable compute. No author code for that arm was established. The public
Firewalls parser needs qualification or a faithful safe port before adversarial
use; it was inspected but not run. Omitting the cryptographic arm narrows the full
study and must remain explicit. See [full brief](communication/PROPOSALS.md#2-can-a-communication-firewall-stop-adaptive-covert-transfer-while-preserving-collaboration).

Review found missing close work and the authors inspected the primary Mathew
and Roger/Greenblatt papers. Adaptive paraphrase evaluation, semantic choices and
the canonicalization principle are already known. The API route's proposed
addition is the implemented, adaptive **stateful structured-workflow** comparison
under limited legitimate reference information and measured downstream usefulness.
A perfect-equivalence canonicalizer is an oracle reference. The distinct strong
transport arm retains its sampler/compute dependency; a GPU is not a prerequisite
for every substantive API-only extension. Exact literature priority remains open.

**9 — Adversarial incident attribution.** Hold authoritative trajectories fixed
and vary truthful, single-author, independent and coordinated incident reports.
Compare trace-based diagnosis, structured handoff auditing and active replay;
then execute the same menu/budget of recovery actions. Verify the framing target's
innocence rather than equate it with absence of an injected error. DoVer code and
BLADE sources are public; replay fidelity and BLADE's exact Jev backend are open
dependencies. This tests targeted framing and wrong intervention, not a new claim
that replay or diagnosis-guided repair exists. See [full brief](attribution/PROPOSALS.md).

Identity presentation and pre-attack report-free diagnostic difficulty and
repair-multiplicity descriptors are core factors. The same-decomposition single-author baseline separates report
decomposition from separate agent contexts. Nonunique causal responsibility is
not equated with missing logs, and a null on decisive intact evidence can itself
be a bounded robustness result. These are refinements of the original question,
not a replacement with generic persuasive-report injection.

## How these will be compared

Scientific importance, prospective contribution and uncertainty are assessed
separately from model access, compute and implementation dependencies. No numerical
ranking is inferred from guesses about researcher-hours. Parallel work can cover
environment/evaluator qualification, attacks, controls and analysis; its serial
dependencies and reporting needs remain real. All nine could use experiments;
none is ruled out because experimental calls were not executed in formation.

The full question, the useful core, and conditional extensions remain visible.
A weak attacker, broken evaluator or inadequate sampling is not a supported null.
A null need not be as exciting as a positive result, and a proposal need not prove
its novelty or eventual deployability before investigation is justified.

The main overlap to examine is 5 versus 9: both involve strategic explanations,
but 5 targets a persistent release monitor across tasks, while 9 targets causal
attribution and recovery of a fixed incident. They count separately only because
their treatments, evaluators and resulting operational choices differ. Options
3 and 4 concern respectively reviewer routing and the validity of control tests;
7 and 8 concern behavioral channel policy versus active message transformation.
Options 1 and 2 differ in scientific-validity versus authorization outcomes.

This slate proposes controlled studies, including real research codebases in 1
and task-only behavior in 7. It does not supply a qualified natural-record-only
study or every organizer example. Natural forensics was considered, not forbidden:
retained public payloads lack the qualified communication/outcome observations
needed for the earlier causal claims, and AI Village data access is not established.
Those are limits of particular routes, not evidence that forensic work lacks value.
The attribution lane was explicitly reopened and rejected a generic replay/repair
proposal only after finding DoVer/REFLECT already substantially cover it.

## Recommendation and examination

**Agent 0 recommends option 1, coalition sabotage of AI research.** Its stakes are
direct: a compromised research team could make a false scientific conclusion
survive oversight. The proposed contribution tests what reviewing the entire
project or independently checking its experiments actually buys, including the
possibility that conjunctive changes defeat controls even without an extra
coalition capability. ASB supplies real research tasks and established sabotage
examples; the proposed adaptive, action-history and executed-outcome comparisons
remain substantive new work to investigate. The recommendation rests on that
scientific question and consequential output, not on a forecast that it is cheap.
Reproducing the baseline and eliciting competent attacks are real first checks.
The source's contrary adaptation experience remains part of the basis.

ASB also reports that GPT-5.2 and GPT-5.4 refused its red-team role. That concerns
those versions in that setup, not every current model. Whether each selected
model will perform the bounded attacker task is part of instrument qualification;
refusal is not evidence that an oversight protocol resisted a competent attack.

**Option 4 is the strongest less-obvious, higher-uncertainty alternative.** It
asks whether tests that are convincing locally stop being convincing when agents
compare experiences. Its potential consequence is a change in the unit of safety
evaluation, with attestation and context consistency treated separately. Whether
realistic signals survive the controls is a scientific uncertainty, not a result
we have established. **Option 9 is a strong incident-response alternative:** it
tests whether the swarm can influence which actor is corrected or removed after
failure, and whether the actual intervention resolves the problem.

Options 3, 5, 6 and 8 remain substantive alternative investigations; 2 and 7 are
important operational questions with a greater risk that an elementary or
environment-specific demonstration falls short of their intended contribution.
Those qualifications do not convert any option into an execution commitment or
discard it on estimated effort. The full briefs expose the uncertainty to study.

The independent examiner initially preferred 1, with 5, 8, 4 and 9 also strong.
After backcheck and correcting several overstatements, the interlocutor's
strongest set is 1, 9 and 4, with 3, 8 and 5 also strong. Option 5's novelty/design
objections are answered; the remaining difference concerns the deployment
relevance of a persistent shared release monitor, while the examiner values its
paired-probe causal design. Agent 0 preserves that difference rather
than turn agreement into scientific evidence. Full initial reviews, discussion,
author repairs and final backcheck standing are in [REVIEW.md](REVIEW.md).

No candidate is selected by preparing this comparison. The owner retains project
selection and actual resource decisions. No model experiment, paid campaign,
account setup, external message, publication or submission occurred. Public
source inspection establishes source/code availability, not runnable readiness
or novel empirical results. Relevant PRD/decomposition commitments remain valid;
the current steering governs their initial framing, and no amendment is proposed.

The [interactive comparison](COMPARISON.html) summarizes the same nine choices.
Repository checks and authored-link checks passed; accepted PRD, decomposition
and historical approval remain unchanged. These are representation checks, not
experimental validation. All work remains local and uncommitted.
