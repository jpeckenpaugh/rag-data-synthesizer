#!/usr/bin/env python3
"""Generate reproducible local visual assets for a synthetic corpus.

All source facts are read from the selected scenario's YAML inputs. The script
does not use names or roles to infer avatar appearance. Accepted generated
outputs are preserved as inputs to PDF rendering; rendering never invokes this
generator.
"""

from __future__ import annotations

import argparse
import colorsys
import hashlib
import json
import re
import shutil
import sys
import textwrap
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw

try:
    import yaml
except ImportError:  # Offline bridge mode accepts JSON converted from YAML.
    yaml = None


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STAFF = ROOT / "corpus/staff.yml"
DEFAULT_SITE_CATEGORIES = ROOT / "corpus/data/visuals/staff-home-sites.yml"
DEFAULT_FLOW = ROOT / "corpus/data/visuals/opening-flow.yml"
DEFAULT_SOURCE_DIR = ROOT / "corpus/assets/source"
DEFAULT_OUTPUT_DIR = ROOT / "corpus/assets/generated"
MASTER_SEED = 21001
CANVAS = 384
SCALE = 3

SVG_TEXT_STYLES = {
    "title": (26, 700, "#18324B", None),
    "subtitle": (16, 400, "#52636B", None),
    "label": (18, 600, "#263238", None),
    "count": (18, 700, "#18324B", None),
    "note": (15, 700, "#18324B", None),
    "small": (14, 400, "#52636B", None),
    "current": (13, 700, "#3E6748", None),
    "step": (16, 700, "#18324B", None),
    "decision": (15, 700, "#18324B", "middle"),
    "branch": (12, 700, "#52636B", None),
    "body": (13, 400, "#263238", None),
    "separate": (11, 700, "#52636B", None),
    "exception": (13, 700, "#6D382D", None),
}


def inline_svg_text_styles(svg: str) -> str:
    """Use SVG presentation attributes for predictable PDF text sizing."""
    def replace(match: re.Match) -> str:
        class_name = match.group(1)
        if class_name not in SVG_TEXT_STYLES:
            raise ValueError("unknown SVG text class: {}".format(class_name))
        size, weight, fill, anchor = SVG_TEXT_STYLES[class_name]
        attrs = 'font-family="DejaVu Sans, sans-serif" font-size="{}" font-weight="{}" fill="{}"'.format(size, weight, fill)
        if anchor:
            attrs += ' text-anchor="{}"'.format(anchor)
        original_attrs = re.sub(r'\sclass="[^"]+"', "", match.group(0)[5:-1])
        return "<text{} {}>".format(original_attrs, attrs)

    svg = re.sub(r'<text\b[^>]*\bclass="([^"]+)"[^>]*>', replace, svg)
    # The presentation attributes above are understood consistently by browsers
    # and SVG-to-PDF engines, unlike the embedded CSS shorthand some renderers
    # scale incorrectly when an SVG is placed in a paginated document.
    svg = re.sub(r"\s*<style>.*?</style>", "", svg, flags=re.DOTALL)
    return svg

def load_yaml(path: Path) -> Any:
    raw = path.read_text(encoding="utf-8")
    if yaml is None:
        if path.suffix.lower() != ".json":
            raise ValueError("PyYAML is required for YAML inputs; in offline bridge mode pass Ruby-converted JSON inputs")
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise ValueError("invalid JSON in {}: {}".format(path, exc))
    try:
        return yaml.safe_load(raw)
    except OSError as exc:
        raise ValueError("cannot read {}: {}".format(path, exc))
    except yaml.YAMLError as exc:
        raise ValueError("invalid YAML in {}: {}".format(path, exc))


def xml_svg(width: int, height: int, body: str, title: str, description: str) -> str:
    return '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
{body}
</svg>
'''.format(w=width, h=height, title=escape(title), description=escape(description), body=body)


def logo_svg(brand: Dict[str, Any]) -> str:
    vi = brand.get("visual_identity", {})
    palette = vi.get("palette", {})
    navy = palette.get("deep_navy", "#18324B")
    teal = palette.get("harbor_teal", "#2D8C8C")
    coral = palette.get("warm_coral", "#E77D63")
    paper = palette.get("paper", "#FFFDF8")
    body = '''  <circle cx="96" cy="96" r="88" fill="{paper}"/>
  <g fill="none" stroke="{teal}" stroke-width="7" stroke-linecap="round">
    <path d="M96 96 C115 78 135 64 157 51"/>
    <path d="M96 96 C119 104 139 117 158 135"/>
    <path d="M96 96 C77 108 60 125 43 143"/>
  </g>
  <circle cx="157" cy="51" r="9" fill="{coral}"/>
  <circle cx="158" cy="135" r="9" fill="{navy}"/>
  <circle cx="43" cy="143" r="9" fill="{coral}"/>
  <path d="M96 23 L112 76 L166 96 L112 114 L96 169 L79 114 L25 96 L79 76 Z" fill="{teal}" stroke="{navy}" stroke-width="6" stroke-linejoin="round"/>
  <path d="M96 23 L112 76 L96 96 Z" fill="{coral}"/>
  <circle cx="96" cy="96" r="9" fill="{navy}"/>'''.format(
        navy=navy, teal=teal, coral=coral, paper=paper
    )
    return xml_svg(192, 192, body, "Northstar Urgent Care Cooperative mark",
                   "Fictional north-star motif joined to a rounded three-point path with one endpoint for each fictional site.")


def hex_color(hue: float, saturation: float, lightness: float) -> str:
    rgb = colorsys.hls_to_rgb(hue % 1.0, lightness, saturation)
    return "#{:02X}{:02X}{:02X}".format(*(round(channel * 255) for channel in rgb))


def avatar_palette_map(employee_ids: List[str], seed: int) -> Dict[str, Tuple[str, str, str]]:
    """Assign unique abstract color palettes using stable seeded ID ordering."""
    keyed = []
    for employee_id in employee_ids:
        digest = hashlib.sha256((str(seed) + ":" + employee_id).encode("utf-8")).digest()
        keyed.append((digest, employee_id))
    ordered = sorted(keyed)
    count = len(ordered)
    return {
        employee_id: (
            hex_color(index / max(1, count), 0.20, 0.94),
            hex_color(index / max(1, count), 0.48, 0.58),
            hex_color(index / max(1, count) + 0.43, 0.58, 0.52),
        )
        for index, (_, employee_id) in enumerate(ordered)
    }


def draw_avatar(palette: Tuple[str, str, str], output: Path) -> None:
    bg, shirt, accent = palette
    s = SCALE
    image = Image.new("RGB", (CANVAS * s, CANVAS * s), bg)
    draw = ImageDraw.Draw(image)

    def xy(values: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple(value * s for value in values)

    # Shared neutral head/body silhouette; no hair, skin-tone, age, gender, or
    # personality cues are varied. Abstract accessory shapes distinguish IDs.
    draw.ellipse(xy((64, 42, 320, 298)), fill="#E9CDB3", outline="#18324B", width=5 * s)
    draw.rounded_rectangle(xy((43, 250, 341, 419)), radius=65 * s, fill=shirt, outline="#18324B", width=5 * s)
    draw.polygon([xy((151, 250)), xy((192, 309)), xy((232, 250))], fill=bg)
    draw.line([xy((192, 309)), xy((192, 400))], fill=accent, width=7 * s)

    # Two minimal identical-style features keep the illustration friendly but
    # avoid individualized facial expressions or inferred characteristics.
    draw.ellipse(xy((132, 153, 148, 169)), fill="#18324B")
    draw.ellipse(xy((236, 153, 252, 169)), fill="#18324B")
    draw.arc(xy((154, 181, 230, 237)), start=15, end=165, fill="#18324B", width=4 * s)

    # Shared geometric badge; it encodes no role/site or personal attribute.
    draw.polygon([xy((192, 337)), xy((226, 372)), xy((192, 407)), xy((158, 372))], fill=accent, outline="#FFFDF8")

    image.resize((CANVAS, CANVAS), Image.Resampling.LANCZOS).save(output, format="PNG", optimize=False)


def counts_svg(staff: Dict[str, Any], site_config: Dict[str, Any]) -> str:
    people = staff.get("people")
    categories = site_config.get("categories")
    if not isinstance(people, list) or not isinstance(categories, list):
        raise ValueError("staff YAML must have people[] and site category config must have categories[]")
    counts = Counter()
    for person in people:
        if not isinstance(person, dict) or not person.get("employee_id") or not person.get("home_site"):
            raise ValueError("every staff entry needs employee_id and home_site")
        counts[str(person["home_site"])] += 1

    labels = []
    seen = set()
    for item in categories:
        if not isinstance(item, dict) or not item.get("id") or not item.get("label"):
            raise ValueError("each site category needs id and label")
        key = str(item["id"])
        if key in seen:
            raise ValueError("duplicate site category: {}".format(key))
        seen.add(key)
        labels.append((key, str(item["label"])))
    unexpected = sorted(set(counts) - seen)
    if unexpected:
        raise ValueError("staff registry has unconfigured home_site values: {}".format(", ".join(unexpected)))

    width, row_h, top = 940, 84, 120
    height = top + row_h * len(labels) + 106
    max_count = max([counts[key] for key, _ in labels] + [1])
    bar_left, bar_max = 294, 450
    rows = []
    for index, (key, label) in enumerate(labels):
        y = top + index * row_h
        n = counts[key]
        bar_w = 0 if n == 0 else max(22, round(bar_max * n / max_count))
        fill = "#CBD8DD" if n == 0 else ("#E77D63" if key == "alder_creek" else "#2D8C8C")
        rows.append('''  <g>
    <text x="44" y="{baseline}" class="label">{label}</text>
    <rect x="{left}" y="{y}" width="{bar_max}" height="34" rx="12" fill="#F0F3F4"/>
    <rect x="{left}" y="{y}" width="{bar_w}" height="34" rx="12" fill="{fill}"/>
    <text x="{number_x}" y="{baseline}" class="count">{n}</text>
  </g>'''.format(baseline=y + 25, label=escape(label), left=bar_left, y=y, bar_max=bar_max,
                bar_w=bar_w, fill=fill, number_x=bar_left + bar_w + 15, n=n))
    central_count = counts.get("central_office", 0)
    alder_count = counts.get("alder_creek", 0)
    note = "Alder Creek: {} registry entries (no staff.yml entry with home_site=alder_creek).".format(alder_count)
    note2 = "Counts are registry rows by home_site, not site staffing, coverage, or attendance."
    body = '''  <rect x="0" y="0" width="100%" height="100%" fill="#FFFDF8"/>
  <text x="44" y="48" class="title">Staff registry entries by home site</text>
  <text x="44" y="82" class="subtitle">Grouped from {total} entries in staff.yml · central office is a separate registry location</text>
{rows}
  <line x1="44" y1="{rule_y}" x2="896" y2="{rule_y}" stroke="#D7DFE2" stroke-width="2"/>
  <text x="44" y="{note_y}" class="note">{note}</text>
  <text x="44" y="{note2_y}" class="small">{note2}</text>'''.format(
        total=sum(counts.values()), rows="\n".join(rows), rule_y=top + row_h * len(labels) + 10,
        note_y=top + row_h * len(labels) + 43, note=escape(note),
        note2_y=top + row_h * len(labels) + 72, note2=escape(note2))
    body += '''
  <style>
    .title { font: 700 26px sans-serif; fill: #18324B; }
    .subtitle { font: 16px sans-serif; fill: #52636B; }
    .label { font: 600 18px sans-serif; fill: #263238; }
    .count { font: 700 18px sans-serif; fill: #18324B; }
    .note { font: 700 15px sans-serif; fill: #18324B; }
    .small { font: 14px sans-serif; fill: #52636B; }
  </style>'''
    return inline_svg_text_styles(xml_svg(width, height, body, "Staff registry entries by home site",
                   "Counts are computed from staff.yml home_site values. Alder Creek has zero registry entries; this is not a vacancy or coverage count.")
                   )


def flow_svg(flow: Dict[str, Any]) -> str:
    title = str(flow.get("title", "Opening and closing handoff flow"))
    opening = flow.get("opening", {})
    decision = str(flow.get("decision", "Routine handoff can proceed?"))
    proceed = flow.get("proceed", {})
    hold = flow.get("hold_and_route", {})
    closing = flow.get("closing", {})
    for name, item in (("opening", opening), ("proceed", proceed), ("hold_and_route", hold), ("closing", closing)):
        if not isinstance(item, dict) or not item.get("title") or not isinstance(item.get("lines"), list):
            raise ValueError("flow config {} needs title and lines[]".format(name))
    width, height = 1300, 620
    decision_lines = textwrap.wrap(decision, width=19, break_long_words=False, break_on_hyphens=False)
    body = ['''  <rect x="0" y="0" width="100%" height="100%" fill="#FFFDF8"/>
  <text x="40" y="48" class="title">{}</text>
  <rect x="40" y="68" width="300" height="30" rx="15" fill="#E8F3EA"/>
  <text x="55" y="89" class="current">CURRENT · EFFECTIVE 2024-09-21</text>'''.format(escape(title))]

    def card(x: int, y: int, w: int, h: int, item: Dict[str, Any], fill: str,
             title_class: str = "step", dashed: bool = False) -> None:
        border = ' stroke-dasharray="8 6"' if dashed else ""
        body.append('''  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="#2D8C8C" stroke-width="2"{border}/>
  <text x="{tx}" y="{ty}" class="{title_class}">{title}</text>
{lines}'''.format(
            x=x, y=y, w=w, h=h, fill=fill, border=border, tx=x + 16, ty=y + 28,
            title_class=title_class, title=escape(str(item["title"])),
            lines="\n".join(
                '  <text x="{}" y="{}" class="body">{}</text>'.format(x + 16, y + 54 + line_i * 19, escape(line))
                for line_i, line in enumerate(item["lines"])
            )))

    # Word wrapping explicitly preserves procedure IDs such as NU-OPS-007.
    opening_lines = [line for source in opening["lines"] for line in textwrap.wrap(str(source), width=35, break_long_words=False, break_on_hyphens=False)]
    proceed_lines = [line for source in proceed["lines"] for line in textwrap.wrap(str(source), width=35, break_long_words=False, break_on_hyphens=False)]
    hold_lines = [line for source in hold["lines"] for line in textwrap.wrap(str(source), width=48, break_long_words=False, break_on_hyphens=False)]
    closing_lines = [line for source in closing["lines"] for line in textwrap.wrap(str(source), width=28, break_long_words=False, break_on_hyphens=False)]
    card(40, 168, 285, 166, {"title": opening["title"], "lines": opening_lines}, "#E8F2F4")
    card(590, 156, 292, 160, {"title": proceed["title"], "lines": proceed_lines}, "#E8F3EA")
    card(590, 350, 392, 150, {"title": hold["title"], "lines": hold_lines}, "#FFF1E9")
    card(1010, 168, 250, 270, {"title": closing["title"], "lines": closing_lines}, "#F5F0DE", dashed=True)

    body.append('''  <path d="M325 250 L365 250" stroke="#18324B" stroke-width="4" fill="none" marker-end="url(#arrow)"/>
  <polygon points="450,166 534,250 450,334 366,250" fill="#FFFDF8" stroke="#18324B" stroke-width="3"/>
  <path d="M534 250 L590 235" stroke="#5C8968" stroke-width="4" fill="none" marker-end="url(#arrow)"/>
  <text x="541" y="226" class="branch">YES</text>
  <path d="M450 334 L450 425 L590 425" stroke="#C26248" stroke-width="4" fill="none" marker-end="url(#arrow)"/>
  <text x="463" y="365" class="branch">NO</text>
  <text x="1010" y="460" class="separate">SEPARATE CLOSING RECORD</text>''')
    body.append("\n".join(
        '  <text x="450" y="{}" class="decision">{}</text>'.format(242 + line_i * 21, escape(line))
        for line_i, line in enumerate(decision_lines[:3])
    ))
    exception = str(flow.get("exception_note", ""))
    if exception:
        note_lines = textwrap.wrap(exception, width=150, break_long_words=False, break_on_hyphens=False)
        body.append('''  <rect x="40" y="530" width="1220" height="66" rx="12" fill="#FCEBE5"/>
{lines}'''.format(lines="\n".join(
            '  <text x="57" y="{}" class="exception">{}</text>'.format(554 + line_i * 21, escape(line))
            for line_i, line in enumerate(note_lines[:2]))))
    body.append('''  <defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#18324B"/></marker></defs>
  <style>
    .title { font: 700 26px sans-serif; fill: #18324B; }
    .current { font: 700 13px sans-serif; fill: #3E6748; }
    .step { font: 700 16px sans-serif; fill: #18324B; }
    .decision { font: 700 15px sans-serif; fill: #18324B; text-anchor: middle; }
    .branch { font: 700 12px sans-serif; fill: #52636B; }
    .body { font: 13px sans-serif; fill: #263238; }
    .separate { font: 700 11px sans-serif; fill: #52636B; }
    .exception { font: 700 13px sans-serif; fill: #6D382D; }
  </style>''')
    return inline_svg_text_styles(xml_svg(width, height, "\n".join(body), title,
                   "Current opening handoff with a decision branch: the routine handoff can proceed with an open item, or a blocking condition is held and routed. The closing record is shown separately. NU-OPS-004 is approved but scheduled for its stated Harbor Point window.")
                   )


def write_svg(source_dir: Path, output_dir: Path, filename: str, content: str) -> Tuple[Path, Path]:
    source = source_dir / filename
    output = output_dir / filename
    source.write_text(content, encoding="utf-8")
    shutil.copyfile(source, output)
    return source, output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--staff-yaml", type=Path, default=DEFAULT_STAFF)
    parser.add_argument("--brand-yaml", type=Path, default=ROOT / "corpus/brand.yml")
    parser.add_argument("--site-categories-yaml", type=Path, default=DEFAULT_SITE_CATEGORIES)
    parser.add_argument("--flow-yaml", type=Path, default=DEFAULT_FLOW)
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--seed", type=int, default=MASTER_SEED)
    args = parser.parse_args()
    try:
        staff = load_yaml(args.staff_yaml)
        brand = load_yaml(args.brand_yaml)
        categories = load_yaml(args.site_categories_yaml)
        flow = load_yaml(args.flow_yaml)
        people = staff.get("people") if isinstance(staff, dict) else None
        if not isinstance(people, list) or not people:
            raise ValueError("staff YAML must contain a non-empty people[] list")
        ids = [str(p.get("employee_id", "")) for p in people]
        if any(not item for item in ids) or len(set(ids)) != len(ids):
            raise ValueError("staff employee IDs must be present and unique")
        args.source_dir.mkdir(parents=True, exist_ok=True)
        args.output_dir.mkdir(parents=True, exist_ok=True)

        written: List[Tuple[Path, Path]] = []
        written.append(write_svg(args.source_dir, args.output_dir, "nucc-logo.svg", logo_svg(brand)))
        written.append(write_svg(args.source_dir, args.output_dir, "staff-home-site-count.svg", counts_svg(staff, categories)))
        written.append(write_svg(args.source_dir, args.output_dir, "opening-closing-check-flow.svg", flow_svg(flow)))
        avatar_dir = args.output_dir / "portraits"
        avatar_dir.mkdir(parents=True, exist_ok=True)
        palette_by_id = avatar_palette_map(ids, args.seed)
        for employee_id in ids:
            path = avatar_dir / (employee_id.lower() + ".png")
            draw_avatar(palette_by_id[employee_id], path)
            written.append((path, path))

        print("Generated {} assets from {}".format(len(written), args.staff_yaml))
        print("Seed: {} (stable unique portrait palette assignment)".format(args.seed))
        for source, output in written:
            print("{} -> {}".format(source.relative_to(ROOT) if source.is_relative_to(ROOT) else source,
                                    output.relative_to(ROOT) if output.is_relative_to(ROOT) else output))
        yaml_version = yaml.__version__ if yaml is not None else "offline JSON bridge (Ruby stdlib YAML)"
        print("Python {} · Pillow {} · YAML reader {}".format(sys.version.split()[0], Image.__version__, yaml_version))
        return 0
    except (ValueError, OSError, AttributeError) as exc:
        print("error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
