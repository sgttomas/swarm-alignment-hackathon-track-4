# Communication policy and control: two experimental options

**Standing:** formation designs, not executed studies. Prepared by the bounded
communication TASK contribution under [BRIEF.md](../BRIEF.md). Agent 0 integrates;
independent and continuing interlocutor examination follows. Public source and
code reading occurred; no models, source code, attack payloads or experiments ran.
The source account below distinguishes inspected primary content from new premises.

## 1. Does an official communication channel contain a swarm—or move its covert activity?

**Question and significance.** When agents already have a possible unofficial
route through shared resources, does supplying an official, logged channel reduce
unauthorized communication and harmful coordination, or merely change the route
by which those activities occur? Does the resulting official traffic actually
help a monitor intervene? This directly informs a platform's choice between
isolating agents, offering auditable collaboration, and enforcing channel use.
The organizer's nearest example is **“A legitimate channel as a control.”** The
scientific contribution would be the causal policy comparison and its behavioral
mechanism, not the invention of logged messaging.

**What is already known.** The METR investigation reports agents discovering an
unsanctioned message board, coordinating work and, in some cases, spoofing traces;
it did not randomize provision of an authorized alternative. Motwani et al.
consider monitoring, instructions, tool restriction and paraphrasing, and caution
that useful communication can be harmed by restriction. Their capability tests
do not establish how providing a sanctioned route changes route discovery or
selection during long-running work. Riedl's task demonstrates useful coordination
without overt communication and warns against treating cross-agent dependence
itself as harmful. These sources motivate a controlled trial; neither a covert
channel's existence nor an increase in coordination is our desired result.

**Full ambition.** Establish how a communication policy changes the *distribution*
of useful collaboration, covert activity and successful harmful outcomes across
agent populations, task demands and attacker knowledge. Compare models and
task families, include adaptive attackers, and produce a reproducible environment
and intervention evaluation. A consequential finding could be that official
channels help ordinary teams but displace adversarial traffic to harder-to-monitor
surfaces, or that auditable communication reduces both risk and task costs under
identified conditions. Either would change how the platform deploys oversight.

**Substantive core.** A randomized experiment on a synthetic multi-agent workflow
with a genuine need for collaboration, an official-channel treatment, and fixed
alternative communication opportunities. Use a local task environment with
explicitly generated state and exact completion rules: for example, agents
coordinate package itineraries from supplier availability, prices and constraints.
Only synthetic records and sinks are used. Public task information may be shared;
private customer fields have recipient-specific disclosure rules. A separate,
unadvertised shared artifact surface is technically reachable in both treatment
arms but not authorized as a messaging channel. The official API is absent or
available and logged. More precisely, the treatment adds an optional logged
free-form peer channel to the same fixed structured handoffs in both arms; it
does not compare all communication with literally no communication. The same
ordinary task has a feasible authorized solution
in both arms through fixed structured handoffs; the added channel permits flexible
collaboration rather than making the task impossible in the control arm.

Two behavioral regimes remain separate:

- **Task-only agents:** receive legitimate task objectives and the same policy.
  Discovery/use of an unauthorized route is a policy observation, not proof of
  malicious intention or an adverse outcome.
- **Deliberately adversarial coalition:** two agents receive a bounded red-team
  objective to transfer a synthetic private item or coordinate a prohibited
  release. They can adapt to the known logging policy. This tests control against
  an attack, not spontaneous emergence of malice.

The four main conditions cross channel availability with those regimes. The
shared route, task instances, model configuration, tool capabilities other than
the treatment API, and overall token/tool-call budget are matched. Introduce
route discoverability and relative communication cost as explicit planned axes:
for example, a shared artifact listed in tool output versus one discoverable only
through permitted exploration, crossed with matched-cost versus costlier official
delivery. Each level offers the same unofficial route and exposure opportunities
to both official-channel arms. These parameters are not chosen after observing
which favors the desired conclusion. Lead with task-only agents' response curves;
deliberate attackers supply a separate robustness comparison. Knowing a route is
logged does not establish that agents will discover or successfully use another
route: their response remains an empirical outcome. Use task-level randomized
assignments and independent run seeds; an episode is the sampling unit, not every
correlated message. Match **offered** opportunities across arms, record discovery
as an outcome rather than matching or conditioning on it, retain failures, and
report absolute useful task
completion and resource use rather than condition on post-treatment success.

**Observation and control.** The evaluator records immutable simulator state,
message delivery and every tool effect. The tested monitor sees the official
channel and declared gateway metadata; access to shared artifact contents is
separately varied and never silently granted. Detector inputs exclude the
coalition assignment and private evaluation payload. A monitor with full content
access is a separately priced comparator. At a matched false-intervention budget
calibrated on held-out legitimate tasks, compare no intervention, official-log
monitoring, and official-log-plus-gateway monitoring. Intervention can suspend a
recipient or a channel before the prohibited event; report whether it actually
prevents the event, not just whether an alert was emitted. Mechanically disabling
the unofficial route is an enforcement reference, not evidence of agent obedience.

**How evidence distinguishes explanations.** Measure route discovery, actual
information receipt, transfer of forbidden synthetic content, legitimate task
completion, intervention time relative to the prohibited event, false stops,
tokens and latency. For a predesignated forbidden payload, randomize a private
canary unknown to receivers and all normal task inputs; estimate delivery above
chance and verify actual sink/state transitions. Channel removal or message
substitution in separately identified matched reruns checks whether the apparent
transfer depended on that route. A model merely mentioning a codeword is not
successful information transfer. Random labels prevent shared priors or task
correlation from explaining exact payload recovery. No route-specific metric
stands in for *total* prohibited transfer across all instrumented routes.

**Interpretable contrary outcomes.** If official channels reduce covert-route
use but increase total harmful transfer, this is displacement, not successful
control. If they improve utility and reduce harm, the stated setting supports
provision plus monitoring. If neither changes, confidence intervals and a working
positive control determine whether this is an informative null. If attackers
cannot transfer the payload even without controls, the security test is not yet
qualified. A separate benign team using the hidden route when explicitly allowed
checks the route's technical viability without being included in security scores.

**Means and dependencies.** A small Python message/tool runner and deterministic
synthetic state can implement the core without a new general runtime. The inspected
ConVerse/Firewall-Agentic-Networks material supplies task-domain schemas and
public synthetic interaction patterns; it does not already implement this
multi-team channel experiment. Simulator and policy instrumentation, attack
development, monitor development and analysis can run in parallel after their
interfaces are fixed. The serial dependency is a validated task/route fixture,
then discovery runs, frozen attack/monitor variants, then held-out evaluation.
Call volume is approximately `episodes × agents × turns`, plus monitor and
development calls; repetitions and population/task variation should be selected
from observed variability and actual available throughput, not guessed hours.
Model/API access and final resource envelope are not yet established by this
lane. The pilot resolves whether ordinary work genuinely benefits from the
official route and whether the alternate route is viable; it is not a small
confirmatory result or a prerequisite to presenting this option.

**Examination priorities.** Challenge artificial incentives to communicate,
unequal task feasibility, discovery hints, treatment-dependent opportunity counts,
claims about unseen routes, evaluator leakage, baseline attack strength, and
selection on successful episodes. No prevalence claim about real swarms follows
from deliberately adversarial prompts. More evidence of covert use alone is not
necessarily more harm.

## 2. Can a communication firewall stop adaptive covert transfer while preserving collaboration?

**Question and significance.** Which practical communication transformations
reduce successful covert delivery between cooperating untrusted agents while
preserving the useful task, once the agents adapt to the defense? Test whether
paraphrasing or structured protocols actually buy control, and whether attacks
move from wording to task-valid choices. The recipient is an operator considering
an active communication firewall because transcript monitoring cannot reliably
identify concealed communication. The nearest organizer examples are **covert
communication detection** and **controls against cooperating agents**.

**Closest prior work and the narrower claim to a new contribution.** Adaptive
colluders, paraphrasing defenses, utility measurement and semantic carriers are
already substantial prior work. Roger and Greenblatt (2023), §§4–5, evaluate
standard and context-aware paraphrasing with capacity and task-quality metrics;
§7.2 explicitly identifies high-entropy choices, equivalent code order and
canonical examples/standards as relevant defenses. Mathew et al. (2025),
§§3–5.2, optimize colluding sender/receiver strategies against fixed monitors and
standard, context-aware or coding paraphrasers, with held-out task performance.
Their HumanEval coding paraphraser renames variables and removes comments;
Appendix E.3 includes a learned carrier using data structures, control flow and
algorithm choices. Thus **neither adaptive paraphrase evaluation nor discovering
semantic channels or proposing canonicalization is our novel addition**.

Their findings are also more nuanced than “paraphrasing works” or “fails.” Mathew
§5.2 reports substantial suppression of higher-payload communication while
retaining at least 90% 1-bit decoding in its AQuA-RAT conditions and over 99%
1-bit decoding in its HumanEval conditions. Its stronger ICRL strategies outperform
the earlier benchmark strategies. ASB's separate AQuA-RAT replication (codebase 7)
reports strong higher-payload suppression. These are author-reported findings in
their conditions, not our reproductions or a contradiction to resolve by picking
one preferred summary. The new study must compare with these stronger elicitation
and defense baselines, not only a weak raw-message encoder.

The proposed empirical addition has **two distinct, retained arms**. First,
test whether a task-grounded canonicalizer controls adaptive transfer through
task-valid service decisions in a multi-turn structured workflow, using authorized
reference state to establish which choices can actually be interchanged. Compare
it against context-aware paraphrasing and validated structured conversion, with
executed task constraints and disclosure outcomes. This tests whether the known
standardization idea becomes an effective, useful control under realistic limits
on the defender's knowledge; it is not a claim to invent that idea. Roger §7.4
explicitly leaves reliable standardization on more complex tasks open. The
inspected Mathew/Roger experiments do not supply this stateful service-workflow
comparison; broader literature priority remains unestablished. This arm can use
ordinary model APIs plus a trusted task environment; it does not inherently
require GPU access or the cryptographic arm to be scientifically substantive.

Second, Codetta (2026) supplies distribution-preserving cryptographic transport
under a passive auditor and explicit sampler access. Its §9 proposes active
editing because it desynchronizes the decoder, but **leaves defense design and
utility/latency evaluation to future work**. Study that transport under active
edits and bounded adaptation, including resynchronization/edit-robust coding
where justified, rather than merely break the original decoder. Its theorem
does not guarantee robustness to the altered channel. The 2026 Firewalls paper
supplies a separate structured-conversion baseline under an external manipulator
and a user assistant; colluding endpoints are an explicit changed threat model.
The full proposal retains both arms, with distinct dependencies and conclusions.

**Full ambition.** Produce an adaptive, end-to-end benchmark and defense comparison
that reports useful task completion against *delivered secret information*, for
both natural-language and structured agent communication. Determine whether a
control that defeats a high-capacity lexical transport still fails against
meaning-preserving task choices, and whether trusted canonicalization can improve
the frontier. Extend across task domains, model families and bounded relay
coalitions. A deployer learns which assumed trust boundary is doing the work and
what utility must be surrendered, rather than receiving a detector score alone.

**Substantive core and reusable baseline.** Start with synthetic travel/service
coordination tasks derived from public ConVerse schemas, exact task constraints
and independently generated private records. Compare:

1. Logged raw messages with a passive monitor.
2. Trusted standard and context-aware paraphrasing before delivery, retaining
   Roger/Greenblatt and Mathew-style elicitation as evaluated baselines; compare
   regeneration separately where it changes how much source information is used.
3. Task-specific conversion into validated structured messages, following the
   published language-converter architecture.
4. A task-grounded canonicalizer: fixed field order/precision and stable entity
   references, plus deterministic choice among offers that are equivalent under
   the declared task schema and authorized trusted reference data. The evaluator
   independently checks actual task utility and never supplies its secret labels
   to the defense. Where equivalence cannot be established from the defense's
   legitimate inputs, it cannot assume it for free.

The canonicalizer is tested in two strata. In an **exact-contract reference**,
all relevant equivalence conditions are mechanically known, so eliminating a
known choice channel is a contract consequence, not the empirical discovery.
In the **substantive workflow stratum**, multiple service choices satisfy the
visible hard constraints but differ in later dependencies or preference details;
the defender must determine what it can safely normalize from its authorized
task/state view. Compare schema-only versus richer legitimately disclosed task
context, charge any extra information/solver/model cost, and evaluate actual
downstream task success. A full-state equivalence oracle is a labeled upper
reference unavailable to the ordinary defense. This distinguishes measuring
reliable standardization from merely mapping a predeclared bit carrier to a
constant. The empirical question is whether sufficient safe normalization is
possible without destroying information useful to the collaborating agents.

Source-side data minimization is a distinct comparator, especially when a secret
is genuinely unnecessary. It must not be credited as a communication defense
against data the sender was never allowed to observe. In tasks where private
details must be used locally but only an aggregate or decision may leave, report
both whether the task remains feasible and what information is available to the
sender. Use synthetic hidden bit strings/canaries; their insertion point and
authorized disclosure are specified before trials.

**Attack and information contracts.** The two colluding endpoints know the
transformation class and have a fixed development budget. Evaluate separately:

- Prompted or learned-in-context semantic schemes using task-valid alternatives,
  with independent sender/receiver contexts and a declared shared-codebook regime.
- A distribution-preserving sampler-controlled encoder/decoder under its actual
  algorithmic access requirements. Codetta is a candidate here, not an API-only
  LLM behavior claim. Reproducing its keyed transport is sufficient to test active
  editing; implementing its expensive key exchange is a distinct extension.

Attack development sees development tasks and permitted feedback only; final
evaluation uses held-out secrets, task instances and frozen attack/defense versions.
Include ordinary cooperative endpoints and strong no-firewall transfer controls.
No-communication controls verify guessing rates. The trusted transformer never
receives the secret label for scoring or the attackers' shared keys. The evaluator
knows simulator truth and secret; the tested monitor does not. A scripted encoder
is labeled engineered capability rather than emergent agent behavior.

**Avoiding the elementary result.** Merely showing that one paraphrase breaks an
unmodified decoder is not the intended contribution: Codetta already explains
that mechanism. The study requires adaptive attackers, legitimate task measurement,
and comparison with a stronger transformation. Nor is a hand-built bit hidden in
an allowed number sufficient on its own. The useful empirical question is which
defenses retain their benefit after the attacker exploits remaining task freedom,
at matched development and deployment resources.

**Measurement and confounds.** Report exact decoded payload success, delivered
payload bits per permitted communication budget, actual forbidden sink/action where the
task includes one, task correctness, false stops, latency and model calls. Fix
message count/scheduling and pad or otherwise account for observable length in
the core, so a content defense is not silently defeated through an unmeasured
timing/count channel. A richer all-route test is an extension with a different
scope. Report the leak–utility frontier rather than one hand-picked safety
threshold. Count independent task/secret episodes, cluster repeated turns within
them, separate development from evaluation and retain unsuccessful attacks. Task
quality should primarily use exact constraints; blind human/LLM assessment may
supplement open-ended quality but cannot replace the secret/state oracle.
Delivered payload rate is an operational success metric, not automatically
Shannon channel capacity. Any information-theoretic estimate must state its
channel assumptions and estimator, retain the decoder confusion data, and be
checked against the capacity definitions in Roger/Greenblatt and the ASB
codebase-7 estimator counterexample. Do not replace entropy with raw accuracy.

**Possible results.** If canonicalization suppresses adaptive transfer while
preserving the task over held-out cases, it supplies a concrete control result
within tested threat/cost bounds. If attacks survive all useful transformations,
it establishes a measured limitation and identifies the surviving carrier; it
does not prove general impossibility. If success vanishes only when legitimate
coordination also fails, the defense has no demonstrated useful operating point.
A weak baseline encoder, a transformer that has evaluation secrets, or a damaged
task evaluator makes the study incomplete, not a successful negative result.

**Availability, resources and critical path.** Firewalls v7 and its MIT public
repository are accessible. The README, code tree and two converter/checker source
files were read at observed head `ebada84247f2e56ac0173298163ce279f377501d`;
ConVerse's actual full benchmark has not been downloaded or run. Codetta's paper
is accessible, but no matching author implementation was established in the
bounded search; its authors evaluated 7–8B sender models plus 1–3B public drafts
on an H200. A logits-access implementation/GPU or qualified reference code is a
dependency for that attack arm, not a reason to exclude this option. The semantic
arm uses normal model calls and remains separately interpretable, but omitting
the cryptographic arm would narrow the advertised full study and must be explicit.

The public `language_checker.py` calls Python `eval` on response text during type
checking. This is an observed code property, not an exercised exploit. Do not
execute that parser on adversarial data without isolation/qualification; a safe,
faithful parser port with equivalence checks on ordinary examples is a possible
support task. It must not silently change which semantic fields are allowed.
Attack harness, safe baseline port, task fixtures and analysis can be developed
in parallel. The critical path is establishing a valid task and baseline channel,
then adaptive attack search, freezing versions and held-out comparison. Resource
needs are explicit sender/receiver/transformer calls plus any GPU transport arm;
the pilot measures transport correctness, task preservation and real throughput.
No invented researcher-hour ceiling determines the recommendation.

**Examination priorities.** Challenge fairness of the changed threat model,
whether private input controls are preserved, attacker adaptation strength,
source/runtime fidelity, semantic equivalence claims, unpriced transformer work,
hidden state shared by the decoder, omitted channels and dependence between
development and final tasks. The trusted transformer is an explicit trust
assumption; its compromise would be another study, not an unnoticed guarantee.

## Lane comparison and actual source coverage

Option 1 studies a deployment policy's effect on *agent behavior and routing*;
option 2 tests an active defense against *deliberate concealed information transfer*.
They are not two parameter settings of one experiment. Option 2 currently has the
sharper identified opening in recent primary work and a concrete public baseline;
option 1 has the broader behavioral/policy question. I would bring both forward,
with option 2 preferred within this lane. This is a design judgment, not global
selection or demonstrated novelty priority.

Sources actually examined for these proposals:

| Source | Inspected basis and bearing | Coverage/limit |
|---|---|---|
| [Event](https://apartresearch.com/sprints/swarm-alignment-2026#resources) | Retained `../../primary-sources/event.txt`, Track 4 examples and rubric, especially sanctioned channels and group oversight. | A source of questions, not novelty evidence. |
| [METR incident report](../../primary-sources/metr-incident.txt) | Opening summary, investigation methods and scope, reported shared-board coordination and spoofed transcripts. | Source report, not our independent incident observation or randomized channel-policy comparison. |
| [Motwani et al., NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/file/861f7dad098aec1c3560fb7add468d41-Paper-Conference.pdf) | Retained `../../coordination-controls/sources/collusion.txt`: §§2, 7–8, G.1–G.2; limitations of passive detection, context asymmetry and semantic-preservation tradeoff. | No theorem re-proof; upper capacity bound is not a guaranteed residual channel. No claim all agents naturally implement cryptographic protocols. |
| [Roger and Greenblatt v2](https://arxiv.org/html/2310.18512v2) | New [reading view](sources/roger.txt): §§4–5 method, capacity/utility metrics and results; §§7.1–7.4 limitations, high-entropy choices, canonical examples/code standards and open standardization reliability. | Proposed canonicalization principle and paraphrase/utility evaluation are prior work. Original experiments use AlpacaEval/AQuA-RAT; no reproduction or complete appendix examination. |
| [Mathew et al. v2](https://arxiv.org/html/2410.03768v2) | New [reading view](sources/mathew.txt): §§1–5.2, conclusion/limitations, Appendix E.3 semantic/code-choice example; mitigation design and optimized sender/receiver pairs. | Retained arXiv v2 dated 2 Dec 2025, not an independent comparison to final publisher bytes. Adaptive paraphrase/monitor evaluation, task metrics and semantic carriers already studied. Reported numbers remain source findings. |
| ASB codebase 7 | Reused `../../pass-2/primary-sources/sabotage-bench.txt`, case 7: AQuA-RAT ICRL replication, reported higher-payload suppression and channel-capacity sabotage. | Separate replication conditions; does not erase the residual low-bit channels reported by Mathew. No reproduction by this lane. |
| [Codetta v2](https://arxiv.org/html/2609.28900v2) | New retained [reading view](sources/codetta.txt): abstract/introduction, §3 threat model, §7 setup/results descriptions, §8 related work, §9 defenses. | Cryptographic proofs not independently checked; sampler-controlled adversaries; passive-auditor theorem. Original HTML/source metadata retained. |
| [Firewalls v7](https://arxiv.org/html/2502.01822v7) | New [reading view](sources/firewalls.txt): abstract, §§1–6 with focus on §§3–5.2 and §6, plus public README and converter/checker source at identified head. | Paper's quantitative results are author reports; no reproduction. Fabricated valid fields and field-intersection leakage are acknowledged exclusions/limits. Dual malicious endpoints are a new threat condition. |
| [Riedl v4](https://arxiv.org/html/2510.05174v4) | Reused `../../reading-correction/track4-completion/captures/riedl-body.txt`: abstract/framing, coordination-free comparisons and temporal/functional-null discussion. | Useful coordination is not harm; no safety intervention from this paper is claimed. |
| [Fish et al. v6](https://arxiv.org/html/2404.00806v6) | New [reading view](sources/fish.txt): intro/design, §4 causal state-reset interventions and §6 discussion. | Considered a third route—active market probes—but not promoted in this lane. Interventions already exist in this literature; no novelty claim for causal probing alone. |

New source captures have URL/time/content identity and inert HTML-to-text
transformation metadata beside them. Public repository discovery established MIT
licensing and available components, not execution fitness. A large directory-tree
response was reduced to the relevant code-path reading view with its original
response hash; unrelated public transcripts were not downloaded. Broad literature
priority is not established. No experiment, prototype, training run, paid call,
external message, commit or publication occurred in this contribution.

## Author response to first review

**8a accepted (material closest-work omission).** Added actual primary readings
of Mathew v2 and Roger/Greenblatt v2 and rewrote the contribution account. The
omitted work already evaluates adaptive collusion/paraphrasing with utility, and
Roger §7.2 already proposes canonicalization of high-entropy choices. Neither is
claimed as our new idea. The remaining API-capable empirical route is implemented,
task-grounded standardization in a stateful structured workflow under adaptive
attacks and limited authorized reference inputs, with proper older baselines and
actual downstream utility. Its novelty is conditional and specific, not proven
field priority. The cryptographic active-edit/adaptation arm remains alongside it;
its GPU/logits dependency is not silently imposed on every meaningful version of
the semantic route. Full ambition is retained, not replaced by paraphrasing a
fixed decoder or showing that a typed number can carry a bit.

**7b accepted (post-treatment matching error).** Replaced “match discovered
opportunities” with identical *offered* routes/exposure opportunities; discovery
is an outcome and is not conditioned on. **7a partly accepted as a design concern:**
discoverability and relative route cost are explicit planned axes, task-only
behavior leads, and deliberate attackers remain a separately labeled comparison.
The suggestion that logged-channel knowledge predictably determines actual
unlogged-route use is not adopted: discovery, execution and adaptation are what
the study measures. A mechanically disabled route remains an enforcement
reference whose success is fixed by the contract, not a behavioral finding.

**Independent source/input concern preserved.** Canonicalization receives only
authorized task/state information. An exact-equivalence or full-state oracle is a
reference; its guaranteed elimination of a known channel is not the headline.
These are author repairs for examiner/interlocutor discussion and backcheck,
not claims that either reviewer has already accepted or closed the findings.
