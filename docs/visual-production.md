# Reproducible visual production for synthetic corpora

This guide describes a scenario-neutral workflow for adding expressive, fact-grounded visuals to synthetic company document collections and rendering the source Markdown to PDFs for RAG ingestion.

## Principles

- Plan visuals at collection level before creating assets. A visual has a document purpose, intended reader, placement, source evidence, caption, and alt text.
- Keep claims in selectable text too. A chart or diagram may clarify facts, but must not be the only place a material policy or value appears.
- Distinguish **decorative** art (branding, flourishes, non-semantic icons, portraits used as identifiers) from **evidence-bearing** visuals (charts, timelines, maps, workflow diagrams, annotated forms). Decorative art must not imply unsupported facts. Evidence-bearing visuals cite source documents and precise fields/sections.
- Preserve approved generated assets as inputs. Rendering should not regenerate art. This makes the released PDF repeatable even if drawing libraries, fonts, or image-generation services later change.
- Make the visual plan and data input scenario-specific; keep the schema, scripts, and production instructions reusable across organizations.
- Keep fictional data visibly identified as synthetic and never use real personal information or imply real-world guidance.

## Repository layout

```text
docs/visual-production.md
schemas/illustrations.schema.json
scripts/generate_visuals.py
scripts/render_pdfs.py
requirements.txt
corpus/
  brand.yml
  illustrations.yml
  assets/source/
  assets/generated/
  data/                 # explicit chart inputs, when any
  documents/markdown/
  documents/pdf/
reports/content-approval.md
reports/content-review.md
reports/rendering.json
```

Use `brand.yml` for scenario identity settings (display name, optional short name, palette, logo asset, and treatment notes). Use `illustrations.yml` as the per-run visual registry and plan. The JSON Schema validates the registry shape; domain checks should additionally verify that cited document IDs exist, source paths resolve inside the corpus, and referenced Markdown fields/sections or data inputs exist. The schema validates shape; it does not establish that the visual's claims are true.

## Workflow

1. **Inspect sources and plan.** Read the approved corpus plan, fact ledger, staff registry, and relevant Markdown. Identify a small set of visuals that genuinely help readers navigate or understand the material. Record proposed status until the underlying content and source facts are approved.
2. **Bootstrap agents with review.** For new contributors, first request a read-only repository review, findings, and only blocking questions. Assign bounded implementation after the coordinator resolves assumptions. The coordinator owns the source of truth and resolves conflicting proposals.
3. **Record provenance.** Every visual entry has a stable ID, target document, purpose, placement, caption, alt text, category, status, and generation method. Evidence-bearing items require one or more sources with document ID and locator (section, field, or structured-data path). Chart entries also identify their exact input file and fields. Record a seed for seeded procedural generation. For generated or edited art, preserve the accepted output and record tool/model/prompt metadata where available; do not rely on regeneration for byte identity.
4. **Create assets.** Prefer local SVG for logos, diagrams, simple maps, and iconography; use Pillow for small raster illustrations or template-based cartoon portraits. Use chart libraries only when needed and pin them. Do not use remote assets or fonts at render time. Record asset license/provenance for any externally sourced material.
5. **Review facts before layout.** Check every arrow, label, date, grouping, number, and claim against its cited source. Check decorative art does not imply an unsupported role, site condition, demographic, credential, or event. Keep unknowns visibly unknown.
6. **Render deterministically.** Parse Markdown and YAML front matter, resolve local assets from the scenario root, apply reusable print styles, and write PDFs to the dedicated PDF directory. Generate `corpus/documents/README.md` from the corpus inventory with sibling-relative PDF links. Pin Python dependencies and document external font/system requirements. Set a stable locale, page size, font files, and asset paths. Treat source Markdown and saved assets as inputs; do not change content as a renderer side effect.
7. **Inspect visually and textually.** Render representative PDFs to page images and review title hierarchy, page breaks, tables, contrast, image cropping, headers/footers, and page numbering. Extract PDF text with a pinned tool such as `pypdf`; check document identity and meaningful text survive extraction. For evidence-bearing graphics, verify their essential point is also stated in surrounding text or accessible caption.
8. **Record and release.** Save a report with commands, Python and dependency versions, OS/font notes, generated file list, checksums, inspection sample, findings, and resolutions. For a full RAG release, add a manifest that maps each Markdown source, visual asset, and PDF with checksums; the current scripts do not generate that manifest. Keep RAG evaluation answer keys outside the ingestion tree.

## Data-backed charts and diagrams

Never invent values to fill a graphic. Use a small YAML/CSV/JSON source file whose records are fictional and approved. Include source document IDs and source field names in the plan. If values are derived, document the transformation, units, grouping, exclusions, and seed if random sampling is used. The output must be reproducible from the saved input and pinned script. If the source document intentionally contains definitions but no results, do not produce a results chart.

Workflow diagrams should depict only steps, roles, branches, and destinations supported by the referenced source. Label planned or draft processes accordingly. If a route is unknown in the corpus, show an explicit “not established” node or omit the route; do not draw a plausible substitute.

## Asset-generation environment

The canonical environment uses Python 3.14 and the repository's shared `.venv`. From the repository root, create and populate it with the root requirements file, then generate the assets:

```sh
python3.14 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/generate_visuals.py
```

The generator reads scenario YAML directly with the pinned PyYAML dependency and writes editable vector sources under `corpus/assets/source/` plus canonical render inputs under `corpus/assets/generated/`. For another scenario, pass its staff, brand, category, and diagram-input files with the corresponding command-line options. Use the same Python 3.14 `.venv` and root `requirements.txt`; do not silently substitute another Python version or an unrecorded conversion path. The renderer consumes saved assets and does not regenerate them.

## Reusable acceptance checks

- Share a fictional logo/letterhead while preserving layout variation where document type needs it.
- Use expressive fictional portraits only from approved fictional staff registry fields; never treat an avatar as a real likeness or evidence of protected traits.
- Make quick-reference, policy/procedure, working-record, and directory layouts readable for their distinct uses.
- Trace evidence-bearing diagrams to source sections and have facts reviewed independently.
- Create data charts only from approved structured inputs; no results chart is needed when a source defines measures but provides no results.
- Inspect representative PDF pages and extracted text; recheck affected outputs after content or asset changes.
- Before claiming scenario portability, run a second fictional company configuration and record the changes needed.

## Northstar status and visual lifecycle

The Northstar document content is approved for the fictional 2024-10-01 snapshot; NU-OPS-021 is a current approved directory. Visual approval is tracked separately from document approval. At the current release, the brand configuration itself still has `status: proposed`; the logo, eight portraits, and staff home-site count graphic are marked reviewed, and the NU-OPS-002 opening/closing flow is approved. Other registry entries marked `proposed` have no asset path and are planning candidates, not visuals included in the PDFs. Several of those candidates still contain draft-era wording; refresh and fact-check an entry against the approved source before generating it.

The registry status values are `proposed`, `approved`, `generated`, `reviewed`, and `deferred`. Keep their meanings distinct: `proposed` is a candidate, `approved` records design/fact approval, `generated` means files exist, `reviewed` means the documented review occurred, and `deferred` means the candidate is intentionally postponed. Do not treat `generated` alone as approval or review.
