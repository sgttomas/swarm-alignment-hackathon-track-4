# Independent review of the hackathon research basis

The owner requested two independent reviewers: Claude Opus 5.5 at x-high effort
and GPT-6.1-Sol at x-high effort. Together with the parent, they should seek an
agreed path forward, resolve warranted changes, and bring remaining material
disagreements to the owner if convergence cannot be reached after three rounds.
Review convergence does not constitute the owner's acceptance of the PRD,
decomposition, method registration, setup, or research results.

## Scope and current candidate

Review the complete candidate in `round-1/candidate/`, identified by
`round-1/CANDIDATE_MANIFEST.json`. Files are copies of the current working-tree
documents, which are uncommitted; the project's existing HEAD contains only the
initial README. The snapshot is to remain unchanged. Reviewers have disjoint
return files outside it and must not edit production or candidate files.

Examine the PRD and RESEARCH_DECOMP together with AGENTS.md, init/steering/entry
material, the local research-decomp draft and walkthroughs, the method review
account, README, and the hackathon source account. These are a coherent proposed
research operating basis, not completed research. Inspect the actual relevant
sources where needed rather than treating the author's summaries as proof.

## Owner intent and conversation context

- The project is for Apart Research's November 6–8, 2026 Swarm Alignment Hackathon:
  `https://apartresearch.com/sprints/swarm-alignment-2026`. All four tabs matter:
  Overview, Resources, Guidelines, and Schedule.
- The owner selected Track 4, Multi-Agent Oversight and Control, and intentionally
  kept several questions open: covert coordination, completion reports versus
  actual state, diagnosis with incomplete evidence, and controls for cooperating
  agents. Other fruitful angles are welcome. They are not four compulsory studies.
- The participant wants useful workflows and tooling and will follow fruitful
  research paths. Research conclusions must rest on their principles, facts,
  reasoning, and evidence; Chirality conformance is not scientific warrant.
- The owner selected this architecture: AGENTS.md, init-prompt.md, LOOP_INIT.md,
  actual steering, a project-local research-decomp, and the Library's existing
  coordinated-knowledge-work. Standing research/review instructions belong in
  AGENTS.md; particular undertakings belong in steering.
- The working framing is oversight under incomplete, unreliable, or distributed
  evidence. It is proposed framing, not a final hypothesis or novelty claim.
- The parent recommended formation/feasibility before substantial dependent
  tooling or confirmatory research: primary-source examination, obtainable-data
  inspection, candidate cases, competing explanations/propositions, a checked
  comparison, and a recommendation. Existing-record analysis, controlled trials,
  and theoretical/methodological/synthesis routes remain possible.
- The source account records website reading and limited access checks only.
  No dataset archive was downloaded or analyzed. AI Village metadata reported a
  manual access gate; Transluce's public ZIP endpoint responded to HEAD; Swarm
  Traces returned 403 from this session. These checks do not establish fitness
  or general unavailability. Raw website capture is temporarily retained at
  `/tmp/apart-four-tabs-readiness/` if still present.
- No research study, formation output, execution tree, or downstream setup has
  been performed. The local research-decomp draft was used explicitly to produce
  the proposed decomposition but is not registered. The owner has not accepted
  the PRD or decomposition; they are willing to consider approval after this review.

## Most recent setup discussion: evaluate this proposal too

The owner asked whether research deliverables should be initialized like other
projects with ScopeOfWork.md, deliverable.yaml, and Work/. The parent's answer,
not yet implemented, was:

1. Adopt the applicable decomposition portions as a setup basis.
2. Initialize all five agreed deliverable homes with substantive scopes and actual
   known input needs, under `execution/PKG-nn/DEL-nn-nn/`.
3. Activate formation through DEL-01-01 with bounded support as needed.
4. Refine case-specific work and input conditions as research forms.

Scope contracts would promise competent investigation and usable outputs, not
positive findings. Work/ would hold evolving research. Case-specific input
conditions would avoid blanket finish-to-start assumptions. The currently planned
`docs/RESEARCH_BASIS.md` output would instead belong under DEL-01-01/Work/, with
project-level navigation pointing to it; the file has not been created yet.

The parent proposed using the current PROJECT setup profile, with explicit
mapping, rather than inventing a RESEARCH enum/schema. Check this against the
actual Library contracts. Source inspection suggests reusable formats but has
not established an executable handoff or granted acceptance. The candidate still
contains the earlier deferred-setup wording and docs/ research-output destination;
decide what should be reconciled and whether the proposed route is justified.

## Relevant external/local sources

The Library is `/Users/ryan/dev/chirality-library`, currently identified at
`897e04e963e4e0eb9ba8126adf92faff36dd5d65`. Its own development/PR instructions
do not govern this consumer project. Relevant sources include:

- `agents/AGENT_HELP_HUMAN.md`, `agents/AGENT_HELPS_HUMANS.md`;
- `workflows/create-workflow/WORKFLOW.md`;
- `workflows/coordinated-knowledge-work/WORKFLOW.md` and its REVIEW-NOTES.md;
- `workflows/project-setup/WORKFLOW.md` and `resources/current-project.md`;
- `workflows/scope-of-work/WORKFLOW.md` and its brief/check/tool resources;
- `tools/scope_of_work/common.py`, `tools/scaffolding/current_locality.py`,
  `tools/deliverables/README.md`, and `workflows/dependency-extract/WORKFLOW.md`;
- the thesis and book sources identified in the candidate PRD, when their
  meaning matters to a finding.

Chirality Root is the separate `/Users/ryan/dev/chirality`. Its incomplete,
uncommitted PRD was found in
`/Users/ryan/.t3/worktrees/chirality/t3-bdac946d/docs/planning/root-prd-20261105/candidate/PRD.md`.
It is design context, not an available monitoring service or an accepted research
commitment. The hackathon's work need not wait for Root to be implemented.

## Review questions and return

Assess the whole candidate independently before reading the other review.
Distinguish acceptance blockers, material improvements, and preferences. Do not
manufacture findings to fill a checklist. Examine:

- fidelity to owner intent and all four event tabs, source standing, and research
  relevance/novelty assumptions;
- whether formation, contribution scope, evidence, review/repair, and progression
  are concrete enough to guide useful work without premature narrowing;
- whether the participant tooling and documentation burden are proportionate to
  the hackathon, and what should be removed, deferred, or made more concrete;
- setup compatibility, scope/need semantics, locality ownership, source identity,
  and the distinction between initialization and activation;
- actual contradictions, unsupported claims, missing conditions, or misleading
  readiness/acceptance statements, with evidence and consequences;
- whether the five deliverables and proposed path should be retained or changed.

Return a readable review to the exact disjoint file in your task. Include:

1. Candidate identity checked and your overall verdict for owner consideration.
2. Findings with stable local IDs, location, evidence, consequence, and a concrete
   proposed repair or a reason to retain the candidate.
3. Your recommended path forward: what can be accepted, what setup should create,
   what should execute first, and any actual owner decisions still needed.
4. What changes would make you agree, remaining objections, and review limits.

Read-only source examination and proportionate local checks are allowed; write
only your assigned review. Do not run paid models or experiments, request dataset
access, contact third parties, change shared libraries, commit, register methods,
set up execution, or delegate further. Return through the actual task completion
mechanism. For later rounds, a fresh task will supply both reviews, the parent's
disposition, and a new identified candidate; do not self-schedule another round.
