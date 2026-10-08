# Reusable synthetic corpus generation workflow

This runbook captures the workflow used to create the Northstar Urgent Care Cooperative corpus. It separates reusable coordination and review practices from scenario-specific facts and paths. The process currently relies on agent-assisted prose authoring; it does not use an automated document-content generator.

## Roles and source of truth

The **primary coordinator** owns the run, plan, fact ledger, dependency schedule, integration, final approval, rendering, and release record. The coordinator does not author source documents. Fictional staff profiles provide document authorship and voice; bounded author agents draft or revise the assigned documents. Independent reviewers assess consistency, domain boundaries, access and roles, retrieval quality, and style.

The coordinator makes routine fictional design decisions when authority has been delegated, records decisions in the ledger or approval record, and raises only material blockers that cannot be resolved from the brief and approved design. A draft author does not approve their own work. Accepted facts and document approval are separate: an accepted ledger entry does not by itself approve any document.

For each new company, keep scenario facts in scenario files and reusable instructions in `docs/` and `scripts/`. In this repository, the Northstar-specific brief is `CLINIC_DETAILS.md`; the scenario plan, staff registry, fact ledger, brand configuration, visual plan, source Markdown, and PDFs live under `corpus/`.

## Run sequence

### 1. Establish the brief and acceptance criteria

Record the fictional organization, domain, setting, audience, collection size, safety boundaries, desired document mix, RAG challenges, output formats, and a snapshot or run date. State which details must be fictional, which topics are out of scope, and how unsupported questions should be represented. Resolve critical design choices before assigning work; record non-blocking unknowns for later decisions or deliberate abstention cases.

### 2. Plan the collection before prose

Create a high-level list of proposed document titles and sections. Give each document a stable ID, purpose, type, author, owner, audience, access scope, site or department scope, status/date plan, relationships, and intended retrieval behavior. Map every intended author to a fictional entry in the staff registry.

Represent prerequisites explicitly. A procedure should be stable before an exception to that procedure is drafted; an amended policy should be stable before its amendment is reconciled; working records should use established terminology and role routes. Store a staged dependency plan in the corpus inventory so the order can be reviewed and reused.

### 3. Create and maintain the fact ledger

Record cross-document facts and decisions in a structured ledger before drafting. Use these states consistently:

- `proposed`: a candidate fictional convention awaiting a coordinator decision.
- `accepted`: a fictional fact or convention approved as corpus canon.
- `unresolved`: an intentional unknown that documents and agents must not infer.

Include affected document IDs and a short decision or rationale. Keep the ledger focused on shared claims; Markdown remains authoritative for each document's full content. Record content approval separately in document front matter/revision history and in a run approval record. Approval can preserve genuine unknowns without resolving them.

### 4. Bootstrap contributors and draft in dependency-aware batches

When starting new agents, first request a read-only repository review and a short list of blockers or open questions. Use that review to give them bounded assignments with the relevant plan/ledger context, exact IDs, exclusions, dependencies, required metadata, deliverables, and acceptance criteria.

Start with documents that establish shared roles, routing, access labels, and governance. For a multi-author collection, drafting one independent first document per staff profile is a useful way to establish distinct voices early. Work on independent documents can run concurrently. Hold dependent exceptions, amendments, and working records until their prerequisite material has passed its reconciliation gate. Do not assign overlapping edits to the same source files.

Authors may enrich documents with useful operational detail and grounded examples, but should not add filler or unapproved cross-document facts. They should flag assumptions and missing evidence for the coordinator. Update the plan and review affected dependents when an accepted shared fact changes.

### 5. Review, revise, and approve content

Use independent reviews with distinct lenses, for example:

- Domain plausibility, scope, and fictional safety boundaries.
- Dates, precedence, exceptions, and cross-document continuity.
- Staff roles, access scope, routing, and named contacts.
- RAG answerability, evidence specificity, and intentional unknowns.
- Voice variation, repetition, and readability.

Findings should identify the document, claim or section, severity, evidence, and proposed resolution. Return document edits to the assigned author when practical; have the coordinator reconcile shared plan/ledger changes. Preserve intended history and exceptions while fixing accidental contradictions.

Before rendering, verify required front matter, plan/source agreement, valid relationships, dates, approved-by and approval-date records, current/scheduled/superseded lifecycle state, and fiction/safety boundaries. Record approval decisions and remaining unknowns. Do not ask the user to repeat a manual approval pass when the coordinator has been authorized to approve; ask only about significant decisions outside that authority or a genuine blocker.

### 6. Plan and produce visuals

Create a scenario-specific brand configuration, visual registry, and explicit data inputs. Each visual should have a purpose, target document, placement, caption, alt text, source evidence, and generation method. Mark a visual as evidence-bearing or decorative. Check every number, label, date, relationship, role, and route against approved source material.

Use local SVG or code for logos and diagrams, and deterministic local generation for portraits or charts when suitable. Fix and record seeds where used. Never make up chart values or put a material fact only in an image. Preserve accepted output assets as renderer inputs; PDF rendering does not regenerate visuals. See [visual production](visual-production.md) for detailed asset guidance.

### 7. Generate PDFs and the document index

Use the shared Python 3.14 `.venv` and root `requirements.txt`. Install the native WeasyPrint dependencies for the host OS and use consistent fonts when page-wrap repeatability matters. The scenario-specific [corpus rendering runbook](../corpus/README.md) contains the tested Northstar commands and renderer behavior; pass the corresponding paths for another scenario.

Generate visuals first when inputs or assets changed, then render the approved Markdown. The renderer writes one PDF per `document_id`, updates the Markdown document index when given the corpus YAML, and records Python/package/platform/Pango versions, source and PDF hashes, visual-asset hashes, page counts, and extracted text counts in the JSON rendering report. That report is rendering provenance, not a full RAG ingestion manifest.

### 8. Validate the release

At minimum, verify:

- The plan, staff registry, ledger, source front matter, and document relationships agree.
- Every inventory document has exactly one Markdown source and PDF; lifecycle statuses agree across the plan, source, and rendered PDF.
- All generated index links resolve and the index remains outside the PDF ingestion directory.
- The report's source/PDF/asset hashes match the files on disk.
- PDFs have extractable text, correct identity and metadata, and no stale drafting notes, banners, literal markup, or broken links.
- Representative first, middle, and final pages have readable typography, page breaks, tables, illustrations, captions, and headers/footers. Reinspect affected documents after a source or asset change.
- Evidence-bearing visuals agree with text and cited sources; no image supplies unsupported data.
- Intentional unknowns remain unanswered and any RAG evaluation answers, when created, stay outside the ingestion tree.

The renderer performs basic required-metadata and PDF extraction checks, but it is not a comprehensive corpus validator. Record manual checks and findings in the run report or progress log; do not describe unimplemented automated checks as complete.

### 9. Record and release the run

Keep the brief, plan, staff registry, accepted and unresolved ledger decisions, source Markdown, visual inputs and accepted assets, PDFs, index, rendering report, content review, approval record, and progress log together. Record commands and tool/environment versions. Commit a coherent release after checks pass. Preserve the actual accepted prose and assets: seeds make deterministic visuals reproducible, but model-authored text may vary between runs.

## Current implementation and future work

Implemented in this repository:

- Scenario planning and staff authorship are represented by the brief, corpus YAML, and staff registry.
- A shared decision ledger and document-level approval records capture accepted decisions and deliberate unknowns.
- Deterministic visual generation and scenario-configurable Markdown-to-PDF rendering are available.
- The document index and a rendering provenance report are generated with the PDFs.
- The Northstar scenario has 21 approved Markdown sources and PDFs for the 2024-10-01 fictional snapshot.

Not yet implemented or demonstrated:

- An automated content-authoring engine or comprehensive corpus-wide validator.
- A full machine-readable RAG ingestion manifest and separate evaluation dataset.
- A second company scenario proving the process and tools generalize beyond Northstar.
- Byte-for-byte PDF reproduction across different operating systems, Pango builds, and font installations.

Treat those as explicit follow-up work. A successful Northstar render demonstrates this run's process; it does not prove every other scenario will work without configuration changes.
