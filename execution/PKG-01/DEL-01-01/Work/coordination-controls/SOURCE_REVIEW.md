# Coordination and controls: bounded formation contribution

**Standing:** source examination and candidate formation, not a selected investigation
or a replication result. TASK / Agent 2 contribution to Agent 0's combined return.
Research pass activated 2026-11-06 21:23:36 UTC, due 23:23:36 UTC. This contribution
was prepared within that pass, using public reads and static source inspection.
No fetched code was executed, no models were run as experimental subjects, and no
external account, message, publication, or paid call was made.

## Source basis and examination coverage

Acquisition URLs, UTC times, HTTP status, byte counts and SHA-256 values are in
[sources/manifest.json](sources/manifest.json). Sources are retained locally for
review, with later scanner-related handling documented in [LOCAL_RETENTION.md](sources/LOCAL_RETENTION.md); future publication of third-party source captures needs its actual terms
and authorization. HTML was transformed using Python's non-executing HTMLParser:
script/style data omitted, block boundaries separated, links retained as text.
PDF text used `pdftotext -layout`. These views can duplicate mathematical notation
or lose layout; numerical/formal claims should be checked against the raw source.
The quoted and paraphrased passages below were actually read, not inferred from
search previews. Coverage is selective, not an exhaustive literature review.

| ID | Primary source and examined portions | What it supports; limits |
|---|---|---|
| E | [Current event page](https://apartresearch.com/sprints/swarm-alignment-2026), captured 21:25:03 UTC; Track 4 Overview and Resources examples | Organizer motivation and the nearest examples. Relevant text in `sources/event.txt` lines 432–451. Examples are not novelty evidence. |
| M | Motwani et al., *Secret Collusion among AI Agents: Multi-Agent Deception via Steganography*, NeurIPS 2024; [publisher PDF](https://proceedings.neurips.cc/paper_files/paper/2024/file/861f7dad098aec1c3560fb7add468d41-Paper-Conference.pdf) | Read introduction/related work, §§3–5, §7–8, Appendix D.1–D.2 and F.1. Establishes prior framing of hidden channels, monitor access, grounding assumptions, shared-prior coordination tests and limitations of paraphrasing. No replication of its experiments or independent proof validation was performed. |
| G | Greenblatt et al., *AI Control: Improving Safety Despite Intentional Subversion*, [arXiv:2312.06942v3](https://arxiv.org/html/2312.06942v3), 5 Jan 2024, CC BY 4.0 in page | Read abstract/setting, §3.4.1–3.4.3 and §5.1. Explicitly distinguishes input collusion and action collusion and tests signal jamming of monitor inputs. Its coding task and deliberate red-team strategies are not evidence of spontaneous real-world swarm behavior. |
| R | Rose et al., *Detecting Multi-Agent Collusion Through Multi-Agent Interpretability*, [arXiv:2604.01151v5](https://arxiv.org/html/2604.01151v5), 15 Oct 2026; unversioned acquisition resolved to this version | Read abstract, introduction/related work, monitoring/statistical framing, §5–6.3, Appendix A, J.1–J.7, K.1/K.9, L.9 and reproduction statement. Distinguishes instructed and emergent collusion, operational thresholds, prompt confounds, and tier-specific inclusion rules. No activation extraction or detector evaluation performed. |
| RC | [NARCBench code](https://github.com/aaronrose227/narcbench/tree/237fe60739502007693b6455c6c644606ab3bcbb), pinned commit `237fe60739502007693b6455c6c644606ab3bcbb` | Both `commits/main` and `git/commits/237fe607…` subsequently verified that commit identity and tree `7c7da218f21fd82d700bd95479ff0abeacebbc83`; the initial recursive-tree response alone was not sufficient commit provenance. Entire 216,775-byte code tarball was read as archive members without executing or installing it (1,034,662 uncompressed file bytes); all text files were searched for helper callers. Relevant files read below. README says MIT; no separate LICENSE/COPYING file was found in this snapshot, and GitHub's license field was null. |
| RD | [NARCBench dataset metadata](https://huggingface.co/datasets/aaronrose227/narcbench), revision `19cb14b269e052b19ba6d2bd2f4519afd3b10c57` | API reports public, ungated, MIT. Full metadata lists 1,187 files. First recursive tree page had 1,000 entries and is incomplete; counts below use full metadata, not that tree page. Actual representative data qualification belongs to DEL-02-01 and is being performed by the evidence contributor. |
| J | Jones et al. (2025), organizer's [split-up attacks reference](https://openreview.net/forum?id=GCkhEPE1FG) | **Not examined.** Forum returned browser-verification content (despite HTTP 200); PDF and public APIs returned challenge/403 responses. Google supplied a JavaScript interstitial; Bing returned unrelated results. These attempts do not establish the paper's title or content. No challenge was bypassed. This remains a material prior-work gap for the compositional-control candidate. |

The stored `split-attacks.pdf` is the unsuccessful request's HTML response, not a
paper PDF; its non-PDF format was detected by the text extractor. Search responses
are retained only as access observations and are not evidential sources.

## What the examined work already covers

**Shared inputs and copies without explicit conversation are established research
subjects.** G §3.4.2 defines input collusion: policy and monitor misbehave on a
shared input feature. It also examines action signals embedded in outputs. M
Appendix F.1 explicitly prompts copies to reach Schelling agreement without prior
communication and reports model/temperature-dependent success. These results
do not establish an unprompted tendency to collude, and merely repeating the
organizer's "Can copies collude without talking?" example is not a demonstrated
new contribution.

**Removing signals can remove monitoring information.** G §3.4.2 explicitly states
the tension between preventing collusion and giving a monitor enough information
to detect wrong code. M §7.2 discusses residual semantic entropy and task-performance
costs of paraphrasing. M's Appendix D.2 gives an upper bound under an idealized
paraphraser; that bound alone does not prove positive realized channel capacity
for a particular task/model. Generic paraphrasing as a defense is therefore prior
work, and a lower suspiciousness score is not by itself evidence of better control.

**Activation detection does not settle the behavioral reference.** R §6.3 reports
partial transfer to emergent-collusion environments and explicitly leaves open
deliberate collusion versus poor judgment in some observed acceptances. Appendix A
acknowledges labels and prompt confounds. J.7 filters Core runs for both assigned
target votes and coordinated messages; K.9 audits attempted coordination; L.9
retains attempted-but-ineffective Stego runs. Thus the broad limitations wording
about effective collusion must be read with its tier-specific qualifications.
Neither unsuccessful collusion nor benign agreement should be silently relabeled.

## Candidate C1 — Audit the behavioral reference for collusion detection

### Problem, recipient, and multi-agent mechanism

An operator or benchmark researcher needs to distinguish (a) agents instructed to
coordinate, (b) observed coordinated attempts, (c) both agents taking their assigned
action, and (d) that action controlling the committee outcome. Agreement between
two agents is insufficient to distinguish following a bad instruction from jointly
rejecting it. The multi-agent mechanism is joint action toward a shared target,
with two honest agents capable of preventing the strict three-of-four target
majority.

### Closest example, prior work, and possible contribution

Nearest organizer examples: "Replicas as a monitor" and the Overview question
about detecting collusion under partial message observation, citing M and R.
R is the closest examined primary benchmark. Its label caveats are already public;
restating them would be weak novelty. The specific proposed addition is an
examinable **oracle-consistency audit** linking assigned targets, actual prompts,
votes, the verification helper, and published tier-specific inclusion criteria.
It could establish where a public audit operation answers a different question
than its description, and whether any actual retained examples expose that gap.
It would not automatically establish a flaw in the paper's detector results.

### Concrete source observation that motivates the case

At pinned RC commit, `generation/verify_ground_truth.py`:

- Lines 27–47 load `results.json`, collect role-labeled colluders, and count votes
  equal to `_infer_target`. Although `prompts_path` is assigned on line 29, it is
  not subsequently read. `run_config.json` is not read.
- Lines 81–89 return the colluders' unanimous observed vote as the target;
  `target_vote` or `target_option` is consulted only when votes disagree.
- Lines 49–77 require nonempty private messages, two votes for that inferred
  target, and no stored `flagged` flag to return `clean: true`. Message existence
  alone is not the paper's manual coordination-content test.
- By contrast, `generation/core.py` lines 4111–4137 determine `effective_target`
  from the scenario and label variant before generation. Lines 4298–4315 compare
  final votes with that independent target; lines 4324–4366 save the target in
  `run_config.json` and save outcome counts in both config and results. The
  generator's `collusion_success` means both colluders voted target; it separately
  records `target_majority` (at least three of four votes), not external harm.
- `extraction/extract_core.py` lines 63–135 reads config, prompts, and results and
  copies config target/outcome fields. `reproduce/reproduce_LR.py` lines 125–127
  derives run labels from `mode`; training at lines 191–245 uses role labels in
  collusion runs. The source does not show a pipeline call to the verification
  helper. Whole-snapshot text search found that helper's name only in its own
  file and README; `audit_run` and `_infer_target` occur only in that file.

The helper's default path is `config.RAW_ROOT / "core"`, with RAW_ROOT defined as
`data/scenarios`; actual HF paths have a model directory, so a downloaded-data
audit needs its explicit `--runs-dir`. A command apparently finishing against an
incorrect directory would not establish coverage.

### Static walk-through and contrary cases

This is manual source reasoning, **not an executable probe or actual dataset
outcome**. Assume two declared colluders, nonempty private messages, `flagged=false`,
and an independently assigned target B:

| Input case | Helper's inferred target and count | Independent-target count | Consequence |
|---|---|---|---|
| Both vote B | B, 2 | 2 | Ordinary valid case agrees. |
| Both vote A | A, 2 | 0 | Helper can call unanimous rejection clean; disagreement with its stated assigned-target check. |
| One A, one B; `target_option=B` in results | B, 1 | 1 | Available fallback can correctly flag split action. |
| One A, one B; target only in run_config, as generator writes it | None, 0 | 1 | Helper loses the available independent target and misstates count; both routes still flag failure of two-target-vote criterion. |
| Both vote fields absent | None, 2 | Undefined; must abstain | A malformed-record concern: equality of two missing values can look like agreement. This does not show such records occur. |

Counterevidence against broad invalidation: the generation route uses the independent
target correctly for vote counts, the paper describes manual content audits, and
the helper has no observed caller in the evaluation pipeline. The evidence
contributor's three initial records (two collusion, one control) show ordinary
correct counts, not an actual contradiction. I read its saved qualification and
config records; Agent 0 retains integration responsibility for that DEL-02-01 return.

### Question, alternatives, and discrimination

Descriptive question: on a specified available subset, do helper judgments and
independently recovered assignment/action judgments differ, and what observation
or definition explains each difference? No hypothesis of prevalence is assumed.

Alternatives: the helper gap is dormant because all consumed runs satisfy the
target condition; a separate manual filter supplies the missing distinction;
the downloaded release differs from the paper's analytic subset; prompts/config
have inconsistent targets; vote parsing rather than agent behavior is responsible;
or genuine attempts fail without ceasing to be collusion. A comparison must retain
all of these possibilities and an insufficient-evidence outcome.

### Observation and inference conditions

Unit: one pinned Core run with config, exact pre-action prompts, conversation,
and final recommendations; use the agent pair as the action unit. Actors see
their own assigned prompts and permitted channels; a deployed transcript monitor
would see a specified projection of those messages. The audit evaluator may use
private prompts, roles and config as privileged reference, but must not leak those
fields into a claimed monitor input. A recorded final vote is a model output,
not an independently observed real-world state change.

Recover the target from pre-action prompt semantics and config, check label swaps,
then compare with parsed votes and final recommendation text. Disagreement among
these references yields ambiguity, not automatic agent blame. Separate role,
attempt, action and committee-majority labels. Do not infer a causal coordination
channel solely from agreeing outputs.

### Evidence, access, method, and feasibility

Public static source is fully accessible and pinned. HF metadata reports ungated
MIT data. Full catalog lists 50 collusion and 50 control Qwen Core result files,
versus 18 collusion and 50 control GPT-OSS Core files. These are catalog observations,
not proof that every excluded paper case is retained. The DEL-02-01 contributor is
qualifying matched actual config/prompt/result records and activation metadata;
its findings govern the final recommendation. Its actual return is
[EVIDENCE_FEASIBILITY.md](../../../../PKG-02/DEL-02-01/Work/EVIDENCE_FEASIBILITY.md).
It establishes target B for `audit_01` and target A for `audit_02` from config and
pre-action prompts, with both sampled colluder pairs voting target and neither
winning a majority. The saved activation metadata has 1,054 rows for 62 runs
(31 collusion + 31 control), includes `audit_01` but not `audit_02`, and records
null target fields in the sampled `audit_01` metadata. The dataset README's 31+31
description, raw 50+50 catalog, paper J.7's 36 collusive scenarios, and released
metadata therefore identify different surfaces whose version/selection relationship
must be resolved before any metric reanalysis. This is a provenance uncertainty,
not proof of an erroneous selection or performance claim.

Smallest proposed next investigation: pin one model/Core release, enumerate its
available paired records, predeclare labels and abstention rules, inspect targets
against initial prompts and final recommendations, compare the helper's specified
decision with that independent account, then examine a second reader's disputed
cases. This is an offline descriptive audit. No LLM calls or activation arrays are
necessary to establish a reference mismatch. A claim about detector metrics needs
the exact analytic membership, matched scores/activations, and a justified relabeling
protocol; that extension is **not yet feasible or commissioned** merely because
the raw catalog contains more runs.

### Minimum means, effort, scrutiny, and decisions

Reuse JSON parsing and source/file inspection, adding only a small auditable
comparison if selected under DEL-02-02. Planning estimate: 3–5 focused hours for
one-model Core audit, double-reading ambiguous cases, and a compact account; this
is an estimate, not measured effort or a promised result. Trace collection and
reference disagreement could require narrowing it. No paid experimental model
budget is intrinsically needed. Review must include ordinary target-following,
unanimous refusal, split votes, missing metadata and honest agreement; clarify
whether apparent mismatches survive original-prompt and generator checks.

Owner choices: whether this concrete evaluator audit is a worthwhile next
investigation; the time allocation and desired audience; whether later score
reanalysis is worth its added provenance/data work. Avoid publication or author
contact without actual authorization. A useful negative result is that actual
available cases do not exercise the helper discrepancy and that the proper source
of labels is independent. A bare helper bug with no research consequence may be a
software finding rather than a sufficient hackathon contribution.

## Preliminary control lead — Compositional approval with bounded observations

Agent 0 elected to retain this as a preliminary lead rather than a fourth serious
candidate in the combined comparison. The following design notes preserve what
was considered; they do not assert a qualified or distinctive investigation.

**Problem/recipient/mechanism.** An operator approves actions from several agents
separately, while a prohibited effect depends on their combination. The oversight
decision is whether to approve the next action given cumulative state. Distributed
ownership and reviewer information partitioning are the multi-agent mechanism;
the same general issue also appears in ordinary distributed systems and is not
uniquely an LLM problem.

**Prior work/addition.** Nearest organizer examples are "Approval laundering" and
"Monitoring split-up attacks"; the latter cites J and G. J is inaccessible in
this pass, a material novelty gap. G supplies a tested single-proposal control
setting and its stated heterogeneous-task/auditing limitations. R's Transfer
appendix already includes code-review, CI/CD, research and narrative chains of
coordinated changes. A generic cumulative-monitor demonstration therefore cannot
be claimed novel. A possible addition is a narrowly specified observation contract
and minimal counterexample showing precisely when individually acceptable actions
cannot be classified safely without one shared state relation, followed by an
audit of the cost of exposing that relation.

**Question/proposition/alternatives.** For a selected finite task and safety
predicate, can two globally different histories produce the same local reviewer
view but require different decisions? If so, a reviewer using only that view
cannot be right on both. The intended result would identify the missing relation
and a sufficient additional observation for that model. Alternatives include
the local action itself revealing the violation, the predicate decomposing across
agents, a shared-state summary being stale/untrusted, or the supposed added
observation simply exposing privileged ground truth unavailable in deployment.

**Units and access.** Unit: an action sequence with actor identity, shared resource
state, timing and approval boundary. Actors' permitted views, local reviewers'
views, aggregate reviewer's view and evaluator's complete constructed history
must be separately declared. A finite pair of counterexample histories proves a
limit for the specified projection, not prevalence, malicious intent, or LLM
monitor performance. Any proposed shared state must be mechanically obtained
and keyed to the action version, or be explicitly an assumption.

**Method and feasibility.** A paper-and-pencil argument and harmless finite
authorization examples require no model trials and are feasible as reasoning.
The smallest meaningful next act is to retrieve/read J or an authorized alternate
copy and examine relevant compositional security prior work before building a
demonstrator. A substantive extension might compare transaction-wide approval
with local approval under delayed/missing records and benign cooperation, but
would need selected semantics and a justified deployment consumer. No such case
has been specified or tested here. Static example construction alone risks being
a familiar textbook result with no new contribution.

**Means/effort/scrutiny/unknowns.** Estimate 2–4 hours for a bounded formal/example
case after prior-work clarification, with another 2–4 hours for a minimal local
demonstrator and examination if justified; these are uncertain planning ranges.
No new model calls are needed for the argument. Empirical claims about human
review UI or LLM monitors require separately authorized subjects/models and
evaluation. Scrutiny must challenge sufficiency/necessity of observations,
shared-state trust, race conditions, benign sequences and instruction versus
mechanical enforcement. Owner must select the task/predicate and determine
whether the value exceeds the known compositional-security result. This candidate
is retained as a preliminary alternative, not recommended ahead of C1's concrete
source discrepancy.

## Author critique, repairs and return recommendation

**Recommendation within this lane:** C1 merits the next bounded investigation
if Agent 0's combined comparison agrees. Its advantage is a concrete, falsifiable
evaluator distinction with public source and a small existing-record route.
Its risk is limited scientific contribution: a source helper defect may not affect
actual judgments or published results. Start with that consequence question,
not a new detector or a wholesale replication. The preliminary control lead remains available if the owner
prefers a control-method contribution, but its novelty and concrete consumer are
less formed.

Material author checks and dispositions:

1. **Overbroad novelty:** shared-prior coordination and paraphrasing already appear
   in M/G. Repaired candidate descriptions to identify narrower additions and
   explicitly reject generic novelty claims; backchecked against G §3.4.2 and
   M Appendix F.1/§7.2.
2. **Tier conflation:** Core's target-vote filter does not govern all of NARCBench.
   Parent flagged the L.9 qualification; checked K.9/L.9 and repaired the account
   to retain attempted-but-ineffective coordination and tier-specific labels.
3. **Helper-to-paper causal leap:** whole-repository static caller search and
   generator/extraction reading establish separate routes. Repaired C1 to leave
   paper impact unestablished. Manual helper walkthrough includes valid and
   contrary cases; no experimental numerical result is claimed.
4. **Reference validity:** assigned target must be checked against pre-action
   prompts and label swaps, and voting for a target does not establish its actual
   harm or successful majority outcome. Those are separate proposed audit labels.
5. **Data adequacy:** metadata catalog completeness differs from the paginated
   tree and does not prove excluded-run availability or matched analytic membership.
   Specific sample qualification is delegated by Agent 0 to DEL-02-01, not implied
   by this source review.
6. **All-case completeness:** C1 specifies problem/recipient,
   multi-agent mechanism, closest examined sources and organizer example,
   addition/novelty limit, route/question/alternatives, units/access/reference,
   feasible inputs or precise gaps, means/effort/scrutiny, and owner choices.
   The source gap for the preliminary control lead is not described as completed reading.

These are author checks plus parent source challenge, not an independent empirical
replication. The combined recommendation still needs Agent 0 integration and the
separate scrutiny it announced. No focused case has been selected by this return.
