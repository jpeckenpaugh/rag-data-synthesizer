# Corpus Generation Progress Log

This log tracks assignments, drafts, reviews, integration gates, and commits for the Northstar Urgent Care Cooperative corpus. The primary-agent coordinates the work and does not author source documents.

## Status key

- `planned`: identified in the corpus workflow, not yet assigned.
- `in progress`: assigned and drafting or review is underway.
- `blocked`: waiting on an explicit prerequisite or decision.
- `complete`: accepted at the current workflow gate.

## Current snapshot

- Corpus plan: `corpus/corpus.yml` defines the approved 21-document corpus and its 2024-10-01 fictional snapshot; `corpus/staff.yml` defines eight fictional author profiles.
- Current gate: content is approved. All 21 Markdown sources have document-level approval records; 004 and 018 are approved/scheduled, 016 and 017 are superseded, and the rest are current.
- Final Python 3.14 render produced 21 PDFs (64 pages) and refreshed `corpus/documents/README.md` plus `reports/rendering.json`. Final source/PDF hashes match, all 21 index links resolve, searchable text contains no stale draft banner or literal HTML line break, and representative pages were visually inspected.
- Four independent read-only reviews and the bounded author revision/approval passes are complete. No high-severity contradictions were found. Deliberate unanswered questions are recorded in `corpus/fact-ledger.yaml` and `reports/content-approval.md`.
- The primary-agent coordinates, integrates, and approves corpus content; staff-author subagents draft and maintain the source documents.

## Assignment and document status

| Document | Intended author | Workflow status | Lifecycle at 2024-10-01 |
| --- | --- | --- | --- |
| NU-OPS-001 | EMP-001 Mara Venn | complete | current |
| NU-OPS-002 | EMP-003 Tessa Quill | complete | current |
| NU-OPS-003 | EMP-002 Ilan Rook | complete | current |
| NU-OPS-004 | EMP-003 Tessa Quill | complete | scheduled |
| NU-OPS-005 | EMP-004 Ren Solis | complete | current |
| NU-OPS-006 | EMP-001 Mara Venn | complete | current |
| NU-OPS-007 | EMP-007 Oren Pike | complete | current |
| NU-OPS-008 | EMP-002 Ilan Rook | complete | current |
| NU-OPS-009 | EMP-005 Dev Arlen | complete | current |
| NU-OPS-010 | EMP-005 Dev Arlen | complete | current |
| NU-OPS-011 | EMP-006 Niko Fen | complete | current |
| NU-OPS-012 | EMP-003 Tessa Quill | complete | current |
| NU-OPS-013 | EMP-006 Niko Fen | complete | current |
| NU-OPS-014 | EMP-002 Ilan Rook | complete | current |
| NU-OPS-015 | EMP-001 Mara Venn | complete | current |
| NU-OPS-016 | EMP-002 Ilan Rook | complete | superseded |
| NU-OPS-017 | EMP-004 Ren Solis | complete | superseded |
| NU-OPS-018 | EMP-008 Lio Marr | complete | scheduled |
| NU-OPS-019 | EMP-006 Niko Fen | complete | current |
| NU-OPS-020 | EMP-007 Oren Pike | complete | current |
| NU-OPS-021 | EMP-004 Ren Solis | complete | current |

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
- Resolved the rendering environment issue and completed the Python 3.14.7 render of all 21 Markdown sources to 21 PDFs (64 pages total). Applied layout fixes before final inspection. Representative PDFs NU-OPS-001, NU-OPS-002, NU-OPS-010, and NU-OPS-021 were visually inspected; document IDs and searchable text were confirmed in the PDF inventory/extraction results. No coordinator drafting-note content leaked into the PDFs; NU-OPS-010 has no removable drafting note, so its report flag is false while its extracted coordinator references are ordinary document content. `reports/rendering.json` records per-source, per-PDF, and per-visual-asset SHA-256 values plus Python, dependency, platform, and Pango provenance. The PDF rendering/review phase is closed; corpus content approval and integration gates were pending at that earlier checkpoint. No tests are claimed complete.
- After PDF render QA, reran `scripts/generate_visuals.py` canonically with `.venv` Python 3.14.7, PyYAML 6.0.3, and Pillow 12.3.0. All 11 generated asset SHA-256 values remained byte-identical to those recorded in `reports/rendering.json`. This confirms asset regeneration reproducibility; it does not change the content approval gate or imply test completion.
- 2026-10-08: Dispatched four independent read-only reviewers for policy/procedure consistency, chronology/exceptions, roles/access/routing, and records/RAG detail. No high-severity contradiction was found. Consolidated targeted fixes and bounded enrichment opportunities in `reports/content-review.md`; source documents were not edited. Content approval remains pending decisions on the proposed 60-minute interruption update cadence, metric ownership, ratification of proposed history, and whether currently unspecified policy areas stay open. The planned `corpus/fact-ledger.yaml` is absent and should be restored or created before final integration.
- 2026-10-08: Completed a bounded author revision pass across NU-OPS-002/003/008/010/011/012/014/017/018/019/020/021 and reconciled all 21 audience strings plus selected relationships in `corpus/corpus.yml`. Added a blank handoff template, a clearly fictional facilities issue lifecycle, a blank supply request/receipt example, role-focus summaries based on the staff registry, and retrieval/scope/date clarifications. Kept all documents in draft status, policy unknowns unresolved, and the NU-OPS-019 role allocation explicitly candidate-only. Final integration audit found no blockers; the NU-OPS-021 provenance scope now includes responsibilities in both source and plan. Created `corpus/fact-ledger.yaml` to track eight approval-relevant proposed/unresolved claims without resolving them. Regenerated 21 PDFs (67 pages) and the document index; source/PDF hashes and all 21 links were verified, and changed-content pages were visually reviewed. No tests run.

### 2026-10-08 — Corpus content approval and finalization

- Approved the 21-document fictional corpus as source material for RAG ingestion against the 2024-10-01 snapshot, exercising the primary coordinator's explicit discretion to approve. Three staff-author subagents finalized approval metadata and reader-facing lifecycle language in their assigned ranges; the primary coordinator reconciled the machine-readable inventory and fact ledger.
- Lifecycle states: current NU-OPS-001–003, 005–015, 019–021; approved/scheduled NU-OPS-004 and NU-OPS-018; superseded NU-OPS-016 and NU-OPS-017. The two current working records remain explicitly incomplete where appropriate.
- Ratified fictional dates and precedence, NU-OPS-006 update cadence/status labels, and NU-OPS-019 reporting role allocation. Preserved repository location, purchase authority, retention periods, Alder Creek backup, and metrics source/platform/results as deliberate unknowns.
- Durable approval decision: `reports/content-approval.md`; shared accepted/unresolved claims: `corpus/fact-ledger.yaml`. PDFs and rendered metadata have been regenerated and checked after approval (21 PDFs, 64 pages).

- Final approval QA complete: corrected stale flow-diagram draft labeling, replaced raw HTML hard breaks that appeared literally in PDFs, synchronized NU-OPS-018 scheduled lifecycle metadata, and updated its reference in NU-OPS-008. Regenerated all PDFs and confirmed source/PDF hashes, lifecycle values, index links, searchable text, and visual layout. `git diff --check` passes; no test suite was run.
