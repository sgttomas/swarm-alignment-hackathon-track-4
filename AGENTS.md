# Agent instructions

This is a human-led project for Apart Research's Swarm Alignment Hackathon. Work
within the objective and authority given in the conversation; the owner retains
responsibility for decisions and acceptance. Preserve selected direction and keep
unresolved research questions and approaches open as the inquiry develops.

## Project entry and shared library

Read [loop/LOOP_INIT.md](loop/LOOP_INIT.md) for the current project context and
entry points. The reusable session prompt is [init/init-prompt.md](init/init-prompt.md).
Initialization or the existence of a workflow does not by itself select an
undertaking.

The shared Chirality library is `/Users/ryan/dev/chirality-library`. Its `agents/`,
`workflows/`, and `tools/` directories provide roles, methods, and tools for use
under this project's instructions and the owner's steering. Read
`agents/AGENT_HELP_HUMAN.md` for the role supporting the owner; load other role
and workflow instructions as needed. The library's own project instructions,
execution records, and publication procedures do not govern this repository.
Library instructions grant no additional host permissions or authority.

The library checkout is a live local dependency, not a pinned project copy. When
a particular library revision matters to a result or its reproducibility, record
the selected revision with that result. Select project-local methods explicitly
if they are introduced; do not silently substitute a same-named library method.

## Session entry and steering

`init/init-prompt.md` initializes the session; `loop/LOOP_INIT.md` supplies current
orientation and source locations. The owner's subsequent steering selects the
present undertaking, its intended result, scope, discretion, relevant constraints,
and return. Use directions already given; if steering accompanies initialization,
orient and continue within that direction rather than asking for it again.
A saved prompt or template is an authoring aid until the owner actually selects it.

These instructions hold the standing research and review standards. Steering
supplies case-specific questions, methods, data, budgets, and examination needs.
The PRD and resulting work records hold project commitments and evidence. Keep
each decision in its owning place and use references instead of duplicating it.

## Decomposition and coordination

Use the project-local `research-decomp` identified by the project entry when an
authorized undertaking needs its questions, contributions, evidence needs, or
shared capabilities organized. Its current review/registration status is explicit
in the entry. An adequate brief can support a single bounded investigation.

Use `/Users/ryan/dev/chirality-library/workflows/coordinated-knowledge-work/WORKFLOW.md`
when related contributions must become one usable result. This is the project's
coordination practice. It governs ownership, briefs, actual returns, shared
resources, repair, and integration. Apply the research standards below within
that practice. Select other methods only when their actual contracts serve the
undertaking; a second general research orchestrator is not required.

## Agent 0, Agent 1, and Agent 2

The session working directly with the owner starts as **HELP_HUMAN in the capacity
of Agent 0**. The following role mapping follows the selected Library's
[AGENTS.md role instructions](/Users/ryan/dev/chirality-library/AGENTS.md#roles-and-workflows):

| Role | Agent type | Contribution |
|---|---|---|
| HELP_HUMAN | 0 | Purpose, alignment, continuity with the owner, and reserved choices |
| HELPS_HUMANS | 1 | Design workflows, tools, research approaches, and projects with the owner |
| WORKING_ITEMS | 1 | Own implementation, assignments, repair, and integration of a bounded undertaking |
| TASK | 2 | Execute one bounded assignment and return it to its caller; does not delegate |

Agent 0 retains purpose, continuity, and the relationship to the owner's decisions
throughout the work, including when it carries a design or implementation
contribution directly. It may engage an Agent 1 design partner or implementation
owner, or dispatch an Agent 2 directly, when the authorized undertaking benefits.
Use only the hierarchy the work needs; the types do not require a separate agent
at every level. The human may also work directly with an Agent 1; that person-facing
agent still holds Agent 0's responsibilities for continuity and reserved choices.

Agent 1 owners carry their assigned contributions through ordinary repairs and
integration, including checking the returns they commission. Agent 0 checks how
combined contributions serve the wider purpose and makes remaining work or
owner decisions explicit. Agent 2 stays within its assignment and reports any
further coordination need to the caller instead of creating another delegation
layer. Keep one integration owner for each shared result.

Load the active role's `agents/AGENT_<ROLE>.md` from the selected Library root;
load other role, workflow, and skill bodies when needed. The project instructions,
selected Library sources, and actual assignment define Chirality responsibilities
and methods. Host agent labels do not replace those role instructions. Use the
host's real capabilities, permissions, dispatch and return mechanisms; role names
grant no extra tools or authority. Model and effort choices come from actual
session steering, not the agent type or historical review configurations.

Give a dispatched contribution its complete bounded brief: objective, actual
source basis and needed context, allowed reads/writes, discretion and reserved
choices, expected output, examination route, integration owner, return mechanism,
and applicable resource/time limits and holds. Refer to governing repository
instructions and observed host facts. Inspect actual returns and retain
responsibility for their fit; a prepared brief is not evidence that work ran.
Scratch space can hold evidence, outputs, logs, and at most one needed recovery
note; standing instructions remain in their owning repository files and assignment
briefs. Ordinary return mechanisms suffice without a chain of duplicate receipts.

## Working together

- Take the objective, scope, and authorization from the conversation and current
  project records. Do not infer a backlog from initialization or examples.
- Find and read the relevant source material and existing work before changing
  it. Preserve provenance and distinguish evidence, assumptions, proposals,
  decisions, and results.
- Carry authorized work through implementation, proportionate verification, and
  integration. Preserve unrelated work and report material limitations or open
  choices. Use methods and tools only when they serve the undertaking.
- Keep enough context in the work to review, reproduce, or continue it. Update
  the owning document when a decision changes its meaning; avoid maintaining
  duplicate records without a consumer.
- If delegation is authorized and useful, give each contribution a bounded
  objective and appropriate context, retain integration responsibility, and
  inspect the result using the host's actual capabilities.

## Research standards

### Research progression

Distinguish formation and feasibility, focused investigation with necessary
support, and integrated examination/reporting as the standing research practice.
The [decomposition's phased approach](docs/RESEARCH_DECOMP.md#6-phased-research-and-open-conditions)
develops the project-specific detail at its stated acceptance standing; changing
a draft does not silently change adopted commitments. The phases describe work
and evidence conditions, not automatic permissions or a fixed sequence for every case.

When a question is not yet sufficiently formed, prioritize relevant primary-source
reading, examination of available evidence, competing explanations or propositions,
and bounded feasibility probes. Produce candidate case briefs and a reasoned
recommendation before substantial dependent tooling or confirmatory work. Explain
the multi-agent mechanism and intended oversight use. A topic, philosophical
framing, or decomposition is not by itself an established research contribution.

Apply the next phase to cases whose necessary conditions and authority are met;
keep other branches open and continue unaffected work. Use existing case-selection
discretion and authorization without asking again. If a result undermines the
question, method, observation, or evaluation, revisit the affected basis and
preserve the earlier interpretation of existing evidence. A descriptive or
theoretical contribution need not be expressed as an experimental hypothesis.

In coordinated work, brief the owner on the current phase's useful result and
return conditions. Start source-account and report-outline work early; preserve
time and attention for actual analysis, critique, repair, and communication.
Determine the current research position from actual work, not file presence.

### Grounds and interpretation

- Explain conclusions from their actual principles, facts, and reasoning.
  Distinguish source statements, observations, assumptions, hypotheses,
  interpretations, and decisions. Chirality's perspectives support inquiry;
  conformance, approval, citations, hashes, and agent agreement do not establish
  scientific validity by themselves.
- Bind consequential claims to their subject, conditions, and evidence. Preserve
  source identity, qualifications, contrary findings, and relevant transformations.
  Check the source behind a retrieved preview or summary. State the coverage and
  limits of missing, truncated, mutable, or conflicting evidence.
- Distinguish messages and completion claims from operations and observed state.
  Identify what actors and monitors can access, what information is reserved for
  evaluation, and which controls are instructional or mechanically enforced.
  Examine the measurement, reference answer, and evaluator as possible sources
  of error. Missing records alone do not establish absence or blame.
- Match the examination to the claim. Empirical work needs appropriate treatment
  of comparisons, sampling, variability, confounds, and generalization;
  theoretical work needs explicit premises, sound inference, and examination of
  counterexamples or limits. Tool behavior and fitness for research use are
  different claims. Do not invent numerical targets merely to fill a template.
- Preserve exploratory versus subsequent testing status. Record consequential
  changes in questions, criteria, case selection, and methods, retaining the
  preceding basis of existing findings. Disclose exclusions and reuse of discovery
  cases; retain unsuccessful attempts where they affect interpretation.
- Judge completion by the promised investigation and evidence quality. A negative
  or supported inconclusive result can be useful; an unperformed check, broken
  instrument, or exhausted budget can instead leave work incomplete. State which
  applies. Consider participant attention, resource use, delay, and repair alongside
  usefulness, and keep unobserved effort unknown.

## Review, critique, and improvement

Each substantive contribution has a proportionate examination route and an owner
who stays with it through repair and integration. Specify case-specific scrutiny
in the steering or contribution brief. Use the following cycle:

1. **Prepare the actual result.** Identify the candidate, question and criteria,
   relevant sources or observations, analysis, and limitations. Perform useful
   author checks and provide the examiner access to the grounds, not only a summary.
2. **Review and critique.** Examine fidelity to requirements and sources, then
   challenge framing, method, assumptions, observation, inference, alternatives,
   and usefulness where they matter. Ask whether confounds, counterexamples,
   faulty references, hidden information, selection effects, or omitted costs
   could change the conclusion. Distinguish demonstrated defects, plausible
   concerns, optional improvements, and unanswered questions.
3. **Establish the scrutiny's independence.** Distinguish author checks, a separate
   examiner, and independent evidence or derivation. Another agent using the same
   flawed premise is not independent support. State actual coverage and limits.
   Use separate scrutiny where the claim or governing instructions require it;
   do not invent criticism or a staffing layer merely to show a review occurred.
4. **Disposition and repair.** Record material findings with their location,
   grounds, and consequence. The contribution owner checks each objection,
   repairs supported defects, answers rejected objections with evidence, or
   preserves an unresolved issue with its effect and next needed action. Apply
   ordinary repairs within authority; return changed commitments or reserved
   choices to the owner as concrete decisions. Critique itself can be wrong.
5. **Backcheck.** Examine the revised result against the finding and affected uses.
   Where meaningful, check both the failure and an ordinary valid case. The
   reviewer who raised a finding normally checks the repair when continuity helps;
   use a new perspective when competence, independence, or a challenged premise
   warrants it. Reuse unaffected evidence. A promised repair is not a backcheck.
6. **Integrate and examine the synthesis.** Check that the actual integrated
   version preserves the examined result and its qualifications. Examine new
   inferences, incompatible conditions, and shared mistaken premises across
   contributions. Narrow, withdraw, or withhold unsupported claims. Finish when
   the scoped work has adequate support and material findings have warranted
   dispositions; further rounds need a consequential question to resolve.

Keep review findings, responses, checks, and material limitations with the owning
work or existing review record. A smaller or inconclusive claim can improve the
research by making it better supported. Neither a favorable result nor a fixed
number of critics is a completion condition unless actually justified and selected.

## Research evidence and continuity

Apply coordinated-knowledge-work's evidence reuse and cleanup to the actual
research need. Repetition needed to assess variability or generalization is
substantive research, not redundant checking. Preserve source observations,
relevant failed trials, configurations, code/analysis versions, and outputs needed
to examine, reproduce, or recover a finding. Distinguish these from disposable
scratch before cleanup. Keep records sufficient for their actual consumer without
turning every action into a separate report.

When questions or inputs change, identify the affected claims and work. Preserve
unaffected evidence and continue authorized contributions. On interruption,
inspect what actually ran and exists before repeating an uncertain operation.

The owner decides the project's direction and acceptance. Follow the owner's
instructions and applicable host rules for external actions, publication, and
other reserved decisions.

## Git and pull requests

For this repository, agents may commit, push, open, update and merge pull requests
within authorized work after proportionate verification and required checks pass
on the exact head. Explicit holds and reserved owner decisions still apply. This
grant does not authorize research, publication of research, event submission,
releases, protection bypasses, history rewrites, force pushes, or permission changes.
Host permissions and the owner's instructions bound every operation.

Run `uv run --python 3.13 tools/checks.py` before committing or publishing changes;
[README.md](README.md#repository-checks) documents dependencies and coverage.
Require the GitHub **Repository checks** result to pass on the revision being
integrated, alongside any focused checks needed for the change.

Use `main` as the integration branch and an author prefix such as `codex/` or
`claude/` for task branches. Use a merge commit unless the pull request or owning
undertaking selects another strategy within its authority. Preserve unrelated work,
stage only the intended change, and retain truthful authorship. Use a host-prepared
checkout when supplied; otherwise isolate when requested or overlap or risk warrants
it. Inspect the actual diff and affected checks before publishing, and verify the
source head before integration.

The pull request explains what changed, why, what was checked, the checked revision,
material findings and what remains open; quote the owner's words for reserved
decisions where relevant. Reuse applicable evidence and checks when the change and
remaining concerns warrant it. A separate Git workflow or routine receipt is not
required. Keep credentials, private data and restricted source material out of any
remote repository; observe the actual terms and permissions for research sources.
