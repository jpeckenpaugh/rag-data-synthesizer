#!/usr/bin/env python3
"""Render scenario Markdown documents to paginated PDFs.

This is a scenario-neutral renderer. Keep organization-specific facts in source
Markdown/configuration and presentation rules in CSS or optional brand config.
"""

from __future__ import annotations

import argparse
import ctypes
import ctypes.util
import hashlib
import html
import json
import mimetypes
import platform
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
from urllib.parse import unquote, urlparse

import mistune
import yaml
from pypdf import PdfReader
from weasyprint import HTML
from weasyprint.urls import URLFetcherResponse, URLFetchingError


REQUIRED_METADATA = ("document_id", "title", "status", "version", "effective_date", "access_scope")
COORDINATOR_NOTE_RE = re.compile(r"^\*\*Drafting (?:note(?: for coordinator)?|basis):\*\*", re.IGNORECASE)
HR_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(\s*([^\s)]+)")

DEFAULT_CSS = r"""
@page {
  size: A4;
  margin: 20mm 18mm 19mm;
  @top-left { content: string(org-name); color: #53616a; font-size: 8pt; }
  @top-right { content: string(doc-id); color: #53616a; font-size: 8pt; }
  @bottom-left { content: "Fictional training material"; color: #697780; font-size: 8pt; }
  @bottom-right { content: "Page " counter(page) " of " counter(pages); color: #697780; font-size: 8pt; }
}
* { box-sizing: border-box; }
body { font-family: "DejaVu Sans", "Arial", sans-serif; color: #202a30; font-size: 10pt; line-height: 1.45; }
.letterhead { display: flex; align-items: center; gap: 10px; padding-bottom: 9px; margin-bottom: 15px; border-bottom: 2px solid var(--primary); }
.letterhead img { max-width: 54px; max-height: 42px; object-fit: contain; }
.brand-name { string-set: org-name content(); color: var(--primary); font-weight: 700; font-size: 11pt; }
.brand-tagline { color: #58666d; font-size: 8pt; }
.document-meta { border: 1px solid #cbd4d8; border-left: 4px solid var(--accent); border-radius: 3px; padding: 9px 11px; margin: 0 0 17px; background: #f5f8f8; }
.document-meta h1 { margin: 0 0 6px; color: var(--primary); font-size: 19pt; line-height: 1.2; }
.meta-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4px 12px; font-size: 8.5pt; }
.meta-label { color: #56646b; font-weight: 700; }
h1, h2, h3, h4 { color: var(--primary); page-break-after: avoid; }
h1 { font-size: 18pt; }
h2 { margin-top: 1.2em; font-size: 14pt; border-bottom: 1px solid #d7dfe2; padding-bottom: 3px; }
h3 { margin-top: 1.05em; font-size: 11.5pt; }
p, ul, ol, blockquote, table, pre, figure { orphans: 3; widows: 3; }
table { width: 100%; border-collapse: collapse; margin: 0.8em 0 1em; font-size: 8.5pt; page-break-inside: auto; }
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #c9d2d6; padding: 5px 6px; text-align: left; vertical-align: top; }
th { background: #eaf0f1; color: #26363d; }
blockquote { border-left: 3px solid var(--accent); margin: 0.8em 0; padding: 4px 12px; background: #f7f8f5; color: #3d484d; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 0.9em; background: #eef1f2; padding: 1px 3px; }
pre { white-space: pre-wrap; background: #f2f4f4; padding: 8px; border: 1px solid #d8dfe1; }
img { max-width: 100%; height: auto; }
td img { display: block; width: 76px; height: 76px; object-fit: contain; }
figure { margin: 1em auto; text-align: center; }
figcaption { font-size: 8pt; color: #57646b; margin-top: 4px; }
a { color: var(--primary); text-decoration: underline; }
.doc-id { string-set: doc-id content(); }
.content hr { border: 0; border-top: 1px solid #cbd4d8; margin: 1.2em 0; }
"""


class RenderError(Exception):
    """A user-correctable source or rendering configuration error."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pango_version() -> Optional[str]:
    """Return the loaded host Pango version when its library is discoverable."""
    library = ctypes.util.find_library("pango-1.0")
    if not library:
        return None
    try:
        pango = ctypes.CDLL(library)
        version_fn = pango.pango_version_string
        version_fn.restype = ctypes.c_char_p
        value = version_fn()
        return value.decode("ascii") if value else None
    except (AttributeError, OSError, UnicodeDecodeError):
        return None


def used_visual_assets(markdown: str, asset_map: Dict[str, Dict[str, str]],
                       source_path: Path, repo_root: Path,
                       logo_path: Optional[str], brand_cfg_path: Optional[Path]) -> List[Dict[str, str]]:
    """Return unique local image files referenced by this document and its letterhead."""
    paths = set()
    for match in IMAGE_LINK_RE.finditer(markdown):
        destination = match.group(1)
        if destination.startswith("asset:"):
            asset_id = destination[len("asset:"):]
            if asset_id not in asset_map:
                raise RenderError("Unknown illustration asset id {!r}".format(asset_id))
            value = asset_map[asset_id]["path"]
            paths.add(Path(value).resolve())
        else:
            local_file_uri(destination, source_path.parent, repo_root)
            parsed = urlparse(destination)
            raw_path = unquote(parsed.path if parsed.scheme == "file" else parsed.path)
            candidate = Path(raw_path)
            if not candidate.is_absolute():
                candidate = source_path.parent / candidate
            paths.add(candidate.resolve())
    if logo_path:
        logo_base = brand_cfg_path.parent if brand_cfg_path else repo_root
        local_file_uri(logo_path, logo_base, repo_root)
        parsed = urlparse(logo_path)
        raw_path = unquote(parsed.path if parsed.scheme == "file" else parsed.path)
        candidate = Path(raw_path)
        if not candidate.is_absolute():
            candidate = logo_base / candidate
        paths.add(candidate.resolve())
    records = []
    for path in sorted(paths, key=lambda item: item.as_posix()):
        if not path.is_relative_to(repo_root.resolve()):
            raise RenderError("Visual asset path is outside repository root: {}".format(path))
        if not path.is_file():
            raise RenderError("Visual asset file not found: {}".format(path))
        records.append({"path": str(path.relative_to(repo_root.resolve())), "sha256": sha256_file(path)})
    return records


def parse_front_matter(source: str, source_path: Path) -> Tuple[Dict[str, Any], str]:
    lines = source.splitlines()
    if not lines or lines[0].strip() != "---":
        raise RenderError("{}: expected YAML front matter beginning on line 1".format(source_path))
    try:
        closing = lines.index("---", 1)
    except ValueError:
        raise RenderError("{}: YAML front matter has no closing --- delimiter".format(source_path))
    raw = "\n".join(lines[1:closing])
    try:
        metadata = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        raise RenderError("{}: invalid YAML front matter: {}".format(source_path, exc))
    if not isinstance(metadata, dict):
        raise RenderError("{}: front matter must be a YAML mapping".format(source_path))
    missing = [key for key in REQUIRED_METADATA if metadata.get(key) in (None, "")]
    if missing:
        raise RenderError("{}: missing required metadata: {}".format(source_path, ", ".join(missing)))
    return metadata, "\n".join(lines[closing + 1:]).lstrip("\n")


def remove_coordinator_note(markdown: str) -> Tuple[str, bool]:
    """Remove a final coordinator-only drafting block, preserving normal rules."""
    lines = markdown.splitlines()
    marker = None
    for index, line in enumerate(lines):
        if COORDINATOR_NOTE_RE.match(line.strip()):
            marker = index
    if marker is None:
        return markdown, False
    # Only remove the note if it is a terminal block. This avoids hiding an
    # ordinary in-document phrase that happens to use the same label.
    if any(line.strip() for line in lines[marker + 1:]):
        return markdown, False
    hr_index = marker - 1
    while hr_index >= 0 and not lines[hr_index].strip():
        hr_index -= 1
    if hr_index >= 0 and HR_RE.match(lines[hr_index]):
        marker = hr_index
    return "\n".join(lines[:marker]).rstrip() + "\n", True


def remove_duplicate_title(markdown: str, title: str, document_id: str) -> str:
    """Avoid printing the same title in both the metadata panel and body."""
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        if not line.strip():
            continue
        match = re.match(r"^#\s+(.+?)\s*#*\s*$", line)
        if not match:
            return markdown
        heading = match.group(1).strip()
        heading = re.sub(r"^{}\s*(?:[—–:-]\s*)?".format(re.escape(document_id)), "", heading, flags=re.IGNORECASE)
        if heading.casefold().strip() == title.casefold().strip():
            del lines[index]
            return "\n".join(lines).lstrip("\n")
        return markdown
    return markdown


def load_yaml_mapping(path: Optional[Path], label: str) -> Dict[str, Any]:
    if path is None:
        return {}
    if not path.is_file():
        raise RenderError("{} config not found: {}".format(label, path))
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise RenderError("{} config has invalid YAML: {}".format(label, exc))
    if data is None:
        return {}
    if not isinstance(data, dict):
        raise RenderError("{} config must contain a YAML mapping".format(label))
    return data


def brand_values(config: Dict[str, Any]) -> Dict[str, str]:
    """Read intentionally small, scenario-neutral presentation fields."""
    brand = config.get("brand", {})
    organization = config.get("organization", {})
    visual_identity = config.get("visual_identity", {})
    if not isinstance(brand, dict) or not isinstance(organization, dict) or not isinstance(visual_identity, dict):
        raise RenderError("brand config 'brand' and 'organization' entries must be mappings")
    palette = visual_identity.get("palette", {})
    logo_cfg = visual_identity.get("logo", {})
    if not isinstance(palette, dict) or not isinstance(logo_cfg, dict):
        raise RenderError("brand visual_identity.palette and visual_identity.logo must be mappings")
    name = (organization.get("display_name") or organization.get("name") or brand.get("organization_name")
            or config.get("organization_name") or config.get("name") or "Organization")
    tagline = organization.get("tagline") or config.get("tagline") or ""
    primary = (brand.get("primary_color") or palette.get("deep_navy") or palette.get("primary")
               or config.get("primary_color") or "#28566a")
    accent = (brand.get("accent_color") or palette.get("warm_coral") or palette.get("accent")
              or palette.get("harbor_teal") or config.get("accent_color") or "#d28b42")
    logo = (brand.get("logo") or logo_cfg.get("asset_path") or config.get("logo") or "")
    for key, value in (("primary_color", primary), ("accent_color", accent)):
        if not re.match(r"^#[0-9A-Fa-f]{6}$", str(value)):
            raise RenderError("brand {} must be a six-digit hex color".format(key))
    return {"name": str(name), "tagline": str(tagline), "primary": str(primary), "accent": str(accent), "logo": str(logo)}


def illustration_assets(config: Dict[str, Any], config_path: Optional[Path]) -> Dict[str, Dict[str, str]]:
    """Read saved asset paths and display metadata without altering the plan."""
    if not config:
        return {}
    base_dir = config_path.resolve().parent if config_path else Path.cwd()
    assets = config.get("assets", {})
    if isinstance(assets, dict):
        result = {str(key): {"path": str((base_dir / str(value)).resolve()) if not Path(str(value)).is_absolute() else str(value)}
                  for key, value in assets.items()}
    elif isinstance(assets, list):
        result = {}
        for item in assets:
            if not isinstance(item, dict) or not item.get("id") or not item.get("path"):
                raise RenderError("illustrations assets list items require 'id' and 'path'")
            item_path = Path(str(item["path"]))
            result[str(item["id"])] = {"path": str(item_path.resolve() if item_path.is_absolute() else (base_dir / item_path).resolve())}
    else:
        raise RenderError("illustrations config 'assets' must be a mapping or list")

    # The scenario visual plan uses `visuals: [{id, asset_path, ...}]`. Keep
    # that planning shape intact and expose only assets that have been created.
    visuals = config.get("visuals", [])
    if visuals is not None:
        if not isinstance(visuals, list):
            raise RenderError("illustrations config 'visuals' must be a list")
        for visual in visuals:
            if not isinstance(visual, dict):
                raise RenderError("illustrations visuals entries must be mappings")
            if visual.get("id") and visual.get("asset_path"):
                asset_path = Path(str(visual["asset_path"]))
                result[str(visual["id"])] = {
                    "path": str(asset_path.resolve() if asset_path.is_absolute() else (base_dir / asset_path).resolve()),
                    "alt_text": str(visual.get("alt_text") or ""),
                    "caption": str(visual.get("caption") or ""),
                    "target_document_id": str(visual.get("target_document_id") or ""),
                }
    return result


def local_file_uri(path_value: str, base_dir: Path, repo_root: Path) -> str:
    parsed = urlparse(path_value)
    if parsed.scheme not in ("", "file") or parsed.netloc not in ("", "localhost"):
        raise RenderError("Only local image assets are allowed: {}".format(path_value))
    raw_path = unquote(parsed.path if parsed.scheme == "file" else parsed.path)
    candidate = Path(raw_path)
    if not candidate.is_absolute():
        candidate = base_dir / candidate
    candidate = candidate.resolve()
    root = repo_root.resolve()
    if not candidate.is_relative_to(root):
        raise RenderError("Asset path must stay inside the repository: {}".format(path_value))
    if not candidate.is_file():
        raise RenderError("Local image asset not found: {}".format(candidate))
    return candidate.as_uri()


def make_markdown_renderer(asset_map: Dict[str, Dict[str, str]], source_dir: Path, repo_root: Path,
                           document_id: str) -> mistune.Markdown:
    class LocalAssetRenderer(mistune.HTMLRenderer):
        def image(self, text: str, url: str, title: Optional[str] = None) -> str:
            if url.startswith("asset:"):
                asset_id = url[len("asset:"):]
                if asset_id not in asset_map:
                    raise RenderError("Unknown illustration asset id {!r}".format(asset_id))
                asset = asset_map[asset_id]
                target = asset.get("target_document_id")
                if target and target not in ("shared", "all", document_id):
                    raise RenderError("Illustration {!r} is planned for {}, not {}".format(asset_id, target, document_id))
                src = local_file_uri(asset["path"], source_dir, repo_root)
                alt = asset.get("alt_text") or text or ""
                caption = asset.get("caption") or ""
            else:
                src = local_file_uri(url, source_dir, repo_root)
                alt = text or ""
                caption = ""
            alt = html.escape(alt, quote=True)
            title_attr = ' title="{}"'.format(html.escape(title, quote=True)) if title else ""
            image_html = '<img src="{}" alt="{}"{} />'.format(html.escape(src, quote=True), alt, title_attr)
            if caption:
                return '<figure class="planned-visual">{}<figcaption>{}</figcaption></figure>'.format(
                    image_html, html.escape(caption))
            return image_html

    renderer = LocalAssetRenderer(escape=True)
    return mistune.create_markdown(renderer=renderer, plugins=["table", "strikethrough", "url"])


def local_only_fetcher(repo_root: Path):
    root = repo_root.resolve()

    def fetcher(url: str) -> Dict[str, Any]:
        parsed = urlparse(url)
        if parsed.scheme != "file" or parsed.netloc not in ("", "localhost"):
            raise URLFetchingError("External resources are disabled: {}".format(url))
        path = Path(unquote(parsed.path)).resolve()
        if not path.is_relative_to(root):
            raise URLFetchingError("Resource is outside repository root: {}".format(url))
        if not path.is_file():
            raise URLFetchingError("Local resource not found: {}".format(path))
        media_type = mimetypes.guess_type(str(path))[0] or "application/octet-stream"
        return URLFetcherResponse(
            path.as_uri(),
            path.read_bytes(),
            {"Content-Type": media_type, "Content-Length": str(path.stat().st_size)},
            status=200,
        )

    return fetcher


def html_document(metadata: Dict[str, Any], body_html: str, brand: Dict[str, str], logo_uri: str) -> str:
    doc_id = str(metadata["document_id"])
    title = str(metadata["title"])
    fields = [
        ("Document ID", doc_id),
        ("Status", metadata["status"]),
        ("Version", metadata["version"]),
        ("Effective date", metadata["effective_date"]),
        ("Access scope", metadata["access_scope"]),
    ]
    if metadata.get("site_scope"):
        fields.append(("Site scope", metadata["site_scope"]))
    meta_html = "".join(
        '<div><span class="meta-label">{}:</span> {}</div>'.format(html.escape(str(label)), html.escape(str(value)))
        for label, value in fields
    )
    logo = '<img src="{}" alt="" />'.format(html.escape(logo_uri, quote=True)) if logo_uri else ""
    tagline = '<div class="brand-tagline">{}</div>'.format(html.escape(brand["tagline"])) if brand["tagline"] else ""
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>:root {{ --primary: {primary}; --accent: {accent}; }}\n{css}</style></head>
<body><header class="letterhead">{logo}<div><div class="brand-name">{organization}</div>{tagline}</div></header>
<section class="document-meta"><h1>{title}</h1><div class="meta-grid"><span class="doc-id">{doc_id}</span>{metadata}</div></section>
<main class="content">{body}</main></body></html>""".format(
        title=html.escape(title), primary=brand["primary"], accent=brand["accent"], css=DEFAULT_CSS,
        logo=logo, organization=html.escape(brand["name"]), tagline=tagline, doc_id=html.escape(doc_id),
        metadata=meta_html, body=body_html,
    )


def render_one(source_path: Path, output_path: Path, repo_root: Path, brand_cfg: Dict[str, Any],
               brand_cfg_path: Optional[Path], asset_map: Dict[str, str], include_notes: bool) -> Dict[str, Any]:
    try:
        source = source_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise RenderError("cannot read {}: {}".format(source_path, exc))
    metadata, body = parse_front_matter(source, source_path)
    note_removed = False
    if not include_notes:
        body, note_removed = remove_coordinator_note(body)
    body = remove_duplicate_title(body, str(metadata["title"]), str(metadata["document_id"]))
    brand = brand_values(brand_cfg)
    logo_uri = ""
    if brand["logo"]:
        logo_base = brand_cfg_path.parent if brand_cfg_path else repo_root
        logo_uri = local_file_uri(brand["logo"], logo_base, repo_root)
    markdown = make_markdown_renderer(asset_map, source_path.parent, repo_root, str(metadata["document_id"]))
    body_html = markdown(body)
    document_html = html_document(metadata, body_html, brand, logo_uri)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        HTML(string=document_html, base_url=source_path.parent.as_uri(), url_fetcher=local_only_fetcher(repo_root)).write_pdf(str(output_path))
        reader = PdfReader(str(output_path))
        page_count = len(reader.pages)
        extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as exc:
        raise RenderError("{}: PDF rendering or text extraction failed: {}".format(source_path, exc))
    if page_count < 1:
        raise RenderError("{} produced a PDF with no pages".format(source_path))
    if not extracted.strip():
        raise RenderError("{} produced a PDF with no extractable text".format(source_path))
    return {
        "document_id": str(metadata["document_id"]), "source": str(source_path.relative_to(repo_root)),
        "source_sha256": sha256_file(source_path),
        "pdf": str(output_path.relative_to(repo_root)), "pdf_sha256": sha256_file(output_path),
        "visual_assets": used_visual_assets(source, asset_map, source_path, repo_root,
                                             brand["logo"], brand_cfg_path),
        "pages": page_count, "extracted_characters": len(extracted),
        "coordinator_note_excluded": note_removed,
    }


def report_existing(source_path: Path, output_path: Path, repo_root: Path,
                    brand_cfg: Dict[str, Any], brand_cfg_path: Optional[Path],
                    asset_map: Dict[str, Dict[str, str]], include_notes: bool) -> Dict[str, Any]:
    """Inventory existing outputs and current inputs without rewriting PDFs."""
    source = source_path.read_text(encoding="utf-8")
    metadata, body = parse_front_matter(source, source_path)
    note_removed = False
    if not include_notes:
        body, note_removed = remove_coordinator_note(body)
    body = remove_duplicate_title(body, str(metadata["title"]), str(metadata["document_id"]))
    del body  # Note/title parsing keeps report semantics aligned with render_one.
    if not output_path.is_file():
        raise RenderError("existing PDF not found for report-only mode: {}".format(output_path))
    try:
        reader = PdfReader(str(output_path))
        page_count = len(reader.pages)
        extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as exc:
        raise RenderError("{}: cannot inspect existing PDF: {}".format(output_path, exc))
    if page_count < 1 or not extracted.strip():
        raise RenderError("{} has no pages or extractable text".format(output_path))
    brand = brand_values(brand_cfg)
    return {
        "document_id": str(metadata["document_id"]), "source": str(source_path.relative_to(repo_root)),
        "source_sha256": sha256_file(source_path),
        "pdf": str(output_path.relative_to(repo_root)), "pdf_sha256": sha256_file(output_path),
        "visual_assets": used_visual_assets(source, asset_map, source_path, repo_root,
                                             brand["logo"], brand_cfg_path),
        "pages": page_count, "extracted_characters": len(extracted),
        "coordinator_note_excluded": note_removed,
    }


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    default_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=default_root / "corpus/documents/markdown", help="Directory containing Markdown sources")
    parser.add_argument("--output-dir", type=Path, default=default_root / "corpus/documents/pdf", help="Directory for generated PDFs")
    parser.add_argument("--brand-yaml", type=Path, default=None, help="Optional scenario brand configuration")
    parser.add_argument("--illustrations-yaml", type=Path, default=None, help="Optional local illustration asset registry")
    parser.add_argument("--report", type=Path, default=None, help="Optional JSON rendering report output")
    parser.add_argument("--report-only", action="store_true", help="Refresh the report from existing PDFs without rendering or modifying them")
    parser.add_argument("--include-coordinator-notes", action="store_true", help="Include terminal Drafting note/basis sections intended for coordinator review")
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parents[1]
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()
    if not input_dir.is_dir():
        print("error: input directory not found: {}".format(input_dir), file=sys.stderr)
        return 2
    if not output_dir.is_relative_to(repo_root):
        print("error: output directory must be within repository root {}".format(repo_root), file=sys.stderr)
        return 2
    sources = sorted(input_dir.glob("*.md"))
    if not sources:
        print("error: no .md sources found in {}".format(input_dir), file=sys.stderr)
        return 2
    if args.report_only and args.report is None:
        print("error: --report-only requires --report", file=sys.stderr)
        return 2
    try:
        brand_cfg = load_yaml_mapping(args.brand_yaml.resolve() if args.brand_yaml else None, "brand")
        illustrations_cfg = load_yaml_mapping(args.illustrations_yaml.resolve() if args.illustrations_yaml else None, "illustrations")
        asset_map = illustration_assets(illustrations_cfg, args.illustrations_yaml)
        results = []
        seen_ids = set()
        for source_path in sources:
            # Parse once to get a safe, stable output name and reject duplicate IDs.
            metadata, _ = parse_front_matter(source_path.read_text(encoding="utf-8"), source_path)
            doc_id = str(metadata["document_id"])
            if doc_id in seen_ids:
                raise RenderError("duplicate document_id {!r}".format(doc_id))
            seen_ids.add(doc_id)
            if not re.match(r"^[A-Za-z0-9][A-Za-z0-9._-]*$", doc_id):
                raise RenderError("unsafe document_id for filename: {!r}".format(doc_id))
            output_path = output_dir / (doc_id + ".pdf")
            if args.report_only:
                result = report_existing(source_path, output_path, repo_root, brand_cfg,
                                         args.brand_yaml.resolve() if args.brand_yaml else None,
                                         asset_map, args.include_coordinator_notes)
            else:
                result = render_one(source_path, output_path, repo_root, brand_cfg, args.brand_yaml.resolve() if args.brand_yaml else None,
                                    asset_map, args.include_coordinator_notes)
            results.append(result)
            action = "Inventoried" if args.report_only else "Rendered"
            print("{} {} -> {} ({} pages, {} extracted chars)".format(action, doc_id, result["pdf"], result["pages"], result["extracted_characters"]))
        report = {
            "renderer": "render_pdfs.py", "python": sys.version.split()[0], "mistune": mistune.__version__,
            "weasyprint": __import__("weasyprint").__version__, "pyyaml": yaml.__version__,
            "pypdf": __import__("pypdf").__version__, "platform": platform.platform(),
            "pango": pango_version(),
            "report_mode": "existing_outputs" if args.report_only else "rendered_outputs",
            "sources_rendered": len(results), "documents": results,
        }
        if args.report:
            report_path = args.report.resolve()
            if not report_path.is_relative_to(repo_root):
                raise RenderError("report path must stay inside repository root")
            report_path.parent.mkdir(parents=True, exist_ok=True)
            report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            print("Wrote report {}".format(report_path.relative_to(repo_root)))
        return 0
    except (RenderError, OSError, yaml.YAMLError) as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
