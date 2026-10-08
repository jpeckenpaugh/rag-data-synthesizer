# Reproducible visual production for synthetic corpora

This guide describes a scenario-neutral workflow for adding expressive, fact-grounded visuals to synthetic company document collections and rendering the source Markdown to PDFs for RAG ingestion.

## Principles

- Plan visuals at collection level before creating assets. A visual has a document purpose, intended reader, placement, source evidence, caption, and alt text.
- Keep claims in selectable text too. A chart or diagram may clarify facts, but must not be the only place a material policy or value appears.
- Distinguish **decorative** art (branding, flourishes, non-semantic icons, portraits used as identifiers) from **evidence-bearing** visuals (charts, timelines, maps, workflow diagrams, annotated forms). Decorative art must not imply unsupported facts. Evidence-bearing visuals cite source documents and precise fields/sections.
- Preserve approved generated assets as inputs. Rendering should not regenerate art. This makes the released PDF repeatable even if drawing libraries, fonts, or image-generation services later change.
- Make the visual plan and data input scenario-specific; keep the schema, scripts, and production instructions reusable across organizations.
- Keep fictional data visibly identified as synthetic and never use real personal information or imply real-world guidance.

## Suggested reusable layout

```text
docs/visual-production.md
schemas/illustrations.schema.json
scripts/generate_visuals.py
scripts/render_pdfs.py
scripts/requirements-render.txt
corpus/
  brand.yml
  illustrations.yml
  assets/source/
  assets/generated/
  data/                 # explicit chart inputs, when any
  documents/markdown/
  documents/pdf/
reports/visual-review.md
reports/rendering.md
```

Use `brand.yml` for scenario identity settings (display name, optional short name, palette, logo asset, and treatment notes). Use `illustrations.yml` as the per-run visual registry and plan. The JSON Schema validates the registry shape; domain checks should additionally verify that cited document IDs exist, source paths resolve inside the corpus, and referenced Markdown fields/sections or data inputs exist.

## Workflow

1. **Inspect sources and plan.** Read the approved corpus plan, fact ledger, staff registry, and relevant Markdown. Identify a small set of visuals that genuinely help readers navigate or understand the material. Record proposed status until the underlying content and source facts are approved.
2. **Bootstrap agents with review.** For new contributors, first request a read-only repository review, findings, and only blocking questions. Assign bounded implementation after the coordinator resolves assumptions. The coordinator owns the source of truth and resolves conflicting proposals.
3. **Record provenance.** Every visual entry has a stable ID, target document, purpose, placement, caption, alt text, category, status, and generation method. Evidence-bearing items require one or more sources with document ID and locator (section, field, or structured-data path). Chart entries also identify their exact input file and fields. Record a seed for seeded procedural generation. For generated or edited art, preserve the accepted output and record tool/model/prompt metadata where available; do not rely on regeneration for byte identity.
4. **Create assets.** Prefer local SVG for logos, diagrams, simple maps, and iconography; use Pillow for small raster illustrations or template-based cartoon portraits. Use chart libraries only when needed and pin them. Do not use remote assets or fonts at render time. Record asset license/provenance for any externally sourced material.
5. **Review facts before layout.** Check every arrow, label, date, grouping, number, and claim against its cited source. Check decorative art does not imply an unsupported role, site condition, demographic, credential, or event. Keep unknowns visibly unknown.
6. **Render deterministically.** Parse Markdown and YAML front matter, resolve local assets from the scenario root, apply reusable print styles, and write PDFs to the dedicated PDF directory. Pin Python dependencies and document external font/system requirements. Set a stable locale, page size, font files, and asset paths. Treat source Markdown and saved assets as inputs; do not change content as a renderer side effect.
7. **Inspect visually and textually.** Render representative PDFs to page images and review title hierarchy, page breaks, tables, contrast, image cropping, headers/footers, and page numbering. Extract PDF text with a pinned tool such as `pypdf`; check document identity and meaningful text survive extraction. For evidence-bearing graphics, verify their essential point is also stated in surrounding text or accessible caption.
8. **Record and release.** Save a report with commands, Python and dependency versions, OS/font notes, generated file list, checksums, inspection sample, findings, and resolutions. A manifest should map each Markdown source, visual asset, and PDF with checksums. Keep RAG evaluation answer keys outside the ingestion tree.

## Data-backed charts and diagrams

Never invent values to fill a graphic. Use a small YAML/CSV/JSON source file whose records are fictional and approved. Include source document IDs and source field names in the plan. If values are derived, document the transformation, units, grouping, exclusions, and seed if random sampling is used. The output must be reproducible from the saved input and pinned script. If the source document intentionally contains definitions but no results, do not produce a results chart.

Workflow diagrams should depict only steps, roles, branches, and destinations supported by the referenced source. Label planned or draft processes accordingly. If a route is unknown in the corpus, show an explicit “not established” node or omit the route; do not draw a plausible substitute.

## Asset-generation environment

The canonical environment uses Python 3.14 and the repository's shared `.venv`. From the repository root, create and populate it with the root requirements file, then generate the assets:

```sh
python3.14 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/generate_visuals.py
```

The generator reads scenario YAML directly with the pinned PyYAML dependency and writes editable vector sources under `corpus/assets/source/` plus preserved render inputs under `corpus/assets/generated/`. For another scenario, pass its staff, brand, category, and diagram-input files with the corresponding command-line options. The renderer consumes saved assets and does not regenerate them.

Optional offline fallback only: if an existing compatible Python already has Pillow but cannot install PyYAML, Ruby's standard-library YAML parser can make temporary JSON inputs. This does not replace the Python 3.14 `.venv` plus root `requirements.txt` setup and is not the canonical environment or a release dependency:

```sh
bridge_dir="$(mktemp -d)"
ruby -ryaml -rjson -e 'ARGV.each_slice(2) { |src, dst| File.write(dst, JSON.pretty_generate(YAML.safe_load(File.read(src)))) }' \
  corpus/staff.yml "$bridge_dir/staff.json" \
  corpus/brand.yml "$bridge_dir/brand.json" \
  corpus/data/visuals/staff-home-sites.yml "$bridge_dir/sites.json" \
  corpus/data/visuals/opening-flow.yml "$bridge_dir/flow.json"
python3.12 scripts/generate_visuals.py \
  --staff-yaml "$bridge_dir/staff.json" \
  --brand-yaml "$bridge_dir/brand.json" \
  --site-categories-yaml "$bridge_dir/sites.json" \
  --flow-yaml "$bridge_dir/flow.json" \
  --seed 21001
```

The offline path still uses the same generator and pinned Pillow version; Ruby only converts the YAML inputs to JSON so the generator's standard-library JSON reader can load them. Preserve the exact bridge and generation command in the rendering/asset provenance report when using this fallback.

## POC acceptance checks

- At least one logo/letterhead is shared without forcing every PDF into the same page design.
- At least one expressive but explicitly fictional directory portrait set is planned or created from staff-registry fields only.
- A quick-reference card and a policy/procedure use distinct layout treatments.
- At least one evidence-bearing diagram is traceable to cited source sections and checked by an independent reviewer.
- A data chart is generated only if an approved structured input dataset exists; no chart is required merely to decorate a document.
- PDF visual inspection and text extraction both pass for representative outputs.
- A second scenario could replace `brand.yml`, `illustrations.yml`, source Markdown, and assets without editing the schema or reusable process guide.

## Current prototype choices

The initial Northstar Urgent Care Cooperative visual plan is a prototype, not an approved final brand or illustration set. Its status values are `proposed`, `approved`, `generated`, `reviewed`, and `deferred`. NU-OPS-021 is now included in the corpus inventory and has a Markdown draft. For each asset, the registry status records its current workflow state: `generated` means the files exist, while `reviewed` means they have received the documented review. Items marked `proposed` still need generation or approval as indicated by their plan entry.
