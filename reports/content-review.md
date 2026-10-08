# Full-Corpus Content Review

**Review date:** 2026-10-08

**Scope:** Read-only consistency and RAG-content review of all 21 draft documents, the corpus inventory, staff registry, and cross-document relationships.

**Result:** The initial review found no high-severity factual contradiction. Bounded author revisions and corpus-plan reconciliation are now complete; the corpus remains in draft status and still requires content approval.

## Approval decisions

These items change fictional operating expectations or the status of proposed history, so they need an explicit corpus decision before final approval:

1. **NU-OPS-006 update cadence:** The draft proposes updates every 60 minutes during a service interruption. NU-OPS-013 deliberately uses material-change and shift-handoff triggers for severe weather instead. Confirm whether the 60-minute cadence is accepted for NU-OPS-006.
2. **NU-OPS-019 metric ownership:** Clarify whether site leads produce local counts for central role validation, or central roles produce counts while site leads report local source availability.
3. **Proposed dates and precedence:** The dates are chronologically coherent, including the 2024-09-21 handoffs from NU-OPS-016 to NU-OPS-003 and NU-OPS-017 to NU-OPS-005. Since the documents remain drafts, decide whether approval should establish these as true fictional history or keep them hypothetical proposals.
4. **Unspecified procedures:** NU-OPS-001/015 do not name a repository location, and NU-OPS-008 does not establish purchase authority. Retaining these as deliberate unknowns supports abstention testing; filling them would require new fictional policy.

## Targeted consistency revisions

| Document(s) | Finding | Suggested revision |
| --- | --- | --- |
| NU-OPS-017 | Header says proposed end date 2024-09-21 while body says the period ends immediately before that date. | State that 2024-09-20 is the last effective date and 2024-09-21 is the proposed successor handoff/review date. |
| NU-OPS-018 | The audience is limited to operations-lead-eligible staff, while the procedure says “Northgate receiving staff” may use the steps. | Separate who can retrieve the exception, who may physically receive an item, and who owns/authorizes the exception steps. |
| NU-OPS-020 / NU-OPS-012 | NU-OPS-012 tracks a cross-site handoff-record location/retention follow-up; NU-OPS-020 lists other open questions but not this one. | Add a distinct question with status/owner supported by NU-OPS-012, or explicitly say the huddle tracks it separately. Keep vendor-visit retention separate. |
| `corpus/corpus.yml` / NU-OPS-009, 011, 014 | Inventory audience labels diverge from the source front matter. NU-OPS-014 includes contractors in the inventory audience though its source excludes them from retrieval. | Align inventory audience values to the authored source and access-scope model, or explicitly revise the source through its author. |
| NU-OPS-011 / NU-OPS-009 | NU-OPS-011 body routes sensitive/out-of-scope cases to NU-OPS-009, but its relationship metadata omits that reference. | Add a `references` relationship in the source and inventory. |
| NU-OPS-012 | The notes distinguish service-interruption updates and facilities/workplace incident records, but the relationship list does not name all these sources. | Add precise references to NU-OPS-003, NU-OPS-006, and NU-OPS-011 where relevant. |
| NU-OPS-014 | The visit-log status field mixes arrival expectation with authorization to begin work. | Define the status stage so readers can distinguish an expected/arrived visit from scope clearance. |
| NU-OPS-010 | EMP-005 is eligible for `operations_leads`, but the rationale is not stated in the document. | Clarify that this is an explicit corpus fixture assignment or provide an approved role rationale; do not infer eligibility from title alone. |
| NU-OPS-021 | The directory omits the registry's existing `responsibilities` summaries. | Consider adding short registry-backed role-focus summaries, clearly distinguished from access, coverage, or authorization. |

## Useful content additions

Prefer a few coherent, clearly labeled examples that connect existing record fields and routes. Avoid lengthening normative prose for its own sake.

- NU-OPS-002: blank or illustrative handoff record using fields already present.
- NU-OPS-003: compact issue lifecycle example connecting intake, priority, route, status, and closure without adding a response-time promise.
- NU-OPS-008: blank request/receiving example; leave approver and purchase authority unresolved unless separately approved.
- NU-OPS-014: concise arrival-to-scope-clearance-to-sign-out example after the status field is clarified.
- NU-OPS-021: registry-backed role-focus summaries, if approved.

Any new IDs, dates, and event outcomes should be explicitly marked as fictional examples and cross-referenced consistently. Preserve the missing metric values in NU-OPS-019, the unanswered questions in NU-OPS-020, and the absence of a vendor-visit retention period; these are intentional RAG abstention cases.

## Review method and limits

Three independent read-only reviews covered policy/procedure consistency; dates, history, and exceptions; and roles/access/routing. A fourth reviewed records, handoffs, metrics, and retrieval specificity. Reviewers found no high-severity contradiction, confirmed staff author IDs and access classes match their source registries, and identified the scoped items above. No source content was changed during the initial review pass. The fact ledger now records accepted shared decisions and remaining unresolved claims without replacing Markdown or approving documents by itself.

## Revision pass completed

The original staff profiles applied bounded changes to NU-OPS-002, 003, 008, 010, 011, 012, 014, 017, 018, 019, 020, and 021. The updates add concise blank/fictional examples, clarify visit-record versus work-scope status, distinguish retrieval access from physical receipt and exception ownership, resolve the NU-OPS-017 date label, track the handoff-record question, and make unresolved metric ownership explicit. The corpus inventory now matches all 21 Markdown audience fields and includes the revised NU-OPS-011/012 cross-reference relationships. The final independent read-only integration audit found no blockers; the NU-OPS-021 provenance scope was reconciled in both source and plan.

At the end of the revision pass and before coordinator approval, all documents remained `status: draft`; examples and the candidate metric workflow were then illustrative/proposed. That intermediate render contained 21 PDFs (67 pages). On 2026-10-08, the coordinator approved the corpus and ratified the fictional dates/precedence, NU-OPS-006 cadence, and NU-OPS-019 role allocation. The repository location, purchase authority, record-retention details, Alder Creek backup, and metrics source/platform/results remain intentional unknowns. The final post-approval render contains 21 PDFs (64 pages); its source/PDF SHA-256 hashes match, all 21 relative index links resolve, and changed/representative pages were visually inspected. See `reports/content-approval.md`, `corpus/fact-ledger.yaml`, and `reports/rendering.json` for the final state. No test suite was run.

## Coordinator approval

On 2026-10-08 the primary coordinator approved the 21-document corpus as fictional source material for the 2024-10-01 snapshot. The prior draft review gate is closed. Lifecycle states, approved dates, and approved workflow decisions are recorded in the document front matter/revision records, `corpus/corpus.yml`, `corpus/fact-ledger.yaml`, and `reports/content-approval.md`. Intentional unknowns remain unresolved by design and do not block content approval. See the approval record for the final lifecycle listing and ratified decisions.
