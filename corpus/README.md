# Corpus authoring and PDF rendering

Markdown files in `documents/markdown/` are the source of truth. PDFs under
`documents/pdf/` are generated ingestion artifacts. Do not edit a PDF by hand;
change its Markdown source and rerender it.

The renderer is scenario-neutral. Use the same script for a new company corpus
by passing that scenario's Markdown input directory and PDF output directory.
The optional brand and illustration configuration files are presentation inputs;
they must not be used to introduce facts that are absent from the source
documents or their approved data.

## Requirements

- Python **3.14** for the repository's reproducible environment. The renderer
  and asset generator share this one environment.
- WeasyPrint's native text/layout dependencies, including Pango 1.44 or newer.
  On macOS, install the native library with `brew install pango`; Linux and
  Windows requirements differ. Follow the [versioned WeasyPrint 70.0
  installation guide](https://doc.courtbouillon.org/weasyprint/v70.0/first_steps.html#installation).
- Fonts available to Pango. The default stylesheet requests DejaVu Sans and
  falls back to Arial or a sans-serif font. Installing the same font family on
  each machine helps keep line wraps and page breaks consistent.

The exact Python package versions for rendering and visual generation are
pinned in their component files and aggregated by the root
[`../requirements.txt`](../requirements.txt). Install from that one entry
point; do not create separate renderer and asset-generation environments.
The Python packages alone do not pin the operating system, Pango, font files,
or fontconfig. For byte-for-byte repeatability, use the same OS/container image,
native libraries, and fonts. `--report` captures Python, package, platform, and
Pango versions when available. Per document it records page and extracted-text
counts, coordinator-note handling, SHA-256 hashes for both the Markdown source
and rendered PDF, plus each used local visual asset's repository path and
SHA-256 hash. These hashes identify the exact inputs and outputs described by a
rendering report.

## Install

From the repository root, create the shared Python 3.14 environment and install
all pinned renderer and asset-generation dependencies:

```sh
python3.14 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
```

Install WeasyPrint's native libraries using the platform-specific guide above
before invoking the renderer. Do not run installation commands from this
document blindly on a different operating system.

## Render the current scenario

From the repository root:

```sh
.venv/bin/python scripts/render_pdfs.py \
  --input-dir corpus/documents/markdown \
  --output-dir corpus/documents/pdf \
  --corpus-yaml corpus/corpus.yml \
  --brand-yaml corpus/brand.yml \
  --illustrations-yaml corpus/illustrations.yml \
  --report reports/rendering.json
```

Input Markdown files are processed in filename order. Each source must begin
with YAML front matter and provide `document_id`, `title`, `status`, `version`,
`effective_date`, and `access_scope`. The output filename is the document ID
(for example, `NU-OPS-001.pdf`); duplicate or unsafe IDs and missing required
metadata stop the run with an error. The output directory must be inside this
repository. Existing PDF outputs with the same ID are overwritten.
When `--corpus-yaml` is supplied, the renderer also writes
`corpus/documents/README.md` from the inventory. The index lists each
document's ID, title, access scope, audience, and purpose, with relative links
such as `./pdf/NU-OPS-001.pdf`. It is a generated navigation aid, not an
authored document or PDF ingestion input.

To refresh only the provenance report after an external or manual PDF rebuild,
use `--report-only` with the same paths. This inventories existing PDFs and
current source/asset hashes without rewriting PDF files:

```sh
.venv/bin/python scripts/render_pdfs.py \
  --input-dir corpus/documents/markdown \
  --output-dir corpus/documents/pdf \
  --corpus-yaml corpus/corpus.yml \
  --brand-yaml corpus/brand.yml \
  --illustrations-yaml corpus/illustrations.yml \
  --report reports/rendering.json \
  --report-only
```

The PDF header displays the configured organization name and the metadata panel
shows document ID, title, status, version, effective date, and access scope;
`site_scope` is displayed when present. Page headers and footers contain the
document ID, organization name, fictional-material notice, and page numbers.
Tables repeat their header row when they continue across a page. The renderer
uses local assets only: network fetches and paths that resolve outside the
repository are rejected.

## Regenerate scenario visuals

The root requirements also include Pillow and PyYAML for the deterministic
portrait and SVG generator. Run it from the repository root when the approved
staff registry, brand, or visual inputs change:

```sh
.venv/bin/python scripts/generate_visuals.py \
  --staff-yaml corpus/staff.yml \
  --brand-yaml corpus/brand.yml \
  --site-categories-yaml corpus/data/visuals/staff-home-sites.yml \
  --flow-yaml corpus/data/visuals/opening-flow.yml \
  --source-dir corpus/assets/source \
  --output-dir corpus/assets/generated \
  --seed 21001
```

The command writes saved visual assets only; it does not modify Markdown or
render PDFs. Keep the accepted files under `corpus/assets/` as inputs to the
PDF renderer. Rendering never regenerates art.

### Coordinator-only drafting notes

The Markdown sources may end with an internal `Drafting note`, `Drafting note
for coordinator`, or `Drafting basis` section after a horizontal rule. By
default, the renderer strips that terminal block from the reader-facing PDF;
the authoritative Markdown remains unchanged. To include the internal block
for review purposes, pass `--include-coordinator-notes`. Ordinary horizontal
rules elsewhere in a document remain part of the rendered content.

### Optional brand and illustration inputs

When a scenario defines its own brand and visual registry, pass them explicitly:

```sh
.venv/bin/python scripts/render_pdfs.py \
  --input-dir corpus/documents/markdown \
  --output-dir corpus/documents/pdf \
  --brand-yaml corpus/brand.yml \
  --illustrations-yaml corpus/illustrations.yml
```

Brand configuration reads the scenario shape used here: `organization.display_name`,
`visual_identity.palette.deep_navy`, `visual_identity.palette.warm_coral` (or
`harbor_teal`), and `visual_identity.logo.asset_path`. It also accepts the generic
`organization.name` / `brand.primary_color`, `brand.accent_color`, and
`brand.logo` equivalents. An optional organization tagline is displayed when
provided. Colors use six-digit hex notation. Relative logo paths resolve from
the brand YAML file.

The visual plan's `visuals` records are an asset registry once an `asset_path`
is populated. The renderer reads each record's `id`, `target_document_id`,
`asset_path`, `alt_text`, and `caption`. A Markdown image can refer to a planned
asset as `![optional fallback alt text](asset:asset-id)`. The plan's alt text and
caption are applied to the embedded image; a plan target other than `shared` or
`all` is restricted to that document ID. Records with `asset_path: null` remain
planning entries and cannot yet be embedded. Ordinary relative image paths
resolve from the Markdown file. All image paths must exist and resolve inside
the repository. Keep chart labels and source facts in nearby Markdown text too,
so PDF text extraction retains the evidence.

These config hooks control presentation and local asset resolution. They do
not automatically insert document-specific visuals; place each image reference
where it belongs in that document's Markdown. The shared logo is displayed in
the letterhead when its brand configuration path is set.

## Review outputs

The JSON report is an inventory aid, not a visual approval. Inspect PDFs for
page breaks, table readability, image captions, and clipped content. The
renderer also opens each output with `pypdf` and fails if a PDF has no pages or
no extractable text. Check the extracted text itself for the document ID,
metadata, tables, and any facts conveyed by a diagram. Image-only policy or
procedural facts are unsuitable for RAG ingestion.

Do not put answer keys, the Markdown document index, or evaluation material
beneath `documents/pdf/`; the PDF directory is the ingestion boundary.
