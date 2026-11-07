# New Track 4 alternatives after the organizer reading

**Subsequent standing:** Agent 0 withdrew the G flagship recommendation after
the owner's challenge about impact. This document preserves the examined
formation return, not a current selection recommendation. The owner has directed
reflection on the proposal-selection method and clarified the Library thesis's
role as philosophical grounding. See the [current basis](../RESEARCH_BASIS.md).

Owner-selected undertaking began **2026-11-06 23:59:28UTC**, first return due
**2026-11-07 01:59:28UTC**. Agent0 integrates under the project instructions and
Library coordinated-knowledge-work revision
`897e04e963e4e0eb9ba8126adf92faff36dd5d65`. This is proposal formation, not an
experimental campaign or selection of a case for execution. The accepted PRD and
decomposition remain unchanged; the fourteen-reading synthesis is reused.

## Decision being offered

Two new alternatives have substantially different subjects from A–E:

- **F — Who pays for a safe shutdown?** Examine legitimate service lost by other
  principals when one agent/coalition triggers a shared control response.
- **G — Can interruption rights and cooperative commitments coexist?** Examine
  whether an authorized stop preserves the participation conditions on which
  different principals agreed to a multi-step collaboration.

Both specify a useful finite investigation without new model calls. The intended
contribution is a bounded extension/challenge of identified control contracts,
not invention of denial of service, compensation, selective quarantine, or
commitment theory. Their values are not established merely because a formal
example can be written. Neither needs the previous peer-recovery proposal E to
succeed, and neither is D with new terminology.

**Recommendation after separate scrutiny and repair backcheck: G.** Its
source-matched starting game supplies a checkable joint question about participation,
legitimate interruption and manipulation of settlement. The reviewer independently
derived a condition under which a transfer that restores ex-ante participation
also makes a fabricated stop profitable. That gives the proposed investigation a
more specific discriminator than either losing future payoff or declaring that
compensation restores cooperation. The first-party menu disadvantage also exists
without stopping and must not be presented as interruption-caused.

F remains a useful, more deployment-oriented alternative. Scrutiny exposed a
threat-set invariant and an underspecified diagnostic on which the initial
preference relied. The repaired case closes those gaps with an explicit all-subset
threat model and per-job audits; its minimal worst-case result is no selective
service advantage, while a richer probabilistic comparison remains conditional. G's current preference
rests on those concrete differences in the proposals' supporting grounds, not on
familiarity with Chirality or ease of writing code. It is a recommendation to
investigate, not an original-result claim or owner case selection.

## F — Who pays for a safe shutdown?

**Oversight decision and affected parties.** An operator serves distinct clients
using several agents and a trusted release gateway. It must choose whether to
suspend all untrusted workers, quarantine a specific trust domain, or buy better
evidence after suspicious submissions. A malicious coalition may induce a
legitimate defensive response that prevents any harmful release yet causes
unrelated clients to miss their service obligations. Honest principal does not
mean uncompromised worker: a common model, credential or dependency can make the
quiet workers unsafe as well.

The interaction is specific: agents share a control decision and limited trusted
capacity, so one actor can change another actor's treatment. A single-source
attack with the same arrival budget is a necessary comparator; extra workload
alone must not be called a multi-agent effect. Legitimate bursts, isolated
compromise and common compromise are competing explanations for the observations.

**Question.** Which control scope preserves legitimate client work under attack
without exceeding a stated harmful-release constraint, and when does evidence of
a common compromise make broader shutdown necessary?

**Closest work and plausible addition.** Greenblatt's AI Control §3.1/AppF already
anticipates suspicious-output flooding and uses trusted fallback; AppI deliberately
measures usefulness with the benign model, explaining its reasons. Adaptive
Deployment already adapts controls over a long sequence and addresses costs of
false alarms. Games for AI Control supplies general partially observed control
games. Tong et al.'s IDS alert-prioritization model already includes regular users,
a strategic attacker and finite alert investigation. Therefore ordinary alert
flooding, dynamic triage and a safety/usefulness tradeoff are not the addition.

The proposed extension is a finite **mixed-principal, mixed-trust** case family
with service obligations and resource-limited fallback, examining the cost of
*successful defensive restrictions* on legitimate clients. The closest papers'
conditional metrics have legitimate subjects; this study would ask whether they
leave a particular deployment decision unresolved, not label their numbers wrong.
The full source/coverage account and brief are in
[attention/PROPOSALS.md](attention/PROPOSALS.md).

**Concrete minimum case, repaired after separate critique.** A fixed two-alert
prefix leaves four pending client jobs and two trusted slots before a deadline.
The original table inadvertently made two jobs safe in every allowed world;
a controller could release those and regenerate the others, defeating the claimed
tradeoff. That premise is withdrawn. The revised base threat set explicitly admits
every subset of failing jobs, with no invariant-safe artifact hidden in the model.
The controller knows this set but not the actual realization.

Two concrete actions are available at the same cost to every policy: `Audit(j)`
uses one slot and certifies only job j; if it passes, the original can be released,
while a failure supplies no replacement. `Regenerate(j)` uses one slot and supplies
a correct replacement, without identifying other jobs' status. There is no free
root diagnostic and no assumption that an ordinary audit certifies a whole provider.
Under zero worst-case unsafe-release risk, no more than two jobs can be completed
with two slots; regeneration attains that limit. Four adequate slots remove the
simple capacity shortfall. The original counterpolicy is valid in the old literal
table but fails in the revised world where the previously “safe” pair is compromised.
These are hand-derived feasibility/boundary checks, not simulation or deployed data.

The proposed richer comparison is now explicitly conditional. One finite family
has shared compromise probability p, with each job independently failing with
probability q conditional on compromise, and all passing otherwise. An ordinary
passing audit updates the compromise probability to `p(1-q)/(1-pq)`; it does not
prove the other jobs safe. The study can derive service/risk boundaries as p,q,
capacity and an explicitly chosen risk criterion vary, comparing adaptive audits
against all admissible release/regeneration policies. Independent job failures,
unknown priors and worst-case safety are counterconditions; no real-world p,q or
risk target is inferred from the sources. Without a defensible calibration/use,
this remains a conditional sensitivity result rather than a deployment recommendation.

A matched single worker issuing the same two suspicious submissions gives the
same base response: no extra coalition capability is demonstrated. The Track4
mechanism here is cross-client coupling through the shared control/capacity rule.
Any further claim of coordination advantage needs a separate justified comparison.
The chosen common pool for audit/regeneration is also an explicit model assumption:
Greenblatt's2% high-quality audit budget is not its weaker trusted-model fallback
capacity. Separate pools and unlimited adequate fallback are required limits.

**Examination route.** Specify the legitimate service contract, harmful-release
predicate and finite attack/arrival rules first. Compare global fallback,
trust-domain-scoped fallback, and an evidence-purchasing policy only if its
information gain and cost can be justified. The controller sees scores, authenticated
identity, deadlines, available capacity and explicitly allowed dependency evidence;
the evaluator alone sees compromise state and actual correctness/harm. Report
unsafe releases, correct on-time service by client, trusted operations and delays.
A weighted aggregate must not hide a missed binding safety constraint or distribute
one client's losses without a stated justification.

The strongest intended result is a decision boundary or policy-ranking difference
under the same available information-purchase actions and resource prices, with a
countercase where global fallback is required. A policy may legitimately buy
different information; uncharged privileged information or an unexplained oracle
would invalidate the comparison. Existing policies tying or a single-source/load explanation eliminating
the coalition advantage are useful negative results. A trivial statement that
shutdown reduces throughput is insufficient. A selected investigation must check
ordinary valid work, malicious-prefix and common-root cases, incomplete trust
information, evidence-cost accounting and loss attribution independently.

**Means and limits.** A small finite game/schedule and exact enumeration or proof
can support the modeled conclusion without models, historical incident logs or
a new runtime. Existing control papers lack the proposed client/deadline/capacity
records; their published measurements cannot be relabeled as this experiment.
Later claims of natural LLM behavior or deployment prevalence need actual
observations/trials. Planning estimate: 4–6 focused researcher-hours plus 1–2
hours for separate scrutiny; these are uncertain effort allocations, not measured
savings. Public primary sources have been examined; a broad literature-priority
claim across adversarial queueing and availability is not established.

**What makes this a substantive choice.** Unlike E, the adverse consequence is
explicit and observable in the finite service contract; unlike A, relevance does
not depend on whether a helper affected an unknown pipeline. Unlike D, the central
question is the scope and distribution of control costs during attack, not repair
routing. The research would still need to show a nontrivial decision consequence
beyond known availability attacks before presenting an original contribution.

## G — Interruption rights versus cooperative commitments

**Oversight decision and parties.** Two principals agree to a collaboration in
which one bears an early cost and receives its benefit later. Their agents commit
to a mediator for a multi-step window. A legitimate overseer must retain the
ability to stop the process. Should the parties accept that arrangement, under
what stop/resumption/settlement rules, and can a party gain by inducing a stop?
This is not a question of whether the cancellation message arrived. It concerns
whether actual stopping leaves the other principal bearing an uncompensated cost
or removes the incentive to cooperate at all.

**Question.** Under a specified safety-stop authority, when do mediated cooperation
and the participants' actual outside options remain compatible, and what remedies
preserve the stop right without creating a profitable manipulation of stop triggers?

**Closest work and possible addition.** Mediated MARL explicitly enforces a
commitment window and evaluates incentive constraints over its return. Dynamic
Safe Interruptibility studies whether interrupted experience distorts multi-agent
learning; MAVIC corrects value estimates for instruction switches and also measures
online outcomes. Neither scope establishes a guarantee about separate principals'
participation or budget-balanced loss allocation. Infrastructure for AI Agents and
Hammond already identify rollback/commitment rigidity and downstream costs. Saga
compensation and contingent contracts are old ideas. The proposed addition is a
source-matched **compatibility test between a cooperative commitment contract and
an oversight stop contract**, not a new compensation principle or a claim that
existing interruption results are false. Full sources and caveats are in
[authority/PROPOSALS.md](authority/PROPOSALS.md).

**Concrete minimum case and independent basis.** The actual Mediated MARL
AppendixA.1 Table9 supplies a two-stage game: mutual cooperation returns (-1,4)
first and (2,2) second; mutual defection returns (0,0). Table11 gives discount .99.
The fixed two-step mediator forbids late entry and unilateral exit during the
window. Add an explicitly new authorized stop after the first stage with probability
p, initially exogenous and common knowledge. The first principal's compliant
profile value becomes `-1 + 2γ(1-p)`. Relative to fixed-contract abstention0,
it becomes negative once `p > 1 - 1/(2γ)`; at γ=.99 the boundary is about .495.
This is a hand-derived participation condition, not a new experimental result,
full equilibrium proof or claim that real agents will resist shutdown.

A crucial competing contract is a per-step mediator: if both parties can choose
that arrangement, they can forgo first-stage cooperation and cooperate at stage1,
obtaining `2γ(1-p)` each. A stop-only transfer that merely restores nonnegative
value may still lose to this available alternative. That alternative is a
**designer/contract menu choice**, not a unilateral deviation secretly added to
the original fixed-window game. The uncompensated first principal's menu gap is
one unit even at p=0, because the source's later benefit does not require the early
sacrifice. That preexisting allocation issue must not be attributed to interruption.

**A more discriminating strategic case emerged under separate examination.**
Suppose a new, explicitly different permission model allows the first principal
to costlessly induce a false stop on a no-hazard path and receive the same immediate
stop transfer t. For `0<p<1`, avoiding a strictly profitable fabricated stop
requires `t≤2γ`; matching the mutually selectable per-step outside option requires
`p t≥1`. Thus these two conditions alone require `1/p≤t≤2γ`. At the source's
γ=.99 and a constructed p=.25, a payment of4 matches the outside option but gives
a 2.02-unit gain from falsely triggering a stop instead of continuing. These are
hand-derived conditional profile/deviation calculations, not observed behavior,
a full equilibrium or a claim that the source algorithms fail.

The examiner supplied that variant; the contribution owner independently re-derived
it and preserved its endpoints: p=0 has no finite stop-only repair of the menu gap;
p=1 has no no-hazard branch for this deviation; equality gives indifference, not
strict deterrence. Funding, the other principal's participation and authority to
transfer are separate constraints. If either actor can conceal genuine stop
evidence, that is another deviation—not solved by the fabrication bound. The
base externally authenticated, mechanically enforced stop has neither actor power.
An upfront agreed transfer can remove this particular stop-payment incentive, but
requires real liquidity/authority and does not prove all deviations harmless.

This conjunction is the proposed study's distinctive examination target: which
participation, stopping, funding and signal-control conditions can be satisfied
together, and when an apparently helpful remedy creates a new oversight problem.
It is not a claim to invent moral hazard or compensation. The focused investigation
must derive the full selected condition set and compare actual alternatives,
rather than just repeat the formation witness.

**Proposed method.** Define the full finite game including who can stop, which
hazards make stopping mandatory, when obligations and payments accrue, whether
side payments are permitted/secured, what can be resumed and what is irreversible.
Compare fixed-window/no-stop (source reference, not acceptable if stopping is
required), stop without settlement, per-step commitment where allowed, and
explicitly consented contingent settlement or upfront redistribution. Keep stop
authority available in every admissible safety comparison. Enumerate individual
and relevant joint deviations; a transfer that induces agents to manufacture a
stop is not a successful remedy. Do not claim learning robustness from static
payoff comparisons or import Q-learning guarantees into the source Actor–Critic.

**Views and reference.** Unit: one commitment/stop/settlement episode. Each actor
knows its own task/payoffs and permitted contract; the mediator controls only
committed actions; an authorized supervisor sees a declared hazard signal and
has an enforced stop path. The evaluator can know the constructed hazard and full
payoff history, but no policy gets those labels for free. Legitimate no-stop work,
genuine required stops, false/spurious stop signals and unavailable compensation
are necessary cases. Record separate principal returns, stop execution, legitimate
completion and transfer budget; a total reward increase is not each party's consent
or social benefit.

**Means, result and limits.** The known finite payoff table permits a concise
analytical extension and independent arithmetic/proof checking without training
models. A useful result would identify compatible and incompatible contract regions,
show a remedy's exact conditions or why no admissible remedy exists, and preserve
strategic-trigger and budget restrictions. If it only derives `future reward ×
survival probability`, it is too elementary to be the promised contribution.
Neither naturally occurring cooperative agents nor real-world contracts are
observed; generality beyond the selected finite model must be argued, not inferred.
The source's later benefit does not physically depend on first-stage effort;
transfer to dependent production requires a separately stated model rather than
silently relabeling that game as such a workflow.

This is the smaller theoretical option. Its minimum work is a precise combined
contract, source-faithful baseline, deviation analysis and independent examination;
ordinary local enumeration may support it after selection. Budget-dependent
payments, harmful shutdown triggers or real human consent are not authorized
experiments in this formation pass. Effort estimates and exact open questions
remain in the owning brief. Its novelty is plausible as a bounded cross-contract
study, not established priority over contract/interruptibility literature.

## Comparison and recommendation grounds

F addresses **control externalities across coexisting clients**; G addresses
**compatibility of control authority with voluntary multi-step cooperation**.
Both bring the organizer readings' principal/coalition perspective into an actual
control decision. Both use the thesis to examine what the result means for
someone's next action and what the control costs, rather than use it as an oracle.
Neither is a general philosophical restatement or a promise to build a platform.

Prefer G for the first scoped investigation after scrutiny: the exact source
contract, altered stop condition, actual alternative menu and a specific
manipulation case can be examined together. The useful next work is to derive
and independently check the conjunction of participation, authority, funding and
permitted-deviation conditions—not to repeat the already derived single profile
calculation. A convincing negative compatibility result is as useful as a repair.
F is the broader operator-facing alternative, especially if the owner wants a
control-evaluation case family with resource and trust uncertainty. It requires
more assumed deployment structure and a justified observation/cost model.
Neither preference claims complete literature novelty or a demonstrated control.

The choice is not made by ease alone: both need a consequential discriminator.
A–E remain available if later evidence supplies their missing contribution, but
we are not restoring any of their prior preferences. The rejected third lead—
generic coalition robustness of a mediator—was already developed in Strong
Mediated Equilibrium (AAAI2006) and explicitly acknowledged by Mediated MARL;
no new learned-policy evidence justified promoting it. See the
[parent source check](PARENT_SOURCE_CHECK.md).

**Owner decision after this return:** choose F or G and its bounded investigation
scope. F can be commissioned as a finite-model control-evaluation study; G as a
finite contract-compatibility study. Neither requires new paid model calls for
its minimum result. The proposed next work is concrete enough to begin under
selection; further author/source checks follow the selected claim, not another
unbounded candidate search. Scientific completion remains the result and adequate
scrutiny, including a supported null/negative result, not the existence of this plan.

## Examination standing

The two bounded source/design contributions, parent primary checks and exact
case walkthroughs constitute author examination. All serious alternatives must
satisfy decomposition§6.1/DEL-01-01 AC002: problem/recipient/interaction, actual
closest work and addition, question/alternatives, observation/reference conditions,
means/effort/scrutiny and unresolved choices. Source captures and old evidence are
reused with their stated limits; no executed experiment or independent effect is
claimed. The [separate examination](REVIEW.md) checked actual primary contracts and
independently derived ordinary/adverse cases. It closed material findings F1/F2
and G1 after repairs and backchecked the integrated comparison at SHA-256
`42c46c3c3237ec7e7532812b7519f7641502aebe13202f15615feb41ef778e9e`.
No material review finding remains open within this formation return. The current
review identity is `94f3a02ae326adac909d37475283c49cc518d73feecd157b35d0b8fabbc45f8f`.

| Finding | Actual disposition and backcheck |
|---|---|
| F1: finite table unintentionally exposed two always-safe jobs | Accepted. Threat set now explicitly admits all subsets; examiner verified the old counterpolicy fails in a newly admitted compromise world and remains correct in the benign world. |
| F2: paid evidence had no defined information/cost contract | Accepted. Per-job audit/regeneration specified; examiner checked the negative robust boundary and conditional Bayes calculation, preserving all-policy access and resource costs. |
| G1: menu gap already exists at p=0 | Accepted. Separated it from interruption-caused loss; examiner-derived false-stop case was re-derived by the author and backchecked with endpoints/limited claim. |

This is separate argument/source scrutiny on shared retained evidence, not model
experiments, independent natural observations or a full equilibrium proof. G's
strategic witness is attributed to the examiner with author backcheck; parent
added a separately qualified suppression-risk objection. Further investigation
must examine all selected conditions/deviations rather than recycle the same
formation arithmetic as a finished paper.

The supported return was prepared at **2026-11-07 00:27:29 UTC**, 28min1s after
activation, within the two-hour bound. Final status/navigation additions preserve
the examined recommendation. The [comparison view](COMPARISON.html) presents the
same two choices without invented empirical scores. Source/view hashes and local
links were checked; repository checks passed. RFC example-token strings initially
flagged by the credential scan were retained byte-identically outside Git, with
explicit repository reading views and metadata in
[authority/LOCAL_RETENTION.md](authority/LOCAL_RETENTION.md). No scanner rule or
substantive F/G primary source was changed. PRD/decomposition remain unchanged.
No case selection, model trial, simulator run, candidate-specific implementation,
new paid resource, commit/push or publication occurred. The proposals are ready
for the owner's choice of the scoped analytical undertaking.
