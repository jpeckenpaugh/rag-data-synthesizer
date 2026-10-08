# RAG Data Synthesizer

RAG Data Synthesizer is a workflow and toolset for building realistic fictional document collections for retrieval-augmented generation (RAG) development and evaluation. It supports collection planning, staff-authored source documents, fact and relationship tracking, visual assets, PDF rendering, and release review.

The repository does **not** automatically generate document prose. A coordinator uses bounded author and reviewer agents to draft and reconcile content; the scripts generate scenario visuals and render approved Markdown to searchable PDFs.

All organizations, people, policies, events, and records are fictional. The collections are educational test material, not operational, legal, clinical, or other professional guidance.

## Current implementation

The first scenario is the Northstar Urgent Care Cooperative, a fictional three-site clinic network. Its 21 Markdown documents are approved for the fictional 2024-10-01 snapshot. The repository includes the staff registry, corpus plan, shared-fact ledger, visual plan and assets, 21 rendered PDFs, a generated PDF index, and rendering provenance. The final PDFs total 64 pages.

The Python tools are scenario-neutral enough to render another Markdown collection and generate configured local visuals. A second company scenario has not yet been used to validate the workflow. A proposed starter set of 10 answerable and 5 negative RAG query examples is available; a validated machine-readable evaluation set, full RAG ingestion manifest, and automated corpus-wide validator remain future work. `reports/rendering.json` records rendering provenance and hashes; it is not the full RAG manifest.

## Start here

- [Corpus generation workflow](docs/corpus-generation-workflow.md): reusable planning, agent coordination, dependency-aware drafting, review, approval, and release steps.
- [Visual production guide](docs/visual-production.md): fact-grounded visual planning, deterministic asset generation, and visual QA.
- [Current corpus rendering runbook](corpus/README.md): Python 3.14 setup and the commands to generate visuals and PDFs for the Northstar scenario.
- [Scenario brief and settled choices](CLINIC_DETAILS.md)
- [Corpus plan, document assignments, and drafting stages](corpus/corpus.yml)
- [Fictional staff registry](corpus/staff.yml)
- [Shared-fact decision ledger](corpus/fact-ledger.yaml)
- [Content approval record](reports/content-approval.md)
- [Document index and PDF links](corpus/documents/README.md)
- [Proposed RAG query examples and evidence](corpus/evaluation/QUERY-EXAMPLES.md)

## Project principles

- Plan the collection as a connected body of documents before drafting.
- Use deliberate document relationships, date histories, exceptions, and unanswered questions to create useful retrieval challenges.
- Vary each document's structure, voice, and level of detail while keeping shared facts coherent.
- Keep answer keys outside the document-ingestion directory.
- Record which facts are accepted and which remain intentionally unknown; never fill a visual or document with unsupported data.
- Preserve approved Markdown and visual assets as release inputs. Rendering does not create or revise their content.

## Reproduce the current render

From the repository root, follow the install instructions in [corpus/README.md](corpus/README.md), then run its documented PDF render command with `.venv/bin/python`. The supported environment is Python 3.14 with the root `requirements.txt`; WeasyPrint also requires platform libraries such as Pango and available fonts.

The render command writes PDFs to `corpus/documents/pdf/`, regenerates `corpus/documents/README.md`, and updates `reports/rendering.json`. It overwrites PDFs with matching document IDs. Generate visuals separately before rendering when scenario inputs or accepted assets change.

## Project boundaries and next steps

Current repository outputs include fictional Markdown and PDF documents, scenario configuration, generated visual assets, a document index, progress/review/approval records, PDF rendering provenance, and a manually checked proposed query sample. The workflow does not yet generate or validate a complete RAG evaluation set or ingestion manifest. Before describing the process as proven reusable across organizations, run it once with a second fictional company and record any scenario-specific assumptions or code changes.
