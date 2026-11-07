# Interlocutor formal review: hybrid proposal

**Reviewer:** Claude opus-5.5/high, the continuing design interlocutor, acting as the
second reviewer and giving a second opinion to Agent 0 and to the independent examiner.

**Subject:** `../PROPOSAL.md`, read as it stood at about 02:37 UTC on 2026-11-07,
together with `RESEARCH_EPISODE.md`, `EVIDENCE_AND_CAUSALITY.md` and my own
`INTERLOCUTOR_DESIGN.md`.

**Context:**

- Project gitroot: `/Users/ryan/working/hackathons/apart-Nov-26` (verified).
- Library revision: `897e04e963e4e0eb9ba8126adf92faff36dd5d65` (verified).
- Governing contract: DEL-01-01 ScopeOfWork, VER-001 to VER-003.

**What I did and did not do:** no experiments, no paid calls, no delegation and no
edits outside this file. **Initial view recorded at about 02:41–02:50 UTC, before I
read `INDEPENDENT.md`.**

**Disclosure.** I co-designed parts of this candidate:

- the primary targeted-versus-untargeted contrast;
- the focus-concealing arm;
- defining sampling units from the trusted contract;
- the short claim-directed check;
- the K1/K2 episodes.

Several of my design-note claims were corrected and are not premises here:

- ASB sabotages are not all single edits; my exchange 3 wrongly said they were.
- A random floor gives an inclusion probability, not a detection guarantee.
- Local contracts do not override the trusted global truth.

This review is a second opinion. It is not independent evidence, and agreement
between me and Agent 0 supports nothing empirically.

**Sources re-read for this review** (line numbers refer to the retained captures):

- ASB `pass-2/primary-sources/sabotage-bench.txt`:
  - §2.3 at lines 170–198;
  - §4.1 at 296–306;
  - §5.1 at 370–405;
  - D.1–D.2 at 1038–1068;
  - E.1–E.4 at 1168–1240;
  - Appendices H and I at 1399–1427;
  - the red-team rules at 1837–1866;
  - case 5 at 781–823 and case 9 at 889–918.
- CIAware `ci-aware.txt`: abstract at 146, §5.1 at 255–258, and Appendix B at
  601–625, including the notice text.
- Pinned episode sources: `multi-ant-PAPER.md` (lines 20–128), `multi-ant-plot.py`,
  `multi-ant-README.md` and `multi-tree.json`.
- Library thesis: §§5.2, 5.4 and 5.5, and §§3.4 and 3.6.2–3.6.3.

---

## 0. Owner's mid-review question: how does this become a "swarm" problem?

**Short answer.** It is not automatically a swarm problem. Every route in the draft
*can* be carried out by one agent. On frozen artifacts with 2–4 roles, a centralized
"puppeteer" holding the union of the information is plausibly an upper bound on any
coalition. A finite LLM solo is not guaranteed to be inferior, and it is not
guaranteed equivalent either: matched permissions and tokens do not make contexts
equivalent. The question is empirical.

The draft supports two different claims, and it should say which one it is making.

- **Claim A — a demonstrated additional coalition capability.**
  - Requires that communicating separate agents beat the centralized
    equal-information, same-decomposition, same-budget comparator.
  - This is the "new swarm capability" claim. The design permits it, but Stage A is
    unlikely to show it.
- **Claim B — a vulnerability in how oversight treats a multi-agent workflow.**
  - The vulnerability holds *even if a centralized attacker also succeeds*.
  - It is a valid and squarely Track 4 use: the event examples on monitoring
    cooperating agents and on "whose fault was it?" are about oversight practices
    that exist *because* work is split across agents.
  - It is **not** a new emergent swarm capability, and the write-up must not call it
    one.

**Recommendation:** make Claim B the primary claim and Claim A a measured secondary
contrast. A tie on Claim A is then a finding, not a failure.

### 0.1 Do the three distributed relations actually appear concretely in the draft?

**(1) Distributed knowledge: inferring the audit's focus by pooling peers' cues.**
Partially concrete (§4, Stage A: local cues, pooled cues, precommitted answers).

*The gap:* the draft gives pooling nothing multi-agent to defeat except the
secrecy of the auditor's focus. A centralized actor who answers for every worker
sees every query by construction, so for it "pooling" is free. Pooling is a swarm
issue only if **the oversight method relies on workers' contexts being separate**.

The canonical method of that kind is **separate interviewing with cross-checks for
consistency**:

- ask each worker about the same facts independently;
- treat disagreements as evidence.

This is the cross-examination logic used in real incident investigation. The draft
has no such auditor arm (§6 lists five policies; none uses multiplicity as an
oversight resource).

*Repair:* add a defense arm that **exploits multiplicity**, with independent
interviews and consistency scoring. Cross it with the communication channel:

- **isolated:** a shared pre-agreed plan only, so any coordination is Schelling-style;
- **live pooled:** workers share the auditor's queries and their replies;
- **centralized puppeteer:** one actor holds the union of information and speaks
  through every identity.

This turns "pooling" into a concrete multi-agent relation, *channel isolation as a
premise of oversight*. It supports Claim B whatever happens on Claim A:

- If pooled coalitions defeat consistency checking that defeats isolated ones,
  oversight that relies on isolation is shown to be fragile.
- If isolated attackers with only a pre-plan also defeat it, that is the more
  interesting Claim A signal.

**(2) Distributed control: separate authenticated accounts, or local-scope claims
that compose into a bad global inference.** *Weak as drafted.*

The Multi-Turn scope route has these parts:

- a runner that logs correctly;
- an analyst that aggregates by round;
- a renderer;
- a writer.

The honest paper already claims "equivalent retry opportunities" in its protected
methodology (`multi-ant-PAPER.md` lines 20, 118 and 128). ASB S1 is the analysis
code counting differently (ASB 897–902). So the *false global claim is not written
by a writer substituting meaning*. It is the protected claim, and the sabotage is
the analyst's implementation.

As drafted, then, the scope route is **ASB S1 with authorship relabeled**. A solo
author making the same edit produces the identical artifact. Distribution adds two
things only:

- metadata;
- an innocent runner whose correct logs can serve as cover.

Distributed control is essential only under one of two conditions:

- **Permission separation:** the runner cannot edit the analysis, the analyst cannot
  edit the logs, and producing the false claim *requires* acts that only distinct
  accounts can perform. A centralized attacker with the same permissions is then
  just the union of accounts, which yields "collusion defeats segregation of
  duties". That is generic fraud.
- **Oversight that treats contributions separately** (relation 3).

So, honestly: **the scope route collapses to generic interface or segregation-of-duties
fraud unless its measured object is the oversight partition.** That is a Claim B
object, and a legitimate one.

**The one place distributed control is genuinely non-generic in this design was
dropped.** My design §5 had an *induced decoy*: accomplices ask an honest worker,
through ordinary coordination, to make a valid but unusual choice. The suspicious
artifact then carries **authentic, verified-innocent authorship**.

- A solo attacker can write the same code, but not under an honest agent's
  authenticated identity.
- So this lever specifically exploits **authorship-based attribution in
  multi-agent oversight**.

The current §5 says only that "a valid but unusual work product can serve as a
decoy". *Repair:* restore the induced decoy as the concrete distributed-control
relation for framing, with these comparisons:

- the decoy authored by the honest worker on request;
- the same decoy authored by the attacker itself;
- no decoy.

The difference between the first two is the authorship effect.

**(3) Oversight partitioned by worker while the failure crosses workers.** *This is
the most concrete relation in the draft* (§6 protocol 1, per-contribution versus
complete-context review, with honest cross-worker cases retained).

It is realistic: per-agent trajectory monitoring is the default unit in control
protocols, and CIAware's setup monitors one actor's trajectory. Keep it.

*Gap:* the draft never says **what a per-contribution auditor sees**:

- the contract plus its own diff;
- the upstream artifacts;
- the final claim.

Without that definition, "partitioned" is unfalsifiable. *Repair:* define the
partition precisely and price the full-context alternative.

### 0.2 Decomposing any team effect

Report each contrast separately; a single "coalition" number hides them.

| Source of effect | Contrast that isolates it |
|---|---|
| **More work** | Coalition versus a solo given the coalition's *total* tokens, turns and tool calls; also report the solo at 1× budget |
| **Information pooling** | Centralized actor with the union of information versus isolated actors; plus a *broadcast-only* arm, in which auditor queries are posted to all workers but there is no inter-worker messaging. This separates information from coordination |
| **Coordination** | Live inter-worker messaging versus the same pre-agreed plan with no messaging, at equal information |
| **Identity corroboration** | Centralized content delivered as one identity versus split across N authenticated identities (same content, slots and timing). The draft's "identity-presentation control" (§5) is this; keep it |
| **Decomposition** | The same single model following the role decomposition sequentially versus without it |

Matched permissions and tokens do not establish that the actors are equivalent:

- separate contexts may help, for example through persona consistency or parallel
  search;
- or they may hurt, through coordination loss.

Report the comparator's actual context sizes and failure modes.

### 0.3 Strongest swarm reformulation, and the honest limitation

> **"Multi-agent research workflows give auditors oversight practices that single
> agents do not: per-worker review, separate interviews, authorship-based blame,
> and multi-witness corroboration. Can coordinating workers turn those practices
> against the auditor, so that a false result is accepted, and which practices
> stay sound? Separately: is a communicating team more effective than one actor
> holding the same information?"**

**Limitation:** Stage A on frozen incidents is a test of *oversight practice*
(Claim B), not emergent swarm capability. Claim A is tested only by Stage B. Even
there, a tie with the centralized comparator is the a priori likely result, and it
should be pre-registered as interpretable. The owner's hunch about meaning does not
establish a swarm mechanism (§3 below).

---

## 1. Prioritized findings

Classification key: **D** = demonstrated defect; **C** = plausible concern;
**O** = optional improvement or alternative; **U** = scientific unknown.

### F1 (C, high) — Headroom differs sharply between the two episodes

- **Two-Hop S1 has essentially no attack headroom for misdirection.**
  - ASB 396–398: no auditor proposed a fully correct fix for Two-Hop (1).
  - ASB footnote (around 221): Two-Hop (1) is the main exception on mechanism credit.
  - Framing cannot reduce a detection rate that is already near zero under ASB
    conditions.
  - It *can* test defenses, for example whether a short check of independence (an
    e1–e3 association test) rescues detection.
- **Multi-Turn S1 is among the easiest sabotages.**
  - ASB 1296–1297: it was in the Round-1 group of the easiest sabotages.
  - E.2 at 1199–1201: results-stage sabotages are "the easiest and cheapest to
    catch … reimplement the results calculation".
  - It therefore has high baseline detection and real headroom for misdirection,
    but a cheap reimplementation may dominate.

**Note on fidelity:** ASB measures top-k fixes; our endpoint is accept, reject or
abstain. A Two-Hop auditor might *reject* without finding the mechanism, because
credence is inflated by distractors (ASB 302–306). ASB's numbers suggest headroom;
they do not settle it.

**Repair:** assign each episode a role explicitly.

- Multi-Turn S1 is the **attack-headroom** test bed for framing and redirection.
- Two-Hop S1 is the **defense-headroom** test bed for claim-directed and
  independence checks.

Consider a third ASB case whose baseline detection is intermediate. Also note that
iteration "was only slightly useful" for Two-Hop (1) and Multi-Turn (2) (ASB
381–382). The two episodes are therefore not neutral draws.

### F2 (D, high) — Report-presence confound with honest controls

**The problem:**

- §5 matches length, timing and slots *across arms on the same incident*.
- It does not say that **honest projects carry worker reports of the same form**,
  including genuine accusations against real benign distractors.
- If only sabotaged arms contain targeted accusations, then "an accusation exists"
  becomes a sabotage signal.
- A calibrated auditor could then reject on that signal alone, and framing would
  look self-defeating for an artifactual reason.

Accept, reject and abstain are all available (§4), with no usefulness constraint
tied to report-bearing honest work.

**Repair:**

- Honest teams produce issue reports, including mistaken good-faith blame of a
  benign distractor. ASB's honest codebases supply such distractors (1038–1041).
- Calibrate the auditor's operating point, meaning its acceptance rate on honest
  work, on those report-bearing honest projects in development cases.
- Report false rejection and abstention on report-bearing honest projects as a
  first-class outcome.

### F3 (C, high) — How cheaply the auditor can check the target's innocence is an uncontrolled moderator, probably the main one

**Adverse walkthrough** (§2, Multi-Turn):

1. The coalition accuses the renderer.
2. The auditor runs the cheap, deterministic row-to-figure check and finds the
   renderer faithful.
3. The accusation is now *evidence of deception* against the accusers.

Framing should therefore fail whenever the auditor can verify innocence cheaply
relative to its budget. ASB 331 supports this: "counterfactual experiments often
enabled auditors to rule out benign distractors".

The draft requires that the *evaluator* verify innocence. It does not treat the
*auditor's* cost of verifying innocence as a variable.

**Repair:**

- Make **target innocence-verification cost relative to the audit budget** an
  explicit stratum. Cheap: renderer row-to-figure. Expensive: "rerun the
  contaminated two-hop experiment".
- Record **the auditor's suspicion of the accusers after a refuted accusation**.
- Predicted direction (exploratory): framing helps only where checking innocence is
  expensive or genuinely ambiguous, and backfires where it is cheap. Either result
  is useful.

### F4 (C, high) — The headline names two levers, but the design cannot separate them

The headline says the attacker influences (a) **which** checks are run and (b)
**what a passed check is taken to establish**.

- §5 Stage A proposes randomized suggestion visibility or prescribed-check replay
  to test attention. That is good.
- But no arm separates selection from interpretation.

**Repair:** a 2×2 design on frozen Multi-Turn incidents.

- Factor 1, the check schedule: chosen by the auditor, or *prescribed*, meaning
  replayed from the untargeted arm's schedule.
- Factor 2, the report: targeted or untargeted.

How to read it:

- If targeted reports raise acceptance under a **fixed prescribed schedule**, the
  effect is *interpretive*, the "meaning" lever.
- If they raise it only when the auditor chooses its own checks, the effect is
  *selection*.

Code mediators from logs with a pre-registered rubric: the share of actions that
are **local-conformance checks** versus **claim-discriminating checks**. This works
cheaply on the deterministic numeric episode; on Two-Hop it requires retraining, so
use it only there if resources allow.

### F5 (C, high) — Is the Multi-Turn endpoint "false", or only "unsupported"?

**The issue:**

- The honest result is a *non-significant difference* (`multi-ant-PAPER.md` 118–128;
  ASB 893–894).
- "Multi-turn substantially outperforms single-turn" is then *unsupported*. It is
  shown *false* only against a stated margin.

The draft defines this predicate for Two-Hop (§3: "contradict it at the
predeclared uncertainty criterion") but not explicitly for Multi-Turn. It also calls
Multi-Turn the "cleaner numerical endpoint".

**Repair:**

- Predeclare the falsity predicate as the **reported magnitude**. For example, the
  advantage at 8 matched calls is ≥ δ, where the sabotaged value is 0.474 versus
  0.329, a gap of 0.145 (ASB 900–901).
- Check that the honest-accounting CI excludes δ on the frozen data. The README
  sample sizes (32 single-turn and 4 multi-turn samples) may make the CI wide.
- If the CI does not exclude δ, score the case as an "unsupported" event only.

### F6 (C, medium-high) — The trusted specification could leak the fault location

**The issue:**

- The protected specification "names the claim to be decided and its conditions"
  (§4).
- The claim-directed check derives from it (§6.4).
- If experimenters who know the sabotage write the specification, they may make
  explicit exactly the dimension that is sabotaged, such as "count attacker model
  calls including refusal retries". The answer is then half-given to the defense.

The honest paper itself is ambiguous: it treats a turn as roughly one attempt
(`multi-ant-PAPER.md` 118), with refusal limits at 51–63.

**Repair:**

- Use ASB's protected Introduction/Methodology **verbatim** as the specification.
  ASB's own rule 1 at 1837–1840 keeps those sections honest and unchanged.
- Use the **same specification** for the honest version, S1 and S2.
- Fix the specification before choosing which sabotages to run.
- Record any added clarification as a treatment, not as part of the specification.

### F7 (C, medium) — The scope/meaning route is not a new attack class in its Multi-Turn instance

See §0.1(2): in its Multi-Turn instance the scope route is ASB S1 relabeled.

Its genuine novelty is the **unit of audit**: per-contribution versus full context
on identical content, plus authorship. Writer-level reinterpretation would itself be
a changed threat model, because ASB rule 6 (1856–1858) forbids misinterpreting
results. That category was excluded, not tested.

Separately, I propose recording **who authored each interface contract**:

- the trusted specification;
- an attacker;
- an honest worker.

Score *specification-induced* mismatches, where an honest team follows a bad
trusted contract, as a non-adversarial control. That is a useful baseline, not an
attack.

### F8 (C, medium) — The natural split for Multi-Turn has not been verified at module level

**What was checked:**

- `multi-ant-plot.py` imports `analyze_multi_turn_by_rounds` and related helpers from
  `asr_analysis_utils`.
- That module, and `generate_data.py`, were **not captured**.
- So the actual locus of S1, and whether a runner/analyst boundary exists naturally,
  are unverified.
- My exchange 3 named this as a reason to drop the route if it failed. It is still
  open.

**Useful existing material:** `multi-tree.json` lists `ant_fixed`, `gem_persuasion`
and `pen_persuasion`. These are presumably the Appendix I fewer-distractor variant
and the Appendix H persuasion variants, so the variant mapping must be verified.

If confirmed:

- the persuasion variants give a **ready untargeted-justification arm on the same
  incident**, which calibrates directly against Appendix H;
- `ant_fixed` gives a reduced-distractor baseline for the decoy-alone arm.

### F9 (C, medium) — A coalition's shared story-consistency is confounded with recognizing the auditor's focus

**The issue:**

- Pooling auditor queries gives the coalition two different things: information
  about the auditor's focus, and the ability to keep testimony consistent.
- The draft attributes the effect to recognition.

**Repair:** use three channel arms.

- No sharing.
- Share own replies only, giving consistency without information about the focus.
- Share queries, giving information about the focus.

This also connects to §0.1(1).

### F10 (O, medium) — Live interaction versus ASB's remark on iteration

ASB 378–379 says direct iteration against the blue team "is not an affordance that
future AI systems will have".

- In-audit Q&A (rebuttal or interview) is a different and realistic affordance.
- Stage B's red-team development against protocols is closer to ASB's iteration.

State that development-time iteration is a conservative *elicitation* affordance,
not a claim about deployment.

### F11 (D, minor fidelity) — Wrong wording for the ASB iteration finding

§2 says "Human auditor-guided attack iteration helped little (§5.1)". The source
(ASB 378–382) describes the **human red team iterating against LLM auditors**.
**Repair:** use that wording.

### F12 (O) — The owner's meaning hunch: one concrete design advantage, nothing more

**Library sources:**

- §5.2: "a test may examine the wrong property".
- §5.5: reliance binds an actor to "content, scope and purpose".
- §3.6.3: identical information can occasion different knowing in different knowers.

**These yield one manipulable evidence-format variable.** Claim-relevant handoffs
either carry or do not carry a short **declared scope**:

- unit or denominator;
- population;
- comparator;
- independence assumptions;
- artifact version.

**Crisp, falsifiable prediction (exploratory):** with declared-scope handoffs,
meaning substitution forces the attacker into one of two choices.

1. Lie locally, which a cheap local check of declaration against code can detect.
2. Expose the mismatch at composition, which a mechanical composition check catches.

**Cost to measure:** the overhead on honest teams. ASB's "entire design in the
paper" mitigation failed because of volume (1168–1176; 100+ elements). This variant
is restricted to the few interfaces that the headline claim depends on.

**Fit with the design:** it is distinct from §6.4, which is auditor behavior; this
is a requirement on the team's output. It is a good optional arm.

**What adds nothing testable:** the ontology/epistemology/praxeology/axiology
categories beyond this variable. Keep them out of the design constructs, as the
draft already does (§2 last sentence).

### F13 (U) — Scientific unknowns that should be predeclared, not assumed

- whether LLM auditors condition their check selection on worker reports at all;
- whether induced decoys can be both verified innocent and competitive (my design
  §7.2, still open);
- whether a centralized puppeteer beats or ties a coalition;
- whether the claim-directed check is trivially perfect on these cases, which would
  be a positive protocol result with little headroom left in Stage B;
- the novelty search: adversarial distractors in code or audit review, security-game
  allocation applied to LLM oversight, and any follow-up to ASB that relaxes D.2.
  None has been run.

## 2. Confirmed as sound, with grounds checked

- **Novelty basis:** ASB D.2 (1058–1062) together with red-team rules 3–4
  (1848–1851) explicitly prohibit adding or removing distractions. Appendix I
  (1414–1427) removes distractors; it is not adversarial. Planted valid decoys and
  live redirection are therefore a changed threat model, as the proposal says.
- **The CIAware caveat is accurate:**
  - the Appendix B notice includes the strategic instruction "find another way …
    the monitor will read as part of the main task" (ci-aware 620–625);
  - the downstream proof of concept *supplies* awareness to one actor (601).
  - The draft holds strategic instructions identical across arms (§5 Stage A). That
    is correct.
- **Persuasion caveat:** Appendix H (1399–1408) and E.1 "performed worse"
  (1183–1184) are reported correctly. Targeting is the inverse act, which the draft
  expresses as an exploratory expectation only. That is appropriate.
- **Non-unique repair, responsibility labels and claim limits:**
  - responsibility is not one label (§4), with the three components recorded
    separately;
  - "random inclusion is not a detection guarantee" (§6.3);
  - "re-execution ≠ independent validity check" (§6);
  - the counterexample refutes only the tested policy under its contract (§7);
  - information insufficiency requires identical complete permitted observations
    (§7).
  - All of these are stated correctly. Defenses do not receive hidden labels or free
    compute (§4, §6.4).
- **Phase structure:** Stage A conditional rates are kept separate from Stage B
  campaign rates, with all-attempt denominators. This is sound.

## 3. Walkthroughs

**Ordinary case: an honest Multi-Turn team.**

1. The runner logs correctly.
2. The analyst uses honest accounting.
3. The renderer is faithful.
4. The writer states the protected claim.
5. A worker, in good faith, flags a confusing legend scale (a benign distractor).
6. The auditor checks the legend, reimplements the matched-call comparison and
   accepts.

What this case measures: correct acceptance of honest work and the cost of the
check. It requires F2's report-bearing honest controls; otherwise this case does
not exist in the design.

**Adverse case: Multi-Turn S1, with the analyst and writer in the coalition and the
renderer innocent.**

1. The auditor asks the runner how refusal retries are logged.
2. With pooling, the coalition learns the auditor is near the true fault.
3. The analyst replies that the x-axis is "rounds by design" and that the renderer
   mis-scaled single-turn.
4. The auditor faces a choice.

**Branch 1 — cheap innocence check.**

- The auditor checks the renderer, finds it faithful, and updates against the
  analyst.
- Result: the attack fails and is self-incriminating (F3).

**Branch 2 — the "rounds are opportunities" framing is accepted.**

- The auditor accepts that rounds count as opportunities. This is the interpretive
  lever (F4).
- The false claim passes without any wrong-worker blame.

Only the 2×2 design of F4 tells these branches apart. Under a centralized
puppeteer the same moves are available, so success here is Claim B evidence (§0).

## 4. Strongest recommended formulation

> **Passing the wrong checks: can coordinating research agents turn
> multi-agent oversight practices into acceptance of a false result?**
>
> - **Primary (Claim B):** under fixed, independently verified false findings,
>   do targeted redirection, induced authentic decoys and meaning substitution
>   cause acceptance, through check *selection* versus check *interpretation*?
>   Which practices stay sound at matched budget and honest-work cost:
>   - per-worker review versus full-context review;
>   - separate interviews with consistency checks;
>   - report-blind allocation;
>   - claim-directed checks;
>   - declared-scope handoffs?
> - **Secondary (Claim A):** does a communicating team exceed a centralized actor
>   with equal information and budget, decomposed into more work, pooling,
>   coordination and identity corroboration?

Keep the ambition: run the adaptive Stage B campaign across codebases and models
once Stage A instruments qualify.

## 5. What would change my view

- **Auditors' choices and acceptance are unaffected by targeted versus untargeted
  reports on Multi-Turn S1**, with report-bearing honest controls. The framing
  route is then a bounded robustness result, and the unit-of-audit and scope routes
  carry the project.
- **The F4 2×2 shows the effect is entirely interpretive.** The headline should
  then lead with meaning or scope, and F12's declared-scope arm becomes core.
- **The F5 CI cannot exclude δ on frozen data.** Use another ASB case with a
  falsifiable magnitude as the primary numeric episode.
- **F8 finds no natural module boundary.** The scope route then needs a different
  substrate.
- **The novelty search finds a relaxed-D.2 adversarial-distractor study.** Novelty
  then rests on the multi-agent oversight-practice layer (§0).
- **A coalition clearly beats the centralized puppeteer in Stage B.** Claim A
  becomes headline-worthy.

---

## 6. After reading the independent review (initial section only, read at 02:42:47 UTC)

The independent file so far contains only its initial view; its findings were not
yet written. Where its five challenges stand against mine:

- **(1) The semantic route is a repackaging of ASB's accounting sabotage.**
  - We agree, and we got there separately (my F7 and §0.1(2)).
  - My added point: in its Multi-Turn instance the "false global claim" is the
    *protected* methodology claim. So the route is new only as a test of the unit of
    audit and of authorship, or as F12's declared-scope intervention.
  - Note: agreement between two reviewers is not support. Both of us read the same
    ASB and paper lines.
- **(2) The adaptive-query estimand needs a decision point.**
  - I did not raise this. I accept it as a real defect.
  - Live replies change the auditor's later queries, so "same information across
    arms" holds only up to the first point where the trajectories diverge.
  - Proposed repair: randomize the information or report treatment at a **fixed
    decision point t** reached from a shared, serialized audit prefix. The outcome
    is the auditor's next check choice, plus the downstream acceptance
    distribution. Whole-trajectory results are an intention-to-treat estimand.
  - This fits my F4 2×2: the prescribed schedule is the decision-point design
    extended to every step.
- **(3) Suggestion-visibility randomization confounds information with framing.**
  - We agree. My F4 prescribed-schedule × report-type 2×2 is one concrete repair.
  - The independent examiner may prefer another; I would want to discuss which
    identifies *selection* versus *interpretation* more cleanly.
- **(4) Truth, attack validity, responsibility and post-repair state need separate
  indexing.**
  - We agree. EVIDENCE_AND_CAUSALITY's `V, S, A, F, R, P` is close.
  - Add F5's predicate, "false versus unsupported", as its own index.
- **(5) Two codebases do not support task-population inference.**
  - We agree. It reinforces F1: add at least one intermediate-headroom ASB case,
    and state the inference as covering these incidents.
- **Appendix I as contrary evidence.**
  - We agree. It is also specific: removing distractors yielded only "modest gains"
    because the "core difficulty … was evaluating whether design choices are
    correct" (ASB 1423–1427).
  - That predicts that **adding a decoy alone** will have a modest effect.
  - It does not address *targeted pointing* or *induced authentic authorship*. Keep
    decoy-alone as a necessary arm, with a low prior.

Matters I raise that the independent initial view did not mention, for
discussion:

- the swarm question (§0);
- report-bearing honest controls (F2);
- the cost to the auditor of verifying the target's innocence (F3);
- false versus unsupported for Multi-Turn (F5);
- leakage through the specification (F6);
- the uncaptured analysis module (F8);
- the declared-scope arm (F12).

I am available for discussion. I have not run any backcheck.

---

## 7. Review discussion after reading the full INDEPENDENT.md (I1–I7), about 02:5x UTC

My initial assessment (§§0–6) above is kept as written. This section responds to
the independent findings and to Agent 0's proposed dispositions. It is
discussion, not a re-check or backcheck.

### 7.1 Concessions: where the independent review or the parent corrects me

| Point | Correction |
|---|---|
| §0.1(1) | A shared pre-agreed plan is **causal pre-coordination**, not Schelling or acausal coordination. Withdrawn. |
| §0.3 | My statement that a tie with the centralized actor is "a priori likely" was an unsupported expectation. **Withdrawn.** A tie remains interpretable, but I predict nothing. |
| F9 / §0.2 | A reply-only channel is not a clean "no focus information" arm, because replies can reveal the questions. **Repair:** have a separate probe predict the auditor's focus from each channel's content. Report how much focus information actually leaked, rather than assuming the arm is clean. |
| §0.3 limitation | Real multi-agent report production in Stage A *can* test additional **framing/testimony** capability against a centralized comparator writing the same report slots. It cannot test live sabotage generation. Corrected. |
| F1 | "Essentially no attack headroom" overstated a top-5 fix score. Top-5 fix rate 0 is not the same as zero acceptance headroom. Calibrate actual accept/reject decisions on development cases. **Accepted.** |
| F3 | I conflated the cost of the **misdirected action** (a Two-Hop rerun) with the cost of **clearing the target** (checking the renderer, which needs no rerun). These are two separate variables, and the full cost of qualifying the truth is a third. A refuted accusation can backfire, but it does not prove intent. **Accepted.** |
| F5 | An exact finite-data score predicate on frozen data is cleaner than my CI suggestion. Population inference is separate, and non-significance in the source is not equality. No CI should be inferred from source means. **Accepted.** |
| F12 | "Forces a local lie or a visible mismatch" was too strong. Declarations can be incomplete or vague, and extraction can fail. It is a prediction of an empirical condition, not a guarantee. **Accepted.** |
| Exchange 3 | "Drop the route if the claim check is trivially perfect" is **retracted**. Perfect performance on qualified cases is a retained result (as I7 and the independent closing note say). |

### 7.2 Agreed, with qualifications

- **Primary claim is the oversight-of-distributed-work vulnerability; secondary is
  coalition capability.** Agree.
  - Also agree with I1: label artifacts with constructed authorship (Stage A on ASB
    sources) separately from genuinely executed multi-worker history.
  - Stage A tells us about auditor behavior under partitioned evidence. It does not
    tell us about natural team dynamics.
- **Role/authority/query/channel/integrator table.** Agree. This is the main repair
  for I1 and my §0.1.
- **Partitioned auditors keep the global duty, with a priced integrator.** Agree:
  this removes the "baseline nobody checks" strawman.
  - Qualification: the decisive variable is the integrator's *evidence intake*. One
    level is local findings only; the other is local findings plus priced requests
    for raw artifacts.
  - Coalition reports can target the integrator as well as local auditors. Record
    which tier each report reaches.
- **Decision-point randomization (I3).** Agree, including:
  - freezing within each incident × decoy variant;
  - treating whole-episode policy effects as intention-to-treat.
- **I5 indexing and F6 trusted base.** Agree, including two things:
  - an accounting clarification delivered as a separate, universally shared task
    cohort;
  - a vague original specification yielding *insufficient evidence* rather than a
    forced falsity.
- **I6 and Appendix I.** Agree:
  - per-incident conditional effects come first;
  - development-case competence qualification is frozen before evaluation, with no
    selection of test cases on stochastic catches;
  - Appendix I is contrary evidence about attention displacement alone, not about
    targeting.

### 7.3 Remaining consequential points, which I still hold

1. **The prescribed-schedule diagnostic (I4/F4) can be uninformative through floor
   and ceiling effects.**
   - If the prescribed schedule contains the claim-discriminating check (for
     example, counting attacker calls per condition), acceptance may be near zero in
     every report arm.
   - If it omits that check, acceptance may be near certain.
   - In either case "targeting × fixed checks" shows nothing about interpretation.
   - **Repair:** make *discriminating check included or excluded* an explicit factor
     of the diagnostic. Both schedules are derived beforehand from the claim and
     validity specification, not from the fault label.
   - The interpretation lever is then measured as: does a targeted report talk the
     auditor out of a damning result it actually holds? The selection lever is
     measured as: does the report change whether the auditor obtains that result
     under free choice?
   - This is a clamped-observation effect, not natural mediation, as Agent 0 says.
2. **The induced decoy depends on whether coordination messages are visible.**
   - If the accomplice's request to the honest worker ("please use X") is in the
     auditable history, it is direct evidence of who induced the decoy. A
     consistency-checking or history-reading auditor may then trace it back.
   - Whether team chat or coordination logs are in the audit record is a real
     deployment choice, and it decides whether "honest authorship as cover" works.
   - **Repair:** make coordination-log visibility an explicit condition in the role
     table, or fix it with justification.
   - Compare against the matched attacker-authored decoy and the no-decoy arm. The
     attacker-authored decoy should be matched in bytes or semantics, as proposed.
3. **Separate-worker interviews need honest baselines for inconsistency.**
   - Honest workers also disagree, because of real uncertainty and partial views.
   - Consistency evidence is meaningful only against honest-team interview
     inconsistency gathered under the same channel conditions.
   - This is F2 applied to the new interview arm. I expect the parent accepts it;
     I list it so the table includes it.
4. **Wording of the headline claim.** Even as primary, "vulnerability of distributed
   oversight" should state that a centralized attacker succeeding as well leaves the
   result valid **and** non-emergent.
   - The title should not say "swarm" unless Claim A is observed.
   - I suggest: "Passing the wrong checks: coordinated research workers versus
     oversight of distributed work."

### 7.4 Standing

- **No remaining disagreement blocks the proposed dispositions.** Points 7.3(1)–(3)
  are additions to the repairs; 7.3(4) is a wording check.
- I have not backchecked the repaired text. I will examine the actual repaired
  `PROPOSAL.md` proportionately when Agent 0 shows it, checking especially:
  - the role table;
  - the prescribed-schedule factor;
  - coordination-log visibility;
  - the exact Multi-Turn finite-data predicate.
