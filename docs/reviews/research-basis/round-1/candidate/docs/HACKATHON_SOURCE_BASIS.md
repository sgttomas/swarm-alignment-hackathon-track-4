# Hackathon source basis for research decomposition

**Examined:** 2026-11-06, using a page capture retrieved at 16:40:59 UTC.  
**Source:** [Swarm Alignment Hackathon](https://apartresearch.com/sprints/swarm-alignment-2026).  
**Purpose:** Carry the relevant context from all four tabs into the proposed
research decomposition. This is a source-reading account; it adds no selected
experiments, accepted scope, or research findings.

The HTML response contained all four tab panels. Each panel's text and links were
extracted and read, including the full Track 4 examples. The working capture is
at `/tmp/apart-four-tabs-readiness/`, with the raw HTML, tab extracts, and retrieval
metadata. That temporary location is not a durable archive. The raw response's
SHA-256 is `eb9bcc151d32eccbd5bd57104d45db763812ed27fc393a572474d20ccefb6eb2`.
This document retains the source interpretation and navigation; changing website
content should be rechecked when the affected decision is made.

## Overview: purpose and scope

The [Overview](https://apartresearch.com/sprints/swarm-alignment-2026#overview)
frames population-level failures and potential contributions including
environments, evaluations, defenses, monitors, and forensic tools. The event runs
November 6–8, 2026, with online participation and optional in-person activities.

Track 4 concerns oversight and control when agents coordinate, observations are
partial, or logs may be manipulated. The source points to real-log analysis,
covert-channel detection, and the applicability of trusted-monitor approaches to
cooperating agents. These support the owner's broad Track 4 direction. Incident
accounts on the event page remain claims of their cited sources pending the
examination needed for any research conclusion relying on them.

The Overview also describes prizes, continuation opportunities, partners,
participant backgrounds, and support channels. Those are event context. They do
not supply a research hypothesis, guarantee a follow-up opportunity, or define
this project's technical implementation.

## Resources: questions and available leads

The [Resources](https://apartresearch.com/sprints/swarm-alignment-2026#resources)
tab contains general and track-specific reading, example projects, data/tool
leads, and sponsor support. Its Track 4 examples extend the inquiry space:

- Reconstruct communication and information spread from real swarm records;
  compare what message access and gateway observations can reveal.
- Detect collusion with partial observations while distinguishing legitimate
  cooperation and ordinary successful behavior.
- Attribute failures, test completion reports against actual state, and
  distinguish worker faults from incorrect reference answers or grading.
- Examine replica-based monitoring, model diversity, and coordination through
  shared priors even without an explicit communication channel.
- Investigate attacks or research sabotage distributed across individually
  innocuous actions, including the difference between local and combined review.
- Examine fragmented approval requests and attempts to influence a monitor
  through the agents' own explanations.
- Study authorized communication channels, governance roles, sandbagging, and
  how long coordinated activity can evade observation.

These are candidate questions and example mechanisms. Their presence does not
commission a study or require all of them to be completed. References in adjacent
tracks can inform a Track 4 investigation without selecting another event track.

Potential source and data leads include:

- [Swarm Traces](https://swarmtraces.org/): reconstructed incident material.
- [AI Village](https://huggingface.co/datasets/aidigestorg/ai-village): agent
  interaction records.
- [Transluce agent activity](https://transluce.org/agent-activity): observed web
  activity.
- [swarms.wiki](https://swarms.wiki/): a directory of incidents and research resources.

The Track 4 reading list points to work on
[secret collusion](https://proceedings.neurips.cc/paper_files/paper/2024/hash/861f7dad098aec1c3560fb7add468d41-Abstract-Conference.html),
[multi-agent interpretability](https://arxiv.org/abs/2604.01151),
[AI control](https://arxiv.org/abs/2312.06942),
[failure attribution](https://openreview.net/forum?id=GazlTYxZss),
[emergent communication](https://openreview.net/forum?id=SRn1MtMPRq),
[computer-use security](https://arxiv.org/abs/2601.09923),
[mediated multi-agent learning](https://arxiv.org/pdf/2306.08419.pdf), and
[strategic attacks on mechanisms](https://arxiv.org/abs/2305.02178).
The listing establishes discovery leads; the initial website reading did not
examine these papers or datasets or qualify them for a selected case. Subsequent
access checks are recorded below.

The site advertises $500 in Adaption platform credits and three months of Premium
access for participants, with signup using the event-registration email. This is
an optional resource lead. Account access and suitability for this project are
not established; it is not a selected model provider or committed project budget.

### Follow-up access observations

The following checks were made later on 2026-11-06 while answering which research
materials are available. They examine metadata, a public report page, and HTTP
responses. No dataset archive was downloaded or analyzed, and no account access
request was submitted.

| Material / source | Observed access | Consequence and limit |
|---|---|---|
| [AI Village dataset metadata](https://huggingface.co/api/datasets/aidigestorg/ai-village) | The public API returned `private: false` and `gated: manual`. Its catalog lists agent identities/goals, chat messages, computer-use records, memories, and related files. An unauthenticated README download returned HTTP 401. | Catalog visibility does not establish download access. The stated research terms require manual approval, citation, no re-identification, and separate written permission for training/fine-tuning. Actual access and use conditions must be resolved before dependent work. |
| [Transluce investigation](https://transluce.org/agent-activity) and its [data archive](https://transluce.org/data/urlquery-agent-activity-2026-09-23.zip) | The public page was readable and links an archive of URL-query activity. A HEAD request to the archive returned HTTP 200 and `application/zip`. | A promising route for examining existing observations. No archive contents, schema, coverage, labels, or fitness for a research claim have been checked. The report's interpretations remain source claims. |
| [Swarm Traces](https://swarmtraces.org/) | The direct page request returned HTTP 403. | Access is unresolved from this session; this response does not establish general unavailability. The hackathon's description alone is not evidence of successful data access. |
| [METR incident report](https://metr.org/hugging-face-incident-report-aug-2026.pdf) | A HEAD request returned HTTP 200 and `application/pdf`. | The report endpoint is reachable; the report itself was not read in this access check. |
| [swarms.wiki](https://swarms.wiki/) | A HEAD request returned HTTP 403. | The directory remains an unqualified discovery lead. |

The research route should follow the question. Existing-record analysis can
produce new empirical findings without generating new agent activity. Controlled
experiments can address interventions or missing observations, and theoretical
or methodological work can contribute through examined reasoning. The Guidelines
do not impose new live-agent trials on every submission. A systematic synthesis
needs a substantive contribution and appropriate grounds; merely restating cited
work would be weak against the novelty rubric, rather than explicitly disallowed.

## Guidelines: evaluation and submission

The [Guidelines](https://apartresearch.com/sprints/swarm-alignment-2026#guidelines)
tab supplies the judging rubric, report requirements, AI-use and prior-work
guidance, participation rules, and submission/replacement procedures. The current
reading is consistent with the corresponding requirements in [PRD §3](PRD.md#3-requirements).

The decomposition needs to account for research validity and communication as
well as useful tools. The report has an eight-page main-text limit, a 150–250-word
abstract, author information, and the required limitations/ethics appendix.
Code publication and a video remain optional. Prior work must be distinguished
from the weekend's contribution, including reused Chirality material where
applicable. The three judging dimensions address impact/innovation, execution
quality, and presentation/clarity; they do not guarantee a score or require a
positive research outcome.

The FAQ permits unfinished submissions with honest limitations, recommends
rather than caps teams at five, and allows at most two projects per person.
The source's permission to submit unfinished work does not establish that an
unperformed investigation is complete or that its claims are supported.

## Schedule: timing and learning opportunities

The [Schedule](https://apartresearch.com/sprints/swarm-alignment-2026#schedule)
lists preparatory talks on November 5, event talks on November 6–7, and the
submission cutoff on November 8. Session times are shown in PT and UTC; the
submission cutoff uses AoE. The deadline is **November 8, 2026, 23:59 AoE**,
equivalent to **November 9, 2026, 11:59 UTC**.

At this reading, recordings were linked for the Adaption workshop, John Kitaoka's
agent-swarm security talk, Grant Fleming's swarm-risk talk, and Nguyen Tran's
logistics talk. Listed later sessions concern swarm incidents, swarm detection,
agent languages, the kickoff and logistics, swarm modeling, and insider threats
and AI control. The Schedule supplies RSVP links for those sessions and says
further talks may be added. Talk contents have not been examined here.

Participation in talks is optional under the Guidelines. Relevant sessions or
recordings can inform an investigation, and their availability can affect a useful
next action; attendance is not a universal prerequisite for research work.

## Implications for the first decomposition

The current sources and owner direction are sufficient to prepare a proposed
decomposition. It should trace event constraints to the Guidelines/Schedule,
research motivation to the Overview, and candidate questions and resources to
the Resources tab. Preserve the PRD's draft standing and the distinction between
committed exploration and optional investigations.

The first case, actual data/model access, budget, and case-specific evaluation
design remain conditions to resolve before their dependent execution. They do
not require prematurely fixing the final research claim or preparing every
possible tool before research can begin. The method's registration and acceptance
of a resulting decomposition remain distinct from this source-readiness check.
