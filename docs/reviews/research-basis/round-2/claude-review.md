# Round 2 independent review — Claude Opus 5.5

**Reviewer:** Claude Opus 5.5 (`claude-opus-5-5`), round-2 reviewer.
**Written:** 2026-11-06, starting about 19:28 UTC, roughly 64 hours before the
submission cutoff (2026-11-09 11:59 UTC).
**Inputs read:** the round-2 brief, the common brief, `CONVERGENCE.md`, both
round-1 returns, the parent's complete round-1 disposition, `CHANGES.diff`, and
the whole revised candidate. I also read the Library contracts named below.
**Independence:** I did not open `round-2/codex-review.md` or any round-2 parent
disposition before writing this return. While I worked, a file-change notice
showed me the updated `CONVERGENCE.md` status paragraph. It says the Codex
reviewer recommends adoption with no material objection, and it records one
qualification: a `Last-Modified` header does not prove the bytes changed. Where
that qualification touches my own round-1 claim, I say so below (see C2).
**Configuration limit:** I can confirm my model. I cannot see my own effort
setting, so the claim that it matches round 1 comes from the brief, not from me.

## 1. Candidate identity

- **Candidate files.** All 16 files in `round-2/candidate/` match
  `CANDIDATE_MANIFEST.json` (`research-basis-round-2`, captured
  19:22:49 UTC). There are no extra or missing files.
- **Working tree.** The 16 corresponding working-tree files are byte-identical
  to the candidate. HEAD is still `c8401be`, which contains only the README, and
  no `execution/` directory exists. So the owner would be adopting exactly what
  was reviewed.
- **Round-1 snapshot.** It is unchanged; all 13 manifest hashes still match.
- **CHANGES.diff.** It accounts for every difference between the two
  candidates. `diff -ru` shows 221 changed lines in seven text files. The two
  new JSON files add 83 more, which gives the diff's 304. The binary
  `page.html.gz` is the only file the diff omits.
- **Retained website capture.** `page.html.gz` decompresses to SHA-256
  `eb9bcc15…6eb2`, the hash recorded in the source account and
  `capture.json`. I deleted my temporary decompressed copy afterwards.
- **Library.** It is at `897e04e963e4e0eb9ba8126adf92faff36dd5d65` with a clean
  tree, the same revision as round 1. My round-1 validator results therefore
  still apply.
- **Self-recorded hashes.** The candidate's own §9 hash table matches the
  manifest for the PRD, AGENTS, the research-decomp draft and the source
  account.

## 2. Verdict

**I recommend that the owner adopt the round-2 candidate as the project's
operating and setup basis.** That includes the PRD direction and requirements,
decomposition §§1–8 with the PROJECT setup mapping, and the proposed activation
bounds. I have no objection that blocks adoption, and I do not need a third
round.

The targeted repairs resolve every round-1 finding I would have held out over.
The setup mapping is now concrete, and it holds up against the actual Library
contracts.

Before formation starts, I recommend two small edits to the activation material.
Neither affects adoption:

- **R2-1 (safety):** how agents should inspect attack-payload data.
- **R2-2 (authorship):** state the authorship wording faithfully and treat the
  authorship mode as the owner's choice.

The parent can make both edits and backcheck them without another review round.
If the parent rejects either one, it is a small, concrete choice for the owner,
not a reason for a third round.

## 3. Focus questions

### 3.1 C5: the parent's partial disagreement. I now agree with the parent.

My round-1 C5 said "At formation start, the owner states…" followed by
"Formation then works within those answers." That does read as a prerequisite to
all formation. The parent's localization is better, for four reasons:

1. **The lead-time cost has mostly disappeared.** C5 was motivated by the gap
   between starting formation and first raising a question. With a two-hour
   first return, that gap is at most two hours. The candidate also requires the
   lead-time items to be identified "at the outset" and raised "promptly" with
   alternatives (`docs/RESEARCH_DECOMP.md` lines 464–470; steering lines 43–47).
2. **Most formation work does not depend on spend answers.** Reading sources,
   inspecting public data, and developing argument routes can all proceed without
   them. Controlled-trial candidates can carry conditional cost estimates, and
   §6.1 already requires uncertain costs to be stated explicitly (line 417).
3. **"At the outset" can actually be done.** The known lead-time items (model
   budget, AI Village access, sponsor credits) are named in the candidate. So
   they can be raised before any specific candidate exists.
4. **Waiting would cost more than it saves.** Holding formation until the owner
   answers would add delay, against the deadline, for no evidential gain.

**One clarification is useful but not required.** The boundary "no new paid
experimental model calls" next to "existing authorized access" leaves one case
ambiguous: agents launched from the owner's current host session (Claude Code or
Codex subagents) acting as trial subjects. That is probably the cheapest
controlled-trial route, and many organizer examples are trials. Formation will
rate trial candidates differently depending on whether this counts as existing
access. The owner's model-spend answer should say explicitly whether it covers
host-session agents. Formation already has to flag "any choice outside the
current grant", so this is a clarification, not an objection.

### 3.2 The two-hour first return and event targets. I accept them.

- **It is a checkpoint, not a completion target.** The bound returns the actual
  comparison, or partial work with specific gaps. It records start and due times
  and is extended or redirected through steering (lines 443–453). Its effect is
  to give the owner an earlier chance to redirect, which my four-to-six-hour
  figure did not.
- **It matches my round-1 plan.** The six-hour aim for case selection is
  consistent with my round-1 illustrative plan ("case selected by early Saturday").
- **The shallow-return risk is contained.** The risk of a two-hour pass is that
  the owner anchors on a comparison built from organizer descriptions rather than
  primary sources and data. Selection is still governed by the §6.1 sufficiency
  test (lines 427–433), not by the two-hour return. So the risk is visible and
  bounded.
- **The arithmetic works from now.** Suppose activation is around 21:00–22:00
  UTC today. Then the first return lands around midnight UTC, and the case is
  selected around 03:00–04:00 UTC Saturday if the owner is available. That leaves
  roughly 38 hours of investigation and drafting before the 18:00 UTC Sunday
  draft target. The absolute targets come with "do not silently squeeze out
  investigation or review" (line 462), which is the right protection if
  activation slips.
- **The resource boundaries are usable.** Activation uses existing access, adds
  no new paid calls, applications or messages, and escalates dependencies
  promptly.

### 3.3 C9 authorship wording. I agree in part; R2-2 remains (not blocking).

**The parent is right that personal writing is not required.** The retained
capture's Guidelines say: "Use AI tools however they help you: to check your
reasoning, find gaps in a draft, write and debug code, or help with the writing.
Your team is responsible for everything in the report." So my round-1 wording,
"the owner writes or substantially revises the final text", went beyond the
sources. I withdraw it as a requirement.

**What remains is fidelity and a choice the schedule makes by default:**

- **The source is softened.** In round 1, the template export read: "We strongly
  encourage that the final version of the submission is primarily written by your
  team." DEL-03-01 (lines 296–298) paraphrases this as "encourages team
  authorship". That drops "strongly" and "primarily written by". PRD §3.3
  (line 265) keeps "primarily" but also drops "strongly". AGENTS.md asks that
  source qualifications be preserved.
- **The new clause answers a position nobody held.** No review proposed that the
  owner "personally write every section".
- **The schedule assumes one answer.** It sets "a complete report draft by
  November 8 at 18:00 UTC" and "a checked candidate with participant review by
  … 23:00 UTC" (lines 457–459). That casts the participant as the reviewer of an
  agent-written draft. If the owner instead wants to follow the template's strong
  encouragement, they need writing time before 18:00, working from the
  agent-prepared outline and evidence. Five hours of review afterwards is not
  that time. Left unstated, the schedule makes this choice for the owner by
  default.

**R2-2 repair, one or two sentences:**

1. In DEL-03-01, replace the paraphrase with the template's sentence, or point to
   PRD §3.3. Add "strongly" to PRD §3.3.
2. Add the authorship mode to the reconciliation items at activation (line 461).
   The two modes are: agents draft and the owner revises, or the owner writes
   from agent-prepared material while agents check. The owner chooses, and the
   schedule then reserves time for that mode.

Neither edit creates a new requirement.

### 3.4 The now-concrete setup mapping. It is compatible with the Library.

I checked each element against Library `897e04e`:

| Candidate element (`RESEARCH_DECOMP.md` §8) | Library source | Result |
|---|---|---|
| PROJECT consumer profile; five `execution/PKG-nn/DEL-nn-nn/` homes, each with `ScopeOfWork.md`, `deliverable.yaml` and `Work/` | `project-setup/WORKFLOW.md` 19–22; `current-project.md` 3–7 | Matches |
| `--current` scaffolding, then SOW INIT, then needs | `current-project.md` 27–33, 48–68; `scaffold_deliverable.sh` and `check_min_viable_fileset.sh` both accept `--current` | Matches |
| `DECOMP_VARIANT: PROJECT`, `MODE: INIT`, `STATUS_POLICY: NO_STATUS_TOUCH` | `scope-of-work/resources/brief.md` 15, 37–38; `validate_enum.py` 39 | Valid values |
| `decomposition_basis` = `docs/RESEARCH_DECOMP.md@<commit>`; never the README-only HEAD | `brief.md` 12 ("Accepted decomposition path and commit"); `common.py` 229 | Matches. The validator checks only for `@`; the candidate correctly does not rely on that check alone |
| OBJ-001–003 as package-objective references; PRD O and R references as project scope | `common.py` 256–272: each OUT row must cite a declared reference | Works. The validator constrains neither format, and the Library's own tests use `OBJ-007` |
| Boundary-owner and review checks; native needs; neighborhood query | `checks.md` items 13, 19 and 21; `check_boundary_owner_resolution.py` exists; `tools/deliverables/README.md` | Covered by "applicable review/boundary-owner checks" |
| No claim that `project-decomp` ran | `brief.md` 38 ("matching the accepted decomposition basis") | Honest. No Library tool infers or checks the variant from the decomposition's contents |

Codex's round-1 G2 asked that any adaptation be named openly rather than claimed
as conformance. The "consumer profile" wording does that.

**These setup prerequisites belong in the setup brief and acceptance record.**
None is a defect in the candidate:

1. **The acceptance record must cover the cited PRD references.** The scope-of-work
   brief requires "accepted project-scope references" (`brief.md` 13). The
   mapping cites PRD O1–O5 and the R references for each deliverable. If the
   owner accepts only the decomposition, those references are not accepted.
   Either accept them explicitly, or drop the unaccepted ones from each SOW's
   frontmatter.
2. **The source commit needs the owner's explicit authorization.** The candidate
   claims no authority to commit. However, the parent's round-1 remark that "a
   reversible local candidate commit needs no additional ceremony" should not be
   read as permission to commit on the agent's own initiative. Commits are a
   reserved owner action under the host rules. It can be granted together with
   adoption.
3. **The setup brief must authorize grounded determination of `OUT-*`, `AC-*`
   and `VER-*`** (`brief.md` 26–28).
4. **The setup brief must name who executes setup.** `project-setup` routes
   execution to a WORKING_ITEMS instance (WORKFLOW 12–15), and `scope-of-work`
   expects TASK-shaped briefs. Under AGENTS.md this can be one session acting in
   those roles. The candidate leaves this to the brief, which is acceptable.
5. **Record the Library revision used for setup.** The candidate already notes
   this.

**Optional clarification.** `project-setup` says to load `package-activation.md`
"for an activated package's subsequent production". That file prescribes
`construct-local-work-graph` and TASK dispatch. The candidate activates formation
through owner steering under `coordinated-knowledge-work`, which AGENTS.md
selects. Adding one clause to §8 would prevent an executor from silently
substituting the Library route: "activation follows owner steering and the
selected coordination practice; package-activation is not selected."

### 3.5 Initialization versus activation

The distinction is now clear. Setup creates localities and contracts.
Activation is the owner's steering. A setup-complete return accounts for all five
contracts. DEL-01-01 is authored first, and formation does not wait for unrelated
contracts (lines 604–609).

One effect deserves the owner's attention. In the round-1 candidate, formation
could start with no setup at all. Now the steering says to "first verify … the
authored DEL-01-01 locality" (steering lines 9–10). That puts acceptance, the
commit, scaffolding, and authoring and validating the DEL-01-01 contract on
formation's critical path. I accept this. My estimate is under an hour, and
formation's output gets its proper home. The owner can choose either option:

- **(a) As written:** author and validate the DEL-01-01 contract, then activate
  formation.
- **(b) Faster:** scaffold DEL-01-01, activate formation immediately (its writes
  go to `Work/`), and author the contract in parallel (it writes to
  `ScopeOfWork.md`). The write targets do not overlap, and §6.1 already states
  formation's commitments. Under (b), change the steering line to "verify the
  prepared locality; its contract is authored concurrently from §6.1."

There is also a conditional gap. If the owner adopts the research basis but
declines or defers setup, the steering's only output path does not exist. That
case needs a one-line change to the output path. This is not an objection; it
applies only if the owner makes that choice.

### 3.6 Access observations: C2 is resolved

Both sets of requests are preserved without overclaiming:

- **Original records kept.** The original Swarm Traces 403 row stays in place
  (`HACKATHON_SOURCE_BASIS.md` line 101), so the earlier observation is not
  erased.
- **Dated re-checks added.** Lines 105–123 add the 19:05–19:14 UTC re-checks:
  - my GET 200 and ranged response;
  - the parent's Python 403s and curl 200s;
  - the dataset `Content-Length: 15214685`;
  - the size-guard stop, with "no dataset contents were inspected".
- **Exact requests retained.** The exact parent requests are kept in
  `parent-access-observations.json`.
- **Ranged responses differ.** My round-1 ranged GET returned 206. The parent's
  curl request with a range header returned 200 for the full length. The
  candidate does not choose between these, which is correct.
- **Nothing more is claimed.** Fitness, terms, redactions, whether payloads
  support who-talked-to-whom inferences, and dual-use handling are all left to
  formation (lines 119–123).

**One wording nit (optional).** DEL-02-01 says "request-method differences"
(line 211). Every request was a GET; what differed was the client (Python urllib
versus curl), plausibly its User-Agent. "Client-dependent responses" would point
a future acquisition script at the likely cause instead of a false gating
conclusion.

**A correction to my own round-1 claim.** I wrote that the Transluce file "was
modified on the event day despite its 2026-09-23 file name". A `Last-Modified`
header shows the server's file timestamp. It does not prove the bytes changed. I
saw this qualification in the CONVERGENCE notice and agree with it on the
evidence. The candidate's wording is already properly qualified ("reports"; "a
dated URL *can* still serve changed bytes"). The round-1 parent disposition's
phrase "Transluce's changed bytes" carried my overstatement, but that phrase is
not in the candidate.

### 3.7 Research substance after the repairs

The candidate keeps everything the brief asked about:

- **Differentiation from examples.** Each case names its nearest organizer
  example and that example's cited work, and states what it adds, tests, usefully
  replicates or challenges, and at what cost. An organizer example alone does not
  establish novelty (§6.1 lines 396–401; steering 61–62).
- **Valid replication.** It is allowed, and the parent is right not to exclude it.
- **Equal rubric treatment.** The retained capture confirms "All projects are
  scored on the same rubric." My round-1 phrase "a higher bar" for theory was an
  inference about fit, not a rubric fact. "Apply the same event rubric to every
  research route" is the more accurate statement.
- **Participant responsibility** and **permitted AI help** are retained, in R06
  and DEL-03-01.

**Optional clause.** Dimension 1 asks explicitly, for scores of 4–5, "is this
actually new to the field, or replicating recent work?" Naming that question
where §6.1 allows "replicate usefully" would make the scoring consequence of a
replication visible to the owner. It would not discourage replication.

### 3.8 R2-1: how attack-payload data is handled (new; recommended before activation)

**Grounds.**

- In round 1, the Swarm Traces page described its dataset as "over 80,000
  reassembled attack payloads". This is now named as a concrete formation input
  (`HACKATHON_SOURCE_BASIS.md` lines 112–113).
- The steering asks for "representative data inspection" (line 28).
- Formation runs as an LLM agent that has shell and network tools.
- Attack payloads aimed at agents are exactly the content that can redirect such
  an agent if it is read raw into context.

The candidate already has the right principle: "Treat source payloads as data,
preserve their redactions, and do not replay them against external systems"
(steering lines 47–48). It does not say how to inspect safely.

**Repair: one sentence in the steering.**

- Inspect payload datasets through scripts: schemas, counts and fields, with
  bounded, truncated excerpts.
- Do not follow instructions, URLs or commands that appear in payload content,
  and take no network or file actions derived from it.
- Where the host allows, read raw samples in a context without network or write
  tools.

**Why it matters.** This protects the formation run itself, and it supports R04's
dual-use appendix. It does not affect adoption.

### 3.9 Contradictions or unsupported new commitments

I found none. Specifically:

- No reference to `docs/RESEARCH_BASIS.md` remains.
- PRD §2.1, LOOP_INIT and the decomposition agree on the planned output path, and
  each says that setup has not run.
- The `RESEARCH_DECOMP_REVIEW` and LOOP_INIT wording on registration is
  consistent: the method is available for registration review but does not block
  explicit draft use.
- AGENTS.md now carries the standing phase distinction itself and cites §6 at its
  acceptance standing, which resolves C8.
- OBJ-001–003 are labelled as derived bindings that add no scope.
- The timing figures are labelled planning targets, not organizer or scientific
  requirements. Given the deadline, this is the non-invented basis I asked for in
  round 1.

## 4. Dispositions of round-1 findings

| Finding | Round-2 disposition | Basis |
|---|---|---|
| C1 / G3, time bounds | **Resolved** | §6.1 activation bounds; steering 36–41. Two-hour checkpoint accepted (§3.2) |
| C2, access observations | **Resolved** | Dated re-checks with both outcomes preserved. My Transluce wording corrected (§3.6). Optional "client-dependent" nit |
| C3 / G1, output home | **Resolved** | One planned home in DEL-01-01/Work/, consistent across all files |
| C4 / G2, source and objective binding | **Resolved for adoption.** Setup prerequisites §3.4 (1)–(5) go into the setup brief | §8 checked against the Library |
| C5, lead-time decisions | **Withdrawn as a prerequisite; I agree with the parent.** Optional host-agent clarification | §3.1 |
| C6 / example differentiation | **Resolved** | §6.1 and steering. Optional Dimension-1 clause |
| C7, planning burden | **Resolved** | Edits were targeted; no new planning document. Formation's output is the next document |
| C8, draft authority | **Resolved** | AGENTS.md "Research progression" |
| C9, authorship | **Partly withdrawn.** R2-2 remains, not blocking | §3.3 |
| C10, talks | **Resolved** | Steering 65 |
| C11, registration | **Resolved** | Off the critical path in all three places |
| C12, five deliverables and order | **Resolved** | DEL-01-01 first; does not block. Owner option (b) in §3.5 |
| G4, website capture | **Resolved** | Retained capture verified byte-identical |

## 5. Recommended path forward

1. **Parent:** integrate R2-1 and R2-2, plus any optional items, as small edits,
   and backcheck them. No third round is needed unless the other round-2 return
   raises a consequential question I have not seen.
2. **Owner, adoption:** accept named portions of an identified revision:
   - PRD §§1–2, O1–O5, and R01–R22 as event requirements and research standards;
   - decomposition §§1–8, including the setup mapping and activation proposal.

   Then authorize the source commit and a setup brief covering the executor,
   `OUT-*`/`AC-*`/`VER-*` determination, and exact writes. Choose option (a) or
   (b) from §3.5.
3. **Owner, at activation:** answer now or defer, since none of these blocks
   formation:
   - model spend, including whether host-session agents may serve as trial
     subjects;
   - whether to file the AI Village access request;
   - whether to use Adaption credits;
   - the authorship mode;
   - your own availability against the proposed targets.
4. **Setup:** commit, scaffold all five deliverables, author, validate and declare
   needs for DEL-01-01, activate formation, then author the remaining four
   contracts in parallel.
5. **Formation:** two-hour first return, then case selection aimed within six
   hours, then investigation. The report outline starts immediately.

## 6. Remaining objections and limits

**Remaining objections.**

- **Blocking adoption:** none.
- **Before formation starts (activation-brief items):** R2-1 and R2-2. If the
  parent declines either, I would ask that it go to the owner as a one-line
  choice rather than to a third round.
- **Optional, and I will not hold out over them:**
  - the host-agent clarification;
  - the Dimension 1 clause;
  - the "client-dependent" wording;
  - the package-activation clause;
  - the critical-path option (b).

**Review limits.**

- **No new network checks in round 2.** The Swarm Traces "attack payloads"
  description comes from my round-1 observation. The template's "strongly
  encourage" sentence comes from my round-1 reading of the plain-text export.
- **Validator results are reused, not re-run.** I did not re-run the SOW
  validator. I reused my round-1 throwaway `SOW_V1` test, which is valid because
  the Library revision and `common.py` are unchanged, and I re-read the relevant
  validator code.
- **Nothing was executed.** I did not run scaffolding, `dependency-extract` or
  the query CLI against real localities. My statements about setup compatibility
  rest on reading the contracts, not on a performed setup.
- **Time estimates are mine.** The setup duration and the schedule arithmetic are
  my estimates, not measurements. I do not know the owner's time zone or
  availability.
- **Independence is limited.** I read documents written by the same author and
  share the other reviewer's sources. My independent evidence is limited to:
  - the identity checks;
  - the comparison of the Library contracts with the candidate;
  - the Guidelines and rubric text in the retained capture;
  - my round-1 endpoint and template observations.
- **Read-only boundaries kept.** I did not read the other round-2 return or any
  round-2 parent disposition. I spawned no delegates, scheduled no round, and
  changed no candidate, project or Library file. Apart from this return, my only
  write was a temporary decompressed copy of the capture in `/tmp`, now removed.
