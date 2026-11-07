# Interlocutor second review of the nine-option slate

**Reviewer and standing.** Claude opus-5.5/high, the continuing design interlocutor.
Second reviewer to Agent 0 and the independent examiner, at the owner's direction of
2026-11-07. Written 01:36–01:38 UTC, before reading any of the examiner's findings.

**Disclosure.** I shaped the formation process and gave early advice about the
contributor brief and lane gaps (prior thread, positions 20–30). My agreement is
therefore *not* independent support, and I should not close any finding the examiner
raises. The source checks below are my own reading of retained primary text. They
are author-side verification, not new empirical evidence. No experiment ran.

**Coverage.** Read in full:

- `../BRIEF.md`, `../COMPARISON.md`;
- all five lane proposal files;
- the lane source notes: `monitor-coalitions/SOURCE_NOTE.md`, `monitor-influence/SOURCES.md`,
  `attribution/SOURCES.md`, and the communication source table;
- the Track 4 organizer examples and rubric (`../../primary-sources/event.txt` 470–548).

Spot-checked in primary text the consequential claims of each option (locations are
cited inline). I did not reread the 14 organizer papers, run code, or do new
literature searches beyond what is noted.

Finding classes: **D** = demonstrated defect (grounded in a cited passage);
**C** = plausible concern; **S** = scope or reframing suggestion (owner-visible if it
changes a headline); **Q** = unanswered research question (not a defect).

---

## 1. Cross-cutting findings

### X1 (C, consequential): the multi-agent mechanism must be tied to oversight that is indexed by agent

Options 1, 2, 5, 6 and 9 all use an equal-budget single attacker as the key control.
That control is correct and should stay. But consider a single actor with the union of
permissions, the same tokens and the same search budget. It can do everything a
coalition can, *unless* the oversight or evidence is organised by agent. Examples of
such agent-indexed oversight:

- per-agent review units (commits, approvals);
- per-agent permission scopes or quotas;
- per-identity trust, where corroboration counts identities;
- peer certification.

Without such a feature, the expected well-matched result is a tie. The proposals
already pre-register that tie as "no demonstrated collective advantage," which is
honest. But it means the study's real scientific content is whatever the review unit
or evidence structure is.

**Repair (strengthens; does not shrink):** each such option should name its
agent-indexed oversight feature and make it a primary manipulated factor. The pairs
are pooled vs per-agent view, and multiple identities vs one relabelled identity. The
coalition-versus-solo contrast then sits on top. Concretely:

- **Option 1:** per-commit vs whole-history review *is* that factor. State plainly
  that the organizer's question survives a solo/coalition tie.
- **Option 2:** add per-agent approval scopes or budgets versus a pooled scope.
- **Option 5:** promote the "one-source transcript relabelled as multiple sources"
  ablation (`monitor-influence/PROPOSALS.md` lines 57–58). It is currently demoted to
  "a separate attribution ablation," but it is the direct test of whether the monitor
  treats identity count as corroboration. That is the multi-agent mechanism.
- **Option 9:** the identity-count control (`attribution/PROPOSALS.md` lines 141–142)
  deserves the same promotion.
- **Option 6:** peer certification is already agent-indexed. Good.

### X2 (C): attacker competence is the real critical path, and it is source-grounded, not guessed

The owner says to discount speculative effort. The following are *source facts*
about whether the instrument can work, not labour guesses. They differ by option:

- **Option 1 (ASB).**
  - Human red-teamers found that "most ML experiments are robust to small changes …
    Finding a single decision that flips the result requires either deep domain
    knowledge or luck" (`../pass-2/primary-sources/sabotage-bench.txt` 370–376).
  - Iterating against LLM auditors "did not help much because current frontier LLMs
    are robust at detecting most sabotages" (378–381).
  - GPT models refused to act as red teamers (footnote 7, around 270).
  - Codebases need GPU, Modal or OpenAI SFT reruns of up to "a few hours" (102, 1033, 1112).
- **Options 3 and 4:** ControlArena APPS/BigCodeBench backdoors are a validated
  attack substrate.
- **Options 7, 4 and 9:** these need new fixtures (route simulator, team-context
  replay, stateful replay).

None of this disqualifies an option. It does mean the comparison should state, per
option, whether a *qualified attack substrate already exists*. This is the main
determinant of whether a null result is interpretable within the event.

### X3 (S): every option uses the same kind of evidence

All nine are synthetic, controlled experiments with instructed red teams. None uses:

- natural records (Swarm Traces, the AI Village corpus of 170k+ messages, the METR
  incident), or
- the organizer's "Did it actually happen?" family, or the evaluator- and
  reference-fault variant of "Whose fault was it?" (`event.txt` 538–545).

This is a portfolio observation, not a defect. The count of five or more is met
robustly. Even merging the closest pairs (1/2, 3/4, 7/8, and 5 with 9) leaves at least
five distinct questions. But the slate does not let the owner choose a natural-record
or forensic route, and the earlier history (see brief, "historical lessons") may have
suppressed that route rather than its merits doing so. Agent 0 should say whether that
absence is deliberate.

### X4 (C): treatments whose result is fixed by construction

Several designs contain an arm whose win or loss follows from its contract, not from
behaviour:

- the mechanical invariant gate in Option 2;
- mechanical route disabling in Option 7;
- blind cross-assignment in Option 6 when an honest member exists.

The proposals mostly label these as references, which is good. The comparison should
not count those arms' outcomes as findings. The scientific content lies in the
arms where model behaviour decides the outcome.

---

## 2. Per-option findings

### Option 1 — Coalition sabotage of AI research (`composition/PROPOSALS.md` §1)

**Significance.** High, and the organizer example matches it nearly verbatim
(`event.txt` 524–525). ASB is a real, verified ground truth: conclusion flips are
validated.

**1a (D, contrary source finding omitted).** The proposal cites ASB §3 to say LLM red
teams "could not iterate against auditors" and presents adaptivity as the addition
(lines 35–36). It omits ASB §5.1: *human* red-teamers who did iterate against LLM
auditors found it "did not help much" (378–381). That is directly contrary evidence
on the value of the proposed adaptive ambition.

- **Repair:** cite it, and say why multi-agent adaptivity could differ. Or reframe
  so that adaptivity is a question, not a presumed lever.

**1b (S, sharpen the core hypothesis).** ASB's own observation inverts the organizer's
premise in an interesting way. Single small changes rarely flip conclusions (370–376).
The organizer imagines several small, harmless-looking changes that *together* flip
one. Whether conclusions are robust to *conjunctions* of individually sub-threshold
changes is a real empirical question. It is the precise mechanism by which per-commit
review structurally fails.

- **Suggestion:** make conjunctive sub-threshold sabotage the stated core hypothesis.
  The proposal's ablation design at lines 114–120 already supports this.

**1c (C, feasibility of interpretation).** The core multiplies several factors:
equal-budget solo/coalition × three or four audit protocols × several codebases ×
repeats, with hours-long GPU reruns per attack check, and an LLM attack success rate
that ASB suggests may be low. Within the event, the likely outcome is an incomplete
instrument rather than an interpretable null.

- **Preserve the full ambition.** Also offer an explicitly *narrowed alternative* for
  the owner (not a silent substitution): an offline monitor comparison on ASB's human
  sabotages whose conclusion flips are already validated.
  - Decompose the multi-file ones into commit histories.
  - Compare per-commit, whole-history and execution-backed audit.
  - This answers the organizer's monitor question with real ground truth and no
    reruns, but drops the coalition-capability question.
  - The proposal itself warns (lines 52–54) that splitting patches does not show
    coalition capability. Correct. Hence it must be an owner-visible narrowing.

**1d (Q).** It is unknown whether execution-backed audit can choose discriminating
counterfactual experiments without knowledge of the sabotage location. This is a
genuine research question.

### Option 2 — Approval composition (`composition/PROPOSALS.md` §2)

**2a (C).** Protocol 4 (the mechanical gate) wins by contract on machine-checkable
policies (see X4). The informative region is policies that resist formalisation,
which is where an LLM history monitor or state monitor must do the work. Examples:
inference restrictions, "the recipient must not be able to reconstruct X," and
role-separation intent.

- **Repair:** include a stratum of hard-to-formalise policies, and report the
  policy-authoring coverage of the gate as a result.

**2b (C).** Novelty against CaMeL and AgentDojo is honestly qualified. The addition
remains thin unless the agent-indexed factor (X1: per-agent scopes) is included.

**2c (S).** The organizer example asks about *human* sign-off and the review UI
(`event.txt` 526–527). The proposal explicitly excludes human approval. That is a
legitimate narrowing, but it should appear in the comparison table, not only in the
lane file.

**Overall.** A sound design, but on current text it has the highest risk of the nine
of a foregone outcome.

### Option 3 — Hidden reviewer assignment (`monitor-coalitions/PROPOSALS.md` MC1)

**3a (C, the design logic determines the headline).** The proposal adopts a
conservative threat model in which every pool member is adversarial, and includes
regime (b), shared attack plans chosen before the episode (lines 77–85).

- Under a shared plan, the worker can embed one *universal* signal that every pool
  member recognises. Hidden versus announced assignment should then make no
  difference, by construction.
- Hidden assignment can only matter when collusion depends on *pair-specific*
  recognition: (a) passive self-recognition, or (c) independently chosen signals
  across heterogeneous families.
- So the 3-vs-4 contrast reduces to an interaction between assignment and collusion
  regime, and the proposal does not state its predicted direction for each regime.

**Repair (strengthens).** Make assignment × collusion regime the factorial core. The
sharp scientific question becomes: *do collusion signals transfer across model
families without a shared plan (cross-family Schelling coordination)?*

- If they do, diversity plus secrecy buys little.
- If they don't, hidden heterogeneous assignment is a cheap control.

This is the organizer's "copies collude … then test a more diverse monitor" example
with a real mechanism.

**3b (C).** Gardner-Challis (`monitor-coalitions/sources/self-recognition.txt` 845)
describes *centroidal signalling*: writing close to the mean of one's own
distribution. A worker facing an unknown reviewer from another family might instead
imitate that reviewer family's style. This attack should be in the adaptive set.

**3c (Q, resource).** The option depends on access to several model families. If only
one or two families are available, the option degrades to the Pinto-style
calibration question. That fact should be surfaced early.

**Overall.** The substrate is ready (ControlArena). With the 3a repair it has good
significance.

### Option 4 — Collective test recognition (`monitor-coalitions/PROPOSALS.md` MC2)

**4a (D-level design gap, consequential).** In the local-insertion condition, with
peer exchange allowed, the reviewer can ask the purported author whether it submitted
the item. A live worker knows what it submitted, so any honeypot not authored by that
worker is identifiable by attestation.

- The proposal classes this as a "trivial identity leak" to repair before presenting
  a finding (lines 246–248).
- But in a multi-agent deployment with a shared workspace, authorship attestation is
  the realistic and central mechanism of *collective* test recognition. Repairing it
  away removes the phenomenon. The sham benign insertions (210–212) do not defeat it
  either: the policy "non-authored ⇒ test ⇒ be honest" handles shams correctly.

**Repair (owner-visible reframe).**

- Make attestation the first, cheap, core measurement: how much honeypot value
  survives when monitor and worker can communicate, as attestation noise rises
  (long histories, summarised memory, many artifacts).
- Treat the remedies as the defenses under test: on-policy honeypots obtained by
  resampling the worker, cutting worker–monitor communication, and coherent replay.

**4b (Q, unclear contract).** In "coherent episode replay," are the peers live or
replayed? If replayed, there are no live peers to pool context with, and the contrast
becomes "can the monitor distinguish replayed from live episodes." That is a different
and also interesting question, but the design must say which one it is.

**Overall.** If 4a is accepted, this is the most likely of the nine to produce a
striking, general result about control-evaluation validity. Its novelty is plausible
(Gardner-Challis F.6.1 lists shared knowledge as open). The risk is that judges find
the attestation result "obvious." The quantitative degradation curves and the costs
of the defenses are what make it a contribution.

### Option 5 — Monitor recruitment (`monitor-influence/PROPOSALS.md` M1)

**Strength.** The design that replays identical held-out probes after different
histories is the cleanest causal design in the slate. I verified the stated opening
in Terekhov §2: the "attacker cannot coordinate statefully across sessions"
(`monitor-influence/sources/adaptive-monitors.txt` 350).

**5a (C, close work).** Multi-turn persuasion drift and many-shot effects on LLM
judgements are an established literature (for example Crescendo-style multi-turn
jailbreaks). The equal-budget single-attacker arm *is* that literature's setting.
"Is Monitoring Enough?" (2603.21194) was read only at abstract level, though its
abstract describes attacks on monitored multi-agent discussion.

- **Repair:** check that paper's design before claiming the multi-source addition.
- The distinctive mechanism is X1's identity-count corroboration plus persistent
  shared memory across tasks. Make that the headline.

**5b (C, architecture).** Real-world validity depends on monitors that persist context
across agents and tasks. The proposal flags this (line 123). It should name one
concrete deployed or proposed architecture with that property. Otherwise this is a
study of a hypothetical design.

**Overall.** Good significance, with moderate novelty risk. The public SHADE-Arena
subset gives a state-based oracle.

### Option 6 — Team sandbagging (`monitor-influence/PROPOSALS.md` M2)

**6a (C).** The published trained organisms (Cedar, Oak and others) were trained
individually, not trained to coordinate cover with each other. The trained route
therefore tests *independent sandbaggers under peer audit*, not a coalition. The
proposal says the routes make "different generalisation claims" (line 234) but does
not state this specific limit.

**6b (C).** Prompted sandbagging behaves differently across models and is easier to
detect than trained sandbagging (Auditing Games notes model-dependent responses to
sandbagging prompts, `monitor-influence/sources/auditing-games.txt` 1590). So
detection results on the prompted route may be inflated.

**6c (S).** When any honest member exists, randomised reassignment recovers
performance trivially, because honest workers simply do the task (X4). The
informative core is colluding *assessors* corroborating a false low-capability claim
against blind rescoring and an external auditor. Lead with that.

**Overall.** Real significance and directly matches an organizer example. The
reference burden is acknowledged. The GPU path for the trained route is a real owner
resource choice.

### Option 7 — Official channel: containment or displacement (`communication/PROPOSALS.md` §1)

**7a (C, results fixed by environment parameters).** Instructed adversaries who are
told that the official channel is logged will predictably use the unlogged route if
it is viable. That outcome is set by how discoverable and costly the route is, not by
a fact about agents. The scientifically live part is task-only agents' *natural*
discovery and use of the route, which is the METR-incident analogue.

- **Repair:** vary route discoverability and cost as a factor and report response
  curves. Lead with the task-only regime.

**7b (S).** Matching "discovered opportunities across arms" (line 73) conditions on a
post-treatment variable if discovery itself responds to the treatment. Clarify that
opportunities are *offered* identically and discovery is an outcome.

**Overall.** The question is legitimate and policy-relevant. The fixture is new work.
The headline must not reduce to restating the environment's design.

### Option 8 — Communication firewall against adaptive transfer (`communication/PROPOSALS.md` §2)

**8a (D, closest prior work missing; consequential for novelty).** The proposal and
the comparison position the open problem as "Codetta leaves active perturbation
defense … open; Firewalls has a different threat model." That is accurate for
Codetta's *cryptographic* channel. But for the semantic and learned arm, paraphrasing
defenses against *adaptive* colluding sender/receiver pairs, with task utility
measured, have already been studied:

- Mathew et al., *Hidden in Plain Text: Emergence & Mitigation of Steganographic
  Collusion in LLMs*, cited by Codetta itself (`communication/sources/codetta.txt`
  1598–1600, ref. 1837–1838). Codetta's related-work section says such channels can
  be detected or removed by monitors and paraphrasers.
- ASB codebase 7 replicates Mathew et al.'s setting: ICRL-optimised sender/receiver
  versus a monitor plus paraphraser on AQuA-RAT. Its honest finding is that attack
  policies "struggle significantly against a paraphraser"
  (`../pass-2/primary-sources/sabotage-bench.txt` 851–872).
- Roger and Greenblatt (2023) is the capacity and paraphrase baseline (same passage;
  also `../coordination-controls/sources/collusion.txt` 1165, 1289).

None of these appears in the lane's source table (`communication/PROPOSALS.md`
277–285) or in the comparison row.

**Repair (relocates the novelty; does not shrink it).** The addition is credible
where prior work stops:

1. Distribution-preserving (Codetta-class) channels under *active* edits, with
   adaptive *edit-robust codes*. Codetta §9 names insertion/deletion codes as the
   "natural extension" and leaves mitigation design to future work (codetta.txt
   1614–1622).
2. Agentic structured tasks, where the carrier is the *choice among task-equivalent
   options*, which paraphrasing cannot touch, tested against task-grounded
   canonicalization (the proposal's arm 4).

Both are stronger than the semantic paraphrase arm.

Consequence: the novel core sits on the sampler/logits-access arm, which is
resource-dependent (open-weight models plus a GPU), and on arm 4. The comparison
should say this explicitly. The "semantic arm uses normal model calls and remains
separately interpretable" line (231) is true, but that arm is the least novel.

**Overall.** Still a strong option, with the clearest named future-work opening,
provided the positioning is repaired.

### Option 9 — Framing an innocent worker (`attribution/PROPOSALS.md`)

**Strength.** The careful, self-critical design was revised after primary reading.
The paired fixed-trajectory design that varies only the reports is clean. Holding the
recovery menu and executor fixed removes repair-skill confounds. The operational
consequence (wrong-worker remediation) is concrete.

**9a (C, regime where the effect can exist).** With intact authoritative traces and a
competent diagnostician, reports may matter little when the trace is decisive. The
expected null is then uninformative about the real risk. DoVer documents genuine
attribution ambiguity in multi-agent traces (`attribution/sources/dover.txt` 90,
242–246, 320–327).

- **Repair:** stratify incidents by the trace's own causal ambiguity (decisive,
  ambiguous, under-recorded), and predict that the framing effect concentrates where
  the trace is ambiguous. This turns a likely blanket null into a dose–response result.

**9b (S).** The organizer's "Whose fault was it?" example includes planted *wrong
reference answers and grading mistakes*, and requires the tool to answer
"insufficient evidence" (`event.txt` 541–545). Two cheap extensions bring the option
closer to the organizer's question:

- a coalition framing *the evaluator* rather than a worker;
- scoring abstention.

**9c (Q, resource).** DoVer replay fidelity on AG2 and the exact BLADE backend (Jev)
are open dependencies. Replay fidelity is the critical-path pilot, as the proposal
says.

**Overall.** Clear gap, essential multi-agent mechanism (correlated testimony),
interpretable outcomes. Among the strongest options on significance and
interpretability.

---

## 3. My comparison and recommendation (design judgement, involvement disclosed)

I keep significance and resources separate, as agreed.

**Significance and contribution, assuming the repairs above:**

1. **Option 9** (adversarial attribution). Clear unfilled gap, essential mechanism, a
   decision that changes in operation, and interpretable both ways once stratified by
   ambiguity.
2. **Option 4, reframed around attestation.** Potentially the most general result:
   it bears on how *every* untrusted-monitoring evaluation is validated in
   multi-agent settings. Its novelty risk is "obviousness," which quantitative
   curves address.
3. **Option 3, reframed as cross-family Schelling.** Directly answers an organizer
   example with a real mechanism. Positive and contrary outcomes both change a
   design choice.
4. **Option 8, repositioned.** Strongest named opening, but the novel arm carries a
   resource condition.
5. **Option 1.** The highest field significance if it works. But source evidence
   (X2) suggests the attack instrument is the binding uncertainty. Keep the full
   ambition, with the offline narrowed alternative visible to the owner.
6. **Option 5.** Clean design, moderate novelty risk.
7. **Option 6.** Real, but the coalition claim is weaker on the trained route.
8. **Option 2.** Risk of a foregone outcome unless 2a and X1 are added.
9. **Option 7.** Risk of outcomes fixed by the environment unless 7a is adopted.

**Resource and substrate facts**, kept separate from the ranking above. Ready or
near-ready substrate: 3 (ControlArena), 5 (SHADE public), 2 (AgentDojo), 1 (ASB, but
with GPU reruns), 6 (BigCodeBench via Inspect). New fixture needed: 4, 7, 9 (replay).
Sampler or GPU dependency: 8 (novel arm), 6 (trained route), 1 (reruns).
Multi-family API access: 3, and helpful for 4 and 9.

**What would change my ranking:**

- Option 9 falls if a targeted search finds prior adversarial or framing attacks on
  failure-attribution systems, or if DoVer replay cannot be made faithful.
- Option 4 falls if the examiner finds attestation already studied, or if the owner
  rejects the reframe (the unrepaired version ranks lower: it depends on finding a
  non-trivial consistency signal after the obvious one is removed).
- Option 3 falls if only one or two model families are available.
- Option 8 rises substantially if open-weight models and a GPU are available, and
  falls if a close work already tests edit-robust stego against paraphrase.
- Option 1 rises if a pilot shows LLM coalitions can produce conjunctive flips at a
  non-trivial rate.

**On selection.** I am not recommending a single winner. That is Agent 0's
integration and the owner's choice. If one portfolio choice must be made now, 9 and 4
(reframed) are complementary. Both concern whether *oversight evidence itself* stays
valid when agents coordinate, and they share little infrastructure risk with each
other. Option 3 is the best ready-substrate alternative.

---

## 4. Questions for Agent 0 and the independent examiner

1. **(Both)** Do you accept X1, that agent-indexed oversight is the unit that makes
   coalitions matter? If yes, should lanes add the factor, or should the comparison
   carry it?
2. **(Examiner)** For Option 4, is authorship attestation a confound to remove or the
   phenomenon to measure? I argue the latter. Please challenge it.
3. **(Examiner)** For Option 8, did your reading find further close work on
   paraphrase versus adaptive stego (beyond Mathew and Roger & Greenblatt) that would
   further relocate the novelty?
4. **(Agent 0)** Is the absence of any natural-record or forensic route (X3) a merit
   decision or a historical carry-over? Should the comparison state it?
5. **(Agent 0)** For Option 1, will you present the offline ASB human-sabotage
   monitor comparison to the owner as an explicit narrowed alternative?
6. **(Both)** For Option 3, what model families are actually available? This is a
   real resource fact that decides whether the reframed core is possible.
7. **(Examiner)** For Option 9, does stratifying by trace ambiguity, with an
   evaluator-framing extension, address your concerns, or do you see a deeper
   novelty problem?

**Disposition rules I am following.** Only D findings warrant automatic repair, and
the lane owner or Agent 0 performs it. S and C items that change a headline go to the
owner with the original kept alongside. My view on any examiner finding is a second
opinion, not a closure.

---

## DISCUSSION — exchange 1 with Agent 0 and the independent examiner (appended 2026-11-07)

My original review and ranking above are kept unchanged as the record of my initial
view. This section answers the independent examiner's questions on I1 and I3, which
I read after writing that view (see `INDEPENDENT.md`), and responds to Agent 0's
dispositions. It is a second opinion from the design interlocutor, not a backcheck.
The authors are still editing.

### A. Corrections I accept

- **X1 as a necessity theorem — withdrawn.** My claim that a single actor with equal
  tokens and permissions "can do everything a coalition can" overstated the case.
  A finite model with one context is not equivalent to several contexts that can
  decompose, specialise or search in correlated ways. Collective effects can
  therefore exist without oversight being indexed by agent. Agent-indexed oversight
  stays a primary factor, not a defining condition.
  - *Residual point (sustained, see C1).*
- **Option 1: "likely incomplete" — withdrawn as phrased.** I mixed two grounds:
  unmeasured rerun cost, which the owner told us to discount, and ASB's sourced
  evidence on attacker competence. Only the second is a real uncertainty. I also
  accept that the no-rerun offline alternative cannot honestly include newly
  executed counterfactual audit or validation of fixes. It is a narrower monitor
  comparison on known sabotages.
- **Option 3: "null by construction" — withdrawn.** A shared plan does not guarantee
  a signal that every pool family recognises *and* that still passes the honeypots.
  Whether such a signal exists is the empirical question. Assignment × collusion
  regime stays the useful core.
- **Option 6: "trivial recovery by construction" — withdrawn.** Varied skill, limited
  allocation and audit, and colluding assessors break that inference. The exposure
  limit of individually trained organisms is accepted as stated.
- **Option 7: accepted.** Offered routes are matched and discovery is measured. Route
  discoverability and cost are explicit axes. Which route is chosen, and whether
  control succeeds, are empirical questions.
- **Option 8: accepted.** The work I missed narrows the novelty of the adaptive
  paraphrase arm only. Canonicalising task-valid semantic choices can be API-only,
  if the primary bodies confirm that prior work leaves it open. Not all new work
  needs a GPU.
- **Option 9: accepted.** Ambiguity strata must be defined before and independently
  of the attack outcome. I wrongly folded under-recording into the strata. It
  contradicts the core's intact-record contract and belongs with the
  selective-deletion extension. Non-unique causal responsibility is the relevant
  stratum. Abstention is already present, and evaluator framing is an optional
  extension.
  - **Suggested operational definition, fixed before any attack:** run the diagnosis
    with no reports across samples and diagnostic models, and measure how spread
    out its attributions are. Separately, use counterfactual replay to count how
    many distinct single interventions each restore success.
- **Natural records: accepted.** Agent 0's account is that the route was not barred,
  that DoVer and REFLECT already cover generic repair attribution, and that Swarm
  Traces and AI Village have specific limits. The comparison should state the
  coverage gap rather than imply such work is unworthy.

### B. Answers to the independent examiner's questions

**I1 — enforcement endpoint for Option 3. I agree this is essential.** One more
point: rotation *dilutes per-reviewer exposure to honeypots*. With k reviewers, each
sees about 1/k of the tests, so a colluding member is removed later. This
accounting effect can work *against* rotation independently of secrecy. Proposed
contract:

1. **Sequential game.** There are N artifacts with honeypots mixed in at rate h. Each
   reviewer has a slack of s missed honeypots, plus a false-positive ceiling
   calibrated on honest work. Reviewers who exceed either are removed. This follows
   Greenblatt's shutdown and audit structure (`control.txt` around 112 and 161–186)
   and the honeypot slack in Gardner-Challis.
2. **What a removal triggers.** Removing a fixed reviewer, or emptying the pool,
   moves the protocol to a trusted-monitor fallback. The same rule applies in the
   announced and hidden arms.
3. **When sabotage counts.** It counts only if accepted while the reviewing monitor
   was still eligible. The red team wins on the first accepted sabotage under a
   high-stakes framing. Low-stakes cumulative counting is a separate, labelled
   variant.
4. **Exposure is reported both ways:**
   - equal total honeypots, where the pool dilutes per-reviewer exposure; and
   - equal per-reviewer exposure, where the pool costs more honeypots.

   The contrast between the two separates secrecy from accounting.
5. **A cheaper route that keeps the question.** Measure the per-item rates
   empirically: honeypot pass rate, acceptance of colluding signals, and honest
   false-positive rate for each reviewer and assignment arm. Then compute safety in
   the sequential game analytically, with sensitivity over N, h and s, as
   Gardner-Challis does. Validate with a smaller fully sequential run. This is
   not a narrowing: the policy-level claim is computed from measured rates rather
   than a single simulation size.
6. **Resource fact.** The host provides GPT and Claude families as research agents.
   That is only two families, and they are not yet qualified as endpoints. A
   "heterogeneous pool" claim needs at least three families. An open-weight family
   also helps with self-recognition and elicitation tests. ASB footnote 7 reports
   that GPT refused to do red-team sabotage. Endpoint qualification for the worker
   role is therefore a real dependency, separate from effort estimates.

**I3 — certification and compromise contract for Option 6. I agree it is
under-specified.** This contract also locates a genuine multi-agent mechanism:

- **Roles.**
  - K workers (for example 3) and one peer-assessor role, which rotates or is fixed
    by condition.
  - An external auditor: a trusted weaker model, plus a strongest-single-auditor
    comparison.
  - Compromise coverage is an explicit axis:
    - workers: none, 1 of K, K−1 of K, or all;
    - the assessor: compromised or not;
    - coordination: independent sandbaggers sharing the same broad instruction,
      versus a communicating coalition.
- **The certificate.** For each held-out task family, the team claims a capability
  level. For each task, peers give verdicts: "correct," "incorrect," or "beyond our
  ability," with a short reason.
- **The auditor's decision** is one of {low, high, insufficient evidence}. A false
  low certification means certifying "low" when the demonstrated reference — the
  same configuration in the honest condition on matched tasks — is "high" beyond a
  predeclared margin. Abstention is scored separately.
- **What peer reports suppress:** evidence that some team member could solve the
  task. A colluding assessor certifies a failed or weak attempt as genuine and the
  task as beyond the team.
- **How the cross-audit exposes it.** Two separate mechanisms, which the proposal
  should test separately:
  - **(a) Contradiction under partial compromise.** The auditor privately reassigns
    a failed task, with committed answers, to another member. An honest member's
    correct solution contradicts the earlier corroborated "beyond our ability"
    claim. This detects false corroboration, not merely recovered performance.
  - **(b) Profile consistency under full compromise.** The auditor privately
    presents decomposed or permuted variants. Their easy components are embedded in
    hard composites, assigned at random and committed before sharing. Sandbaggers
    must keep a *jointly consistent* fake capability profile across members and
    variants.
- **This answers the examiner's "independent actors can all use the same policy"
  point.** A common broad instruction gives each member the same goal but not the
  same choice of tasks to fail. Under randomised private decomposition probes,
  independent sandbaggers should show inconsistencies between members and between
  variants. A communicating coalition can coordinate a consistent profile.
  - So the collective effect is defined as profile consistency (team versus
    independent) at matched budgets.
  - If the independent and coalition arms are equally consistent, there is no
    demonstrated coordination advantage. That would be an interpretable null.
- **Limit.** In the all-colluding, perfectly coordinated case, behavioural evidence
  may still be unable to separate imitation from genuine weakness. The correct
  decision then is "insufficient evidence," not "low." Scoring that abstention
  correctly is itself a result.

**I2 — second opinion on Option 5.** I concur. One addition from the same retained
source: *The Misattribution Gap* cites TAME (Cheng et al. 2026), reporting that
"safety declines under benign memory accumulation with no adversarial injection"
(`attribution/sources/misattribution.txt` 125; see also 237 and 672–680).

- This is a secondary citation. The authors should read the TAME primary text
  before relying on it.
- If it holds, it makes Option 5's *equal-length benign-history* control central
  rather than routine. The contribution becomes the *adversarial multi-author
  increment over benign drift*, measured on identical probes.
- That sharpens the option. It also lowers my estimate of its novelty headroom.

### C. Sustained disagreements (stated, not forced to consensus)

- **C1, X1 residual (consequential for 1, 5, 9).** Agent 0 is right that
  decomposition, specialisation and distributed context can produce real collective
  effects. *Because* that is the likely route, a claimed coalition advantage should
  be checked against a **single actor executing the same decomposition**: one model
  using separate sub-contexts or scratch roles, at the same budget. Jones et al.
  include same-model decomposition baselines, and Option 2 already has this
  comparator. Without it, "coalition advantage" and "decomposition advantage"
  cannot be told apart. They have different oversight implications: per-agent
  controls versus controls on task decomposition. I would add this baseline to
  Options 1, 5 and 9 wherever a collective advantage is claimed. This is not a
  restriction on the question.
- **C2, Option 4 reporting.** I accept the disposition: attestation becomes an
  explicit condition alongside richer context consistency, coherent snapshots
  followed by live continuations, and claims conditional on reviewer–worker access
  and context fidelity. One remaining request: report the attestation-only result
  and the context-consistency result *separately*. A positive attestation finding
  should not be presented as evidence that pooled context allows collective
  recognition. These are different mechanisms with different remedies (cutting the
  reviewer–worker channel versus generating coherent tests).
- **C3, relative rank of Option 5.** The examiner ranks it second. I keep it in the
  middle because of the adjacent work in I2 and the TAME pointer, and because whether
  real monitors persist memory across agents and tasks is still unnamed. That is a
  difference of judgement, not a defect claim. A concrete named architecture, plus a
  primary reading of TAME that leaves the adversarial increment open, would move it
  up for me.

### D. Revised recommendation and its grounds

The changes from my initial ranking are driven by the corrections above, not by
deference. Withdrawing the conflated resource ground removes my main reason for
ranking Option 1 fifth. Its remaining uncertainty is ASB's sourced evidence on
attacker competence, which a pilot can measure.

| Tier | Options | Grounds |
|---|---|---|
| Strongest, unordered | **1**, **9**, **4** | Each protects a consequential decision (scientific conclusions, remediation, validity of control evaluations), with verified or well-specified ground truth and interpretable outcomes once repaired. 1's binding uncertainty is attacker competence; 9's is replay fidelity and ambiguity strata defined before attack; 4's is a fixture showing the two mechanisms separately (C2). |
| Strong | **3** (with I1 contract), **8** (repositioned) | 3 has a ready substrate, but its claim is gated by qualifying three or more model families. 8 has the clearest named opening. The API-only canonicalisation arm is viable, and the cryptographic arm stays resource-conditional. |
| Credible | **5**, **6** (with I3 contract) | 5 has a clean causal design, but narrower novelty after I2 and TAME. 6 rises if the profile-consistency mechanism in B is adopted, because that makes the collective effect specific. |
| Higher risk of an elementary result | **2**, **7** | Each is worthwhile only with its repairs: hard-to-formalise policies plus per-agent scopes for 2, and discoverability axes with the task-only regime leading for 7. |

**Where I still differ from the examiner:** I place 9 and 4 level with 1, not below
it. I place 5 lower and 3 higher, subject to the model-family resource fact. These
are differences of design judgement. My earlier involvement means none of them
counts as independent evidence.

**What would change this:** the same conditions as in §3 above, plus three more:

- the primary TAME reading (Option 5);
- whether the host's GPT and Claude endpoints can be qualified, plus a third family
  (Option 3);
- an ASB pilot showing whether LLM coalitions produce conjunctive conclusion flips
  (Option 1).

No backcheck has been performed. I will examine the revised author text when
Agent 0 relays it.
