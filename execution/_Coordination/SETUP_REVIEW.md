# Independent setup verification and repair

The independent TASK verifier examined all five deliverables sequentially through
`scope-of-work MODE=VERIFY`, then inspected their native needs against
`dependency-extract`. The accepted PRD/decomposition were recovered from commit
`3a73e382ac01d80bb3b1ac8790b88faeeecd9ae6` and their hashes compared with the
[owner decision](../../docs/APPROVAL.md). Library revision:
`897e04e963e4e0eb9ba8126adf92faff36dd5d65`.

## Finding F1 and disposition

The verifier found one narrow coverage gap in
[DEL-01-01's contract](../PKG-01/DEL-01-01/ScopeOfWork.md): its case-definition
criterion applies to every serious candidate, but its sole linked method examined
only a representative candidate. The accepted decomposition requires the fields
for each serious case.

**Accepted and repaired by the integration owner.** The linked method now first
inspects every serious case brief against the criterion's fields and conditions,
then retains the representative evidence/alternative walkthrough for deeper
scrutiny. The output, criterion and accepted scope were unchanged. The parent
backchecked that the method covers the universal completeness condition and
regenerated/checked the affected deterministic checklist and scope/boundary checks.
The independent verifier did not re-read the repaired bytes; its return states
that this repair and backcheck satisfy its only remaining condition.

## Performed checks and actual limits

The verifier reported:

- Five valid SOW_V1 contracts and five passing boundary-owner checks, with semantic
  inspection of the act-to-owner allocation.
- Twenty-one exact acceptance-checklist entries with source text, order, contract
  hash and matrix links preserved; repeat derivation was byte-identical.
- A successful native check and all five neighborhoods. The shared cycle is
  conditional/preliminary/rework feedback, not a blanket finish-to-start gate.
- Six explicit unknown supplier bindings for unselected primary sources,
  environment/oracle/examiner routes. Native suppliers resolve. External and
  unknown inputs are not declared satisfied.
- Work/ homes with only Git folder markers, no lifecycle/status files, and a
  malformed temporary contract rejected without a checklist.

The parent performed the current-route preparation/authored checks, scope
validation, deterministic checklist/idempotence checks, boundary-owner checks,
source recovery checks and native check/neighborhood inspection. Temporary
mechanical reports are in `/tmp/apart-setup-verification/`; independent temporary
checks are in `/tmp/apart-independent-verify/`. They are reproducible diagnostic
outputs, not owning scope or dependency declarations.

This is independent source/contract scrutiny plus the stated parent repair
backcheck. It is not scientific evidence, research-result acceptance, input
suitability, or research activation. No formation clock, data research, trial,
manuscript production or external action was performed. The owner's research
hold remains in force.
