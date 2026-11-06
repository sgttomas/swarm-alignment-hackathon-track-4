# Round 1 independent review — Claude Opus 5.5

**Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), independent round-1 reviewer.  
**Written:** 2026-11-06, finished about 19:10 UTC, 64.8 hours before the submission deadline (2026-11-09 11:59 UTC).  
**Independence:** I received only the brief and source paths. `codex-review.md` was already in `round-1/` while I worked, and I did not open it.

## 1. Candidate identity and verdict

**Identity checked.** All 13 files in `round-1/candidate/` match the SHA-256 values in
`CANDIDATE_MANIFEST.json`. The candidate `AGENTS.md` is byte-identical to the live
project `AGENTS.md`. The Library is at `897e04e963e4e0eb9ba8126adf92faff36dd5d65`
with a clean working tree. The PRD's earlier Library revision `40d060bf…` is an
ancestor of it, and only `workflows/README.md` changed between the two, in an
unrelated passage about the `dbm-concordance-seed` package. The Library PRD,
software-prd and create-workflow hashes match those recorded. Root's candidate PRD
hash `10d4d78b…` matches, and its worktree base is `17275f0b…` as stated. The
temporary site capture still exists, and its `page.html` hash matches the source
account (`eb9bcc15…`).

**Verdict: adoptable as a working basis after a few targeted repairs.
Formation should not start until it has a time bound and certain owner decisions.**

The PRD and decomposition are careful, honest about their standing, and accurate
on the event's requirements. I checked R01–R12 against the raw capture and the
template's plain-text export. The research standards are sound. They require each
case to state its multi-agent mechanism. They separate what the actor, monitor and
evaluator can access. They allow an insufficient-evidence result, keep exploratory
work distinct from confirmation, and allow formation to conclude that no candidate
is feasible. These should be kept.

The defects are not about the research standards. Two concern fitness for the actual
event: there is no time bound anywhere, and a data-access observation is now out of
date. The rest are setup and wording reconciliation. None needs a structural rewrite.
The larger risk is that more document work competes with research time: 2,345 lines
of planning material exist and no research has started.

## 2. What I examined

- The full candidate, read completely.
- The Library contracts named in the brief: project-setup and `current-project.md`,
  scope-of-work (WORKFLOW, brief, checks, tools), `tools/scope_of_work/common.py`
  and `id_catalog.json`, `tools/scaffolding/current_locality.py`,
  `tools/deliverables/README.md`, dependency-extract, coordinated-knowledge-work and
  its REVIEW-NOTES, create-workflow, package-activation, the HELP_HUMAN and
  WORKING_ITEMS roles, and the `DECOMP_VARIANT` enum.
- The capture extracts for all four tabs, with spot checks against the raw HTML
  for the submission-form fields.
- The template's public plain-text export.
- Read-only public checks of the data endpoints around 19:05 UTC. I fetched only
  headers or a single byte; I downloaded no dataset.
- Two local checks. First, `validate_workflow_metadata.py` on the candidate draft
  returned **PASS research-decomp**, which backchecks the review account's claim.
  Second, I wrote a throwaway research-style `ScopeOfWork.md` in `/tmp` and ran
  `validate_scope_of_work.py` on it (see C4). Nothing was written in the project
  or the Library, and the temporary files were removed.

## 3. Strengths to retain

- **R01–R12 are accurate.** The capture confirms the PDF limit of 25 MB and the
  form's project title, project summary, "Are you interested in publishing this
  project?", team name and location fields. The template export confirms
  "Recommended length: 4 pages", "Appendix (optional)", the LLM Usage Statement,
  the instruction to replace guidance text, and "strongly encourage … primarily
  written by your team". The deadline conversion is correct. §3.3 handles the
  differences between sources well.
- **Source standing is kept honestly.** Incident narratives are treated as claims
  of their sources. Endpoint reachability is not treated as fitness for use. Root
  is treated as design input, not a service.
- **Research standards that matter for Track 4:**
  - R17 requires that a monitor not rely on ground truth it could not access.
  - The PRD requires each case to state its multi-agent mechanism, which guards
    against completion-claim work collapsing into single-agent reliability.
  - Inconclusive results are distinguished from incomplete work.
  - Formation can return that no candidate is currently feasible.
- **Case-specific input conditions.** The decomposition states case-specific needs
  rather than blanket finish-to-start rules, and treats phases as evidence
  conditions rather than approval gates.

## 4. Findings

Each finding has one of four severities:

- **A (repair before acceptance):** factual or consistency fixes; cheap.
- **B (required before activating formation):** steering content or owner decisions.
- **C (material improvement).**
- **D (optional or preference).**

### C1 — No time or effort bound exists for formation or the event (B)

**Location.**
- `docs/RESEARCH_DECOMP.md` §5, lines 344–347: "No numerical compute or time
  allocation has been invented."
- `docs/RESEARCH_DECOMP.md` §6.1, lines 415–419: "within the actual effort bounds".
- `init/research-formation-steering.md`, lines 51–53: "within any resource limits
  already given in the conversation".
- `docs/RESEARCH_DECOMP.md` §7, lines 500–504: "The next steering must make those
  bounds practical".

**Evidence.**
- No time bound appears in any of the 13 files. A search for hours or time boxes
  returns nothing.
- The brief records no resource limits given in conversation. The steering's stop
  rule therefore points at nothing.
- At review time, 64.8 hours remain before 2026-11-09 11:59 UTC, and no research
  has started.
- The decomposition names its own principal risk: open-ended exploration or
  capability work consuming the event.

**Consequence.** Formation cannot apply its own stopping condition. Without a
deadline-anchored plan, formation and document review can consume Saturday. That
leaves too little time for investigation, critique, and the owner's report writing
(see C9).

**Why this is not an invented target.** A schedule derived from the published
deadline follows from a sourced fact (S3, S15). It is not a number made up to fill
a template, so AGENTS.md's caution does not apply.

**Repair.**
- In the formation steering, the owner sets:
  1. a wall-clock limit for formation's first return;
  2. the latest point at which a case is selected;
  3. when report drafting starts and when the report is frozen;
  4. the spend authorization (see C5).
- Reword the §5 sentence: "Allocation is set in steering from the submission
  deadline; this document supplies no defaults."

**An illustrative plan for the owner to set, not a requirement:**
- Formation's first return within about 4–6 working hours of starting.
- Case selected by early Saturday, November 7 (UTC).
- Investigation through Saturday and into Sunday morning.
- Report outline from the start, a full draft on Sunday afternoon (UTC), owner
  writing and compliance checks on Sunday, and submission with margin before the
  cutoff.

### C2 — Data-access observations are out of date; the Swarm Traces dataset now appears publicly retrievable (A)

**Location.**
- `docs/PRD.md` §3.5, lines 394–401.
- `docs/HACKATHON_SOURCE_BASIS.md`, lines 99 and 101.
- `docs/RESEARCH_DECOMP.md` DEL-02-01, lines 198–202, which uses these
  observations as "initial conditions".

**Evidence from my checks at about 19:05 UTC on 2026-11-06:**
- `GET https://swarmtraces.org/` returns 200, with both the default and a browser
  user agent. `HEAD` returns 501, because the server does not implement HEAD.
- The page is the Swarm Traces report. It links "Download dataset" at
  `/data/final/redacted.jsonl.gz` and a `/viewer/`.
- A single-byte ranged GET of that dataset returns 206, with a total size of
  15,214,685 bytes.
- The page describes the dataset as "over 80,000 reassembled attack payloads",
  redacted at Hugging Face's request.
- `swarms.wiki` returns 200 to a GET. The account recorded a 403 from a HEAD.
- The Transluce ZIP returns 200 to a HEAD, size 4,570,708 bytes,
  `last-modified: Fri, 06 Nov 2026 14:00:24 GMT`. The file was modified on the
  event day despite its `2026-09-23` file name.
- The AI Village API is unchanged: `private: false`, `gated: manual`. Its public
  file listing exposes the file layout for `main-village/` and `game-jam-village/`:
  `chat_messages`, `claude_code_sessions`, `computer_use_turns`, `events`,
  `agent_goals`, `SCHEMA.md`, `example.py`, and others.

**Consequence.** The candidate's hedge was correct ("does not establish general
unavailability"), so this is staleness, not an error. As written, though, the basis
tells formation that the most-cited Track 4 dataset is "unresolved". Three Track 4
examples use Swarm Traces, so that note could bias formation away from analysing
existing records. Separately, the Transluce file is mutable, which reinforces R14
and R21: record a hash and retrieval time on any download.

**Repair.**
- Add a dated re-check row to the source account's follow-up table. Keep the
  earlier observations and record the method, status and size.
- In PRD §3.5 and DEL-02-01, restate Swarm Traces as: "public dataset link
  observed; contents, terms, and fitness unexamined."
- Add two formation questions. First, whether reassembled payload chains can
  support who-talked-to-whom or information-spread inference; this is a fitness
  question, not a given. Second, the dual-use handling of attack payloads
  (relevant to R04).

### C3 — Setup and output-location wording contradicts the latest proposal (A, conditional on the chosen route)

**Location.**
- `docs/RESEARCH_DECOMP.md` §6.1, line 401, and
  `init/research-formation-steering.md`, line 34: both direct output to
  `docs/RESEARCH_BASIS.md`.
- `docs/RESEARCH_DECOMP.md` §8, lines 514–517: setup deferred until mapping is
  qualified; "No execution tree was created".
- `loop/LOOP_INIT.md`, line 63: "No … downstream setup has been executed".

**Consequence.** If the owner adopts the setup route, an agent following the
prepared steering would write formation output to the wrong home. §8 would then
describe a state that no longer holds.

**Repair.**
- **If setup is chosen:**
  - Change the output path in DECOMP §6.1 and in the steering to
    `execution/PKG-01/DEL-01-01/Work/` (filename as chosen).
  - Add a navigation pointer to it in LOOP_INIT.
  - Replace §8's deferral with the selected mapping from C4.
  - PRD §2.1's sentence that `execution/` "is not a prerequisite" can stay. It
    remains true, because setup is chosen, not required.
- **If setup is not chosen:** leave the text as it is.

### C4 — The setup route is compatible with Library contracts, but three preconditions are unstated (A for setup; must be done before setup runs)

**Library evidence.**
- project-setup's current route requires the "accepted decomposition/source
  identity, selected activation scope" (`WORKFLOW.md` lines 21–22;
  `current-project.md` lines 11–16).
- The scope-of-work brief requires `DECOMPOSITION_BASIS` as an "Accepted
  decomposition path and commit", plus non-empty `PROJECT_SCOPE_REFS` and
  `PACKAGE_OBJECTIVE_REFS` (`brief.md` lines 12–14).
- The validator (`common.py` lines 23–30 and 216–282) requires:
  - `decomposition_basis` containing `@`;
  - non-empty scope and objective references;
  - six fixed headings, from Ontology through Axiology;
  - at least one `OUT-*` and one `AC-*`;
  - the canonical matrix columns;
  - each `OUT-*` matrix row citing a declared objective reference and an `AC-*`
    with a `VER-*` or `HUMAN_REVIEW`.
- `DECOMP_VARIANT` is limited to PROJECT, SOFTWARE and DOMAIN
  (`validate_enum.py` line 39). It is optional and inferred.
- `deliverable.yaml` accepts `doc:` and `external:` suppliers, which suit the
  PRD, the source account and owner steering as inputs.

**Local evidence.**
- A throwaway `DEL-01-01` contract validated as `SOW_V1`. Its single criterion
  promised a checked candidate comparison or a supported "no feasible case"
  finding, with no positive result promised.
- Removing `@revision` from `decomposition_basis` made the same contract INVALID.
- HEAD `c8401be` contains only the README. The decomposition is uncommitted and
  unaccepted.
- The decomposition defines O1–O5 but no package-objective identifiers.

**Consequence.** Running scope-of-work `MODE=INIT` now should return
`FAILED_INPUTS`, because no accepted, committed basis exists. Otherwise the contract
would be bound to a mutable working-tree file. The PROJECT profile fits research
contracts without a new RESEARCH enum. Inventing one would require changes to the
Library, which is outside this project's authority. So I agree with the parent's
choice of profile.

**Repair, recorded in DECOMP §8 or the setup brief rather than a new document:**
1. The owner accepts named portions of an identified revision (for example §1–§6).
2. The owner authorizes committing the accepted basis, so that
   `decomposition_basis: docs/RESEARCH_DECOMP.md@<commit>`. Committing also gives
   dated evidence of the weekend's work for R05.
3. Add a package-objective label to each row of §3's package table. Map
   `project_scope_refs` to PRD O1–O5 and to R references where useful.
4. State `DECOMP_VARIANT: PROJECT` explicitly as a mapping, noting that there is
   no RESEARCH variant.
5. Write the `ScopeOfWork.md` contracts so they do not depend on which case is
   selected. Case selection then populates `Work/` and does not substantively
   change the contracts. Substantive contract changes need an owner decision, and
   `MODE=REVISE` needs an accepted scope-change amendment, so case-specific
   contracts would create churn during a three-day event.

### C5 — Owner decisions with lead times are not requested at formation start (B)

**Location.**
- `docs/PRD.md` §6.
- `docs/RESEARCH_DECOMP.md` §6.4.
- `init/research-formation-steering.md`, lines 26–32: "Further resource or
  external-action choices retain their actual authorization requirements".

**Evidence.**
- Most Track 4 examples are controlled trials that need model calls: Catch the
  cartel, Who broke it?, Replicas as a monitor, Can copies collude without
  talking?, Did it actually happen?, and Whose fault was it?
- No model provider or spend is authorized (PRD lines 122–123).
- AI Village requires manual approval, with an unknown delay.
- Adaption credits require signing up with the registration email.

**Consequence.** Formation cannot judge whether controlled trials are feasible
without knowing whether model spend is allowed. It would return "needs a budget
decision" at the end, after these lead times have run.

**Repair.** At formation start, the owner states:
- the model access and spend ceiling; "none" is a valid answer, which limits
  trials to free or local models or to existing records;
- whether to request AI Village access now (an owner action);
- whether to use the Adaption credits;
- whether to ask the organizers or Discord about data.

Formation then works within those answers.

### C6 — The organizer's example projects closely match the owner's four directions, but the consequences for speed, novelty and route choice are not drawn (C)

**Location.** PRD §2.2; DECOMP §2; source account lines 42–55. The examples are
recorded, but their implications are not.

**Evidence.** The Resources tab's Track 4 examples correspond closely to each
direction:

| Owner's direction | Closest organizer examples |
|---|---|
| Completion claims vs actual state | "Did it actually happen?": three workers, "done" checked against a database, effect on later mistakes |
| Diagnosis with incomplete evidence | "Whose fault was it?": planted worker mistake, wrong reference, or grading mistake; "insufficient evidence"; no blame on clean runs |
| Covert coordination | "Catch the cartel", "Forensics on a real swarm", "Catch the swarm at the gateway" |
| Control of cooperating agents | "Replicas as a monitor", "Can copies collude without talking?", "A legitimate channel as a control", "Monitoring split-up attacks" |

Two event sources bear on this:
- Rubric Dimension 1 asks whether a project is "actually new to the field, or
  replicating recent work?"
- The Overview frames the output as "a working result: an environment, an
  evaluation, an attack, a defence, a monitor or a forensic tool". The
  recommended report structure asks for quantitative results, variance and
  baselines.

**Consequence.**
- **Helpful:** formation can start from near-complete designs sized for a weekend,
  rather than from the broad framing alone.
- **Risk:** other teams are likely to pick the same examples. A straight execution
  may score as "generic or well-trodden" unless it is differentiated.
- **Route choice:** a purely theoretical or synthesis route is still legitimate,
  but it faces a higher bar against this rubric and this framing of the output.

**Repair.** Add three points to the formation critique, keeping the broad framing
as the umbrella:
1. Map each candidate to its nearest organizer example and that example's cited
   prior work.
2. State a concrete differentiator and its feasibility cost. Examples:
   validation on real records, combining an evaluator fault with multi-agent
   propagation, or an explicit manipulation of what the observer can access.
3. Assess fit to the event's expectation of a working, validated result.
   Theoretical routes remain permitted where they produce a checkable artifact,
   such as an argument with constructed counterexample cases.

### C7 — The planning documents repeat each other, and further polishing competes with research (C)

**Evidence.**
- The basis is 13 files and 2,345 lines before any research.
- The formation concept is explained in several places:
  - AGENTS.md;
  - PRD §2.7 and R13;
  - DECOMP §6, which mentions formation 22 times;
  - the research-decomp WORKFLOW §1 and walkthroughs;
  - the steering;
  - LOOP_INIT;
  - the review account.
- AGENTS.md itself says to "use references instead of duplicating".
- The single path change in C3 already touches three files.

**Consequence.** The repeated text can drift out of sync, and each review round
costs owner attention during a three-day event.

**Repair.** Do not consolidate now; that would cost more than it saves before the
deadline. Instead:
1. Limit the next revision to the targeted repairs in C1–C5.
2. Treat DECOMP §6 as the owning account of formation, so later edits change it
   plus pointers.
3. Defer consolidation, and registration of research-decomp (C11), until after
   submission.
4. Create no new planning documents. Formation's output is the next document.

### C8 — The live AGENTS.md incorporates an unaccepted draft section by reference (D, minor)

**Location.** AGENTS.md, "Research progression": "Use the [phased
approach](docs/RESEARCH_DECOMP.md#6-…)". AGENTS.md is already loaded as the
project's instructions in every session, including this one.

**Consequence.** The meaning of the standing instructions shifts if the draft §6
changes.

**Repair.** Either accept §6 explicitly together with the decomposition, or make
AGENTS.md's own summary authoritative and cite §6 as detail.

### C9 — DEL-03-01 should reserve the owner's writing time (C, small)

**Evidence.** The template says: "We strongly encourage that the final version of
the submission is primarily written by your team." PRD §3.3 records this
correctly. DEL-03-01, however, names "one synthesis owner" without reference to the
owner's own authorship.

**Repair.** Add one sentence to DEL-03-01: agents draft and check; the owner
writes or substantially revises the final text. Reserve that time in the C1 plan.

### C10 — Talks relevant to formation inputs (D)

**Evidence.** The Schedule lists talks directly relevant to formation:
- "Getting Started with Swarm Incidents", by Gutenberg PBC (the swarms.wiki
  publisher), 18:00 UTC on November 6;
- "To Catch a Swarm", by Swarmchaser, 19:00 UTC on November 6, in progress at
  review time;
- "Mitigating Insider Threats from AIs with AI Control", 19:00 UTC on November 7.

The FAQ says recordings are posted to Discord and the Schedule tab.

**Repair (optional).** The steering can name these recordings as sources to check
for data-access and prior-work leads once they are available.

### C11 — Registering research-decomp is not on the critical path (D)

**Location.** `docs/RESEARCH_DECOMP_REVIEW.md`, lines 171–173: "The next decision
is review of this package for registration." Also LOOP_INIT lines 56–58.

**Assessment.** The draft passes the metadata validator, which I re-ran. Using it
by explicit path is adequate and consistent with AGENTS.md ("Select project-local
methods explicitly"). Registration mainly enables App discovery and reuse, and the
method has had only one authoring use.

**Recommendation.** The owner decides registration separately; I suggest after the
event. It should not be presented as the next decision ahead of formation.

### C12 — Keep the five deliverables; merging the two PKG-02 deliverables is optional (D, retain)

**Assessment.** Splitting evidence access (DEL-02-01) from analysis and trial
support (DEL-02-02) and from findings (DEL-01-02) preserves a real distinction:
whether a tool works versus whether it supports the research claim (AGENTS.md).
Their consumers also differ.

**Recommendation.** Keep all five deliverables, and let one owner carry a case
across them. If the setup overhead matters, merging DEL-02-01 and DEL-02-02
removes one contract. I do not require it.

## 5. The parent's setup proposal

| Proposal step | My assessment |
|---|---|
| 1. Adopt the applicable decomposition portions as the setup basis | **Agree,** subject to C4: name the accepted portions of an identified revision and commit them. |
| 2. Initialize all five deliverables under `execution/PKG-nn/DEL-nn-nn/` with substantive scopes and actual known input needs | **Compatible with the Library contracts.** The validator accepts a contract promising competent investigation rather than a positive finding; I tested this. Scaffolding is cheap and reports only what it creates. Writing the contracts is the cost. |
| 3. Activate formation through DEL-01-01 | **Agree.** The activation brief is the formation steering plus C1, C5 and C6. |
| 4. Refine case-specific work and input conditions as research forms | **Agree.** Keep contracts independent of the case selected (C4.5), and put case detail in `Work/` and in needs. |
| Use the PROJECT profile with explicit mapping rather than a RESEARCH enum | **Agree.** The enum has no RESEARCH value; adding one would be a Library change outside this project's authority. |
| Move `RESEARCH_BASIS` into `DEL-01-01/Work/` | **Agree,** if setup is chosen (C3). |

**Initialization versus activation.** Initializing a deliverable creates its
location, contract and declared needs. It does not authorize work, and project-setup
says so explicitly. Activation is the owner's steering for that deliverable. So
DEL-01-02 and DEL-02-02 can be initialized without being activated.

**My one difference from the parent's proposal concerns ordering.** Formation
should not wait for all five contracts. My recommended sequence:
1. Commit the accepted basis.
2. Scaffold all five deliverables.
3. Write and validate DEL-01-01's contract and needs.
4. Start formation.
5. Write the other four contracts in parallel, or when each is first used.

DEL-02-01 and DEL-03-01 are touched during formation, through access probes and
the report outline, so they come next. Whether to write all five contracts now or
in that order is an owner preference. The constraint I would hold is that
formation's start does not depend on it.

## 6. Recommended path forward

1. **Owner, now:** decide whether formation should start before review
   convergence. I recommend starting it. The candidate itself says the current
   documents are sufficient for formation, and formation depends on neither PRD
   acceptance nor setup. If the owner prefers to wait, keep round 2 to the
   targeted repairs.
2. **Parent, small edits:**
   - C2: dated re-check and restated access observations.
   - C3: reconcile the wording to the chosen route.
   - C4: write the mapping and preconditions into §8.
   - C1: reword the §5 sentence.
   - C9: add the DEL-03-01 sentence.
   - Optionally C8. Nothing else.
3. **Owner, acceptance:**
   - Accept PRD §1–§2 (direction and framing) and R01–R12 (event requirements).
   - Accept R13–R22 as standards for conducting research, not a list of things
     to build.
   - Accept DECOMP §1–§6 of an identified revision as the setup basis.
   - Authorize a commit.
4. **Setup (WORKING_ITEMS or the parent, under project-setup's current route):**
   commit, scaffold all five, write and validate DEL-01-01's contract and needs,
   then the others without blocking formation.
5. **Formation:** run under the prepared steering, extended with:
   - C1's time plan;
   - C5's spend and access decisions;
   - C6's example mapping, differentiation and route-fit criteria;
   - C2's dataset-fitness and dual-use questions;
   - optionally C10.

   Return a comparison and recommendation within the time limit.

**Owner decisions still needed:**
- the time plan;
- model spend and access, including Adaption credits;
- whether to request AI Village access;
- whether to wait for review convergence before formation;
- whether to write all five contracts now or DEL-01-01 first;
- when to register research-decomp;
- team or solo, and submission details (already listed in PRD §6).

## 7. What would make me agree, remaining objections, and limits

**I would agree with a common recommendation that includes:**
- C1: a deadline-anchored time limit and checkpoints in the formation steering,
  and the reworded §5 sentence;
- C2: the dated access re-check recorded, without deleting the earlier
  observations;
- C3: the wording reconciled to whichever route the owner chooses;
- C4: the setup preconditions and mapping recorded before setup runs;
- C5: the lead-time decisions requested at formation start;
- C6: the example mapping and differentiator check in formation's critique.

C7–C12 are improvements or preferences; I would not hold out over them.

**Remaining objections.** None to the research standards or the five-deliverable
structure. My residual concern is about process cost. Further review or
consolidation rounds should be justified by a consequential open question, as
AGENTS.md itself states, given the time remaining.

**Review limits.**
- I did not download or inspect any dataset, read the Track 4 papers, watch any
  talk, or read Root's PRD content beyond verifying its identity.
- My endpoint observations are from about 19:05 UTC on 2026-11-06 and may change.
  Swarm Traces' terms and license are unread.
- For tab text I relied on the parent's extracts in `/tmp/apart-four-tabs-readiness/`,
  after verifying the raw page's hash and spot-checking the form fields in the
  raw HTML.
- The SOW_V1 test was a synthetic contract in `/tmp`. I did not run project-setup,
  dependency-extract or the deliverables query CLI on real localities.
- The validator checks only for `@`, not that it names a real commit. Requiring a
  commit comes from the brief's schema and project discipline, not from the tool.
- My time-plan figures are a proposal for the owner, not derived requirements.
- I read the same documents the author wrote. My independent evidence is limited
  to the live endpoint checks, the template export, the identity checks and the
  validator runs.
