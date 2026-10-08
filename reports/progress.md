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
- Current stage: Stage 2, Core operational documents.
- Stage 1 assignments: NU-OPS-001, NU-OPS-007, NU-OPS-010 (drafting sub-agents dispatched in parallel).
- Stage 1 gate: passed after coordinator reconciliation and independent continuity/quality review.
- Drafts received for NU-OPS-001, NU-OPS-007, and NU-OPS-010; foundation review and reconciliation are in progress. The coordinator set the fictional corpus snapshot to 2024-10-01 to align with planned bulletin 24-03. NU-OPS-007 has been revised to this timeline; NU-OPS-010 has been revised for the same timeline, draft-status/authorship front matter, and plan-aligned scope examples. Independent continuity and quality reviews are complete; targeted corrections are underway before the gate can pass.
- Last commit: `1c1ff34` — Add fictional clinic corpus plan and staff registry.

## Assignment and document status

| Document | Intended author | Status | Stage / dependency | Draft / review notes |
| --- | --- | --- | --- | --- |
| NU-OPS-001 | EMP-001 Mara Venn | complete | Stage 1 foundation | Draft accepted at foundation gate; 2024-01-15 effective, annual review, Director/site-lead approval boundaries |
| NU-OPS-002 | EMP-003 Tessa Quill | blocked | Stage 2; Stage 1 gate | Base opening/closing procedure; needed by NU-OPS-004 |
| NU-OPS-003 | EMP-002 Ilan Rook | blocked | Stage 2; Stage 1 gate | Current facilities routing; paired with historical NU-OPS-016 |
| NU-OPS-004 | EMP-003 Tessa Quill | blocked | Stage 3; depends on NU-OPS-002 | Harbor Point-only access exception |
| NU-OPS-005 | EMP-004 Ren Solis | blocked | Stage 2; Stage 1 gate | Current schedule notice; paired with NU-OPS-017 |
| NU-OPS-006 | EMP-001 Mara Venn | blocked | Stage 2; Stage 1 gate | Service interruption response |
| NU-OPS-007 | EMP-007 Oren Pike | complete | Stage 1 foundation | Draft accepted at foundation gate; fictional role routes, no-response-SLA limit, Alder Creek role-only mailbox |
| NU-OPS-008 | EMP-002 Ilan Rook | blocked | Stage 2; Stage 1 gate | Base supply/receiving procedure; needed by NU-OPS-018 |
| NU-OPS-009 | EMP-005 Dev Arlen | blocked | Stage 2; Stage 1 gate | Records handling and misdelivery |
| NU-OPS-010 | EMP-005 Dev Arlen | complete | Stage 1 foundation | Draft accepted at foundation gate; exact scope mapping by employee ID; effective before NU-OPS-001 |
| NU-OPS-011 | EMP-006 Niko Fen | blocked | Stage 2; Stage 1 gate | Non-clinical workplace incident reporting |
| NU-OPS-012 | EMP-003 Tessa Quill | blocked | Stage 4; core documents stable | September quality huddle notes |
| NU-OPS-013 | EMP-006 Niko Fen | blocked | Stage 2; Stage 1 gate | Severe-weather coordination card |
| NU-OPS-014 | EMP-002 Ilan Rook | blocked | Stage 2; Stage 1 gate | Vendor visit and sign-in |
| NU-OPS-015 | EMP-001 Mara Venn | blocked | Stage 3; depends on NU-OPS-001 | Limited document-governance amendment |
| NU-OPS-016 | EMP-002 Ilan Rook | blocked | Stage 2; Stage 1 gate | Historical facilities routing, superseded by NU-OPS-003 |
| NU-OPS-017 | EMP-004 Ren Solis | blocked | Stage 2; Stage 1 gate | Historical schedule notice, superseded by NU-OPS-005 |
| NU-OPS-018 | EMP-008 Lio Marr | blocked | Stage 3; depends on NU-OPS-008 | Northgate-only receiving exception |
| NU-OPS-019 | EMP-006 Niko Fen | blocked | Stage 2; Stage 1 gate | Operations metrics definitions |
| NU-OPS-020 | EMP-007 Oren Pike | blocked | Stage 4; core documents stable | Unresolved service desk questions log |

## Event log

### 2026-10-08 — Workflow kickoff

- Confirmed primary-agent role is coordination, integration, and review management; primary-agent will not author corpus documents.
- Dispatched parallel Stage 1 drafting assignments for NU-OPS-001 (EMP-001), NU-OPS-007 (EMP-007), and NU-OPS-010 (EMP-005). Drafts were returned; authors reported proposed dates and shared role/routing/access facts for reconciliation.
- Set the fictional corpus snapshot to 2024-10-01, matching the planned `24-03` revision bulletin; active documents should have effective dates before and review dates after that snapshot. NU-OPS-007 has been revised accordingly.
- Review found NU-OPS-010 needed the same timeline, draft-status/authorship front matter, and exact alignment of its example scope list to `corpus/corpus.yml`; author revised all requested items.
- Independent continuity and quality/style reviews found no clinical-scope or fiction-boundary issues, but the foundation gate remains open. Findings included NU-OPS-001 effective before the proposed NU-OPS-010 matrix, an overly broad NU-OPS-007 audience for its scope, an unregistered Alder Creek named-role implication, vague employee eligibility in NU-OPS-010, and proposed routing/governance rules needing explicit coordinator ratification.
- Sent targeted author revisions: NU-OPS-007 audience narrowed to eligible site-operations staff and Alder Creek represented as a role-only fictional route; NU-OPS-010 role eligibility mapped to employee IDs and dates moved before NU-OPS-001. Ratified the proposed governance and routing mechanics as fictional corpus facts for these drafts; authors retain responsibility for revising their own documents.
- Stage 1 gate passed: confirmed NU-OPS-001 effective date follows NU-OPS-010; narrowed NU-OPS-007 audience to `site_operations` eligibility and represented Alder Creek as a role-only mailbox; made NU-OPS-010 employee-ID eligibility explicit with no implicit scope inheritance.
- Approved the foundation routing and governance conventions as fictional corpus facts. Shared roles and routes use reserved `northstar-uc.example.invalid` addresses; no response-time promise, named Alder Creek incumbent, on-call roster, or clinical route is established.
- Independent reviewers confirmed no remaining high/medium continuity, clarity, or scope-boundary blockers. Stage 2 first assignments are NU-OPS-002 (Tessa), NU-OPS-003 (Ilan), NU-OPS-005 (Ren); NU-OPS-011 (Niko) will start as a concurrency slot opens. NU-OPS-018 (Lio) remains dependent on NU-OPS-008.
