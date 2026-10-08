# Corpus Generation Progress Log

This log tracks assignments, drafts, reviews, integration gates, and commits for the Northstar Urgent Care Cooperative corpus. The primary-agent coordinates the work and does not author source documents.

## Status key

- `planned`: identified in the corpus workflow, not yet assigned.
- `in progress`: assigned and drafting or review is underway.
- `blocked`: waiting on an explicit prerequisite or decision.
- `complete`: accepted at the current workflow gate.

## Current snapshot

- Corpus plan: `corpus/corpus.yml` defines 20 documents and the staged workflow.
- Fictional staff registry: `corpus/staff.yml` defines eight author profiles.
- Current stage: First-document-per-staff checkpoint complete; remaining corpus documents proceed by dependency.
- Stage 1 assignments: NU-OPS-001, NU-OPS-007, NU-OPS-010 (complete).
- Stage 1 gate: passed after coordinator reconciliation and independent continuity/quality review.
- Stage 1 drafts NU-OPS-001, NU-OPS-007, and NU-OPS-010 are accepted at the foundation gate. The fictional corpus snapshot is 2024-10-01. Independent continuity and quality/style reviews found no remaining high- or medium-severity blockers.
- First-document checkpoint: all eight staff authors have at least one draft (NU-OPS-001, 002, 003, 005, 007, 010, 011, 018). Independent continuity and quality reviews found no high/medium blocker for this checkpoint. These remain draft artifacts; proposed facts require later corpus approval and ledger integration.
- Last commit: `bcafe96` — Add Stage 1 fictional clinic foundation drafts.

## Assignment and document status

| Document | Intended author | Status | Stage / dependency | Draft / review notes |
| --- | --- | --- | --- | --- |
| NU-OPS-001 | EMP-001 Mara Venn | complete | Stage 1 foundation | Draft accepted at foundation gate; 2024-01-15 effective, annual review, Director/site-lead approval boundaries |
| NU-OPS-002 | EMP-003 Tessa Quill | in progress | Stage 2; Stage 1 gate passed | First draft for Tessa; independent review clear; proposed handoff rules and dates await corpus integration |
| NU-OPS-003 | EMP-002 Ilan Rook | in progress | Stage 2; Stage 1 gate passed | First draft for Ilan; independent review clear; proposed priorities/closure and dates await corpus integration |
| NU-OPS-004 | EMP-003 Tessa Quill | blocked | Stage 3; depends on NU-OPS-002 | Harbor Point-only access exception |
| NU-OPS-005 | EMP-004 Ren Solis | in progress | Stage 2; Stage 1 gate passed | First draft for Ren; independent review clear; proposal reconciled with historical NU-OPS-017 draft |
| NU-OPS-006 | EMP-001 Mara Venn | blocked | Stage 2; Stage 1 gate | Service interruption response |
| NU-OPS-007 | EMP-007 Oren Pike | complete | Stage 1 foundation | Draft accepted at foundation gate; fictional role routes, no-response-SLA limit, Alder Creek role-only mailbox |
| NU-OPS-008 | EMP-002 Ilan Rook | in progress | Stage 2; Stage 1 gate passed | Draft reviewed; Director of Operations is required approver; conditional base for NU-OPS-018 |
| NU-OPS-009 | EMP-005 Dev Arlen | blocked | Stage 2; Stage 1 gate | Records handling and misdelivery |
| NU-OPS-010 | EMP-005 Dev Arlen | complete | Stage 1 foundation | Draft accepted at foundation gate; exact scope mapping by employee ID; effective before NU-OPS-001 |
| NU-OPS-011 | EMP-006 Niko Fen | in progress | Stage 2; Stage 1 gate passed | First draft for Niko; independent review clear; administrative reporting rules await corpus integration |
| NU-OPS-012 | EMP-003 Tessa Quill | blocked | Stage 4; core documents stable | September quality huddle notes |
| NU-OPS-013 | EMP-006 Niko Fen | blocked | Stage 2; Stage 1 gate | Severe-weather coordination card |
| NU-OPS-014 | EMP-002 Ilan Rook | blocked | Stage 2; Stage 1 gate | Vendor visit and sign-in |
| NU-OPS-015 | EMP-001 Mara Venn | blocked | Stage 3; depends on NU-OPS-001 | Limited document-governance amendment |
| NU-OPS-016 | EMP-002 Ilan Rook | blocked | Stage 2; Stage 1 gate | Historical facilities routing, superseded by NU-OPS-003 |
| NU-OPS-017 | EMP-004 Ren Solis | in progress | Stage 2; Stage 1 gate passed | Draft reviewed; historical rule differs intentionally from NU-OPS-005 proposal; conditional status clear |
| NU-OPS-018 | EMP-008 Lio Marr | in progress | Stage 3 draft; NU-OPS-008 is draft-only prerequisite | First draft for Lio; independent re-review clear; location must be designated before use; conditional on both approvals |
| NU-OPS-019 | EMP-006 Niko Fen | blocked | Stage 2; Stage 1 gate | Operations metrics definitions |
| NU-OPS-020 | EMP-007 Oren Pike | blocked | Stage 4; core documents stable | Unresolved service desk questions log |

## Event log

### 2026-10-08 — Workflow kickoff

- Confirmed primary-agent role is coordination, integration, and review management; primary-agent will not author corpus documents.
- Dispatched parallel Stage 1 drafting assignments for NU-OPS-001 (EMP-001), NU-OPS-007 (EMP-007), and NU-OPS-010 (EMP-005). Drafts were returned; authors reported proposed dates and shared role/routing/access facts for reconciliation.
- Set the fictional corpus snapshot to 2024-10-01, matching the planned `24-03` revision bulletin; active documents should have effective dates before and review dates after that snapshot. NU-OPS-007 has been revised accordingly.
- Review found NU-OPS-010 needed the same timeline, draft-status/authorship front matter, and exact alignment of its example scope list to `corpus/corpus.yml`; author revised all requested items.
- Independent continuity and quality/style reviews found initial foundation issues: date ordering, an overly broad NU-OPS-007 audience, an unregistered Alder Creek named-role implication, vague employee eligibility, and unqualified proposed rules. Targeted author revisions resolved these; the Stage 1 gate passed.
- Sent targeted author revisions: NU-OPS-007 audience narrowed to eligible site-operations staff and Alder Creek represented as a role-only fictional route; NU-OPS-010 role eligibility mapped to employee IDs and dates moved before NU-OPS-001. Ratified the proposed governance and routing mechanics as fictional corpus facts for these drafts; authors retain responsibility for revising their own documents.
- Stage 1 gate passed: confirmed NU-OPS-001 effective date follows NU-OPS-010; narrowed NU-OPS-007 audience to `site_operations` eligibility and represented Alder Creek as a role-only mailbox; made NU-OPS-010 employee-ID eligibility explicit with no implicit scope inheritance. Committed the foundation set and progress log as `bcafe96`.
- Approved the foundation routing and governance conventions as fictional corpus facts. Shared roles and routes use reserved `northstar-uc.example.invalid` addresses; no response-time promise, named Alder Creek incumbent, on-call roster, or clinical route is established.
- Independent continuity and quality/style reviewers found no high/medium blockers in the Stage 2 first wave after the authors clarified draft precedence, marked new workflows as proposed, narrowed NU-OPS-011 audience to its access scope, and added a dual-record rule.
- Dispatched NU-OPS-008 (Ilan’s second document) to establish the prerequisite for Lio’s first document, NU-OPS-018. Dispatched NU-OPS-017 (Ren’s second document) to establish the history needed to reconcile NU-OPS-005. The NU-OPS-002 and NU-OPS-008 plan relationships now use `has_exception` to point from each base procedure to its exception notice. Independent review found NU-OPS-017 and NU-OPS-008 coherent as draft proposals; NU-OPS-008 was revised to identify Director of Operations as required approver and make the workflow pending approval. NU-OPS-018 is received as a conditional draft against the unapproved base; independent review found no approval or scope expansion, and requested clarification of its exact eligible audience and proposed holding-location arrangement; author is revising.
- First document coverage: Mara (001), Oren (007), Dev (010), Tessa (002), Ilan (003), Ren (005), and Niko (011) have drafts. Lio’s first document (018) is drafted conditionally against NU-OPS-008; it cannot be approved or activated until both documents pass their gates. Thus every staff profile now has at least one assigned document draft.
