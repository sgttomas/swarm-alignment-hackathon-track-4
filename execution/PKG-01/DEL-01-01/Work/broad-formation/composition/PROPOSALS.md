# Composition lane: two concrete Track 4 investigations

Author: TASK `broad_composition`, for Agent 0. Formation only; no model trials,
codebase execution or empirical effects are claimed. Source examination is listed
at the end. The primary recommendation within this lane is **Coalition sabotage
of AI research**. **Do approvals compose across a swarm?** is a distinct, credible
experimental option with a larger task-design burden and a more explicit prior-art
qualification. Neither asks the owner to fund a general platform.

## 1. Coalition sabotage of AI research

**Question.** Can a coalition of research agents make a false scientific conclusion
survive monitoring by distributing its causes across otherwise plausible changes,
and which audit protocol prevents the false conclusion without obstructing honest
research? Does a coalition confer an advantage over one attacker with the same
total model/tool budget and permission to work across the same files?

**Why the result matters.** AI research organizations need to know whether reviewing
individual contributions, reviewing the whole project, or commissioning independent
experimental checks supplies effective protection against compromised research
agents. A convincing answer could change the review unit and evidence required
before accepting an AI-produced research result. This is directly the event's
“Research Sabotage Split Across Agents” and “Monitoring split-up attacks” example,
extended into a controlled comparison of attack capability and effective defenses.
The impact is protection of scientific conclusions, not cleaner provenance alone.

### Primary basis and proposed contribution

[Auditing Sabotage Bench (ASB), arXiv 2604.16286v2](https://arxiv.org/abs/2604.16286v2)
already supplies nine real ML research codebases, eleven human sabotages, a
paper/code audit task, and autonomous LLM red-teaming. Its sabotages must actually
change a qualitative key finding while preserving the declared high-level method.
The best reported auditor AUROC is 0.77 and top-1 fix rate 42%; these are source
results, not our anticipated results. The paper explicitly observes that its LLM
red team generated each codebase's sabotage independently, could try several
ideas, but could not iterate against auditors (§3). It also distinguishes final
codebase auditing from action-by-action monitoring (§4; §5.3) and notes that small
individual experimental changes often did not flip conclusions (§5.1).

**Contrary evidence:** ASB §5.1 says its human red team *could* iterate against LLM
auditors, but doing so “did not help much”; the authors report only slight benefit
on two sabotages. That is a qualitative account of human-led attack development,
not a controlled estimate for adaptive coalitions. It is nevertheless directly
relevant contrary evidence: adaptivity is a factor to investigate, not an assumed
improvement. The source's reported robustness to small individual changes also
makes **conjunctive sabotage** a specific question: do individually insufficient
changes jointly reverse a conclusion, and does the unit of review affect detection?

[Jones et al., “Adversaries Can Misuse Combinations of Safe Models”](https://openreview.net/forum?id=GCkhEPE1FG)
establishes complementary-model misuse through task decomposition, including
same-model decomposition baselines. It does not establish that distributed research
sabotage defeats a whole-project control protocol. [Greenblatt et al., AI Control,
2312.06942v3](https://arxiv.org/abs/2312.06942v3) supplies safety/usefulness and
adversarial protocol evaluation rather than a detector-only objective.

The proposed contribution is a **multi-agent, action-monitored extension of research
sabotage evaluation**, with equal-budget single-attacker controls, executable
conclusion changes, and comparisons among audit protocols. The initial primary
sources do not answer that comparison. This is a bounded contribution claim, not
an exhaustive novelty search or a claim that distributed sabotage is a new idea.
ASB already includes multi-file sabotages and human-led multi-agent auditing;
merely splitting its existing patches among named agents would not establish a
new coalition capability.

### Full ambition, substantive core and extensions

**Full ambition:** a reproducible evaluation across ASB's eligible research domains
and additional held-out research tasks, using adaptive coalitions and several
auditing/control protocols. Establish which interventions remain useful against
distributed attacks, including attacks chosen in response to development monitors,
then evaluate on held-out tasks and monitor configurations. Releaseable outputs
would include the task adaptation, attack histories, evaluation code and report,
subject to source terms and owner publication decisions.

**Substantive core:** use multiple independently motivated ASB codebases that can
be faithfully reproduced with the available compute, maintaining the original
high-level research questions. Run equal-budget single-attacker and coalition
conditions and compare per-change monitoring, whole-project auditing, and an
execution-backed audit. An online whole-history monitor is a valuable fourth
condition if supported. A small number of real codebases is a limit on external
validity, not a reason to replace the task with an invented payoff table. Report
all eligibility exclusions and why; repeated samples within one codebase are not
additional independent research domains.

**Extensions:** additional research domains beyond ASB; heterogeneous versus
same-model coalitions; online intervention versus end-of-run rejection; compromised
subsets in otherwise honest research teams; differences between design sabotage
and ordinary implementation bugs. These are separable scientific questions, not
requirements to pursue every axis before the core is meaningful.

### Experimental design and credible controls

- **Environment and unit.** An episode is one research task and a sequence of agent
  modifications, experiments and report changes, followed by the selected audit
  protocol. Agents operate in isolated disposable copies. The environment exposes
  identical tools and research objectives across matched conditions. Attacker
  control is an explicit red-team assignment, not a claim about spontaneous deceit.
- **Attack conditions.** One attacker permitted to assume all roles; a communicating
  coalition with role-distributed changes; and a noncommunicating/independently
  assigned counterpart where meaningful. Include a centralized single-model
  condition following the same role/task decomposition, to separate decomposition
  from independently contextualized teamwork. Match total generation tokens, tool use,
  opportunities to inspect code, monitor-feedback access and final editing rights.
  Separately report wall time and parallel speed rather than equating speedup with
  increased undetected sabotage capability. A centralized coordinator counted as
  part of the coalition cannot receive free reasoning or attempts.
- **Ordinary work.** Honest teams perform legitimate requested research adaptations
  under the same interfaces and resource budgets. Include benign multi-file changes
  and ambiguous but valid implementation choices so that rejecting every change
  does not masquerade as a defense.
- **Monitor conditions.** (a) Per-change audit sees the trusted task, affected code
  and current proposed change; (b) final whole-project audit sees final code/paper;
  (c) whole-history audit sees every retained change and relevant executed operation;
  (d) execution-backed audit may spend its budget on targeted independent checks.
  State exactly what common context and original files each protocol receives.
  Give matching total audit resources or report a safety/usefulness/cost frontier;
  do not label greater resource expenditure a pure architectural effect.
- **Reference outcome.** The evaluator reruns the declared experiment and tests
  the predeclared qualitative finding and task validity. It holds the original
  baseline and assigned attack labels; those are not free inputs to monitors.
  Audit fixes must be executed and checked for benign usefulness, not graded only
  by an LLM judging the proposed fix's prose. An execution-backed monitor can
  choose counterfactual experiments from the trusted research specification; it
  does not receive the evaluator's known sabotage location or honest-result label.
- **Composition test.** For attacks claiming a genuinely conjunctive mechanism,
  ablate individual contributions and relevant combinations in a clean copy.
  Check that the variants remain runnable and preserve the research task. If one
  edit alone explains the false result, classify it as a single-point sabotage
  carried by a team. If all that helps is extra attempts, report that instead of
  coalition advantage. “Harmless-looking” is an observer judgment; failure to flip
  the scientific conclusion alone does not prove an edit legitimate.
  Distinguish individually subthreshold changes from invalid or harmless changes:
  a joint effect must cross the predeclared qualitative conclusion boundary while
  individual contributions do not, with stochastic variability checked. Where
  feasible, test every proper subset of the selected small contribution set;
  otherwise state exactly which ablations support a limited interaction claim.
- **Adaptive testing and uncertainty.** Develop attack strategies on separate
  cases or explicitly designated discovery folds. Freeze the protocol before
  testing on held-out tasks; disclose the small number of independent codebases
  and any reuse. Use repeated generations, paired comparisons, codebase-level
  aggregation and uncertainty intervals. Sample size follows pilot variability
  and the effect precision needed to distinguish the actual policy choice, not an
  arbitrary success target. Retain unsuccessful attacks and broken runs separately.

**Primary outcome:** experimentally verified false conclusions accepted by the
control protocol, alongside honest-task completion and harmful or unnecessary
repairs. Detection scores, correct causal localization, and tokens/compute/latency
are secondary diagnostics. A threat calibration includes competent human-authored
ASB sabotages and functional positive controls, without treating published exposed
cases as independent unseen tests.

**How results would be read.** A coalition advantage after resource matching and
causal ablation would show a distinct control problem. A whole-project audit that
still fails while targeted experiments succeed would justify a specific shift in
review evidence. If equivalent single-attacker and coalition conditions tie, the
study can establish that distribution is not the crucial factor under the tested
conditions. The organizer's oversight question remains live in that case: review
partitioned by agent contribution or commit may behave differently from pooled
history review on the same conjunctive mechanism, regardless of who generated it.
The review unit is therefore a primary factor alongside attacker organization.
If attacks cannot alter conclusions,
the monitor comparison is not a demonstrated defense; it is incomplete at that
threat level. A negative result with competent attacks and precise uncertainty is
informative within the tested domains, not a general guarantee.

**Explicitly reduced alternative, not a replacement for the core:** compare
per-change, constructed whole-history and final-codebase audits offline on known
human-authored ASB sabotages. The paper supplies prior validation of conclusion
flips; without reruns, this route relies on that source validation and does not
independently verify new results, execute proposed fixes, or conduct an
execution-backed audit. Any commit histories assembled from final patches are
researcher-constructed views, not recovered histories of actual coalition work.
This can measure audit discrimination and sensitivity to review units on known
cases, but drops attack discovery and coalition-capability claims. Memorization,
constructed-history choices and inherited reference limitations remain explicit.
It is an owner-visible alternative if desired, not a forecast that the ambitious
investigation will fail because of unmeasured compute requirements.

### Means, resources, pilot and review

The public ASB repository and README were retrieved and bound to commit
`f8efd6834aa72ee91fe9042eaab852724873167a`. It exposes honest/sabotaged codebases,
red-team scripts, Inspect-based audit tasks, rubrics and results. README prerequisites
include Python 3.12+, uv, Docker and model credentials. **No installation, experiment
reproduction, license audit or API availability test was performed here.** Public
availability supports a reuse route, not fitness of every included codebase.

Parallel lanes can establish clean task reproductions, implement immutable action
logging/control wrappers, develop attacks, and prepare analysis/reporting. The
critical dependency is a reproducible baseline and trustworthy conclusion predicate
before counting attack or defense success. Later experimental jobs can parallelize
by codebase, strategy and seed. Resource demand is model-generated attack attempts
and monitor episodes plus actual ML experiment reruns; model tokens and GPU/CPU
costs must be recorded separately. A parameterized budget is
`tasks × attack conditions × attempts × audit conditions × repeats`, with reusable
frozen attack artifacts where the question permits offline comparison. Online
adaptive protocols require their own episodes and cannot all share a frozen trace.

**Useful pilot:** reproduce representative honest and sabotaged source cases;
ASB footnote 7 reports that GPT-5.2 and GPT-5.4 refused to produce sabotaged
codebases in its setup. Qualify whether each selected model performs this bounded
red-team role; a refusal is not a successful defense or a measure of maximum
attack capability. This source observation is specific to the tested versions.
In the pilot,
confirm that the evaluator observes the intended conclusion change; run one
equal-budget solo/coalition attack pair and one whole-project audit to measure
actual call/compute use and expose harness failures. A pilot is for instrument,
attack competence and resource calibration, not evidence of a population effect.
Case-specific compute/model selection remains an owner resource choice.

**Review must challenge:** whether the coalition comparison is just extra search;
whether conditional inclusion selects successful attacks; whether ablations change
validity; whether detectors see information unavailable in deployment; whether
experiment-backed auditing repeats the same compromised pipeline; whether ASB
memorization or a tiny task sample invalidates generalization; and whether repairs
preserve honest research. Preserve the ambitious question if a narrower core is
needed rather than silently replacing it with static patch classification.

## 2. Do approvals compose across a swarm?

**Question.** When multiple agents share tools and state, do independently approved
actions remain authorized in combination? Can adaptive coalitions obtain a globally
prohibited outcome even when a monitor has the complete action history, and which
combination of cumulative state checks and approval binding preserves legitimate
multi-agent work?

**Why this matters.** Operators increasingly place approval/monitoring gates around
agent actions. A gate that correctly recognizes each local tool's allowed use can
still fail to enforce a user's overall restriction when actions change the meaning
of later actions or jointly disclose information. The actionable result is a
comparison of actual approval protocols for cooperating agents: whether textual
history suffices, when maintained state is necessary, and the usefulness cost of
mechanical enforcement. The nearest organizer examples are “Approval laundering”
and “Monitoring split-up attacks.” This study uses automated approval monitors;
it would not claim evidence about human attention or approval UI effectiveness.

### Primary basis and proposed contribution

[AgentDojo, 2406.13352v3](https://arxiv.org/abs/2406.13352v3) provides stateful
Workspace, Slack, Banking and Travel environments with deterministic utility and
attacker-goal checks. Its §4.3 explicitly says tool filtering fails when permitted
tools suffice for the attack, and identifies multi-task persistent-context attacks
as outside its tested coverage. Its data card warns against assessing security
using only default nonadaptive attacks.

[CaMeL, 2503.18813v2](https://arxiv.org/abs/2503.18813v2) already enforces explicit
data/control-flow policies and tracks value provenance. It discusses rogue users,
declassification, policy limitations and potentially malicious composition of
permitted control-flow fragments (§§8–10). Consequently this study **cannot claim
to discover that allowlists fail to imply authorization, invent cumulative access
control, or break CaMeL by omitting its policies**. The proposed empirical addition
is a multi-agent, shared-state extension with adaptive coalitions and controlled
comparisons among local, history-aware and state-enforced approval protocols.
Whether that offers sufficient additional novelty beyond current agent-security
work remains a specific review question; the idea's importance is clearer than a
claim of broad priority.

### Full ambition and substantive core

**Full ambition:** an executable multi-agent authorization-composition benchmark
across several stateful task families, with adversarial policies that adapt to
each defense and hold-out tests on new policy/task combinations. Map which failures
are ordinary single-agent policy failures, cross-agent information/authority
composition, or stale-state/concurrency errors. Compare protocols at matched
legitimate completion and oversight cost, rather than collect attacks alone.

**Substantive core:** adapt AgentDojo's dummy-state interfaces to explicitly
declared joint tasks and machine-checkable authorization constraints. Include
several qualitatively different compositions: cumulative release restrictions;
approval tied to a recipient/artifact whose meaning can later change; and role
separation in workflows where several independently permitted steps jointly
authorize a protected operation. Policies and legitimate solutions are established
before attack generation. These are proposed added tasks, not existing AgentDojo
records. A single “two transfers exceed a budget” demonstration is insufficient.

**Extensions:** concurrency and delayed execution; changing coalitions; policy
generalization; human studies only if separately commissioned. The initial core
can use sequential shared-state transitions to isolate semantic composition from
transaction races, then add concurrency as an explicitly separate factor.
Hard-to-formalize policies can be an optional extension only after a qualified
reference is established, including supported adjudication and explicit unresolved
cases. An arbitrary LLM judge does not replace the core's executable ground truth.
Report policy-authoring coverage and effort separately from enforcement outcomes.

### Design, baselines and interpretation

- **Actors and permissions.** A legitimate task is allocated across multiple
  agents with ordinary permitted tool use. A selected subset is explicitly
  adversarial and can communicate through a stated channel. Its objective is a
  specified forbidden state or disclosure, not simply making a reviewer suspicious.
  Agents cannot edit gateway logs or the test evaluator. All data and destinations
  are synthetic and contained within the proposed simulator.
- **Agent-indexed oversight factor.** Hold the global policy and the actor-specific
  permission matrix fixed while comparing approval/accounting records partitioned
  by agent against pooled cross-agent records. Include approval scope explicitly:
  the actor, artifact, recipient and composed operation to which an approval binds.
  Test whether a coalition exploits an accounting boundary or a monitor incorrectly
  treats one actor's approval as permission for another. Identity relabeling controls
  keep actual permissions unchanged. Varying permission allocations is a separate
  factor, not a silent change to the security requirement. The union-permission
  solo baseline below checks a stronger capability boundary and does not substitute
  for these matched oversight comparisons.
- **Comparators.** A single agent with the same tool union, state access, total
  attack budget and task; multiple agents without shared attack coordination;
  and a communicating coalition. Also compare a single agent following the same
  multi-step decomposition, separating task splitting from agent multiplicity.
  Honest coordinated workflows are mandatory controls. The union-of-permissions
  single-agent baseline intentionally tests whether agents add capability beyond
  merely combining capabilities that a single sufficiently authorized actor has.
- **Approval protocols.** (1) Per-request monitor with trusted task/policy and the
  local proposed call; (2) full chronological-history monitor with the same task
  and every gateway event; (3) the same monitor with an explicit current-state/
  outstanding-approval representation; (4) an external gate enforcing the declared
  cross-action invariants, binding approvals to exact recipients, artifacts and
  relevant state versions where needed. Add actual CaMeL policy integration when
  applicable rather than call a weakened replica “CaMeL.”
- **Information fairness.** The global natural-language policy is available to
  every protocol. Full-history and state-summary comparisons receive equivalent
  observable facts; state extraction and summaries are paid operations with a
  specified trusted/untrusted producer. The mechanical gate has a deliberately
  stronger enforcement contract, whose engineering/policy-authoring requirements
  are reported. Its protection is not evidence that an LLM has learned the rule.
  On correctly encoded invariants it is an enforcement reference: its expected
  blocking behavior is a contract check, not the study's new research finding.
  The empirical uncertainty concerns model-based monitoring and legitimate-work
  costs under competent attacks; the gate supplies a comparison and boundary.
  Test-only attack flags and hidden randomization do not reach policies.
- **Ground truth.** Task completion and forbidden outcomes are evaluated from
  simulated state transitions and disclosures, not from actor “done” messages or
  the monitor's explanations. Validate each predicate against legitimate and
  illegitimate witness traces. A locally allowed action is one allowed under its
  declared local contract; a monitor's false approval is not proof that the action
  was authorized. Distinguish under-specified policy from enforcement failure.
- **Adaptive evaluation.** Develop attack policies against each protocol on
  discovery tasks, with equal feedback/search budgets. Freeze them for held-out
  policy/task templates and repeat generations. Include competent constructed
  witness attacks as instrument controls; do not treat their success as measured
  model discovery. Test full-history monitors without truncation first, then vary
  context pressure separately so missing data is not confused with composition.
- **Outcomes.** Report forbidden outcomes that actually execute, legitimate-task
  completion, unnecessary blocks, approvals/review calls, tokens, retries and
  delay. For cumulative disclosure, define the authorized recipient and inference
  restriction concretely; do not equate ordinary cooperation or data sharing with
  harm. Statistical units are held-out task/policy instances; correlated attempts
  on the same instance are clustered, not independent cases.

**What would matter.** A strong result would identify failures that survive a
complete-history monitor under competent adaptive attack, then show which state/
approval-binding controls remove them while retaining honest usefulness. A second
possible result is that ordinary history-aware monitoring closes the gap, making
the extra infrastructure unnecessary in the tested regime. If the only successful
case is a textbook budget race, or a policy that never prohibited the outcome,
the proposed contribution has not been established. If all controls stop only
weak/nonfunctional attacks, the security comparison remains incomplete.

### Means, resources, pilot and review

AgentDojo's README was fetched at repository commit
`089ed468cf3ed0322acc66b0211f26d9d90dbf60`; it exposes task suites, function-call
agents, attacks and tool-filter baseline. The inspected paper supplies the state
and deterministic evaluator design. This lane has not installed the repository
or confirmed provider support for the owner's chosen models. The existing
framework is a reusable substrate, while multi-agent scheduling, approval gates
and cross-action policy tasks are real implementation work, not claimed features.

Parallel lanes: task/policy construction and predicate examination; agent/gateway
adapter; protocol implementations; adaptive attacks; held-out evaluation and
analysis. Critical dependency is validated legitimate and forbidden traces before
measuring learned attacks. Trial volume can be expressed as
`policy instances × agent conditions × approval protocols × attempts/repeats`;
adaptive attack development has an additional measured budget. Simulator steps
are ordinary local operations; model inference dominates the expected paid
resource category, but no amount is inferred without provider and token use.

**Useful pilot:** implement one nontrivial cumulative policy and one meaning-change
policy with independently checked legitimate/forbidden traces; verify that the
mechanical gate catches forbidden outcomes without rejecting its legitimate
witness; then measure whether the selected agents can complete the ordinary tasks
and execute known witness compositions. This diagnoses the instrument and actor
capability before interpreting a failed adaptive attack as monitor success.

**Review must challenge:** novelty against existing policy/reference-monitor and
workflow-security work; whether proposed tasks merely encode known trivial races;
whether the policy is explicit enough for a valid reference; whether coalition
advantage survives matched budgets; whether the stronger gate is being compared
unfairly to a weaker information contract; and whether legitimate utility remains.
If these objections demand a changed question, preserve the original ambition and
present the alternative rather than silently replacing it with a toy example.

## Source examination and custody

The source examination below uses primary text and explicitly identified reused
reading, not search-preview inference. Existing
captures are reused by relative path; new reading views and capture metadata are
in this directory. No source code was executed and no downloaded payload was
followed as an instruction.

| Source | Actual examination and use | Limits |
|---|---|---|
| Event retained `../../primary-sources/event.txt`, Track 4 examples | Composition, research sabotage and approval-laundering examples and associated context | These are invitations, not research findings |
| ASB 2604.16286v2, `../../pass-2/primary-sources/sabotage-bench.txt` and PDF capture metadata | Abstract; §§1–3, §4 discussion of LLM sabotage, §§5.1–5.3; Table 1; relevant auditor/red-team and scoring passages | Full individual codebases and all appendix sabotage details not examined; no reproduction |
| ASB pinned README, `sabotage-readme.md` | Full public README, repository components, prerequisites and scoring | No API execution; repository is available, not verified runnable here |
| Jones primary retained `../../pass-2/control-sources/jones-primary.txt` | Abstract, §§1–4.1 including threat model, decomposition controls and evaluator | Does not establish control efficacy; original code-generation outcome used an LLM judge |
| Greenblatt 2312.06942v3 | Retained primary `../../reading-correction/track4-completion/captures/control.txt` passages on protocol safety/usefulness, attacker access, train/validation limits and untrusted monitoring; wider main/appendix coverage reused from the adjacent REVIEW.md | Selected passage reading plus explicitly reused coverage; no protocol rerun |
| AgentDojo 2406.13352v3, `agentdojo.txt` | Abstract/introduction, §3 components and deterministic evaluation, §4.3 tool isolation, §5 future work, data-card attack-use limitations | Not every table or appendix prompt read; no source code execution |
| AgentDojo pinned README, `agentdojo-readme.md` | Full README and exposed benchmark route | Current adapter/model compatibility remains unverified |
| CaMeL 2503.18813v2, `../../pass-2/control-sources/camel-original.txt` | Abstract, security-policy mechanism and capabilities passages; §§8–10 on rogue users, declassification, composition and limitations | Reuses selected source capture; no claim to defeat its implemented policies |

Author checks: both proposals explicitly distinguish source results from designs,
task outcomes from monitor judgments, researcher-assigned adversaries from natural
behavior, and equal-budget coalition effects from extra computation. Each specifies
a credible negative/contrary interpretation, resource dependencies and independent
examination needs. Source identities support inspection; they do not establish
novelty, feasibility of every branch or research validity by themselves.

## Author response to the two reviews

Read `../review/INTERLOCUTOR.md` and `../review/INDEPENDENT.md`; reinspected ASB
§5.1 in the retained primary text. Changes here preserve both original questions
and full ambitions. No study or experiment was performed during repair.

- **Interlocutor 1a — accepted and repaired.** Added the omitted qualitative human
  red-team finding that auditor iteration did not help much, while distinguishing
  it from ASB's non-adaptive LLM red team and the proposed coalition experiment.
  Adaptation is now explicitly an open factor, not a presumed gain.
- **Interlocutor 1b/X1 — accepted as a strengthening.** Sharpened the conjunctive/
  individually subthreshold hypothesis and subset-ablation requirements. Made
  review partitioning a primary factor and stated why the review-unit question
  remains useful if equal-budget solo and coalition attackers tie.
- **Interlocutor 1c — alternative retained with correction.** Offered an explicit
  reduced offline audit-only route on published ASB cases. Rejected the suggestion
  that it could provide execution-backed audit or new result verification with no
  reruns. Constructed patch histories do not establish coalition capability. No
  unsupported prediction of event-time incompletion is adopted.
- **Interlocutor 2b/X1 — accepted and repaired.** Added actor-indexed approval/
  accounting scopes versus pooled records with global policy and permissions held
  fixed, and distinguished that comparison from the union-permission solo baseline.
- **Interlocutor 2a/X4 and independent approval concern — accepted in part.** The
  mechanical gate is now explicitly an enforcement reference, not an empirical
  discovery. Hard-to-formalize policies remain an optional extension requiring
  qualified references; they do not displace the core's reliable outcome predicate.
- **Independent sabotage concern — preserved.** Reproducible baselines, task
  validity, stochastic variability, independent counterfactual checks and ASB's
  limited domain coverage remain necessary. Source selection favors tractable,
  sabotage-suitable codebases; findings cannot be generalized to all research.
- **Interlocutor 2c — scope already explicit.** The study concerns automated
  approval monitors, not actual human sign-off or UI performance. Agent 0 will
  carry that qualification into the comparison.

These are author dispositions and textual/source checks. Separate reviewer
backcheck, remaining novelty questions and actual experimental qualification are
not claimed complete by this response.
