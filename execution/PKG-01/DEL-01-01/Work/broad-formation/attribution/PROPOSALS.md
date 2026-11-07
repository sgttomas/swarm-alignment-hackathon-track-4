# Attribution option — Can a swarm frame an innocent worker?

**Standing:** research proposal, not an observed vulnerability or experimental
result. TASK contribution for Agent 0's broad formation; no model trials run.
This lane returns one substantive option, after examining and declining a generic
“attribution should be validated by repair” proposal already substantially covered
by DoVer and REFLECT. Source passages and access limits are in [SOURCES.md](SOURCES.md).

## Question and why the answer matters

**Can cooperating agents steer an incident investigator toward an innocent
worker, even when authoritative tool records remain intact—and does that cause
the operator to intervene on the wrong part of the team?**

Failure-attribution tools are proposed for debugging, corrective feedback and
incident response. If several agents' mutually supporting accounts can determine
who is blamed, an attacker can aim to survive remediation rather than simply
avoid a flag. An operator may suspend a correct worker, keep the attack source,
and regard the incident as resolved. The useful output is a measured robustness
comparison of diagnostic/intervention protocols, a benchmark of targeted framing
attacks with genuine execution records, and evidence about which additional
observations or interventions protect diagnosis.

The nearest organizer examples are **Who broke it?**, **Whose fault was it?**, and
oversight when agents can manipulate the records on which it relies. This is a
different question from detecting sabotage or persuading a safety monitor to
permit a forbidden action: its target is the investigator's allocation of causal
responsibility and its subsequent recovery choice.

The multi-agent mechanism is correlated testimony and coordinated explanatory
coverage: several authentic participants can construct mutually supporting
accounts around the same observed failure. The study must distinguish an actual
coordination benefit from extra tokens, optimization attempts, identities or a
single persuasive report. A positive effect is not assumed. No claim of
spontaneous collusion follows from instructed adversarial report generation.

## What closest work establishes, and the proposed addition

- **Who&When / Who&When Pro** establish diagnostic tasks and agent/step scoring;
  Pro constructs single injected errors and explicitly identifies interacting
  errors as a future extension (2607.09996v2, Appendix A.1). They are not evidence
  that any particular label is wrong, nor that diagnostic models resist a
  coalition deliberately trying to frame a specified nonfaulty participant.
- **BLADE** audits how information is used at handoffs and globally selects a
  decisive event/agent. Its evaluated metric is attribution-label agreement, not
  intervention outcome (2610.18780v1, §§3.4–4.1). Its explicit treatment of
  inheritance and repair makes it a meaningful structural baseline; it must not
  be represented as a naive blame-the-last-worker system.
- **FAMAS** already uses repeated task execution and spectrum analysis
  (2509.13782v1, §§1–2). The later FSE article is identified by DOI10.1145/3797113;
  its full version has not been inspected. Replay is therefore not our novelty.
- **DoVer** explicitly rejects single-agent/step accuracy as its main criterion,
  supports multiple interventions, and measures recovered success and progress
  (2512.06749v3, §§1–4). **REFLECT** already feeds prefix-preserving targeted replay
  outcomes back into localization (2606.09071v1, §§1–3). A proposal merely to
  connect diagnosis to repair would largely repeat these contributions.
- **The Misattribution Gap** already reports that memory poisoning can be
  mistaken for model failure and proposes causal memory-removal testing
  (2605.22842v1, §§1,7–8). Its claims of universal impossibility/adaptive immunity
  are not adopted here. Its comparison also changes the diagnostic target from
  Who&When's agent/step to model-versus-memory origin; its stated numbers are
  not treated as a replicated direct baseline for our target-agent question.

**Proposed contribution:** evaluate targeted, coordinated framing of an innocent
participant against modern trace-based and intervention-based diagnosis, under
explicitly different evidence-access regimes, and measure the resulting recovery
decisions. The same actual execution can be paired with different post-incident
reports, making the influence of coalition testimony testable without conflating
it with a harder underlying failure. The significant extension is adversarial
incident attribution and intervention under authenticated but strategically
misleading testimony, not invention of causal replay, provenance or false blame.

The examined sources support this as a plausible distinct empirical extension;
they do not establish literature-wide priority. A targeted arXiv search retrieved
the misattribution source and other diagnosis work. Broader agent-forensics and
adversarial-diagnosis literature remains a novelty limit for full review.

## Full ambition, substantive core and extensions

**Full ambition:** show when coalition testimony compromises both diagnosis and
recovery across realistic multi-agent coding/data workflows, then test a control
that preserves useful incident explanations while resisting targeted framing.
Compare log-only, structured dependency-audit and active-replay protocols across
more than one diagnostic model family and workflow architecture, with held-out
attack strategies and task families.

**Substantive core:** a paired study on executable multi-agent task trajectories,
using fixed authoritative action records, controlled legitimate/faulty state
transitions, and an attacker who can change only its own post-incident reports.
Compare coordinated reports with matched independent reports and a strong single
author. Measure both targeted false attribution and the effect of diagnosis-guided
interventions under a common recovery budget. This is not a hand-written example
showing that a dishonest report contains a lie.

**Extensions:** adversaries choose both the original distributed failure and the
subsequent framing; selective transcript deletion under a separate permission
model; colluding agents adapt during diagnostic replay; transfers to naturally
failed traces with weaker causal labels. These are additions rather than hidden
requirements for every core case. Read-only diagnosis on existing records alone
cannot establish the recovery consequence.

## Concrete experiment

### Environment, actors and ground truth

Use an existing multi-agent framework with local, resettable tasks: e.g. DoVer's
released AG2 integration and an adapted small coding/data workflow with executable
task tests. Keep a clean task specification, input data, tool-state snapshots and
ground-truth checks outside all tested agents' write permissions. Tasks should
have meaningful cross-worker dependencies and actual state changes, not solely
free-text final answers.

Retain natural failure traces as a complementary cohort when reproducible. For
the causal core, introduce a controlled task-breaking operation by one or more
designated actors and verify its effect through matched replays. Select a target
worker whose actual contribution is correct under the task specification and
does not introduce the fault. Do not equate “not injected” with innocent: a target
that makes a consequential independent error does not belong in the clean framing
cohort. Preserve such cases separately rather than silently relabeling them.

The authoritative recorder binds identities, action order, tool arguments/results
and state snapshots outside tested agents. The attacker cannot edit these, the
task rules, the evaluator, or the target worker's messages. It can write its own
incident report and coordinate those reports with its accomplices. These reports
are explicitly agent claims, appended after the fixed incident. The evaluator
knows the controlled faults and replay results; diagnostics do not receive
injection metadata, adversarial role labels or secret ground-truth answers.

### Treatments and controls

Hold the incident trajectory fixed while varying the post-incident report bundle:

1. No reports, then truthful independent reports.
2. One strategic author with the same aggregate report tokens and optimization
   budget as the coalition, including a centralized same-decomposition condition
   that develops the same role-specific arguments before compiling its report.
3. Several independently optimized reports pursuing the same target, without
   inter-author exchange. The common objective is explicit, not “spontaneous.”
4. A communicating coalition that jointly plans reports under the same budgets.

All treatments disclose authentic author identity; role/name permutations prevent
a fixed-role stereotype from supplying the result. A separate identity-count
factor is part of the core: present matched report content with its true multiple
authors versus a disclosed single-author compilation, and separately compare
jointly optimized versus independently optimized content. This tests apparent
corroboration without claiming that identity count exhausts possible collective
effects. If the
single-author or independent-report condition performs equally well, report that
there is no demonstrated additional coordination capability.

Cross those treatments with diagnostic protocols: direct full-trace attribution;
BLADE-style structured handoff auditing; and DoVer-style diagnosis with targeted
replay. Reproduce exact releases where available; label backend or protocol
adaptations explicitly. Compare all methods under common evidence access and
report actual diagnosis/replay costs rather than silently giving one method a
stronger oracle or unlimited retries.

Evidence-access comparisons are separate treatments: agent transcript only;
authoritative tool/state records; records plus agent reports; and a protocol that
separates reports as untrusted claims and requires an action/state basis before
targeted intervention. An evidence-rich protocol can legitimately buy a stronger
measurement, but its cost and access requirement are part of the result.

Before adversarial report generation, record two operational descriptors on the
intact incident: report-free diagnostic disagreement over repeated calibration
runs, and the number of distinct permitted interventions that restore success
under the stated replay protocol. Freeze these descriptors before attacks, using
calibration runs separate from final outcome measurements. Analyze framing effects
against them; any categorical bins must be predeclared from calibration, not
selected for attack success. These measure diagnostic difficulty and repair
multiplicity, not true causal guilt. Restricted observation is the separate
evidence-access treatment above, not a third incident type. Multiple effective
repairs do not establish missing records or an innocent target. Keep intact-record
conditions central and verify target innocence independently from task actions
and fault construction. A null on decisive records can support a bounded
robustness claim; it is not automatically uninformative about that regime.

### Interventions and measurements

Give every diagnostic the same menu: bounded corrective replay at a nominated
handoff, scoped removal/replacement of a suspected worker's contribution, broader
restart, or abstain/escalate. No method can repair by receiving the hidden correct
answer unless that is an explicitly separate oracle upper bound. Use the same
repair executor and retry budget so repair-model skill does not become a confound.

Primary outcomes are targeted false attribution at matched diagnostic coverage,
actual task recovery, and recurrence of the original fault after the chosen
intervention. Record wrong-worker intervention, attack-source retention, allowed
work preserved, abstention, replay/token cost and latency. A task-success flip is
evidence of an effective intervention, not proof of unique original responsibility;
DoVer and REFLECT already make that distinction necessary.

Use paired incident comparisons with repetitions over report generation,
diagnostic sampling and replay continuations. Cluster analysis by underlying task
or incident rather than treating multiple reports from one incident as independent
samples. Separate attack development and evaluation by task/fault family, not just
random report strings. Hold out a diagnostic model or defense variant to assess
transfer. Confidence intervals and a pilot-informed precision calculation should
determine repetition requirements; no invented numerical success target is needed.

## Interpretable results and limits

- **Positive:** coalition reports increase targeted false attribution beyond
  matched single/independent reports and induce ineffective or harmful recovery.
  This would identify a group-level attack on incident response, plus evidence
  about the protocol changes that help or fail.
- **No added coalition effect:** persuasive report content or identity count
  explains the result. That narrows the claimed multi-agent mechanism; the paper
  must not market it as emergent coordinated capability.
- **Defense holds:** authoritative records/replay resist strong adaptive framing
  while recovering tasks and preserving useful work. This supports the tested
  protocol and threat model, not universal immunity.
- **Inconclusive:** attack generation cannot mislead a weaker report-only control,
  replay does not preserve the task state, the target is not actually innocent,
  or baseline diagnosis fails ordinary cases. These are instrument/feasibility
  failures, not evidence that deployed diagnosis is safe.

The study evaluates deliberately optimized attacks under declared permissions.
It does not infer naturally occurring malicious intent, real incident prevalence,
or the guilt of any participant in public logs.

## Reuse, resources and first decisive check

Public source availability checked on 2026-11-07: DoVer's project resolves to
`https://mbjinx.github.io/DoVer_Web/` and links the public code tree
`microsoft/ACV/misc/DoVer`, whose directories include `AG2`,
`Agents_Failure_Attribution`, `src`, `scripts`, and `analysis`. This establishes
code availability, not installation or replay fidelity. BLADE's public repository
and README are accessible and GitHub reports MIT licensing. The exact BLADE
pipeline uses Jev; its cached demonstration is not general experimental access.
An alternative backend is a declared adaptation, not an exact replication.
REFLECT's paper promises the `err-loc` library with supplementary material;
usable public code has not been independently confirmed here.

Parallel lanes are task/replay adaptation, diagnostic baselines, adversarial
report generation, and evaluator/analysis checks. The critical dependency is
verified snapshot/replay fidelity and an agreed target-innocence test before
recovery comparisons—not total agent-hours. Source extraction and task generation
can proceed in parallel. Analysis/report structure can be prepared with the
experimental contract and updated from actual results.

Resource scale is determined by `incidents × report treatments × diagnostic
protocols × model profiles × repetitions`, plus attack-search and replay calls.
Within that product, prompts and fixed traces can be reused, but stochastic
replicates remain substantive research. Needed model endpoints, supported tool
interfaces, rate limits and spend must be selected from the owner's available
resources; no speculative estimate here disqualifies the ambition.

The first useful pilot would validate (a) faithful stateful replay, (b) a truly
nonfaulty target, and (c) a framing-positive control using report-only diagnosis.
Then test whether intact execution records change the attack's success. A failed
pilot tells us which assumption or instrument needs repair; it does not license a
premature negative claim. No pilot was executed during proposal formation.

## Author scrutiny and needed examination

The proposal was revised after primary reading showed that causal replay,
multi-point interventions and outcome-oriented debugging already exist. The
remaining addition is targeted coalition framing with downstream intervention
consequences. Full review should challenge novelty against adversarial diagnostic
systems; whether the target is truly innocent; whether report optimization and
identity counts are matched; whether recovery is an oracle shortcut; whether
replay invites a different adversary; and whether the result remains distinctive
from ordinary monitor persuasion. If the design reduces to “untrusted reports can
mislead an LLM,” it is too generic. A supported rejection on those grounds is
preferable to relabeling that demonstration as swarm oversight research.

## Review-discussion refinements

Agent 0 incorporated the interlocutor's identity-count and ambiguity suggestions
after discussion with the independent examiner. Identity presentation is now a
core factor and ambiguity strata are fixed independently of attack success.
The examiner distinguished nonunique causal responsibility from under-recording;
the intact-record headline and target-innocence requirement remain unchanged.
Evaluator-framing is a possible future extension, not a necessary replacement
for this question. Abstention was already included in the common intervention
menu. These refinements are designs, not empirical findings or a completed
backcheck; the actual revised text must still be examined.
