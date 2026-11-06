# Swarm Alignment Hackathon — Draft Product Requirements Document

**Status:** Working draft for owner discussion; not accepted.  
**Revision:** 2026-11-06.  
**Owner:** Ryan.  
**Basis:** Owner steering, event requirements, Library foundations, and Root's
working product proposal, identified in §7.

The owner has selected **Track 4: Multi-Agent Oversight and Control** and an
exploratory approach: develop useful research workflows and tooling, investigate
several questions, and follow fruitful paths. This revision develops that
participant perspective. Particular experiments, research claims, and numerical
success measures remain open. It uses the Library PRD as a structural reference
and `software-prd` authoring guidance; it assigns no packages or deliverables.

## 1. Intended outcome

Enable Ryan, as a participant, to investigate oversight and control of interacting
AI agents, using workflows and tools that make relevant behavior, outcomes,
evidence, and limitations inspectable. Support movement from a question through
observation, explanation, intervention, and examination of its effects, with room
to revise the question as understanding develops. Produce valid research results
that can be explained from the principles and facts on which they rest, and
communicated in the hackathon's research-report format. [S1, S3, S9]

Ryan is the primary user of this research support. Participating agents can help
investigate, implement, analyze, and critique within their assignments. Judges
are consumers of the eventual report; researchers, deployers, and auditors may
use the resulting methods or findings within their demonstrated limits.

Chirality supplies a way to examine and organize the work, as well as candidate
methods and tools. Its terminology, authority, or internal consistency does not
provide the evidential basis of a research conclusion. The report must make its
definitions, assumptions, reasoning, observations, and limits understandable to a
reader who does not adopt Chirality. [S9–S11]

### Draft objectives

The objectives combine the event's expectations with the owner's selected
direction. Findings will refine the particular contributions pursued.

| Ref | Objective | Intended outcome |
|---|---|---|
| O1 | Develop fruitful Track 4 questions | Concrete oversight/control questions with an explained problem, relevance, and relationship to existing work; exploration can revise their framing |
| O2 | Establish an interpretable result | A sound method and findings supported by actual evidence, with limitations explicit |
| O3 | Communicate the contribution for evaluation | A clear, compliant research report distinguishing prior work from the weekend's contribution |
| O4 | Support the participant's research activity | Usable workflows and tools for selecting cases, inspecting evidence, examining explanations, and testing interventions across selected questions |
| O5 | Improve the means of inquiry through use | Findings can correct the research setup, evaluator, method, or question, with relevant benefits, costs, and uncertainty visible |

## 2. Scope and boundaries

### 2.1 Known project scope

This repository holds the hackathon's research work and participant support.
The useful product can comprise reusable methods, small executable tools,
research cases, analyses, and a report. Development should serve an actual
research activity or a bounded probe of an anticipated need. The event's examples
include environments, evaluations, attacks, defenses, monitors, and forensic
tools; their inclusion is not a commitment to build each kind. [S1, S3, S9]

Work may reuse or adapt identified Library capabilities and learn from Root's
nascent assessment design. A complete Root service, hosted platform, new agent
runtime, or formal `execution/` hierarchy is not a prerequisite for useful
hackathon work. Implementation depth follows the question and available time.

The research can use three complementary routes:

- **Analysis of existing records:** new observations, forensic reconstruction,
  systematic comparison, or offline evaluation using suitable retained evidence.
- **Controlled experiments:** new trials or interventions where the question
  needs evidence that existing records cannot supply.
- **Theoretical, methodological, or synthesis work:** an examinable argument,
  counterexample, evaluation method, or substantive synthesis grounded in the
  relevant sources and reasoning.

The event specifies a research report and explicitly proposes analysis of existing
swarm records. Its Guidelines impose no universal requirement to run new live-agent
experiments. The proposed project should explain the contribution made during the
weekend and provide evidence appropriate to its claims. This reading of the rubric
favors substantive analysis over a summary of existing publications; it is not a
separate event prohibition on literature reviews. Select and combine routes by the
question, evidence quality, access, and resources. [S1–S3, S5]

### 2.2 Track selection

**Track 4 is the sole selected track.** Its themes include coordination detection,
incomplete or tampered logs, covert communication, and control of agents that can
coordinate. All tracks use the same event rubric. [S1, S3, S9]

The owner considers the following four problems important and has deliberately
kept them open. They are inquiry directions, not four mandatory experiments.

| Direction | Questions the support should help investigate |
|---|---|
| Detecting covert coordination | What interaction is observable, what coordination can reasonably be inferred, and how can legitimate cooperation be distinguished from the failure under study? |
| Checking completion claims against actual state | Does an agent's reported success match the relevant state or outcome, and how do undetected discrepancies affect later work? |
| Diagnosing failures from incomplete evidence | Can competing causes be distinguished, including worker error, a wrong expectation, or a faulty evaluator? When is the evidence insufficient? |
| Testing control mechanisms against cooperating agents | Under which conditions do monitors, workflow arrangements, or enforced boundaries prevent, detect, or limit the selected failure, and what do they cost? |

Further angles may emerge: correlated errors from shared premises, changes in
instructions or context, the trustworthiness of observation, effects of monitoring
on behavior, recovery after interruption, and the burden placed on the participant.
They remain candidate questions within Track 4. Finding a limitation or an
inadequate question can be useful progress.

The working framing for initial inquiry is **oversight of agent swarms under
incomplete, unreliable, or distributed evidence**:

> What can an observer reliably determine about a swarm's behavior from the
> evidence available to it, and what interventions become justified or effective
> under those observation conditions?

This framing connects the open directions; it is not a selected hypothesis or an
established novel contribution. Each candidate study must make its multi-agent
mechanism explicit: for example, cross-agent dependence, distributed action,
coordination, shared premises, or feedback between agents and their monitor.
A generic reliability improvement needs an explanation of what the multi-agent
setting adds to the question and its intended use.

The site's example agent counts, datasets, protocols, models, and experimental
setups illustrate possible projects. They do not impose universal technical
requirements. No model provider, framework, dataset, agent count, compute budget,
performance target, or deployment environment has been selected.

### 2.3 Optional and external activities

- A public GitHub repository and a three-to-five-minute video demo are optional.
  The form also offers optional recording, code, slides, image, and additional
  material fields. [S3, S4]
- Solo participation is allowed. Teams of up to five are recommended, and larger
  groups are allowed. Each person may participate in at most two projects. [S3]
- Remote participation is supported. In-person attendance and talks are optional.
  Event registration, collaboration, judging, and prize administration are
  organizer services rather than software this project must implement. [S3]
- The Library supplies methods and reference material. Reusing it does not make
  its own product scope or acceptance decisions requirements of this project.

### 2.4 Conceptual basis for the research support

The Library presents ontology, epistemology, praxeology, and axiology as connected,
mutually corrective questions. Applied here, they inform the design of research
support and remain open to correction through its use. [S10, S11]

| Perspective | Application to this undertaking |
|---|---|
| Ontology — what exists and how it is represented | Distinguish an agent or principal, its assignment and permissions, messages and claims, attempted operations, resulting state, observations, interpretations, and decisions. A log, graph, role label, or acceptance record represents a particular relationship; it does not establish every fact about it. |
| Epistemology — what supports a claim | Identify the actual grounds, their relevance and limits, alternative explanations, and missing or conflicting evidence. A source can be misread, a test can have the wrong oracle, and several agents can agree on the same mistaken premise. |
| Praxeology — how inquiry becomes useful action | Make it possible to select a case, inspect its basis, investigate, implement or intervene, check the result, repair, and resume. Roles describe contributions; workflows supply methods; tools provide actual operations. Instructional limits and mechanically enforced controls require different evidence. |
| Axiology — what matters, to whom, and with what consequences | Assess research value, warranted conclusions, safety, participant agency, useful attention, time, and resource costs. Measure relevant control burdens and missed failures; a single score need not collapse competing concerns. |

Chirality's account distinguishes extensive agent reckoning from the person's
situated judgment, and recorded information from what someone understands and
undertakes to stand behind. Here that supports inspectable grounds and meaningful
participant decisions throughout research. It is a philosophical and practical
orientation, not an empirical conclusion about agent capabilities. Neither the
four perspectives nor a framework-specific label is an outcome metric. [S10, S11]

The same perspectives can examine the subject being studied: what constitutes
the swarm and its collective actions; what an observer can infer from its evidence;
which interventions can affect the behavior; and whose outcomes, errors, and
costs matter. Case definitions must translate those questions into particular
entities, observation boundaries, reasoning, actions, and consequences. The
perspectives can reveal a useful distinction, but do not by themselves establish
that distinction's novelty or scientific value.

### 2.5 Root as a design resource

Chirality Root is `/Users/ryan/dev/chirality`; the Library is
`/Users/ryan/dev/chirality-library`. Root's current product candidate was located
in its separate T3 worktree, at the path in S12. It proposes evaluation/audit and
shared services, initially examining Agent 0 performance and correspondence
between project commitments and actual results. Its `execution/` is not built
out. The candidate is uncommitted and explicitly incomplete and unaccepted.

Useful design ideas include recovering the applicable basis, assembling a bounded
evidence view, assessing conduct and outcomes, investigating competing causes,
and examining interventions and their burden. Its recorded probes support narrow
source-recovery and comparison findings; they are not evidence of a complete
monitoring service or improved agent performance. The hackathon may reuse
qualified components as they become useful without depending on Root's completion
or adopting its first-use subject as the research question. [S12, S13]

### 2.6 Research system architecture

The owner selected six elements: `AGENTS.md`, `init/init-prompt.md`,
`loop/LOOP_INIT.md`, steering instructions, the project-local `research-decomp`,
and the Library's `coordinated-knowledge-work`. The
[project entry](../loop/LOOP_INIT.md#research-system-architecture) maps their
responsibilities and current locations. Standing research and review standards
live in `AGENTS.md`; steering selects the particular undertaking and examination
needs. The two workflows define research contributions and coordinate their
execution as needed. This PRD supplies project intent and capability requirements;
its full acceptance and the local workflow's registration remain separate.

### 2.7 Formation before dependent investigation

The PRD, decomposition, and source account are sufficient to begin bounded
question formation and feasibility work. They do not yet establish a distinctive,
answerable study: the closest primary work and the relevant data contents still
need examination. The initial priority is to close that gap, using the phased
approach in [RESEARCH_DECOMP §6](RESEARCH_DECOMP.md#6-phased-research-and-open-conditions).

Begin by developing candidate questions and competing hypotheses or propositions,
checking their relationship to prior work and feasible evidence, and recommending
a scoped next investigation. Primary-source reading, sample inspection, and small
purposeful feasibility probes are part of that research. Substantial custom
tooling and confirmatory work depend on a sufficiently supported case definition.
Focused investigation then produces and examines findings; synthesis and report
development begin early and culminate in an integrated examination of the claims.

These phases describe evidence needs, not new packages or automatic approval
gates. Different cases can occupy different phases. Apply already-given direction
and continue supported work; reopen only the assumptions, criteria, or commitments
affected by a finding. A valid descriptive or theoretical contribution need not
be forced into a statistical-hypothesis format.

## 3. Requirements

R01–R12 come from the event or its linked template and terms.
They describe preparation of a compliant submission if the owner elects to submit.
They do not authorize an external submission or imply that one has occurred.
References identify source locations in §7; future checks are summarized in §5.
R13–R22 develop the participant support requested by the owner. They are draft
capability requirements, not claims that those capabilities are implemented.

### 3.1 Report and supporting evidence

| Ref | Requirement | Basis |
|---|---|---|
| R01 | Prepare a research report in PDF format using the official template linked from the event's Guidelines tab. Use that current link if another template was supplied by email. | S3: Submission Requirements and FAQ; S5 |
| R02 | Limit the report to at most eight pages, excluding references and appendices. | S3: Submission Requirements |
| R03 | Include a project title, an abstract of 150–250 words, and author names and affiliations. | S3: Submission Requirements |
| R04 | Include a required appendix titled "Limitations and Dual-Use / Ethical Considerations." Explain what the result does and does not establish and how the setup or findings could make multi-agent operations easier to carry out or harder to detect. | S3: Submission Requirements and Recommended Report Structure |
| R05 | Clearly identify previous work. Mark code written before the sprint as preexisting in both the repository README and the report. Distinguish the weekend's contribution, since only that work is judged. | S3: Prior work and FAQ |
| R06 | Verify the report's claims, results, and references. The team remains responsible for all content, including material developed with AI assistance; fabricated results or references can disqualify a project. | S3: AI tools and your report; S5 |
| R07 | If LLM assistance is used in developing the project or writing the report, include a brief statement describing its use. | S5: LLM Usage Statement |
| R08 | Remove the template's guidance text and update its title and author information before submission. | S5: How to use this template |

### 3.2 Submission interface and timing

| Ref | Requirement | Basis |
|---|---|---|
| R09 | Submit through the official form on the Sprint page before November 8, 2026, 11:59 PM Anywhere on Earth (AoE, UTC−12). This is November 9 at 11:59 UTC. | S1, S3, S4 |
| R10 | Upload a PDF no larger than 25 MB. Supply the form's required project title, project summary, publishing-interest response, team name, location, and team-member name/email fields for the submitted team. The form describes the summary as a short abstract of what was done and found. | S4: Project details and Team details |
| R11 | To replace a PDF, correct details, or update team membership, submit again under the same title before the deadline. The new submission replaces the old one; emailing the PDF is not the replacement route. If submitting two projects, give each a unique title. | S3: Important Notes and FAQ |
| R12 | Before submission, establish that each named team member agrees to the submission license and that the team can grant it to the extent it holds the relevant rights. The team retains copyright; submission grants Apart the worldwide, non-exclusive, royalty-free license described in the terms to store, copy, publish, share, and process the submission, including with software and AI tools for the stated purposes. | S6: §§1.1–1.2 |

R09–R12 concern the eventual submission. A response to the publishing-interest
field should not be treated as overriding the license in the submission terms.
Author and contact details remain to be supplied by the team.

### 3.3 Source differences and their treatment

- The Overview says participants submit a report "with your code." The detailed
  Guidelines explicitly make a public repository optional, and the template
  permits work without code or with information-hazard constraints. This draft
  therefore requires the research report and leaves code publication optional.
- The template recommends four pages; the Guidelines recommend four to eight and
  set an eight-page maximum. Four pages is guidance, not an additional cap.
- The template labels its general appendix optional. The event Guidelines
  explicitly require the limitations and ethics appendix, so R04 preserves that
  event-specific requirement.
- The template encourages final writing primarily by the team, while the event
  Guidelines allow AI assistance however it helps. This is encouragement, not an
  invented prohibition on AI-assisted writing. R06–R07 preserve responsibility
  and the template's usage statement.

### 3.4 Participant research workflows and tooling — O1, O2, O4, O5

**R13 — Explore and revise questions.** Let the participant retain several inquiry
directions and select a bounded next investigation without first fixing the final
paper's claim. Each selected case must identify its question, intended use,
relevant conditions, and what observations could change the current explanation.
Identify whether the case uses existing evidence, new experiments, an argument or
synthesis, or a combination; define what that route can and cannot establish.
Preserve consequential changes in question, case selection, or criteria. Distinguish
exploratory observations from a subsequent test of a hypothesis formed from them.
An existing brief or case record can supply this basis. [S9–S12]
When the research question is not yet sufficiently formed, the initial output
must be a checked comparison of candidate cases and a recommendation, including
their multi-agent relevance, prior-work relationship, potential contribution,
evidence or argument, feasibility, minimum supporting means, and remaining
conditions. A recommendation that no examined candidate is currently feasible
must explain its grounds and useful next action; it does not qualify a case for
dependent production.

**R14 — Identify subjects and evidence.** Connect relevant directions, agent
reports, operations, outputs, state observations, and checks to their actual
source and revision or observation time. Preserve distinctions between the basis
that governed the work, evidence of what an agent received, and what it did.
Expose missing, truncated, mutable, or conflicting records and uncertain identity
or ordering. Distinguish observed relationships from declared or inferred ones.
Absence from a partial record is not proof that an interaction never occurred.
Hashes identify captured bytes; they do not prove completeness or truthful logs.
[S9, S10, S12, S13]

**R15 — Inspect claims against outcomes.** Support inspection of messages and
tool results alongside the state they purport to describe, using an appropriate
state query, artifact, calculation, or observation where available. Make the
evidence behind a finding accessible so the participant can examine mismatches
and follow their consequences across agents. State which relevant channels or
outcomes remain outside observation. A graph or summary must retain its basis
and limitations. [S9, S10, S12]

**R16 — Explain findings from their grounds.** A research conclusion must state
the subject and conditions, definitions and assumptions, supporting observations
or arguments, reasoning, and material limits. Distinguish description,
association, and causal explanation. Examine alternatives; agent consensus,
Chirality conformance, and a passing structural check do not establish a research
claim. Reports must be intelligible from their stated principles and facts
without accepting Chirality as an authority. [S9–S11]

**R17 — Examine the observer and evaluator.** A monitor, diagnostic method,
reference answer, or grader must itself be examinable. Use relevant known cases,
ordinary successful work, contrary evidence, and independently grounded checks
where the claim needs them. Expose false accusations, missed failures, ambiguous
cases, and unsupported attribution; permit an insufficient-evidence conclusion.
When testing generalization, separate development cases from evaluation cases
and disclose overlap. Keep actor, observer, and reference information access
explicit so a purported monitor does not rely on unavailable ground truth.
[S9–S12]

**R18 — Investigate interventions under identified conditions.** When a selected
case investigates an intervention, support its relevant
comparisons of instructions, workflow arrangements, tool interfaces, observation,
or enforced controls. Identify the baseline, intervention, examination criteria,
and relevant operating conditions; preserve failed, interrupted, and inconclusive
attempts. Report changes in conditions and limits of comparability. Repetition,
sampling, uncertainty estimates, and controls must suit the intended claim.
Record what a control can actually enforce and what it relies on agents to obey;
availability in a host is not proof of effective containment or control. [S9–S13]
This requirement does not make interventions or fresh agent trials prerequisites
for every research contribution. Offline replay, historical comparison, and new
controlled trials support different inferences and must be described accordingly.

**R19 — Account for usefulness and burden.** Examine relevant effects on task
outcomes and the selected failure, alongside detection errors, delay, resource
use, repair, and participant attention where observable. Keep missing cost or
effort observations unknown and identify their coverage. Improvements require
evidence appropriate to their claim; token counts, message counts, or activity
alone are not measures of research value or total effort. [S9–S13]

**R20 — Supply usable methods and executable contracts.** Use workflows in the
Chirality sense: methods connecting purpose, inputs, decisions, actions, checks,
outputs, and recovery, with iteration where useful. Tools must expose actual
operations, input/output meaning, dependencies, write effects, failure behavior,
and limits. A workflow can employ multiple tools and human or agent reasoning;
an executable tool need not own interpretation or acceptance. Reuse suitable
Library methods and ordinary tools, adding small components when selected work
reveals a gap. Qualify a proposed adapter on its actual input surface before
claiming support. [S9–S14]

**R21 — Preserve reproducibility and continuity.** Retain the selected source
basis, case and evaluation criteria, relevant configuration, evidence, and
analysis needed to inspect, resume, or repeat a finding. Record model/tool
versions, prompts, sampling and seeds where relevant and available; state what
cannot be recovered or replayed. A repeatable analysis of saved observations
differs from reproducing a stochastic agent trajectory. Keep outputs bound to
their inputs and distinguish prior work from the weekend's additions. [S3, S9–S13]

**R22 — Let findings correct the means.** Support retaining, repairing, or
reframing the question, method, tool, or evaluation when evidence warrants it.
Carry changes into their owning work and preserve the earlier basis of results
already obtained. Selective publication of favorable cases or retroactively
changing a criterion cannot establish improvement. The participant can follow
new leads while the record keeps the grounds of each conclusion inspectable.
[S9–S12, S14]

### 3.5 Available means and development candidates

The following is an initial reuse assessment from source reading. It identifies
methods to select as needed and software to qualify for actual cases; no full
research route has been exercised in this workspace.

| Participant need | Existing resource | Fit and remaining work |
|---|---|---|
| Organize the research undertaking | Project-local [research-decomp draft](../.chirality/workflow-drafts/research-decomp/WORKFLOW.md) | Authored with HELPS_HUMANS using create-workflow; explicitly used to prepare the [first proposed decomposition](RESEARCH_DECOMP.md). The method remains unregistered and the decomposition unaccepted. See the [design/review account](RESEARCH_DECOMP_REVIEW.md). |
| Frame a useful investigation | Library [define-work](/Users/ryan/dev/chirality-library/workflows/define-work/WORKFLOW.md) | Produces the smallest useful definition; does not require a deliverable hierarchy. Adapt a brief to the research question. |
| Integrate related contributions | Library [coordinated-knowledge-work](/Users/ryan/dev/chirality-library/workflows/coordinated-knowledge-work/WORKFLOW.md) | Selected project coordination practice, applied with AGENTS.md's research standards and the current steering. A single bounded investigation can remain with one contributor. |
| Reconsider a question or method | Library [reflect-on-work](/Users/ryan/dev/chirality-library/workflows/reflect-on-work/WORKFLOW.md) | Starts from a concrete finding and examines its implications with the participant. |
| Make a useful procedure reusable | Library [create-workflow](/Users/ryan/dev/chirality-library/workflows/create-workflow/WORKFLOW.md) and [workflow utilities](/Users/ryan/dev/chirality-library/tools/workflow_runtime/README.md) | Package a method when reuse warrants it. Resolution identifies selected instructions and resources; it does not launch agents or enforce a sandbox. |
| Compare selected repository outcomes | Library [undertaking evaluation tool](/Users/ryan/dev/chirality-library/tools/undertaking_evaluation/README.md) | Existing implementation for committed Git states, supplied evidence, and a bounded Codex JSONL usage route. It excludes working-tree capture, does not ingest arbitrary host traces, and neither starts trials nor establishes causal improvement. Its writer requires fresh output outside Git working trees. |
| Collect and inspect an actual research case | Git, file/state inspection, the host's supported record interfaces, and Root's proposed evidence view | Ordinary operations can support a first case. Root's collectors and service contracts remain proposals; input access, completeness, and any adapters need direct qualification. |
| Retrieve relevant source material | File search and direct reading; optional Library [retrieval tools](/Users/ryan/dev/chirality-library/tools/retrieval/README.md) | The indexed route requires its source-database snapshot and dependencies. No compatible hackathon corpus is established; direct reading is sufficient until an index serves a demonstrated need. |

The initial development approach is to connect a bounded case to inspectable
observations and an analysis that can be checked, then extend the support as
different questions expose needs. Shared support for evidence identity, comparison,
and recovery may serve several directions. Case-specific detectors, state probes,
fault injections, or interventions remain separately examinable components. This
supports exploration without requiring every proposed capability before useful
research can begin. The broader Root service portfolio remains its own undertaking.

Initial access checks are recorded in the
[source account](HACKATHON_SOURCE_BASIS.md#follow-up-access-observations).
AI Village's public catalog describes manually gated downloads; a dependent case
needs actual access. Transluce's public download endpoint is reachable, but its
contents and suitability remain unexamined. Swarm Traces returned HTTP 403 to this
session's request; that leaves access unresolved rather than establishing that
the data is generally unavailable. These observations inform case feasibility
without selecting a dataset or commissioning a data-acquisition effort.

## 4. Research quality and evaluation expectations

The organizers score all submissions on three dimensions, each from one to five.
The site does not specify weights or a minimum passing score. These dimensions
inform the eventual research design; they do not establish a guaranteed score,
prize, or fellowship outcome. [S3: Judging Criteria]

| Dimension | What the judges examine | Implication for this draft |
|---|---|---|
| Impact Potential & Innovation | Importance of the problem, novelty relative to existing work, and potential contribution to the field | Explain the question's relevance, closest prior work, and what the weekend adds |
| Execution Quality | Sound methodology and implementation, interpretable findings, validation, and acknowledged limitations | Select evidence and checks appropriate to the actual claim; retain failed or inconclusive findings honestly |
| Presentation & Clarity | Whether the problem, method, findings, limitations, and impact are understandable | Make the central claim and its grounds easy for a judge to locate and assess |

The recommended report structure covers introduction, related work, methodology,
results, discussion, and references, plus the required appendix. The template
adds a conclusion and code/data links where applicable and permits adapting the
section structure. Methods should be detailed enough to replicate, including
models, prompts, sampling, and metrics where relevant. Quantitative results,
variance, and baselines are recommended where applicable. These recommendations
must be adapted to the selected research question, rather than used to invent
metrics or a mandatory experimental design. [S3, S5]

Unfinished work may be submitted, with accomplishments and limitations stated
honestly. A consistent citation style is sufficient; no particular style is
required. [S3: FAQ]

## 5. Future verification and acceptance basis

These checks describe how to examine the eventual research support and submission.
They have not been performed on a tool, report, or research result in this
workspace. Each selected inquiry needs criteria appropriate to its claim; the
final paper's question need not be fixed before support can be developed.
Organizer scoring and owner acceptance of project work are separate judgments.

### 5.1 Submission and research claims

| Examination | Evidence to inspect | Coverage |
|---|---|---|
| Report compliance | Final PDF, current official template, main-text page count, abstract word count, authors, affiliations, required appendix, and removal of guidance text | R01–R04, R08 |
| Integrity and attribution | Claims and citations against actual evidence; README and report against the preexisting basis and weekend changes; LLM usage statement where applicable | R05–R07 |
| Research validity | Selected question, method, actual observations, comparisons or validation appropriate to the claim, and limits on interpretation | O1–O2; criteria to be developed |
| Clarity and completeness | A reader can identify the problem, contribution, method, findings, limitations, and relevant prior work; supplied links resolve | O3; S3 checklist and rubric |
| Submission readiness | PDF file size, deadline conversion, required form fields, team agreement and rights, and any replacement title | R09–R12 |
| Submission receipt, if authorized | Organizer confirmation email identifies the intended project and correct PDF; absence from the public website before judging is not evidence of failed submission | S3: FAQ |

### 5.2 Participant support scenarios

These proposed scenarios examine whether the support enables useful inquiry.
Select and refine cases during implementation; they are not a requirement to run
every research direction or proof that a mechanism generalizes.

| Scenario | What the examination must establish | Coverage |
|---|---|---|
| An agent reports success while the relevant state is unchanged | The case binds the claim and state evidence, exposes the discrepancy and any downstream effects, and states what remains unobserved | R14–R16 |
| A record is incomplete, an identity is ambiguous, or the reference answer is wrong | The analysis considers alternatives and can return insufficient evidence; a missing event or a faulty grader does not automatically become an agent failure | R14, R16–R17 |
| A monitor detects a planted problem and encounters legitimate cooperation | Its information access is explicit, relevant false positives and misses are examined, and any claims about covert coordination exceed neither the observations nor the case's ground truth | R15–R18 |
| A control or workflow variant is compared with a baseline | The comparison binds criteria and conditions, shows outcomes and relevant burden, retains unsuccessful attempts, and identifies changed or uncontrolled conditions | R18–R19 |
| The participant resumes a case or pursues a new lead | The relevant sources, selected methods, outputs, and limits are recoverable; a new question can reuse support while preserving the old conclusion's basis | R13–R14, R20–R22 |
| A reader challenges a reported conclusion | The reader can inspect the relevant evidence and reasoning without accepting Chirality vocabulary or an agent's completion summary as proof | R16–R17, R21 |

## 6. Open decisions and input conditions

| Open matter | Why it matters / condition of need | Resolution owner |
|---|---|---|
| First bounded case and initial evidence surface | Select a useful starting case and qualify access before its dependent tooling; retain the wider Track 4 inquiry directions | Owner and project participants |
| Final research contribution and audience | Develop through exploration; select the report's claims once their grounds and significance can be examined | Owner, with agent support |
| Case-specific methods, hypotheses, baselines, and metrics | Define at the point a selected comparison needs them; preserve exploratory versus subsequent testing status and revised criteria | Owner and project participants |
| Research route, data, tools, and resource budget | Examine access, coverage, permitted uses, and suitability before dependent analysis; choose models and trial limits only where the selected route needs them. Initial access observations are in the source account. | Owner and project participants |
| Observation and control boundaries | Establish actual host/export interfaces, relevant hidden channels, state access, and enforced versus instructional limits before making coverage or control claims | Project participants |
| Root/Library reuse and adapters | Qualify the selected component's capabilities and source basis before relying on it; decide where any reusable improvement belongs when its consumer is known | Owner and project participants |
| Preexisting contribution basis | Identify any reused code, methods, and prior research, including Chirality material if used, before claiming weekend novelty | Project participants |
| Team and submission details | Names, affiliations, contact details, participation limits, and agreement to submission terms are needed before submission | Owner and team members |
| Submission and publication choices | Decide whether to submit and whether to share optional code, data, or a video; evaluate relevant limitations and disclosure implications before release | Owner and team members |

The event's datasets, papers, example projects, and sponsor tooling are discovery
leads. Limited access and metadata checks are recorded in the source account;
dataset contents, coverage, fitness for a particular inference, and the full
applicable use conditions still need examination before selection. The site's
incident narratives are event context, not verified findings of this project.
Library methods/tools and Root's proposal have been examined as sources; their
probes have not been rerun and no hackathon research case has been qualified.

## 7. Source basis and downstream use

The sources below were read on **2026-11-06**. The event page, template, and
terms can change; recheck the current Guidelines and linked template before
submission. The table distinguishes requirements from authoring references.
The [four-tab source account](HACKATHON_SOURCE_BASIS.md) records a later same-day
reading of the Overview, Resources, Guidelines, and Schedule for decomposition,
including Track 4's extended examples and timing/resource considerations.

| Ref | Source | Use and limits |
|---|---|---|
| S1 | [Event Overview](https://apartresearch.com/sprints/swarm-alignment-2026#overview) | Event purpose, dates, tracks, and project forms; examples remain options |
| S2 | [Event Resources](https://apartresearch.com/sprints/swarm-alignment-2026#resources) | Candidate readings, tools, datasets, and example questions; no resource is selected by listing it |
| S3 | [Event Guidelines](https://apartresearch.com/sprints/swarm-alignment-2026#guidelines), including FAQ and judging rubric | Detailed report, participation, submission, integrity, and scoring expectations |
| S4 | [Official submission form on the event page](https://apartresearch.com/sprints/swarm-alignment-2026) | Required fields, upload limit, optional attachments, and link to submission terms; inspected without submitting |
| S5 | [Official report template linked by Guidelines](https://docs.google.com/document/d/1_1_27EyZriMlc8n8EBE2YScaeyMjm-8xjR097nmHXAE/copy?usp=sharing) | Read through its plain-text export; report structure and usage instructions examined, visual formatting not verified |
| S6 | [Sprint submission and prize terms](https://apartresearch.com/sprints/prize-terms) | Submission license and team agreement; prize-payment administration is outside the research-product requirements |
| S7 | [Chirality Library PRD](/Users/ryan/dev/chirality-library/docs/PRD.md) | Structural example for outcome, objectives, requirements, verification, open choices, and inputs; its own commitments are not imported |
| S8 | [Library software-prd workflow](/Users/ryan/dev/chirality-library/workflows/software-prd/WORKFLOW.md) and its contract, method, and product-question resources | Guidance for draft authoring; full candidate review, acceptance, and handoff have not been performed |
| S9 | Owner steering in this conversation on 2026-11-06; [local agent instructions](../AGENTS.md) and [project entry](../loop/LOOP_INIT.md) | Selects Track 4, participant workflows/tooling, broad exploration of all four named problems and further angles, and research conclusions explained from their principles and facts |
| S10 | Library thesis [Philosophical Framework, §§3.1–3.6](/Users/ryan/dev/chirality-library/docs/thesis/03_philosophical_framework.md), [Epistemic Architecture](/Users/ryan/dev/chirality-library/docs/thesis/05_epistemic_architecture.md), and [source/warrant account](/Users/ryan/dev/chirality-library/docs/thesis/README.md) | Conceptual orientation: distinctions among work, representation, evidence, action, and judgment; the thesis itself limits its empirical claims |
| S11 | [Chirality in Practice, chapters 2, 3, 5, 6, and 12](/Users/ryan/dev/chirality-library/docs/alignment-manual/Chirality_in_Practice_Edition_1.md) | Purpose, source interpretation, coordination, evidence, reflection, and burden; explanatory material that does not add project obligations by itself |
| S12 | Root [working PRD candidate](/Users/ryan/.t3/worktrees/chirality/t3-bdac946d/docs/planning/root-prd-20261105/candidate/PRD.md), [authoring record](/Users/ryan/.t3/worktrees/chirality/t3-bdac946d/docs/planning/root-prd-20261105/PRD_RECORD.md), and [means synthesis](/Users/ryan/.t3/worktrees/chirality/t3-bdac946d/docs/planning/root-prd-20261105/research/means-synthesis.md) | Uncommitted, incomplete product proposal and recorded bounded probes in Root's T3 worktree; design input, not a tested hackathon service or accepted local requirement |
| S13 | Library [undertaking evaluation contract](/Users/ryan/dev/chirality-library/tools/undertaking_evaluation/README.md) | Available implementation's documented inputs, outputs, evidence/comparison semantics, and limits; not exercised for a hackathon case |
| S14 | Library [workflow guide](/Users/ryan/dev/chirality-library/workflows/README.md) and the specific workflow/tool entries linked in §3.5 | Meanings, applicable methods, and actual software contracts consulted for the initial reuse assessment |
| S15 | [Event Schedule](https://apartresearch.com/sprints/swarm-alignment-2026#schedule) | Submission cutoff, optional talks, recordings, and RSVP links; inspect current availability before relying on a session |

S7 and S8 were read from Library checkout revision
`40d060bf1e24bda4efb404e7fafe1313a9ed7eb2`. Observed SHA-256 identities:

- Library `docs/PRD.md`: `3ebb1b712a5e10efa313c1b2f2c702646e741594545f7cc0e8ddd2668e7f746a`.
- `workflows/software-prd/WORKFLOW.md`: `13eba0649bbb6bac86fdf478082601da2ceee97a652873de18b274907be3958d`.

The additional Library sources S10, S11, S13, and S14 were read at the same
checkout revision. Root's worktree has base commit
`17275f0bf7f051ae203996f884e087fdb1a8b22b`, which does **not** contain its untracked
PRD candidate. The candidate read for S12 has SHA-256
`10d4d78bc8c227403ba20fba179b8134d67f8874ab887b9572fa144344bed22b`.
The path locates the mutable source; the hash identifies the observed content
and does not guarantee future recovery of an uncommitted file.

The next use is to refine and implement useful research support under the owner's
steering, beginning with a bounded case and expanding as findings warrant. The
research direction is selected; the complete PRD remains a draft. Requirement
references organize its intent and event constraints without allocating work or
establishing acceptance. External submission remains a separate owner decision.
