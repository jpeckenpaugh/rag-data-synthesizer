# Corpus Generation Progress Log

This log tracks assignments, drafts, reviews, integration gates, and commits for the Northstar Urgent Care Cooperative corpus. The primary-agent coordinates the work and does not author source documents.

## Status key

- `planned`: identified in the corpus workflow, not yet assigned.
- `in progress`: assigned and drafting or review is underway.
- `blocked`: waiting on an explicit prerequisite or decision.
- `complete`: accepted at the current workflow gate.

## Current snapshot

- Corpus plan: `corpus/corpus.yml` defines 21 documents and the staged workflow.
- Fictional staff registry: `corpus/staff.yml` defines eight author profiles.
- Current stage: all 21 Markdown sources and their PDFs are present. The Python 3.14 render and PDF review phase is complete: 21 PDFs, 64 pages total; representative visual review and document-ID/text extraction checks are complete. Corpus content approval and integration gates remain pending.
- Stage 1 assignments: NU-OPS-001, NU-OPS-007, NU-OPS-010 (complete).
- Stage 1 gate: passed after coordinator reconciliation and independent continuity/quality review.
- Stage 1 drafting and review gate passed. Subsequent full-corpus review identified draft-status/date wording in NU-OPS-007 and NU-OPS-010; authors have corrected those drafts. All source documents remain drafts pending final corpus approval.
- First-document checkpoint: all eight staff authors have at least one draft (NU-OPS-001, 002, 003, 005, 007, 010, 011, 018). Independent continuity and quality reviews found no high/medium blocker for this checkpoint. These remain draft artifacts; proposed facts require later corpus approval and ledger integration.
- Last content checkpoint: `e91f500` — Draft first clinic documents across staff profiles.

## Assignment and document status

| Document | Intended author | Status | Stage / dependency | Draft / review notes |
| --- | --- | --- | --- | --- |
| NU-OPS-001 | EMP-001 Mara Venn | complete | Stage 1 foundation | Draft accepted at foundation gate; 2024-01-15 effective, annual review, Director/site-lead approval boundaries; representative PDF visually inspected |
| NU-OPS-002 | EMP-003 Tessa Quill | in progress | Stage 2; Stage 1 gate passed | First draft for Tessa; independent factual findings resolved; opening/closing flow asset reference is in place; representative PDF visually inspected after layout fixes; content approval remains pending |
| NU-OPS-003 | EMP-002 Ilan Rook | in progress | Stage 2; foundation accepted | Proposed issue/effective dates aligned to 2024-09-21 handoff; updated draft review pending |
| NU-OPS-004 | EMP-003 Tessa Quill | in progress | Stage 3; depends on NU-OPS-002 | Re-review clear; task performer limited to Harbor Point Site Lead; expiration structured; conditional draft |
| NU-OPS-005 | EMP-004 Ren Solis | in progress | Stage 2; Stage 1 gate passed | First draft for Ren; independent review clear; proposal reconciled with historical NU-OPS-017 draft |
| NU-OPS-006 | EMP-001 Mara Venn | in progress | Stage 2; bounded NU-OPS-013 context available | Draft reviewed; audience now exact `site_operations` set; proposed interruption mechanics under review |
| NU-OPS-007 | EMP-007 Oren Pike | in progress | Stage 1 foundation; final status review | Draft dates/routes now explicitly proposed pending Director approval; role routes and Alder Creek role-only mailbox retained |
| NU-OPS-008 | EMP-002 Ilan Rook | in progress | Stage 2; Stage 1 gate passed | Draft reviewed; Director of Operations is required approver; conditional base for NU-OPS-018 |
| NU-OPS-009 | EMP-005 Dev Arlen | in progress | Stage 2; foundation accepted | Draft reviewed with no blocker; administrative records only, patient/clinical records excluded |
| NU-OPS-010 | EMP-005 Dev Arlen | in progress | Stage 1 foundation; final status review | Exact scope mapping retained; dates explicitly labeled proposed fixture dates pending approval; representative PDF visually inspected and extracted text has no coordinator drafting-note leakage |
| NU-OPS-011 | EMP-006 Niko Fen | in progress | Stage 2; Stage 1 gate passed | First draft for Niko; independent review clear; administrative reporting rules await corpus integration |
| NU-OPS-012 | EMP-003 Tessa Quill | in progress | Stage 4; core references drafted | Draft received; independent review underway; no metric totals or unresolved answers invented |
| NU-OPS-013 | EMP-006 Niko Fen | in progress | Stage 2; foundation accepted | Draft reviewed; audience and site-lead ownership match exact scope; bounded context for NU-OPS-006 |
| NU-OPS-014 | EMP-002 Ilan Rook | in progress | Stage 2; foundation accepted | Draft reviewed; audience narrowed to site operations staff/site leads; contractors excluded from retrieval |
| NU-OPS-015 | EMP-001 Mara Venn | in progress | Stage 3; depends on NU-OPS-001 | Draft received; limited amendment pending Director approval; independent review underway |
| NU-OPS-016 | EMP-002 Ilan Rook | in progress | Stage 2; depends on NU-OPS-003 | Draft reviewed; proposed period ends 2024-09-20, NU-OPS-003 begins 2024-09-21 |
| NU-OPS-017 | EMP-004 Ren Solis | in progress | Stage 2; Stage 1 gate passed | Draft reviewed; historical rule differs intentionally from NU-OPS-005 proposal; conditional status clear |
| NU-OPS-018 | EMP-008 Lio Marr | in progress | Stage 3 draft; NU-OPS-008 is draft-only prerequisite | First draft for Lio; independent re-review clear; location must be designated before use; conditional on both approvals |
| NU-OPS-019 | EMP-006 Niko Fen | in progress | Stage 2; NU-OPS-013 complete | Definitions draft received; NU-OPS-012 references it without establishing results or approving definitions |
| NU-OPS-020 | EMP-007 Oren Pike | in progress | Stage 4; depends on NU-OPS-012 and core references | Draft received; both open unknowns supported by cited drafts; plan graph synchronized, full final gate pending |
| NU-OPS-021 | EMP-004 Ren Solis | in progress | Stage 5 review/integration; derived from staff registry and references NU-OPS-007 | Draft received; author references for portraits and registry-count visual are in place; independent factual findings resolved; representative PDF visually inspected after layout fixes; content approval remains pending |

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

- Completed the 12-document Stage 2 core set as drafts. Independent quality review found no high/medium blockers; continuity review gave a conditional pass to continue dependent drafting after audience/approval reconciliation. The plan now matches front-matter audiences for 006, 009, 011, 013, and 014; 011/013 name Director of Operations approval as pending under governance.
- Received Stage 3 drafts NU-OPS-004 (Tessa) and NU-OPS-015 (Mara). Independent review found NU-OPS-015 clear; NU-OPS-004 was revised to limit the task performer to the Harbor Point Site Lead, align its `operations_leads` audience, and add a structured expiration date. Re-review is underway; both remain conditional on their base documents and approvals.
- Received Stage 4 draft NU-OPS-012 (Tessa), using NU-OPS-019 as proposed context and preserving the unresolved service-desk item. Independent review is underway; NU-OPS-020 remains to be drafted.
- Received NU-OPS-020 (Oren), completing the 20-document Markdown set. It records the unresolved Alder Creek Site Lead backup question from NU-OPS-012 and a second deliberate unknown: NU-OPS-014 gives no vendor visit-log retention period. Independent review confirmed both unknowns are supported and no answer, deputy, or retention schedule was invented.
- Full-corpus review checked all 20 authors against `corpus/staff.yml`, scope/audience alignment, exception and historical date boundaries, and unresolved-question evidence. It found no additional factual contradictions. Authors corrected the draft-status/date language in NU-OPS-007 and NU-OPS-010; the coordinator aligned relationships in `corpus/corpus.yml`. A final focused review of plan/document metadata remains pending.
- No Markdown-to-PDF renderer, dependency declaration, or run instructions are present yet. Once source review and plan reconciliation pass, the next phase is to establish a reproducible PDF rendering process, render the 20 files, visually inspect output and text extraction, then build the manifest and evaluation materials.
- Added NU-OPS-021 Staff and Site Directory to the authoritative inventory as the 21st document. It is an all-staff, organization-wide directory derived from `corpus/staff.yml`; it references NU-OPS-007 for role routing without changing that document's `site_operations` scope. NU-OPS-021 is assigned to Stage 5 independent review/integration and has no dependency on operational drafting stages. The collection remains approximately 20 documents. Directory and visual-plan review remain pending.
- Began the visual/PDF reproducibility phase. Eleven assets are generated: the fictional logo, the NU-OPS-002 opening/closing flow, eight staff portraits, and the NU-OPS-021 home-site count graphic. Asset references in NU-OPS-002 and NU-OPS-021 are complete, and independent factual-review findings for those references have been resolved. Root Python 3.14 `.venv` and pinned requirements files are in place; virtual-environment creation succeeded, but dependency installation is blocked by DNS and native Pango is unavailable in the environment. No PDFs have been rendered. Visual inspection, PDF text-extraction review, and the render gate remain pending; no rendering or integration tests are claimed complete.
- Resolved the rendering environment issue and completed the Python 3.14.7 render of all 21 Markdown sources to 21 PDFs (64 pages total). Applied layout fixes before final inspection. Representative PDFs NU-OPS-001, NU-OPS-002, NU-OPS-010, and NU-OPS-021 were visually inspected; document IDs and searchable text were confirmed in the PDF inventory/extraction results. No coordinator drafting-note content leaked into the PDFs; NU-OPS-010 has no removable drafting note, so its report flag is false while its extracted coordinator references are ordinary document content. `reports/rendering.json` records per-source, per-PDF, and per-visual-asset SHA-256 values plus Python, dependency, platform, and Pango provenance. The PDF rendering/review phase is closed; corpus content approval and integration gates remain pending. No tests are claimed complete.
- After PDF render QA, reran `scripts/generate_visuals.py` canonically with `.venv` Python 3.14.7, PyYAML 6.0.3, and Pillow 12.3.0. All 11 generated asset SHA-256 values remained byte-identical to those recorded in `reports/rendering.json`. This confirms asset regeneration reproducibility; it does not change the render gate or imply test completion.
