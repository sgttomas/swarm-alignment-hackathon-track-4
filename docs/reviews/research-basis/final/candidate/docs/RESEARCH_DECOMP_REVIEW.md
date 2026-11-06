# Research-decomp draft: design and examination

**Status:** Prepared for human review before registration, 2026-11-06.

The owner requested a project-local `research-decomp`, using `create-workflow`
with HELPS_HUMANS involved. A separate HELPS_HUMANS design partner authored the
method; the parent retained integration, authored the constructed walkthroughs,
examined the result against this project's draft PRD, and checked the package.
This is a design and walkthrough account, not an independent acceptance audit,
an executed research decomposition, or evidence from a research experiment.

## Reviewable package

- [WORKFLOW.md](../.chirality/workflow-drafts/research-decomp/WORKFLOW.md):
  applicability, roles, inputs and outputs, research basis, bounded contributions,
  examination, shared means, review, handoff, and recovery.
- [execution.json](../.chirality/workflow-drafts/research-decomp/execution.json):
  compatible roles are HELP_HUMAN, HELPS_HUMANS, and WORKING_ITEMS. TASK can
  contribute through a bounded brief; metadata grants no tool permissions.
- [Constructed walkthroughs](../.chirality/workflow-drafts/research-decomp/resources/walkthroughs.md):
  eight optional examples for examining the method, including formation, failure, and recovery.

The project's [AGENTS.md](../AGENTS.md) owns standing research and review
instructions. The [steering template](../init/steering-template.md) is an optional
aid for the owner's run-specific direction. These are project instructions and
entry material, not additional resources within the reusable workflow package.
The [prepared formation steering](../init/research-formation-steering.md) makes
the first research undertaking concrete for later selection by the owner.

Intended identity: `source=project`, `kind=workflow`, `name=research-decomp`.
The source root is this hackathon project. No host-assigned `sourceRootId` or
effective-catalog entry has been observed; no identifier has been invented.
The package is available for review by its explicit path above. Its proposed
registration destination is `.chirality/workflows/research-decomp/` after the
owner reviews and accepts the actual package. It is not registered. After the
authoring work, the owner explicitly selected the draft to prepare the
[first proposed research decomposition](RESEARCH_DECOMP.md). That direct use
does not establish catalog registration or acceptance of the resulting proposal.

## Authoring basis and choices

Selected method: `source=bundled`, `sourceRootId=chirality-root`, `kind=workflow`,
`name=create-workflow`, at
`/Users/ryan/dev/chirality-library/workflows/create-workflow/WORKFLOW.md`.
The Library's retained `chirality-root` catalog identifier is distinct from
the separate Chirality Root repository.

The Library source revision for this authoring work is
`897e04e963e4e0eb9ba8126adf92faff36dd5d65`. The selected create-workflow file's
SHA-256 is `8f6457a9aab6dd08e9967bf8770863d7ab3e3d87a1bcd01594c7c0d5505bfa2a`.
HELPS_HUMANS used `agents/AGENT_HELPS_HUMANS.md` at that source.
The earlier domain-decomp review used historical revision
`f002cb9670468737f3c8e0d7d4ca1f6854c46e96`; the current Library has restored that
workflow. This local design draws on the conversation's comparison of domain,
project, and software decomposition and the foundations in
[PRD §7](PRD.md#7-source-basis-and-downstream-use).

The method carries forward scope and ownership clarity, source fidelity,
conceptual reconciliation, bounded implementation, and interface examination.
It adds explicit treatment of research claims, exploration versus subsequent
testing, competing explanations, observer/evaluator reliability, and inconclusive
results. These are locally authored design choices for this method.

The owner's subsequent feedback requested instructions for reviewing, critiquing,
and improving results and suggested examining `research-orchestration`. The parent
read that workflow's entry, contract, method, brief, checks, and tool behavior at
the same Library revision. An intermediate draft added a review guide while
preserving that workflow's actual domain/retrieval prerequisites and restricted
write contract. Its local R0–R5 labels were not adopted as a general hierarchy of
scientific warrant.

The owner then selected AGENTS.md, init-prompt.md, LOOP_INIT.md, steering,
research-decomp, and coordinated-knowledge-work as the architecture. Standing
research and review instructions now live in AGENTS.md; the separate package
guide was removed. Steering supplies the particular question, discretion,
conditions, and examination needs. Research-decomp specifies each contribution's
review/repair arrangement and hands the work to the selected coordination practice.
Coordinated-knowledge-work is that practice here; research-orchestration is not a
required layer. The [project entry](../loop/LOOP_INIT.md#research-system-architecture)
maps the six elements. These revisions were integrated and checked by the parent;
no new independent review or research run is claimed.

Further owner feedback asked that readiness for research be distinguished from
having an answerable scientific case, and that the initial formation work be
explicit. The method now requires a bounded formation contribution where needed,
with primary-source/evidence examination, candidate questions and competing
explanations or propositions, feasibility, and a reasoned recommendation. It
specifies progression into focused investigation and synthesis through actual
evidence/use conditions. Cases can progress separately; phases add no fixed
approval sequence or package hierarchy. The project's detailed application is
in [RESEARCH_DECOMP §6](RESEARCH_DECOMP.md#6-phased-research-and-open-conditions).
The Library's coordinated-knowledge-work remains unchanged; the project's
instructions and phase-specific briefs supply this research application.

There is no fixed number of packages, contributors, experiments, or checkpoints.
Human review addresses a concrete proposed basis and contribution structure;
existing decisions retain their scope. Full corpus atomization, exclusive domain
taxonomies, numerical context-size classes, and retrieval thresholds are not
default obligations. They can be selected for a particular need under its basis.

## Walkthrough against the hackathon PRD

This examination read and traced the method's treatment of the PRD. It did not
assign packages or commission experimental work.

| PRD concern | Examination of the draft method |
|---|---|
| Four open directions within Track 4; O1 and R13 | Step 1 permits committed exploration with candidate questions. Step 2 groups by useful contributions, avoiding four compulsory studies or packages. |
| An initially broad framing and unqualified source leads | Step 1 now defines actual formation work and its checked case-comparison return; step 4 makes dependent work wait only for its necessary conditions and actual authority. The project applies this to the multi-agent mechanism and oversight use. |
| Completion claims, source coverage, and actual state; R14–R15 | Steps 2–3 require input suitability and examination of observations. The completion-report example distinguishes state, observation time, monitor access, and evaluation-only information. |
| Conclusions explained from principles and facts; R16 | Steps 1 and 3 require definitions, grounds, competing accounts, and inference limits. The theoretical example checks an argument without forcing an experiment or framework score. |
| Evaluator failures and interventions; R17–R19 | Step 3 specifies the needed examination and review arrangement. Project AGENTS.md owns the review/critique/repair/backcheck cycle and examination of new synthesis claims. Step 4 considers burden without equating activity counts with total value. |
| Reuse of available means; R20 | Step 4 ties shared capabilities to consumers or bounded feasibility inquiries. No complete Root service, arbitrary trace adapter, or new agent runtime is presumed. |
| Revised questions and continuity; R21–R22 | Steps 3 and 6 preserve earlier criteria, failed attempts, source identity, and the basis of existing results while allowing authorized refinement. |
| Report and event constraints; R01–R12 | Steps 1, 2, and 5 carry adopted constraints and check coverage. Format compliance remains distinct from research validity. |

The eight constructed walkthroughs examine broad exploration/shared means,
completion claims, inconclusive versus incomplete work, theory/source disagreement,
changed criteria, interruption/downstream setup, and a critique that invalidates
an apparent improvement, plus formation before dependent tooling. The critique
case checks a mistaken reviewer objection and propagation of the corrected result
into the report. The formation case checks incomplete data, a theoretical route,
different case readiness, and the return when no feasible candidate is established.
Read-through found no need
to promise a favorable outcome or require the final paper's hypothesis before
bounded useful work can be defined.

The session-entry walkthrough also checked that initialization alone selects no
undertaking, already-given steering remains usable, the unfilled steering template
is not executable direction, a bounded inquiry can proceed without full
decomposition, and related contributions use the selected coordination practice.
The local workflow's draft status remains explicit throughout that route.
The later phase walkthrough checked that metadata-only access observations do
not qualify a study, that a hypothesis can be revised after contrary evidence
without rewriting its earlier status, and that already-authorized progression
does not prompt a new approval merely because a phase label changes. These are
document examinations; the formation steering has not been executed by this revision.

## Verification and remaining limits

The Library's `validate_workflow_metadata.py` passed with one workflow checked
and zero issues. It was run against this project's draft directory using an
isolated `uv run --no-project --with PyYAML` environment. Additional direct checks
passed for resource links and containment, ordinary files without symbolic or
hard links, absence of special permission bits, frontmatter/folder identity,
whitespace, and absence of this run's absolute paths in the reusable package.
Local project, user, and Library paths were inspected for a same-named package;
none was found before this draft was created.

The candidate examined has these SHA-256 identities, relative to its package:

| File | SHA-256 |
|---|---|
| `WORKFLOW.md` | `3582643e25805cd7c897d3f25d2775cb98f19bc99ee9b81973996fb866e4fd8d` |
| `execution.json` | `355ed5f4d297a96f76bba8870cb421acf7e48a3c3f9bb6283756de19677e096c` |
| `resources/walkthroughs.md` | `c996104090d0dfa2465b223601ca6afbe92110fad89b169614af0f4b07685fc0` |

Metadata checks establish structure, and walkthroughs examine described use.
Neither establishes host discovery or research efficacy. Subsequently, the draft
was explicitly applied to this project's PRD and four-tab source account to
produce the first proposed decomposition. That is one actual authoring use, not
an accepted result or a demonstration of improved research performance. The
package remains unregistered; the proposal records its checks and limitations.

Current `project-setup` and `scope-of-work` routes describe PROJECT/SOFTWARE inputs.
This draft preserves useful PKG/DEL conventions but introduces no implemented
RESEARCH variant. A future setup handoff must qualify its actual input mapping
and source standing. Bounded work can use adequate briefs without that route.

The selected [create-workflow method](/Users/ryan/dev/chirality-library/workflows/create-workflow/WORKFLOW.md)
states: "The human reviews the proposed method before it is registered for reuse."
Registration can be considered separately when useful; explicit selection of
the draft is sufficient for an authorized undertaking. The current project
decision concerns the reviewed PRD/decomposition basis, proposed setup mapping,
and initial formation scope. Registration would not itself accept those documents
or commission the research.
