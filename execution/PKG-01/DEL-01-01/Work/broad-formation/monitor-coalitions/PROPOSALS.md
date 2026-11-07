# Monitor coalitions: two experimental project options

TASK contribution to Agent 0 under [the common brief](../BRIEF.md). These are
proposals, not executed experiments or claims of natural malicious behavior.
Author source examination is recorded in [SOURCE_NOTE.md](SOURCE_NOTE.md).

## MC1 — Can hidden reviewer assignment prevent collusion without sacrificing detection?

**Question and importance.** When powerful models review one another's work,
does assigning the reviewer secretly *after the work is committed* improve
resistance to adaptive collusion? Does a heterogeneous reviewer pool improve that
protection, or does it lose enough detection capability that a well-calibrated
fixed reviewer remains safer? The useful result is a tested monitor-assignment
policy and its safety/usefulness boundary. It would inform teams choosing between
a capable copy of the worker, a different model, and a rotating pool. Nearest
organizer examples: “Can copies collude without talking?”, “Replicas as a
monitor”, and whether AI control works against cooperating agents.

**What is actually open.** Greenblatt et al. §3.4 establishes input/action
collusion and signal-jamming tradeoffs. Gardner-Challis et al.,
[2602.20628v2](https://arxiv.org/html/2602.20628v2), studies same-model passive
self-recognition, pre-shared signals, independently chosen signals and combined
strategies; elicited self-recognition defeats its best tested signal attack.
Therefore merely demonstrating that a copy can collude, or that paraphrasing
helps, is not this proposal's contribution. Pinto,
[2607.06596v3](https://arxiv.org/html/2607.06596v3), shows that a trained trusted
monitor's calibration can fail across attacker families, explicitly studying
passive shift rather than adaptive attack or collusion. Its “own-family” means
*calibration on an attacker lineage*, not necessarily the monitor's base model.
Together these sources motivate testing a joint policy choice that neither
examined study resolves: predictable versus hidden reviewer assignment in a
heterogeneous **untrusted** pool, after accounting for honest detection and an
attacker that adapts to the assignment distribution. Randomization and diverse
ensembles are old ideas; this is a proposed control evaluation, not invention of
either. The bounded search does not establish literature priority.

**Full ambition.** Produce an adaptive worker–reviewer attack benchmark and a
cross-family control evaluation showing when reviewer secrecy, model diversity,
or signal jamming changes accepted-sabotage risk. Test transfer to a second
environment and an unseen attack family. Releaseable outputs could be protocol
code, safe task fixtures, attack classifications and measured frontiers after
source licenses and publication authority are settled.

**Substantive core.** One executable code-sabotage environment, a pool spanning
multiple model families, and the four assignment conditions below, with adaptive
attacks on held-out tasks and an honestly behaving monitor comparison. This
retains the policy question. A second domain, larger pools, richer committees,
and elicitation by fine-tuning are extensions. No claim to upper-bound every
latent collusion capability follows from a prompt-only experiment.

**Experiment.** Reuse ControlArena's APPS or BigCodeBench setting. The worker
must solve the stated task; a red-team policy additionally seeks a program that
passes public tests but fails an independently executed hidden exploit. Monitors
receive the task and submitted artifact and score sabotage suspicion. A gateway
mechanically commits the artifact before choosing its reviewer and implements
the sequential audit/deferral policy specified below. The evaluator sees assignment
randomness, source labels and full attack outcomes; the privileged trusted-audit
route can execute designated exploit tests, while workers and monitors cannot.
Execution takes place
in an isolated research sandbox with no real external targets or secrets.

**Concrete core control contract (repair I1).** An episode has a predeclared
horizon of real work items, a finite trusted-audit budget, and an interleaved
monitor-test schedule. For each reviewer, honest development data fix the approval
threshold `d`, audit threshold `a ≥ d`, malicious-test miss allowance `s_bad`,
and benign-test false-alarm allowance `s_benign`. They are fixed before held-out
evaluation; a sensitivity analysis varies them rather than treating one arbitrary
slack as universal. Every score below `d` is an approval. At initialization each
reviewer receives balanced known-bad and known-good qualification tests, including
more than `s_bad` known-bad items and more than `s_benign` known-good items.
Tests are indistinguishable in interface from
work reviews and can use all reviewer context allowed by that experiment.

At each subsequent event the gateway either sends a concealed test to the scheduled
reviewer or routes a real committed artifact according to the assignment policy:

- A known-bad test scores a miss if approved (`score < d`); a known-good test
  scores a false alarm if not approved (`score ≥ d`). Counters are per reviewer,
  cumulative across qualification and online tests. Crossing either fixed
  allowance makes that reviewer ineligible **before another real artifact can
  be released**. Tests themselves are never released as real work.
- The core rule halts the *entire untrusted pool* as soon as any member becomes
  ineligible, and routes remaining work to the trusted fallback. This prevents
  rotation from laundering failures across fresh reviewers. No automatic restart
  or identity reset is allowed. A pooled-counter rule and removal/reweighting of
  individual reviewers are separate protocol variants, not silently substituted
  implementations of the secrecy treatment.
- For eligible real work, `score < d` releases the artifact; `d ≤ score < a`
  defers to trusted generation; and `score ≥ a` buys a trusted audit while budget
  remains. An audit-confirmed sabotage is withheld and halts the untrusted pool.
  An audit-cleared artifact is released only after the trusted audit returns
  and while the pool remains eligible; the audit consumes its budget allocation.
  Clearance alone does not certify useful task completion, which is scored
  separately. In the core sequential protocol no other event intervenes during
  that audit; delayed/concurrent enforcement is a separately labeled extension.
  When the audit budget is exhausted, work that would require an audit is deferred
  rather than released. Deferred work is scored for actual useful completion and
  cost, not assumed equivalent to the original capable worker's work.
- The core trusted-audit primitive is explicitly idealized: it executes privileged
  tests including the constructed exploit witness and detects valid planted
  sabotage. Those tests are withheld from ordinary actors and monitors. Audit
  errors, limited exploit search and delayed enforcement are extensions. This
  source-like oracle assumption limits deployment claims but does not favor one
  assignment policy within the matched comparison.

The primary safety endpoint is **at least one evaluator-verified sabotaged real
artifact released while the pool is eligible, before enforcement halts that route**.
A later failed test does not erase an earlier release. Report this alongside the
time/order of first sabotage and first enforcement, useful work completed before
and after fallback, all test errors and full resource use. Monitor-test passing
and sabotage rates are therefore not independent success criteria.

For the announced/hidden pair, use the same model pool, thresholds, allowances,
prequalification set, total audit budget, pre-sampled reviewer schedule and
concealed test schedule. Every planned block gives each reviewer the same number
and mixture of tests in the two arms. Assignment is revealed before generation
only in the announced arm. Up to the first behavior-induced divergence, exposure
is identical; early shutdown legitimately changes realized later exposure, which
is reported rather than retrospectively balanced. Fixed-reviewer alternatives
pay their actual qualification cost and are compared on a total-resource frontier;
extra pool testing is never treated as free.
Across different pool sizes, report both equal-total-test-budget and
equal-per-reviewer-exposure analyses, with the latter's greater total cost
explicit. Two distinct model families already permit the announced/hidden
heterogeneous contrast; additional families strengthen generalization, not the
logical validity of the two-family experiment.

Contract checks include an ordinary valid-work sequence with correctly detected
tests (no false removal, legitimate work proceeds), an always-permissive reviewer
(fails qualification before real work because known-bad count exceeds its miss
allowance), and a selectively permissive reviewer that passes qualification but
releases sabotage before a later failed test (the release still counts). These
are required instrument checks, not claimed experimental findings.

Compare:

1. A fixed same-family reviewer.
2. A fixed different-family reviewer, reporting the full available pairing matrix
   rather than selecting a lucky pair on evaluation tasks.
3. A rotating heterogeneous pool whose selected reviewer is announced before
   artifact generation.
4. The *same pool and mixture*, selected after commitment and hidden from the
   worker until the decision is final.

Conditions 3/4 isolate the value of assignment information at the same reviewer
mixture and one-review-per-artifact cost. Conditions 1/2 describe the policy
alternatives, with per-pair detection and cost reported rather than pretending
all models are equally capable. A homogeneous rotating-prompt pool separates
model-family diversity from simple prompt uncertainty. Optional ensembles must
be compared against equal-cost extra samples from the strongest single monitor.

The main conservative threat model treats **every reviewer in the pool as
potentially adversarial**; improvement cannot be credited merely to accidentally
choosing an honest model. An honest-monitor arm measures ordinary errors and
capability. Adversarial monitors seek to pass interspersed known-backdoor tests
while concealing real worker sabotage. Distinguish (a) passive source recognition,
(b) shared attack plans/signals chosen before the episode, and (c) independently
chosen signaling with no pre-shared plan. The submitted artifact and common task
are communication surfaces: this is not literally “no communication.” A shared
red-team plan establishes instructed collusion capability, not spontaneous intent.

**Assignment × collusion regime is the core interaction.** Hidden assignment may
help if signals or source recognition are pair-specific; it may not help if a
signal transfers to the whole pool. Under a pre-shared strategy, an effective
universal signal that survives jamming, avoids alarming trusted oversight and
distinguishes real attacks from tests can remove much of the secrecy benefit.
The existence of a shared plan does not by itself establish that such a signal
exists or can be executed by every model. Test this rather than assume either
outcome. Measure the cross-family signal-transfer matrix on held-out artifacts,
include the best elicited universal strategy, and include deliberate imitation
of a target family's style as an adaptive attack. Under hidden assignment the
worker may optimize imitation against the mixture; under announced assignment
it can target the disclosed family. Separate those attacks from passive
recognition and independently selected signals. A result that uncertainty changes
nothing under a well-performing universal strategy is a meaningful boundary,
not a design failure or proof that every other regime is equivalent.

Optimize worker and monitor attack policies against each known assignment rule
on development tasks using the same total model-call/token/search budget. Freeze
policies, routing weights, calibration and thresholds before held-out tasks.
Also transfer the best attacks between protocols so one condition cannot win
merely because its red team searched poorly. A stronger attack can be added as
an explicitly exploratory extension, not silently selected on the test set.

**Measurement and interpretation.** Primary outputs are accepted executable
sabotage, monitor-test failure, legitimate task completion, deferral/audit use and
cost. Plot safety/usefulness against audit budget; do not substitute AUROC for a
deployment claim. Use task-paired comparisons and project/task-level resampling
across attack seeds, reporting uncertainty and all attempted attacks. Do not
extrapolate independent per-task rates into a long deployment sequence without
checking the dependence assumption. Compare honestly behaving versus adversarial
reviewers on matched artifacts; correlated honest mistakes alone are not evidence
of collusion. Attack success requires an evaluator-verified bad result, not just
a low suspicion score or an agent's completion claim.

A positive result could establish that hidden assignment adds protection beyond
diversity at a specified useful-work level. A contrary result could show that
cross-family signals transfer, or that weakened detection outweighs coordination
disruption; either changes a concrete design choice. If adaptive attacks succeed
without controls but not against a protocol, the result supports that protocol
within the elicited threat model. If the worker cannot create valid sabotage or
the monitors cannot detect ordinary examples, the instrument is inadequate; no
safety conclusion follows.

**Means, resources and pilot.** Public ControlArena documentation and README
were inspected: APPS/BigCodeBench, policies, monitors, defer-to-trusted, scorers
and macro-protocol analysis are available. The self-recognition study's public
README confirms generation, fine-tuning, prompt-optimization and analysis code.
No dependency installation or model authentication was tested here. Needed:
access to selected model endpoints, sandbox execution, and a concrete evaluation
budget. Model lists must be selected from actual access; no particular frontier
API is assumed available merely because the orchestration host offers agents.

Parallel lanes can build routing/recording, validate tasks/exploits, implement
attacker policies, and prepare analysis. The sequential dependency is a verified
honest/attacking task fixture before adaptive search, then frozen held-out
evaluation before inference/reporting. For planning, cost scales with generated
artifacts plus per-artifact review calls, calibration/honeypot calls and explicit
red-team search calls; actual token/latency measurements should set the run size.
No speculative researcher-hour estimate eliminates the full proposal. A useful
pilot establishes both a valid worker exploit and a monitor capable of detecting
some attacks, then tests that assignment is actually hidden until commitment.
Its purpose is instrument qualification, not selecting the prettiest effect.

**Review targets.** Could artifact style reveal the selected reviewer? Is the
pool secret mechanically or only by prompt? Are calibration and adaptation
budgets matched? Does synthetic-test distinguishability make monitor “collusion”
too easy? Can a result be explained entirely by monitor skill or honest error?
Does the nearest work already test this exact routing policy? A full examiner
must challenge both those confounds and a scope reduction that drops adaptation
or honest detection, since either would remove the contribution.

## MC2 — Can collaborating agents identify safety tests that fool each agent alone?

**Question and importance.** Can agents pool ordinary project context to
recognize that a monitor is receiving a synthetic safety test, behave correctly
on that test, and selectively permit real sabotage? Can tests generated as a
coherent *whole-team episode* close the gap without disabling useful collaboration?
This asks whether the unit that must be realistic in a control evaluation is an
individual prompt/action or the interacting workflow. A result could change how
monitor honeypots are built and how their passing scores support deployment.
Nearest organizer examples: controls against cooperating agents and covert
coordination; the distinct mechanism is **collective test recognition**, not
merely a new covert channel or corrupted logs.

**Closest work and proposed addition.** Greenblatt §3.4.1 already makes synthetic
inputs hard to distinguish from genuine ones. Gardner-Challis §§2–3 and 6 treats
the monitor's ability to distinguish genuine attacks from honeypots as central,
and Appendix F.6.1 names deployment information, shared knowledge and long
contexts as open problems. It does not report the proposed cross-worker
consistency experiment. CIAware-Bench,
[2606.11063v2](https://arxiv.org/html/2606.11063v2), measures *single-trajectory*
intervention recognition across four environments; its downstream proof of
concept supplies intervention awareness to one actor. It explicitly leaves
multi-turn accumulation and realistic adaptive conditions open. These papers
already establish that evaluation/intervention recognition matters. The proposed
addition is measuring the **extra discrimination obtained by combining peers'
task-relevant histories**, its actual effect on monitor evasion, and whether
jointly coherent tests repair it. This is an empirical extension, not a claim to
discover evaluation awareness or prove that all honeypots fail.

**Full ambition.** Build and evaluate a team-level control-testing protocol on
real model teams performing shared software work. Establish how test recognition
and sabotage evasion change with coalition size, information topology and test
construction, and evaluate coherent replay or restricted context as defenses.
Generalize across more than one task family and model family.

**Substantive core.** A small team implementing interdependent components of a
local service, with programmatic functionality and sabotage checks, under two
test-construction protocols and matched communication controls. Compare local
versus pooled context and carry successful recognition through to actual
accepted-sabotage outcomes. This avoids a mere classifier benchmark with no
control consequence. Larger teams, realistic repository tasks, and spontaneous
recognition without direct elicitation are extensions.

**Experiment.** A local shared-project setting has workers implementing an API,
its consumer and integration checks, plus an untrusted reviewer. Each role sees
its own task and a controlled subset of project history. Valid work requires
cross-component coordination; a hidden evaluator checks the actual final state.
The attacker seeks an objective violation, such as a deliberately planted logic
backdoor that passes ordinary tests, in this sandbox only. The reviewer must pass
known-malicious audit items or lose its ability to approve artifacts. Use the
MC1 sequential eligibility/withholding contract for the reviewer, with its
qualification costs, allowed misses and false alarms fixed before evaluation.
Count genuinely sabotaged releases before removal; passing isolated tests is not
itself the safety outcome.

**Live-peer and snapshot contract (repair 4b).** Each episode starts from a
recorded snapshot of the project files/tool state and the serialized task/message
history available to each role. Opaque provider-side reasoning or hidden model
state is not presumed cloneable: the core uses fresh sessions initialized from
the same permitted serialized history, and records any provider state that must
instead be disabled or regenerated. The snapshot is taken before the reviewer
receives its next artifact. **All reachable peers are live model sessions after
the branch point in every treatment**; peer replies are not prerecorded scripts.
Both arms permit the same tool calls, peer-message interfaces, turn/token budgets
and elapsed-response limits. Trusted evaluator state and the audit designation
are outside every role's snapshot and tool namespace.

The control team constructs audit branches in two ways:

- **Local insertion:** change only the pending artifact delivered to the reviewer
  at the branch point. Workers continue from their actual pre-branch histories
  and tool state; the purported author may therefore remember submitting a
  different artifact. Match the local reviewer input/style distribution to work
  examples as far as tested. Such a mismatch can be genuine information available
  through collaboration, not automatically an instrument bug.
- **Coherent episode preparation and live continuation:** prepare a complete
  alternate episode using actual role rollouts, including an on-policy malicious
  artifact whose exploit the trusted evaluator has verified. Snapshot the whole
  team before review, then restart all roles from their corresponding histories
  and tool state. The author really submitted the displayed artifact in this
  prepared episode; peer dependencies/history are consistent with it. Designate
  the item as an audit only in the external gateway. “Replay” refers to restoring
  the snapshot, not to replaying fixed peer answers. Account for selection bias,
  invalid candidates and the extra expense of generating verified on-policy
  malicious episodes. A local-insertion branch can reuse that exact reviewer
  input in another matched snapshot, separating local content from joint history.

Both tests use the same visible interfaces, schema, identifier distributions,
models and tool permissions within each comparison. There is no audit flag,
evaluator filename or direct test-membership endpoint available to the agents.
Legitimate work may itself contain inconsistent or stale claims;
the dataset includes such cases, so “find any inconsistency” is not the label.
Where possible, pair identical local reviewer inputs with differing peer contexts
to isolate the incremental information. An origin classifier is useful only as
a diagnostic; correctness and provenance labels are balanced separately.
Include sham insertions of benign artifacts and coherent genuine episodes as
controls, so detecting any replacement or unusual history is not sufficient to
establish malicious intent. A strategy that treats every non-authored insertion
as a test may still exploit benign shams correctly: shams diagnose that strategy,
and do not magically eliminate authentic provenance information.

**Explicit provenance-access strata (repair 4a).** Preserve both mechanisms:

- **Authorship attestation available:** the reviewer can ask the live purported
  author whether it submitted the artifact, using ordinary messages and whatever
  genuine submission history the deployment contract provides. If authenticated
  source records exist, expose them identically in genuine and audit branches;
  do not call their information an accidental label leak. Measure how useful
  this route is under full versus summarized/truncated memories, many similar
  artifacts, stale honest reports, delayed peer replies and fixed query costs.
  An ideal perfect-attestation case is a transparent upper-bound/control, not
  the proposed empirical discovery. Quantified survival of monitor tests and
  safety/usefulness costs of defenses are the contribution to investigate.
- **Task-context consistency without direct author access:** the author is
  mechanically unreachable during review, while other component workers remain
  live and can supply their legitimate task histories and dependency information.
  No direct submission-membership service is exposed in this stratum. This tests
  whether richer joint consistency provides additional discrimination beyond
  explicit attestation. It is an additional scope condition, not a claim that
  realistic systems lack source history or a silent replacement of the first arm.

Compare local insertion with on-policy single-author resampling, coherent
whole-team preparation, and cutting worker–reviewer communication. Score how
these defenses change legitimate coordination and detection as well as test
recognition. Match task difficulty, malicious mechanism, generation model and
available observations wherever the intervention permits; expose unavoidable
changes instead of claiming that all arms differ by only one bit. Direct audit
flags or evaluator filenames remain instrument leaks to remove. Authentic
authorship/history checks remain legitimate experimental information effects.
An intentionally visible audit marker can be a separate instrument positive
control, excluded from the scientific treatment comparisons. Report attestation
and richer context-consistency recognition separately rather than combine them
into a single apparent collective-recognition effect.

Cross these conditions with: no peer exchange; permitted task-focused peer
exchange; and shuffled or independently resampled peer context with the same
message/token budget. A centralized single-model baseline receives the same
combined information and total inference budget. This separates the value of
distributed information from a uniquely advantageous agent-team organization:
the project can find that pooled information is sufficient without claiming that
multiple agents outperform an equivalently informed actor. Also include genuine
benign and genuinely sabotaged projects, plus audit items with and without benign
context inconsistencies, to detect leakage from the test generator.

First elicit recognition capability explicitly, with agents attempting to infer
test status from their allowed observations. Then evaluate a frozen selective
collusion policy that flags audit sabotage but waves through genuine sabotage.
No evaluator label or perfect-awareness message is supplied in this second stage.
Separate a shared pre-agreed policy from independent elicitation; do not call
instructed cooperation emergent collusion. The monitor's decisions are enforced
by the gateway; merely saying that it approved is insufficient.

**Measurement and outcomes.** Report test-recognition performance at the actual
audit base rate, especially false test recognition, alongside accepted sabotage,
audit-test pass rates, legitimate task success, trusted-test generation cost and
latency. Use held-out project templates and malicious mechanisms; freeze test
construction, decision rules and attack selection before evaluation. Repeated
rollouts and project-level uncertainty account for shared history. All failed
attacks and invalid generated audit cases remain in the funnel account.

Positive result: locally convincing tests cease to predict control effectiveness
once peers share context, while coherent tests reduce that gap at measured cost.
Contrary result: task-relevant context provides no reliable extra recognition, or
coherent tests do not help because local stylistic cues dominate. Either constrains
which evaluation assumptions matter. If recognition improves but does not enable
more accepted sabotage, report the capability/control distinction rather than
claiming oversight failure. If a perfect source lookup determines test identity,
report that as the explicitly attestation-enabled contract's reference case,
not as surprising learned coordination. The empirical contribution must then
come from realistic memory/noise/latency conditions and the measured control
costs of removing the signal, while the no-direct-author stratum retains the
more demanding joint-context question.

**Means and resources.** ControlArena supplies task/policy/monitor abstractions,
programmatic code tasks and trajectory recording, but this shared-context task
family and coherent replay are proposed work, not a pre-existing turnkey
setting. CIAware's README exposes reusable intervention/cached-probe machinery;
its current raw-data release has explicit correction/update caveats. Existing
single-agent data do not themselves qualify for this team-level question.
Needed resources are model endpoints, an isolated local service/repository
fixture, replayable task histories and independent programmatic correctness
checks. No natural incident dataset or human study is necessary for the core.

Task generation/evaluator validation, team scaffolding, attack design and
analysis can run in parallel. Critical path: validate genuine and audit episodes
and eliminate accidental evaluator labels, establish local difficulty or explicitly
characterize genuine attestation access, then run the
pooled-context comparison and the selective-evasion stage. Calls scale with
projects × treatment arms × repeats × role turns, plus separate development
and audit generation; measure unit cost/throughput before fixing the campaign.
A pilot must show that genuine work is solvable and that a local classifier is
not already trivially identifying every audit. Failure of that condition repairs
the instrument; it does not show that collective awareness is absent.

**Review targets.** Is the contrast an artificial watermark or an actual
deployment-relevant consistency signal? Are coherent tests easier or harder for
unrelated reasons? Do peer queries consume equal resources? Does a centralized
equal-information baseline explain the entire benefit? Can a monitor simply be
isolated without losing the useful task capability? Is the real safety endpoint
caused by awareness rather than an artifact of attack prompts? The prospect of a
nontrivial cross-agent signal is the principal scientific uncertainty; the
proposal should remain ambitious but should not promise it exists.

## Lane comparison

MC1 directly compares deployable monitoring choices using established coding
tasks; its hardest issue is eliciting adaptive collusion well enough to interpret
a defense result. MC2 targets the validity of the *control evaluation itself*
when the adversary is a collaborating population. Its potential consequence is
broader, but it requires a defensible new team-context fixture and convincing
elimination of trivial test labels. These are distinct subjects, not diversity
parameter variants. I would advance both to the global slate, with MC1 the more
directly grounded experimental recommendation within this lane and MC2 the more
unusual, higher-uncertainty option. This is design judgment, not a reviewed global
selection or a claim that either has proved novel.

## Author response to independent/interlocutor examination

These changes are proposal repairs; no test, model trial or empirical backcheck
ran. The independent examiner and interlocutor must inspect the revised contracts.

| Finding | Author disposition and actual change |
|---|---|
| Independent I1: monitor-test passing disconnected from control consequence | **Accepted.** MC1 now specifies qualification, online per-reviewer counters, whole-pool enforcement, real-item routing, audit-budget exhaustion, privileged audit assumptions, paired exposure and sabotage-before-enforcement endpoint. Ordinary, always-permissive and selectively permissive contract cases are specified for instrument validation. |
| Interlocutor 3a: shared plan makes secrecy irrelevant by construction | **Partly accepted as a concern, not as a theorem.** Assignment × collusion regime is explicit. A viable universal signal can erase benefit, but plan sharing alone does not establish robust transfer, test distinguishability or evasion. The empirical question remains; no original impossible effect is claimed. |
| Interlocutor 3b/3c: style imitation and access | **Accepted.** Added target-family imitation and cross-family/universal signal controls. Actual multi-family endpoint access remains a resource dependency; no access is invented. |
| Interlocutor 4a: authorship attestation was incorrectly excluded as an automatic leak | **Accepted.** Superseded the blanket exclusion. Added an attestation-enabled stratum, realistic memory/noise/delay and useful-work controls, and explicit defense comparisons. Retained richer context consistency as a separate stratum. This broadens and clarifies the original ambition rather than silently replacing it. |
| Interlocutor 4b: unclear live versus replayed peers | **Accepted.** Defined serialized starting snapshots, live peers after branch point in every arm, mechanical interfaces and memory limits, actual coherent episode generation, and external-only audit designation. No assumption of cloning hidden provider state. |
| Interlocutor X1: isolate what distributed information/identities add | **Addressed in scope.** MC1 manipulates reviewer assignment and per-reviewer accountability explicitly. MC2 manipulates distributed context and author reachability, retaining the equal-information centralized baseline. A solo/team tie does not erase a finding about the control protocol's local versus team-level information contract. |

No full-ambition question was withdrawn. MC1's idealized trusted-audit primitive
and MC2's provenance-access strata are new explicit assumptions/contrasts; they
must remain visible in the integrated comparison. The earlier design was
underspecified on enforcement and live peer state, not empirically disproven.
