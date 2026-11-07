# Corrective reading: risk mechanisms and cooperative opportunities

Agent 0's source-first examination for the owner-selected corrective pass.
Read actual retrieved PDFs and `pdftotext -layout` views; no experiment, tool/model
trial, new dataset acquisition or cited-study replication was performed.
Acquisition UTC, HTTP, byte identities and URLs are in
`primary-sources/{risks.pdf,cooperative-open.pdf}.capture.json`. Unversioned arXiv
PDFs identify themselves as **2502.14143v1** and **2012.08630v1** respectively;
API metadata is retained separately. The source dates and present evaluation
context must not be conflated. Copies are retained for local research review.

## Actual reading coverage

- **Hammond et al., Multi-Agent Risks from Advanced AI**, Cooperative AI Foundation
  Technical Report1, February2025, arXiv2502.14143v1: abstract/executive summary,
  all main sections §§1–5 (printed pp.5–49), risk definitions, all risk-factor and
  implication sections, illustrative case descriptions, and AppendixB.1–B.3
  experimental details (pp.51–52). Bibliography consulted for identity/context,
  not every cited source independently read. AppendixA attribution/acknowledgment
  is not an additional empirical source. Main-text blocks initially truncated by
  terminal output were reread in smaller page blocks, including pp.14–15,45–46
  and the conclusion. Embedded quantitative case claims were not independently
  reproduced or treated as present-model performance.
- **Dafoe et al., Open Problems in Cooperative AI**, December2020,
  arXiv2012.08630v1: abstract, complete main text §§1–6 (pp.3–33), game tables and
  their explanations, substantive footnotes, and workshop AppendixA (p.34).
  Bibliography is a source list, not a completed bibliography-wide reading.
  No independent equilibrium proof or empirical validation of its aspirational
  hypothesis is claimed. Printed manuscript date is December17; arXiv version
  header December15; preserve both rather than infer a later source version.

## Source arguments before candidate selection

### Hammond: behavior only becomes a failure relative to a system purpose

The taxonomy first asks whether cooperation is desirable, then what preferences
agents have (§2, p.10). Miscoordination concerns agents with identical outcome
preferences failing to achieve the shared objective; the same verbal goal does
not establish identical preferences. Conflict concerns mixed-motive inefficiency;
collusion concerns unwanted cooperation (§§2.1–2.3). The categories are stipulated
analytical definitions and not an intent detector. Agents may also fail through
incompetence or vulnerabilities independently of strategic objectives.

In §2.3 (pp.17–20), unwanted cooperation can arise among agents with complementary
interests at another party's expense. Explicit communication is not necessary;
common causes can correlate decisions. Conversely correlated outputs are not
sufficient evidence of a coordinated strategy. The report connects collusion to
adversarial safety schemes (§4.1, p.43): worker/overseer arrangements may fail
when the expected independence of their objectives or assessments is undermined.
This is a direct Track4 rationale for studying oversight relations, but says
nothing about whether our particular raw-log requirement protects a real interest.

The seven risk factors (§3) are neither exhaustive nor mutually exclusive.
Information asymmetry, network effects, selection pressures, adaptive dynamics,
commitment/trust, collective agency and security can interact. An information
problem and a commitment problem require different interventions. A new evidence
channel may help one without addressing incentives in the other. §3.1.3 already
proposes both centrally designed information revelation and voluntary verified
private-information disclosure. These are antecedents for candidate E, not ideas
newly supplied by our thesis reading.

Network effects (§3.2, pp.23–26) include errors and goal distortions through
handoffs, rewiring and homogeneous-model failures. A dependency graph can omit
important relationships; a successful isolated component can contribute to a
harmful network. The proposed response includes whole-network observation,
credible simulations and protection of critical nodes. It does not license
extrapolating a two-peer study to population-scale safety.

§§3.3–3.4 separate selection over agents/strategies from adaptation within an
interaction, and equilibria from transient/unstable dynamics. Evaluation needs
varied co-players and explicit histories; a same-model fixed pair need not transfer
to heterogeneous independently deployed agents. Statements that all contemporary
evaluation ignores multi-agent risks are dated report framing, not a claim of
November2026 coverage after later work.

Commitment (§3.5, pp.33–36) means binding future conduct so reneging is impossible
or costly; it is not equivalent to a stated promise or the Chirality sense of a
person standing behind a judgment. Credible commitments can support trust but also
threats, lock-in and dangerous rigidity. Human inclusion alone does not guarantee
control (p.35 footnote46). Privacy-preserving observation, renegotiation and limits
on commitment power are therefore substantive design issues, not peripheral ethics.

The report's emergence section (§3.6) explicitly distinguishes genuinely new
collective capability/goal from mere accumulation and acknowledges speculative
standing. Its security section (§3.7) distinguishes attacks by groups from agents
as vulnerable extensions of their principals. The useful reference is an actual
harmful capability, action or outcome under a threat model; anomalous communication
or a role label does not establish it.

Governance/ethics (§4) extends the subject beyond one operator: responsibility,
liability, interoperable infrastructure, privacy, fairness, who has access to
stronger agents, and harm to people outside the acting coalition. The report itself
largely omits benefits and says so; Dafoe is a useful corrective rather than a
second endorsement of suppressing cooperation.

### What the report's experiments establish, and do not

AppendixB describes simple, illustrative settings: forty discrete simulated driving
scenes; repeated article rewriting with generated questions and model grading;
and a model fine-tuned on attack-related synthetic documents before a sentiment
scorer experiment. “Unprompted” in the latter concerns the task-time instruction,
not absence of relevant fine-tuning exposure. Its attempt/success predicates and
parser limitation are explicit. These examples justify taking interaction risks
seriously, not direct prevalence estimates, uniform model incapacity or validation
of the report's whole taxonomy. We did not execute their code or independently
adjudicate the news/driving/scorer references.

### Dafoe: whose cooperation and which social objective?

§3.3 (pp.12–13) distinguishes the individual perspective from the planner
perspective. §3.4 separates vertical principal-agent alignment/control from
horizontal relationships among multiple principals whose preferences matter.
Neither perspective replaces the other: a planner must understand participants'
incentives, while participants may reason about institutions. An overseer trusted
by one operator is not automatically a legitimate authority for another principal.

§4's four capability families—understanding, communication, commitment and
institutions—organize different obstacles. The simple games show why better
information can help an assurance problem but cannot alone solve a complete-
information Prisoner's Dilemma. Institutions can alter the action/payoff structure;
that intervention must not be reported as merely revealing existing evidence.

§4.2 makes common ground and grounding material. A successful transmission need
not yield the same interpretation or usable action. Compression can be useful
and context-sensitive; requiring all raw information is not a generally established
optimal control. Bandwidth and latency are different limitations. Mixed-motive
communication raises incentives to misrepresent and tradeoffs in private information
revelation. Structured transparency seeks narrowly useful disclosure without
requiring all private data to be made public (§4.2.4).

§4.3 distinguishes unilateral/multilateral, conditional/unconditional commitments;
§4.4 distinguishes centralized and decentralized institutions. Reputation, mediators,
automated contracts and trusted hardware are established means, each with
conditions. A tool labeled trusted does not create those conditions. The account
also identifies design tradeoffs among outcomes, interpretability and legitimacy
(§4.4.4).

§5 (pp.30–33) is central to interpreting “safer cooperation.” Improving a coalition's
welfare can harm excluded parties or undermine socially useful competition.
Cooperative and coercive capabilities overlap, and coercion can even support some
legitimate arrangements. The “Broad Cooperative Competence is Beneficial” claim is
explicitly a hypothesis with theoretical/historical arguments and qualifications,
not an empirical guarantee or a reason to declare every cooperation channel good.
No scalar sum of our agents' rewards automatically measures the intended social
benefit. Privacy, distribution and legitimate limits may constrain the comparison.

## Consequences for this project's actual choices

1. **Withdraw a generic anti-agreement objective.** Agreement, shared reward and
   communication are not failure labels. The operator/principal, intended
   cooperation, protected reliance and affected nonparticipants must be specified
   before interpreting a detector's success. Benign cooperation is a necessary
   comparator, not incidental padding.
2. **Demote E's current recommendation until its reliance purpose is grounded.**
   E currently measures evidence-policy compliance in a deliberately restrictive
   benchmark. Correct task answers accepted without raw logs establish protocol
   violation, not yet a consequential harmful coalition. A recovery intervention
   could improve legitimate cooperation, enable inappropriate disclosure or leave
   incentives unchanged. These interpretations must be separated. Shared versus
   separate rewards are meaningful experimental factors, not “bad” and “safe” labels.
3. **Retain the useful E question as conditional.** Under a justified reliance rule,
   explicit data-access authority and a credible consequence model, evidence
   availability × incentive design can be a coherent bounded control question.
   It remains one part of information/commitment/institution design, not a whole
   solution to swarm alignment. The observed metadata-channel limitation remains
   an instrument finding with its original scope.
4. **Qualify D's notion of repair.** A supervisor can restore its own current
   predicate while destroying another principal's legitimate historical use or
   overriding a reserved decision. Its finite fixture already preserves historical
   meaning, but a general recovery claim needs ownership, authorization and
   actual consumer consequences. Graph/receipt correctness is not human recourse.
5. **Retain A/B/C without upgrading them.** A can qualify a benchmark reference;
   B can delimit actual observation; C can prevent unwarranted blame. They are
   supporting questions unless connected to a substantive oversight use. None is
   made novel by the taxonomy, and operator agreement does not validate their
   reference or choose who should bear a cost.
6. **Reopen framing, not accepted commitments.** PRD already requires a multi-agent
   mechanism, intended use, competing explanations, observer examination, burden
   and legitimate cooperation. These sources expose insufficient application of
   those standards in the candidate choice, not a necessary new package or a
   wholesale project change. Case-level corrections belong in the research basis.

The thesis contributes disciplined inquiry into purpose, meaning, evidence, action
and responsibility. These organizer foundations add strategic relations, coalition
boundaries, institutions and the possibility that useful coordination is precisely
what is dangerous to someone else. Neither vocabulary should suppress the other.
A result must be understandable without adopting either as a guarantee.

## Examination and limits

Author fidelity checks compared the distinctions above with the cited source
sections, including contrary qualifications and scope statements. Main bodies
were read rather than inferred from search summaries. The theoretical/historical
arguments and illustrative experiments are reported at their original evidential
standing, not independently verified. Their conclusions do not establish our
proposed interventions' effectiveness or novelty. A separate examiner will assess
the integrated source coverage and changed candidate choice against the original
organizer list. No source list or number of readings supplies that judgment itself.

## Focused source-to-case backcheck: E's actual rewards

The foundational distinction between incentives and welfare prompted rereading
Emergent Collusion's actual §2 and §4.2 source, retained in the prior pass. This is
source interpretation, not a new dataset analysis or model experiment.

Let `v(A→B)` be A's verdict on B and `y(B)` the reference correctness of B's task.
The shared reward is `w × (1[v(A→B)=y(B)] + 1[v(B→A)=y(A)])`, assigned to both
agents. It rewards directional accuracy against the benchmark reference, **not
agreement or ACCEPT itself**. Because the tasks are often reference-correct and
the evidence policy is restrictive, accuracy rewards can conflict with compliant
rejection. That is the source's intentionally constructed pressure; the system
instruction still puts protocol compliance ahead of reward.

The paper's “separate reward” assigns A `w × 1[v(B→A)=y(A)]` and B
`w × 1[v(A→B)=y(B)]`: each is paid for the peer's correct judgment of its own
work. It is **not** an independent verifier rewarded only for its own correct
judgment. The paper separately tests acceptance-only rewards and reports that,
for one tested model/configuration with verdict review disabled in both compared
conditions, collusion falls to zero under that reward, despite its directly
rewarding the violating verdict. The authors suggest rationalization as an
explanation. The numerical observation is their result, not reproduced here;
the proposed explanation is not causally established by the rationale alone.

Consequences for our proposal:

- Withdraw any shorthand that treats shared reward as payment for agreement or
  separated reward as a truthful/independent-verifier control.
- The previously proposed recovery×reward-sharing interaction is mathematically
  specifiable but its actual intervention depends on which of these reward
  functions is chosen. It does not automatically identify the role of aligned
  incentives, trust provenance, harmful collusion or principal welfare.
- A proposed reward for the verifier's own accuracy would be a **new condition**,
  not a reproduction of the source's “separate” arm. Its authority, truth source,
  cost accounting and strategic effects require explicit design.
- No harmful downstream release or affected outsider is recorded in these
  selected peer-verification examples. The existing evidence supports stipulated
  protocol violation and reference-graded task outcomes; welfare/reliance claims
  need a separately justified case. Do not invent an injured principal to upgrade
  an observable procedural mismatch into an established harm.

This backcheck supplies a concrete reason to withdraw E's present priority, rather
than merely append generic philosophical cautions. It preserves the paper's
legitimate narrower question about instruction violation and peer influence.
