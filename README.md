# RAG Data Synthesizer

RAG Data Synthesizer is a project for creating realistic, varied synthetic document collections that can be used to prototype and evaluate retrieval-augmented generation (RAG) systems.

The initial teaching use case is a fictional urgent care clinic. A student and tutor will use its documents to build a RAG workflow and explore document ingestion, retrieval, citations, permissions, versioning, and safe refusal. The generator should be reusable: the clinic is its first scenario, not a hard-coded one-off corpus.

All organizations, people, policies, events, and records in generated collections are fictional. The project is for education and system testing, not for operational, legal, clinical, or other professional guidance.

## Goals

- Generate document collections that feel like they came from a real organization, with distinct voices, useful detail, and plausible variation in structure and quality.
- Make generation configurable for different organizations, domains, audiences, collection sizes, document types, and RAG behaviors.
- Include relationships and realistic friction across documents, such as revisions, exceptions, overlapping guidance, outdated copies, and gaps in coverage.
- Produce usable PDFs along with supporting metadata and evaluation materials.
- Make each generated collection inspectable and regenerable from its inputs.

## Design principles

**Realism with control.** Documents should not read like identical examples filled from a template. Vary language, formatting, level of detail, and document quality while keeping key facts and relationships coherent.

**A corpus is more than a pile of PDFs.** A useful collection has an organizational context, a plausible reason each document exists, and relationships between documents. Generation should plan the collection as a whole before drafting individual documents.

**Explicit fiction.** Use invented organization names and settings, and avoid real patient, employee, or customer information. Include a clear synthetic-data notice in the collection.

**Testable behavior.** Design the corpus to support questions with clear evidence, questions whose answer depends on metadata or document precedence, and questions the corpus cannot answer. Keep expected evidence separate from the PDFs so it can be used to evaluate a RAG system.

**Review before release.** Generated content and rendered PDFs need checks for internal consistency, realistic presentation, accidental sensitive data, and readable page layout.

## Proposed generation process

The workflow is a sequence of stages, with review points between planning, drafting, and release. A run should preserve its configuration and intermediate artifacts so a collection can be inspected and regenerated.

### Multi-agent execution model

Run corpus generation as a coordinated team of specialized sub-agents. The `primary-agent` owns the run from brief through release and invokes the subordinate profiles described below. It is the only agent that coordinates the full workflow or changes the authoritative plan and fact ledger. Sub-agents receive bounded tasks and return proposed artifacts or findings; the primary-agent integrates, resolves, and approves them.

The agent profiles are role instructions, not autonomous sources of truth. They can shape perspective, terminology, and drafting choices, but all agents must work from the same approved corpus brief, plan, and fact ledger. A profile should include its role, scope, voice, allowed inputs, expected output format, and constraints. Person-level details should be fictional, job-relevant, and modest; avoid caricature or traits that encourage unsafe or unprofessional content.

#### `primary-agent` profile

**Role:** Corpus generation lead and coordinator. The primary-agent translates the corpus brief into a coherent document collection, delegates bounded work to sub-agents, and integrates and validates their outputs.

**Responsibilities:**

1. Read and clarify the corpus brief; establish scope, content boundaries, run identifier, and acceptance criteria.
2. Produce and maintain the authoritative corpus plan and fact/relationship ledger. Assign stable document IDs, owners, audiences, access scopes, statuses, dates, versions, relationships, and intended RAG test cases.
3. Select subordinate profiles and assign each a defined document set or review task. Provide only the relevant approved context, including facts and relationships needed for that task.
4. Collect proposed drafts and review findings. Reconcile differences against the ledger; preserve only conflicts that are explicit in the plan, such as a superseded procedure or intentionally unresolved question.
5. Direct revisions, record decisions, and run the corpus-level validation gates before approving content for rendering.
6. Coordinate PDF rendering and inspection, page evidence mapping, manifest and evaluation-set creation, and final packaging.
7. Record provenance: profile/role used for each document, inputs and run identifier, status, review findings, and accepted revisions. Do not expose private model reasoning; record concise decisions and evidence instead.

**Authority and limits:** The primary-agent may delegate and integrate, but it must not invent or silently alter authoritative facts to make drafts fit. If the brief or source of truth is incomplete, it should resolve the gap through the planned fictional corpus design and record that decision before delegating affected drafts. It must enforce the project’s fiction and domain-safety boundaries, and reject content that presents the synthetic corpus as real guidance.

**Expected outputs:** Approved corpus brief, corpus plan, fact/relationship ledger, task assignments, integrated document sources, validation report, page evidence map, manifest, evaluation set, and release summary.

#### Sub-agent profiles

The primary-agent can instantiate these profiles for a run. A profile may be used for several documents, but each assignment should identify exact document IDs and expected deliverables.

| Profile | Perspective and task | Boundaries |
| --- | --- | --- |
| `organization-planner` | Proposes plausible departments, roles, document purposes, and organizational context for the scenario. | Proposes only; primary-agent approves the plan and authoritative facts. |
| `document-author` | Drafts assigned documents in the voice and format appropriate to their fictional author role. | Uses the approved plan and ledger; does not add unplanned policies, dates, contacts, or relationships. |
| `domain-reviewer` | Reviews assigned drafts for professional plausibility, clarity, scope, and consistency with domain boundaries. | Flags issues with quoted claims and document IDs; does not silently rewrite authoritative content. |
| `continuity-reviewer` | Compares drafts against the ledger and related documents; distinguishes accidental contradictions from planned version/history differences. | Reports conflicts and evidence; primary-agent decides disposition. |
| `rag-evaluator` | Creates candidate questions and expected evidence for retrieval, metadata filtering, precedence, citation, and refusal cases. | Uses approved document sources; keeps answer keys in the evaluation area, outside ingestion documents. |
| `style-reviewer` | Checks whether the collection has credible variation in voice, structure, detail, and document quality without losing readability. | Recommends targeted changes; does not impose a uniform template or alter facts. |

For a small corpus, the primary-agent can combine compatible review duties or use fewer profiles. Keep content drafting separate from final corpus approval: a drafting agent should not be the sole reviewer of its own documents.

#### Run sequence and handoffs

1. **Brief and acceptance criteria:** The primary-agent turns the user’s brief into a concise approved specification. Record unresolved choices as explicit assumptions or questions, and do not delegate work that depends on an unresolved safety boundary.
2. **Collection plan:** The primary-agent asks the `organization-planner` for proposals if useful, then owns the final plan and fact/relationship ledger. It divides the corpus into document assignments with stable IDs, source facts, relationships, voice guidance, access scope, and expected output format.
3. **Parallel drafting:** The primary-agent assigns non-overlapping document groups to `document-author` instances. Each assignment includes the relevant ledger excerpt and requires structured metadata plus document source content. Authors return drafts and a short list of claims that rely on the provided facts; they do not edit the shared source of truth.
4. **Independent review:** The primary-agent sends drafts to `domain-reviewer`, `continuity-reviewer`, and `style-reviewer` as appropriate. Reviewers return findings tied to document IDs and specific claims or sections, with severity and a suggested resolution. The primary-agent resolves findings and requests targeted revisions from authors.
5. **RAG evaluation design:** The `rag-evaluator` proposes questions only after the document set is stable enough to identify evidence. The primary-agent verifies each answer key against source text and page evidence, and checks that intentionally unanswerable questions truly lack supporting evidence.
6. **Corpus gate:** The primary-agent confirms required metadata and relationships, checks every planned retrieval scenario, reviews unresolved conflicts and safety findings, and approves the source documents for rendering. Failed checks return to the relevant author or planner; they do not get waived implicitly.
7. **Render and inspect:** The primary-agent coordinates rendering, verifies page references and text extraction, and asks reviewers to inspect representative outputs or flagged pages. Layout defects return to rendering; content defects return to drafting and trigger affected checks again.
8. **Package and record provenance:** The primary-agent packages PDFs, manifest, evaluation set, brief, plan, ledger, validation report, run identifier, and concise decisions. The final release notes any known limitations and confirms that all content is fictional.

#### Standard sub-agent assignment

Each delegated task should contain:

- **Profile and role:** the profile to adopt, including the fictional job role and desired voice where drafting.
- **Scope:** exact document IDs or review questions; explicit exclusions.
- **Approved context:** brief excerpt, relevant ledger entries, document relationships, and neighboring documents when needed.
- **Constraints:** required content boundaries, dates/status, metadata, style goals, and any planned ambiguity or historical conflict.
- **Deliverable:** required format, including document source plus metadata for drafting, or a finding list with evidence and disposition suggestions for review.
- **Acceptance criteria:** how the primary-agent will decide the output is complete and coherent.

Do not provide every agent with an unrestricted instruction to “make the corpus realistic.” Bound realism to the assigned task and approved facts. Agents should mark assumptions or missing information rather than fill gaps with unapproved facts.

#### Provenance and coordination rules

- The primary-agent is the single coordinator and source-of-truth owner; subordinate agents do not delegate further unless the primary-agent explicitly permits it.
- Use stable IDs and structured handoffs so parallel work can be integrated without filename collisions or ambiguous ownership.
- Keep the corpus plan and fact ledger versioned. Draft tasks should cite the versions they used; if either changes, the primary-agent identifies and reruns affected assignments and reviews.
- Preserve intended variation in voice and document quality, but never use profile personality to justify contradictions, misleading authority, unsafe instructions, or invented sensitive data.
- Track which profile drafted and reviewed each artifact in the manifest or provenance record. This supports inspection and later regeneration without embedding agent implementation details in the PDFs.
- A seed can help reproduce planning choices, but language generation may still vary. Record model/tool identifiers and the actual accepted artifacts rather than promising byte-for-byte reproducibility.

### 1. Define a corpus brief

Describe the scenario in a structured brief. It should capture:

- Domain, fictional organization, locations, size, and operating context.
- Intended readers and their roles.
- Collection size and desired mix of document types.
- Topics, departments, terminology, and writing styles to represent.
- Access scopes and metadata needed by the intended RAG exercises.
- Desired retrieval challenges, such as current-versus-superseded guidance, date-sensitive rules, exceptions, ambiguous wording, or unsupported questions.
- Content boundaries, exclusions, and any domain-specific safety constraints.
- A seed or other run identifier where deterministic reproduction is useful.

For the urgent care scenario, the brief might specify an invented clinic network, operations staff and supervisors as audiences, and a collection of policies, procedures, safety guidance, compliance references, and exception notices. The scope should remain operational: no diagnosis, treatment recommendations, patient-specific advice, or real patient data.

### 2. Plan the collection

Create a corpus plan before writing prose. Give each planned document a stable identifier and define its purpose, owner, audience, department, status, dates, access scope, format, and links to related documents. Record relationships such as `supersedes`, `amends`, `exception_to`, and `references`.

The planner should deliberately create a believable collection rather than force an exact balance of document categories. It can include old and current versions, local procedures, forms or checklists, brief notices, and documents with incomplete context. The plan should state which facts are authoritative and which are intentionally ambiguous or absent.

### 3. Build a fact and relationship ledger

Before drafting, maintain a structured source of truth for facts that must remain consistent across documents. Examples include department names, role names, escalation contacts, policy dates, terminology, and which revision is current. Track document-specific claims against this ledger, while allowing controlled differences when a historical document or deliberate conflict calls for them.

This ledger helps distinguish a meaningful retrieval challenge from an accidental contradiction. For example, an older procedure can disagree with a newer policy when the corpus clearly establishes which one is current.

### 4. Draft varied documents

Generate each document from its purpose, audience, source facts, and relationships. Use document-specific instructions rather than one uniform prose template. Vary appropriate features such as:

- Formal policy language, practical step-by-step procedures, short notices, checklists, and reference guides.
- Heading structure, tables, callouts, revision histories, and amount of detail.
- Voice and terminology appropriate to the fictional authoring group.
- Completeness and clarity, including realistic shorthand or ambiguity where it serves a planned evaluation case.

Keep metadata such as document ID, version, effective date, status, owner, access scope, and page-level provenance outside the body as structured data, while rendering relevant parts into the document where a real reader would expect them.

### 5. Validate the corpus

Run automated and editorial checks before rendering or release. Checks should cover:

- Required fields, stable IDs, date logic, and valid document relationships.
- Conflicts with the fact ledger, with explicit allowances for planned historical or ambiguous cases.
- Presence of the scenarios the brief requested, including answerable and unanswerable questions.
- Fictional names and contact details; detection of patterns that resemble real sensitive information.
- Repetitive or obviously templated language that harms realism.
- Domain-specific content boundaries and safety rules.

Validation findings should be actionable and tied to a document and claim. The workflow should support revising the plan or individual documents, then rerunning affected checks.

### 6. Render and inspect PDFs

Render approved document content to PDFs with stable titles, visible version and status information, readable typography, and useful page structure. Preserve a mapping from source sections to rendered pages so the corpus can support page-level citations.

Inspect representative PDFs and the collection as a whole. Check page breaks, tables, headers and footers, revision histories, and text extraction. A visually plausible PDF that cannot be parsed reliably is not a good ingestion fixture, so layout and extractability both matter.

### 7. Generate a manifest and evaluation set

Package the PDFs with a machine-readable manifest containing document metadata, checksums, generation inputs, and document relationships. Include an evaluation set with questions, expected answerability, relevant document IDs and page evidence, required filters, and expected refusal behavior where appropriate.

Evaluation materials should be clearly separated from the documents being ingested. This lets a RAG system be tested without accidentally retrieving its answer key.

### 8. Package and reproduce the run

Keep the brief, generation settings, seed or run identifier, validation report, manifest, evaluation set, and final PDFs together as one corpus release. Record model or tool versions when available. A run should be reproducible when its inputs and generation tools support that, while allowing intentional variation between runs when exploring different realistic corpora.

## Example output layout

```text
corpus-name/
  brief.yaml
  plan.yaml
  fact-ledger.yaml
  documents/
    UC-OPS-001.pdf
    UC-SAFE-004.pdf
  manifest.json
  evaluation/
    questions.jsonl
  reports/
    validation.json
  README.txt
```

The exact formats and directory layout are proposals. The key requirement is that source inputs, generated documents, metadata, and evaluation answers remain distinguishable and travel together.

## Initial scenario: fictional urgent care operations

The first corpus will support a tutoring project about an operations-focused RAG assistant for a fictional urgent care clinic. Plausible document families include:

- Organization-wide operational policies.
- Department procedures and quick-reference guides.
- Incident-response and escalation documents.
- Compliance and quality guidance.
- Revision notices, exceptions, and historical versions.

Potential evaluation cases include finding the current escalation process, distinguishing department-specific instructions, identifying what changed between revisions, enforcing an access-scope filter, citing the supporting page, and refusing an unsupported clinical or patient-specific question.

The initial collection size can be selected during design; the prior 20-document example is a useful starting point, not a fixed requirement. The generator should eventually support different sizes and mixes.

## Proposed project evolution

1. Agree on the corpus brief and document-plan format using the urgent care scenario.
2. Produce and review one small sample collection to tune realism, structure, and safety boundaries.
3. Implement validation and PDF rendering around the reviewed formats.
4. Add the manifest and separate evaluation-set output.
5. Try a second configuration to confirm that the workflow generalizes beyond one clinic corpus.

This README describes a proposed workflow. It does not commit the project to a specific language, model provider, storage system, or production architecture.
