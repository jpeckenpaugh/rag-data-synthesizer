# Fictional Urgent Care Corpus Details

## Purpose

Create source material for building and testing a retrieval-augmented generation (RAG) integration. The corpus should provide realistic, varied organizational documents that exercise ingestion, retrieval, citation, metadata filtering, document precedence, and safe handling of unsupported questions.

## Scenario

The initial corpus represents a completely fictional urgent care clinic organization. The organization, locations, people, roles, policies, events, phone numbers, email addresses, and records must be invented. Do not use real patient, employee, or customer information, or imply that the generated materials describe an actual clinic.

The documents are educational test fixtures. They are not operational, legal, clinical, or other professional guidance. Keep the content focused on administration and operations; do not provide diagnosis, treatment recommendations, or patient-specific advice.

## Audience and use

The primary audience is a builder or evaluator developing a RAG integration. The document set should enable testing of:

- Retrieval of directly supported facts and procedures.
- Page-level citations to rendered PDFs.
- Filtering by document metadata and access scope.
- Current-versus-superseded document precedence.
- Exceptions, amendments, and cross-document relationships.
- Questions whose answers are absent from the collection, including questions that should be refused or explicitly left unanswered.

## Collection size and formats

Target approximately 20 documents. Markdown files are the authoritative working sources. Provide a repeatable process for rendering those Markdown files to PDFs, since the downstream RAG workflow will ingest PDFs. Keep evaluation answers and other test keys separate from ingestible source documents.

## Content and style

Use a mixed collection with plausible variety in document type, length, structure, voice, and completeness. Possible document types include organization policies, department procedures, quick-reference guides, notices, forms or checklists, incident-response and escalation materials, quality guidance, and historical or superseded copies. The selected mix is listed in the settled document inventory below.

Documents should feel like materials from one coherent fictional organization. Give each a plausible purpose, owner, audience, status, date, and relationship to other documents. Include deliberate, understandable retrieval challenges while avoiding accidental contradictions. The corpus should contain both polished official materials and more concise or uneven working documents where appropriate.

## RAG challenge design

The selected challenge design is listed in the settled planning choices below. Include examples of current and superseded guidance, a controlled exception or amendment, department or access-scope distinctions, evidence that supports citation, and questions that cannot be answered from the corpus. Keep answer keys outside the documents used for ingestion.

## Organization and outputs

Create the corpus in this repository using a logical directory structure. Keep Markdown working files distinct from rendered PDFs, planning and source-of-truth artifacts, evaluation materials, and validation or rendering reports. The concrete structure is listed in the settled planning choices below.

Expected release artifacts should include, as appropriate:

- This scenario and requirements file.
- A corpus brief and document plan in `corpus/corpus.yml`, linked to the fictional staff registry in `corpus/staff.yml`.
- A fact and relationship ledger.
- Approximately 20 Markdown source documents.
- Rendered PDF counterparts and a repeatable rendering process.
- A machine-readable manifest with document metadata and relationships.
- A separate RAG evaluation set with expected answerability and evidence references.
- Validation and rendering reports.

## Explicitly settled decisions

- Scenario: fictional urgent care clinic operations.
- Use: source material for building and testing a RAG integration.
- Size: approximately 20 documents.
- Working format: Markdown.
- Ingestion format: PDFs rendered from the Markdown sources.
- Fiction and safety: completely fictional; no clinical advice or real personal information.
- Style: mixed.
- Location: this repository, with a logical folder structure.

## Settled planning choices

### Fictional organization and setting

Use **Northstar Urgent Care Cooperative (NUCC)**, a fictional, independently operated three-site urgent care network in the fictional state of **Westmere**. Its locations are **Harbor Point**, **Alder Creek**, and **Northgate**. The organization has a small central operations office and site-based teams. These names and all associated addresses, people, roles, contact details, events, and records are invented for this corpus. Avoid real street addresses, real phone numbers, and real email domains; use clearly fictional contact details such as `*.example.invalid` where a contact is needed.

The corpus focuses on non-clinical operations: facilities, staffing administration, records handling, service continuity, supply requests, workplace incidents, quality tracking, and internal communications. It does not define clinical workflows or care decisions.

### Document inventory

Create 21 Markdown documents with stable IDs. Versions marked superseded are separate documents and remain in the corpus for historical retrieval tests. This remains an approximately 20-document corpus; NU-OPS-021 is an approved addition to keep the all-staff directory distinct from the narrower role-routing directory.

| ID | Working title | Type / focus | Initial status |
| --- | --- | --- | --- |
| NU-OPS-001 | Operations Governance and Document Control | Organization policy; owners, approvals, and controlled copies | Current |
| NU-OPS-002 | Site Opening and Closing Checklist | Site procedure; routine facility handoff | Current |
| NU-OPS-003 | Facilities Issue Intake and Escalation | Procedure; facilities requests and priority routing | Current |
| NU-OPS-004 | Harbor Point After-Hours Access Exception | Time-bounded site exception to access procedure | Current, limited scope |
| NU-OPS-005 | Staff Schedule Change Notice | Short operational notice; who may approve schedule changes | Current |
| NU-OPS-006 | Service Interruption Response | Procedure; non-clinical outage coordination and communications | Current |
| NU-OPS-007 | Site Contact and Escalation Directory | Reference; fictional roles and internal routing | Current |
| NU-OPS-008 | Supply Request and Receiving Guide | Procedure; routine supplies and receiving discrepancies | Current |
| NU-OPS-009 | Records Handling and Misdelivery Procedure | Administrative procedure; secure routing and incident reporting | Current |
| NU-OPS-010 | Internal Information Access Matrix | Reference; role- and document-scope permissions | Current |
| NU-OPS-011 | Workplace Incident Reporting Guide | Procedure; non-clinical workplace incident reporting | Current |
| NU-OPS-012 | Quality Huddle Notes, September | Informal notes; action owners and unresolved follow-ups | Current, working record |
| NU-OPS-013 | Severe Weather Site Coordination Card | Quick reference; site status and communications | Current |
| NU-OPS-014 | Vendor Visit and Contractor Sign-In | Checklist; facilities vendor access | Current |
| NU-OPS-015 | Document Revision Bulletin 24-03 | Bulletin amending routing and revision practices | Current |
| NU-OPS-016 | Facilities Issue Routing, Revision 1 | Historical procedure, superseded by NU-OPS-003 | Superseded |
| NU-OPS-017 | Staff Schedule Change Notice, Prior Edition | Historical notice, superseded by NU-OPS-005 | Superseded |
| NU-OPS-018 | Northgate Supply Receiving Exception | Time-bounded receiving exception to NU-OPS-008 | Current, limited scope |
| NU-OPS-019 | Monthly Operations Metrics Definitions | Reference; definitions and reporting ownership | Current |
| NU-OPS-020 | Unresolved Service Desk Questions Log | Brief working log; explicitly records facts not established by the corpus | Current, incomplete |
| NU-OPS-021 | Staff and Site Directory | All-staff reference; registry-backed employee and home-site fields | Current |

NU-OPS-007 remains the role-based operational contact and escalation directory with `site_operations` access. NU-OPS-021 is a separate organization-wide, `all_staff` directory of the eight fictional registry entries. It must not imply contact routes, shift coverage, reporting lines, employment status, or named Alder Creek coverage; role-based routing remains in NU-OPS-007.

The plan and ledger should assign fictional authors/owners and publication, effective, review, and supersession dates. Keep the chronology internally consistent: historical versions precede their replacements, exceptions have start/end dates, and the revision bulletin does not silently change unrelated content. The September huddle notes should use a clearly stated fictional year consistent with the corpus timeline.

### Metadata and access scopes

Every document receives structured metadata in the manifest, with at least:

- `document_id`, `title`, `document_type`, `department`, and `site_scope` (one site, multiple sites, or organization-wide).
- `owner_role`, `intended_audience`, and `access_scope`.
- `status`, `version`, `issued_date`, `effective_date`, `review_date` if applicable, and `supersedes` / `amends` / `exception_to` / `references` relationships.
- Source Markdown path, rendered PDF path, and checksum after rendering.

Use three fictional access scopes: `all_staff`, `site_operations`, and `operations_leads`. These are test labels, not claims about real security practice. NU-OPS-010 defines the corpus access matrix. Give some documents narrower scopes so evaluation can check filtering; do not include sensitive personal details. Put metadata in a small YAML front matter block in each Markdown file and repeat it in `manifest.json`. Clearly render reader-relevant title, ID, status, version, effective date, and scope in each PDF; keep internal generation notes out of the reader-facing body.

### Planned document relationships and retrieval challenges

Use these explicit relationships as the controlled source of expected precedence:

- NU-OPS-016 is superseded by NU-OPS-003. The older routing path remains discoverable as history but must not be presented as current.
- NU-OPS-017 is superseded by NU-OPS-005. The prior approval rule is historical.
- NU-OPS-004 is a Harbor Point-only, time-bounded exception to the applicable access portion of NU-OPS-002. It does not override unrelated opening/closing requirements.
- NU-OPS-018 is a Northgate-only, time-bounded exception to NU-OPS-008 for a defined receiving window. It does not change routine receiving elsewhere or outside that window.
- NU-OPS-015 amends NU-OPS-001 document-routing/revision practices and specifies how current controlled copies are identified. Its scope is limited to those stated sections.
- NU-OPS-007 supplies fictional role-based routing details used by procedures. If a role or destination is absent there and elsewhere, the corpus does not establish it.
- NU-OPS-012 and NU-OPS-020 contain incomplete follow-ups by design. They support testing of careful retrieval and abstention, not filling gaps with guesses.
- NU-OPS-021 reproduces identity and home-site fields from `corpus/staff.yml`; the registry is the source of truth for those fields. Its role-routing reference points to NU-OPS-007, whose narrower access scope remains unchanged.

The evaluation set should include supported direct lookups, multi-document synthesis, date/site/access filters, current-versus-historical precedence, exception scope, citation evidence, and unanswerable questions. Each case should identify expected answerability, required filters, evidence document IDs and PDF page references after rendering, and concise expected answer points. Include at least one case where a superficially relevant historical or out-of-scope document must not determine the answer. Include unsupported questions that invite invented contacts, dates, or procedures; the expected behavior is to state that the corpus does not establish the answer.

### Folder layout and rendering process

Use this repository structure:

```text
CLINIC_DETAILS.md
corpus/
  README.md
  brief.yaml
  corpus.yml
  staff.yml
  fact-ledger.yaml
  manifest.json
  documents/
    markdown/
      NU-OPS-001-operations-governance.md
      ...
    pdf/
      NU-OPS-001-operations-governance.pdf
      ...
evaluation/
  questions.jsonl
reports/
  validation.json
  rendering.json
scripts/
  render_pdfs.py
  requirements-render.txt
```

Markdown files are authoritative; PDFs are generated outputs. Implement a repeatable local renderer in `scripts/render_pdfs.py` that reads the corpus Markdown, uses its front matter for visible document metadata, and writes corresponding PDFs under `corpus/documents/pdf/`. Pin the renderer dependencies in `scripts/requirements-render.txt` and document setup and invocation in `corpus/README.md`. Prefer a self-contained Python rendering stack that does not require a separately installed office suite. The process should fail clearly for missing required metadata or source files and should produce stable, readable page headers/footers with page numbers. Record the actual tool/dependency versions and rendering outcome in `reports/rendering.json` after generation. Use the root `requirements.txt` to install the shared Python 3.14 `.venv` dependencies; component pin files document the renderer and asset packages. PDFs are ingestion inputs; keep `evaluation/questions.jsonl` outside the PDF tree so answer keys cannot be ingested accidentally.

### Acceptance targets

- Exactly 21 planned document IDs, with Markdown source for each.
- All organization names and document facts consistently fictional and within the non-clinical operational boundary.
- Every document has complete required metadata and an explicit relationship list, even when empty.
- Planned version history and exceptions are time-, site-, and scope-bounded and internally consistent.
- All PDFs can be generated from the Markdown by the documented command, with visible document identity/status and usable pagination.
- Evaluation material is separate from ingestion documents, includes supported and unsupported cases, and cites final PDF pages.
- The manifest maps each source and PDF and records checksums for the rendered files.

These choices replace the earlier delegation of organization, inventory, metadata, relationships, evaluation design, folder layout, and renderer implementation to later planning.
