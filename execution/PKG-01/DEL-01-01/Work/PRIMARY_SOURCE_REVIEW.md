# Formation source examination — Agent 0

This is primary-source reading for candidate formation, not a replication of the
papers' empirical findings. Captured bytes, retrieval UTC and SHA-256 identities
are in `primary-sources/*.capture.json`; `primary-sources/manifest.json` records
derived text identities and transformations. Retained full texts are local research
copies, not cleared publication assets. In particular, Basin et al.'s author-version
notice permits personal use and explicitly disallows redistribution.

## Event context and timing

The current [event page](https://apartresearch.com/sprints/swarm-alignment-2026)
was retrieved on 2026-11-06 at 21:24:57 UTC (HTTP 200, HTML SHA-256
`dbc791ec06a1c6922a2b1b61e7f41d3f612ab755759ef1e587cd7035736b6e81`). Its HTML contains
the four panels; text and hyperlinks were extracted without executing page scripts.
The relevant Overview, Track 4 Resources, Guidelines and Schedule passages were
read (`event.txt`, lines 160–287, 405–418, 471–518, 525–610, 674–715).

- **Overview:** interacting populations, covert channels and monitor robustness
  motivate Track 4. Incident accounts remain attributed source claims.
- **Resources:** the exact nearest examples are “Forensics on a real swarm,”
  “Did it actually happen?”, “Whose fault was it?”, “Can copies collude without
  talking?”, and “Monitoring split-up attacks.” The latter explicitly links
  Jones et al. and Greenblatt et al. “Did it actually happen?” and “Whose fault
  was it?” have no individual inline paper citation in the inspected panel;
  Zhang et al. is the track-level failure-attribution reference, not an invented
  citation attached to those examples. The forensics example cites Swarm Traces.
- **Guidelines:** current wording retains the eight-page main-text maximum,
  150–250-word abstract, required limitations/dual-use appendix, optional code/video,
  and distinction between prior work and the weekend contribution. The rubric
  evaluates originality, execution, and clarity for all routes; an example is not
  itself a novel result.
- **Schedule:** November 8 23:59 AoE remains the official cutoff, equivalent to
  November 9 11:59 UTC. At activation there were 62 h 35 min until that cutoff.
  The November 8 18:00 and 23:00 UTC internal targets remain feasible calendar
  positions (44 h 36 min and 49 h 36 min after activation), not commitments about
  available participant time. Six hours after activation is November 7 03:23:36 UTC;
  that proposed selection target does not authorize the next phase.

The Schedule now links a recording and slides for John Yan/Elvis Sikora's
“Getting Started with Swarm Incidents,” as well as four earlier recordings. The
recordings are Zoom links; their audio/transcripts were not examined in this pass.
The original incident report and released-data descriptions provide the bounded
primary basis used here. No claim about a talk's content is made. Final writing
allocation, participant review availability and any submission remain owner choices.

## Examined research sources and what they change

### METR incident investigation (2026)

[Brief independent investigation](https://metr.org/hugging-face-incident-report-aug-2026.pdf),
August 26, 2026, retained as `metr-incident.pdf`; examined pp. 1–5 and 22–27,
with targeted searches of the remaining extracted report for relevant limitations.
The report's account uses both a message-board dump and approximately 1,300 private
agent transcripts. On p. 22 the authors explicitly say they traced messages to
agents that wrote and read them. That source basis is materially stronger than
a public reconstructed-payload collection alone.

On pp. 24–26 the authors describe missing channels, incomplete transcripts,
reconstructed action timing and observed small-scale tool-call spoofing; they do
not infer absence from missing events. On pp. 26–27 they describe extensive use
of AI analysis agents, limits of spot checks, and possible errors and framing bias.
These are the investigators' qualifications, not evidence that a particular public
record or conclusion is false. Their full underlying evidence is not available to
this pass, and their access/coverage estimates cannot be transferred to Swarm Traces.

**Formation implication:** study an explicit evidence boundary. Reconstructing a
payload, asserting that it was read, proving a state change, and attributing its
cause are separate claims. Repeating this distinction alone would add little;
a useful follow-on needs a specific audit or tested decision consequence.

### Zhang et al., Who&When (2025)

[Which Agent Causes Task Failures and When?](https://arxiv.org/abs/2505.00212v3),
arXiv v3, June 2, 2025; examined §§2–4.2 and annotation/algorithm appendices via
`who-when.txt`. The event's OpenReview landing page returned a browser challenge
despite HTTP 200; its PDF and API returned 403. This reading uses the authors'
arXiv version, not the blocked OpenReview bytes. The later Who&When Pro references
link the same OpenReview identifier to this work.

§2 defines a decisive agent/step by an intervention changing a failed outcome to
success, choosing the earliest such step. §3 retains failed trajectories and
constructs annotations through expert review and consensus (184 attribution tasks
from 127 systems). It reports annotation uncertainty and disagreement, and §4.2
compares attribution with and without a supplied task reference answer.

**Formation implication:** ordinary attribution, reference access ablation and
cross-agent propagation are already studied. Failed-run selection is appropriate
to their stated task but does not by itself measure false accusation on successful
runs or robustness when the supplied reference is wrong. Human consensus labels
are evidence of the annotation process, not mechanically verified causal truth.

### Liu et al., Who&When Pro (2026)

[Who&When Pro](https://arxiv.org/abs/2607.09996v2), v2, October 9, 2026;
examined §§3.3–3.5, §4.5 and Appendix A in `who-when-pro.txt`. Its method replays
a successful prefix, changes one action, resumes, and retains resulting failures;
static tool observations use a content-addressed cache, while stateful environments
use action-level fidelity checks. It explicitly filters construction artifacts.
Its human review includes a “no clear decisive error” response. Appendix A states
the single-step attribution limit; the benchmark is not a pure multi-agent corpus.

**Formation implication:** a proposal to inject one mistake or control replay drift
is already close to existing work. A useful diagnostic extension would need a
distinct question, such as separating worker errors from corrupted references or
measurements, with independent evidence and abstention. This pass did not qualify
the release for a new analysis or reproduce its stated label fidelity.

### Guo et al., BLADE (2026)

[BLADE](https://arxiv.org/abs/2610.18780v1), v1, October 13, 2026;
examined abstract and introduction, not a full methodological replication.
It explicitly audits source–decision handoffs, distinguishing error introduction,
propagation and repair; its reported experiments use failed Who&When/Pro runs.

**Formation implication:** merely following dependencies or checking faithful
handoffs cannot be presented as an unexamined novelty claim. The current reading
is sufficient to expose that overlap, not to rule out every extension or validate
its reported performance.

### TraceTrial-Bench (2026)

[Trial by Trace](https://arxiv.org/abs/2610.32285v1), v1; examined abstract,
§§2.2–2.3 and relevant method passages in §3. It separates agent outcomes from
harness obligations and distinguishes authoritative state, model-facing records,
artifact state and provider-request evidence. Its §2.3 requires intermediate
distortion, supported order and alternatives before validating propagation;
apparatus failure is a measurement limit rather than a harness defect.

**Formation implication:** generic “check done against actual state,” distinct
measurement boundaries, or apparatus-aware evaluation already have close work.
A three-worker completion study needs a specific interaction effect and comparison.
No TraceTrial data, implementation or numerical result was reproduced here.

### Basin, Klaedtke and Zălinescu (2019)

[Runtime Verification over Out-of-order Streams](https://arxiv.org/abs/1909.11593v1),
ACM TOCL 21(1), DOI 10.1145/3355609; examined introduction pp. 1–3. It gives
three-valued monitoring under delayed/lost/out-of-order observations, explicitly
representing knowledge gaps. Its assumptions include timestamped observations;
it notes limits of clock accuracy. Its conclusions are within its formal model.

**Formation implication:** “unknown” under incomplete evidence is established
runtime-verification practice. Applying it to multi-agent completion reports may
be useful but is not, alone, a new theoretical result. A defensible addition must
state how the actor/monitor/reference boundaries alter an actual oversight decision.

## Search coverage and author checks

The bounded search followed event references, their primary releases, and arXiv
queries saved as `attribution-search.xml`, `partial-observation-search.xml`, and
`reference-error-search.xml`. It found recent work that limits broad novelty claims.
This is not a systematic literature review: queries are narrow, title/abstract
search can miss terminology, and unexamined search hits remain leads. The initial
broad title query and a noisy Crossref query were discovery only; no conclusion
relies on an unretained search preview. The examined paper bodies, not search
snippets, support the comparisons above.

Author checks compared the relevant cited passages with the candidate framing,
preserved source-statement versus interpretation distinctions, and checked the
AoE conversion. PDF extraction emitted font warnings on some arXiv files; prose
used above was legible, but extraction is not a visual proof check of every formula
or figure. The formal proofs and reported experiments have not been independently
verified. Separate scrutiny of the combined comparison and its actual repair backcheck are
recorded in `FORMATION_REVIEW.md` and the owning `RESEARCH_BASIS.md`.
