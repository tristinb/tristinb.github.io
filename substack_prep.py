# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "httpx",
#     "pandas",
#     "beautifulsoup4",
#     "pyyaml",
#     "python-dotenv",
#     "pyperclip",
#     "lxml",
#     "markdown",
# ]
# ///
"""Prepare an Eleventy blog post for cross-posting to Substack.

Transforms tables (→ Datawrapper embeds), image shortcodes, math, footnotes,
and Nunjucks syntax so the output pastes cleanly into Substack's editor.
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
from pathlib import Path

import subprocess
import webbrowser

import httpx
import markdown as md_lib
import pandas as pd
import yaml
from bs4 import BeautifulSoup
from dotenv import load_dotenv

SITE_URL = "https://tristinb.github.io"
DW_API = "https://api.datawrapper.de/v3"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare a blog post for Substack cross-posting.",
    )
    parser.add_argument("post", type=Path, help="Path to the .md post file")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show transformations without calling Datawrapper",
    )
    parser.add_argument(
        "--no-copy",
        action="store_true",
        help="Skip copying rich text to clipboard",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open HTML in browser for preview",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=None,
        help="Custom output path (default: {post}_substack.md)",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

def strip_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter dict, body without frontmatter)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    fm = yaml.safe_load(match.group(1)) or {}
    body = text[match.end():]
    return fm, body


# ---------------------------------------------------------------------------
# Footnotes
# ---------------------------------------------------------------------------

SUPERSCRIPT_DIGITS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def to_superscript(n: int) -> str:
    """Convert an integer to unicode superscript characters."""
    return str(n).translate(SUPERSCRIPT_DIGITS)


def convert_footnotes(text: str) -> str:
    """Convert [^name] refs and definitions to numbered endnotes."""
    # Collect definitions: [^name]: text (may span multiple lines)
    def_pattern = re.compile(
        r"^\[\^([^\]]+)\]:\s*(.*?)(?=\n\[\^|\n## |\n\n(?!\s)|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    definitions: dict[str, str] = {}
    for m in def_pattern.finditer(text):
        name = m.group(1)
        body = m.group(2).strip()
        # Collapse continuation lines
        body = re.sub(r"\n\s+", " ", body)
        definitions[name] = body

    # Remove definition blocks and any "## Footnotes" header
    text = def_pattern.sub("", text)
    text = re.sub(r"## Footnotes\s*\n?", "", text)

    # Number the references in order of first appearance
    ref_order: list[str] = []

    def ref_replacer(m: re.Match) -> str:
        name = m.group(1)
        if name not in ref_order:
            ref_order.append(name)
        num = ref_order.index(name) + 1
        return to_superscript(num)

    text = re.sub(r"\[\^([^\]]+)\]", ref_replacer, text)

    # Append endnotes section
    if ref_order:
        notes = "\n\n---\n\n**Notes** *(Use Substack's native footnote feature: Cmd+Shift+8)*\n\n"
        for i, name in enumerate(ref_order, 1):
            body = definitions.get(name, "")
            notes += f"{to_superscript(i)} {body}\n\n"
        text = text.rstrip() + notes

    return text


# ---------------------------------------------------------------------------
# Math
# ---------------------------------------------------------------------------

def convert_math(text: str) -> str:
    """Wrap $$...$$ and $...$ in [LATEX: ...] markers."""
    # Block math first (greedy across lines)
    text = re.sub(
        r"\$\$(.*?)\$\$",
        lambda m: f"[LATEX_BLOCK: {m.group(1).strip()}]",
        text,
        flags=re.DOTALL,
    )
    # Inline math (non-greedy, single line)
    # Require first char after $ to not be a digit or space — avoids matching $100 dollar amounts
    text = re.sub(
        r"(?<!\$)\$(?!\$)(?!\d)(?! )(.+?)\$(?!\$)",
        lambda m: f"[LATEX: {m.group(1).strip()}]",
        text,
    )
    return text


# ---------------------------------------------------------------------------
# Image shortcodes
# ---------------------------------------------------------------------------

def resolve_image_urls(post_path: Path) -> dict[str, str]:
    """Build the site and extract hashed image URLs from the rendered HTML."""
    post_dir = post_path.parent.name
    project_root = post_path
    # Walk up to find the project root (where eleventy.config.js lives)
    while project_root.parent != project_root:
        if (project_root / "eleventy.config.js").exists():
            break
        project_root = project_root.parent

    rendered_html = project_root / "_site" / "blog" / post_dir / "index.html"
    if not rendered_html.exists():
        return {}

    html = rendered_html.read_text()
    soup = BeautifulSoup(html, "html.parser")
    mapping: dict[str, str] = {}
    for img in soup.find_all("img"):
        alt = img.get("alt", "")
        src = img.get("src", "")
        if alt and src:
            mapping[alt] = f"{SITE_URL}{src}"
    return mapping


def convert_images(text: str, post_path: Path) -> str:
    """Convert {% image %} shortcodes to standard markdown images."""
    # Resolve actual hashed URLs from the built site
    url_map = resolve_image_urls(post_path)

    def image_replacer(m: re.Match) -> str:
        src = m.group(1).strip().strip("\"'")
        alt = m.group(2).strip().strip("\"'")
        if alt in url_map:
            img_url = url_map[alt]
        else:
            # Fallback: flag for manual resolution
            img_url = f"[IMAGE URL NOT FOUND — upload {Path(src).name} manually]"
            print(f"  ⚠ Could not resolve image URL for \"{alt}\" ({src})")
        return f"![{alt}]({img_url})"

    # Match {% image "src", "alt" %} with optional extra args
    text = re.sub(
        r"\{%\s*image\s+\"([^\"]+)\"\s*,\s*\"([^\"]*)\"\s*(?:,\s*[^%]*)?\s*%\}",
        image_replacer,
        text,
    )
    return text


# ---------------------------------------------------------------------------
# Nunjucks stripping
# ---------------------------------------------------------------------------

def strip_nunjucks(text: str) -> str:
    """Remove remaining Nunjucks tags like {% ... %} and {{ ... }}."""
    text = re.sub(r"\{%.*?%\}", "", text)
    text = re.sub(r"\{\{.*?\}\}", "", text)
    return text


def strip_html_artifacts(text: str) -> str:
    """Remove <script> blocks, HTML comments, and stray closing tags."""
    # Remove <script>...</script> blocks
    text = re.sub(r"<script.*?>.*?</script>", "", text, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Remove stray closing tags like </div>
    text = re.sub(r"</?(div|span|button)[^>]*>", "", text, flags=re.IGNORECASE)
    return text


# ---------------------------------------------------------------------------
# Tables — detection and conversion
# ---------------------------------------------------------------------------

def is_interactive_html_table(table_html: str, full_text: str) -> bool:
    """Check if an HTML table contains interactive elements."""
    soup = BeautifulSoup(table_html, "html.parser")
    if soup.find(["input", "select", "textarea", "button"]):
        return True
    return False


def html_table_to_df(table_html: str) -> pd.DataFrame:
    """Parse a static HTML table into a DataFrame."""
    dfs = pd.read_html(io.StringIO(table_html))
    if not dfs:
        raise ValueError("No table found in HTML")
    return dfs[0]


def markdown_table_to_df(table_text: str) -> pd.DataFrame:
    """Parse a markdown pipe table into a DataFrame."""
    lines = [l.strip() for l in table_text.strip().splitlines() if l.strip()]
    if len(lines) < 2:
        raise ValueError("Not enough lines for a markdown table")

    def parse_row(line: str) -> list[str]:
        cells = [c.strip() for c in line.strip("|").split("|")]
        return cells

    header = parse_row(lines[0])
    # Skip separator line (line with dashes)
    data_lines = [l for l in lines[2:] if not re.match(r"^\|?[\s\-:|]+\|?$", l)]
    rows = [parse_row(l) for l in data_lines]
    return pd.DataFrame(rows, columns=header)


def find_markdown_tables(text: str) -> list[tuple[str, int, int]]:
    """Find markdown pipe tables. Returns list of (table_text, start, end)."""
    pattern = re.compile(
        r"((?:^\|.+\|[ \t]*\n){2,}(?:^\|.+\|[ \t]*$)?)",
        re.MULTILINE,
    )
    results = []
    for m in pattern.finditer(text):
        table = m.group(0)
        # Verify it has a separator line
        lines = table.strip().splitlines()
        if len(lines) >= 2 and re.match(r"^\|[\s\-:|]+\|$", lines[1].strip()):
            results.append((table, m.start(), m.end()))
    return results


def find_html_tables(text: str) -> list[tuple[str, int, int]]:
    """Find HTML <table>...</table> blocks. Returns list of (html, start, end)."""
    results = []
    pattern = re.compile(r"<table.*?>.*?</table>", re.DOTALL | re.IGNORECASE)
    for m in pattern.finditer(text):
        results.append((m.group(0), m.start(), m.end()))
    return results


def has_nearby_script(text: str, table_end: int) -> bool:
    """Check if there's a <script> tag associated with this table region."""
    # Look for script tags after the table (within a reasonable distance or at end)
    remaining = text[table_end:]
    # If there's a script tag before the next major section, it's likely interactive
    next_section = re.search(r"\n## ", remaining)
    search_region = remaining[:next_section.start()] if next_section else remaining
    return "<script>" in search_region.lower()


# ---------------------------------------------------------------------------
# Datawrapper API
# ---------------------------------------------------------------------------

class DatawrapperClient:
    def __init__(self, token: str) -> None:
        self.client = httpx.Client(
            base_url=DW_API,
            headers={"Authorization": f"Bearer {token}"},
            timeout=30.0,
        )

    def create_chart(self, title: str) -> str:
        """Create a Datawrapper table chart, return chart ID."""
        resp = self.client.post(
            "/charts",
            json={"title": title, "type": "tables"},
        )
        resp.raise_for_status()
        return resp.json()["id"]

    def upload_data(self, chart_id: str, csv_data: str) -> None:
        """Upload CSV data to a chart."""
        resp = self.client.put(
            f"/charts/{chart_id}/data",
            content=csv_data.encode("utf-8"),
            headers={"Content-Type": "text/csv"},
        )
        resp.raise_for_status()

    def publish(self, chart_id: str) -> str:
        """Publish the chart and return the embed URL."""
        resp = self.client.post(f"/charts/{chart_id}/publish")
        resp.raise_for_status()
        data = resp.json()
        # The public URL follows this pattern
        return data.get("data", {}).get("metadata", {}).get(
            "publish", {}
        ).get("embed-url", f"https://datawrapper.dwcdn.net/{chart_id}/1/")

    def close(self) -> None:
        self.client.close()


def load_cache(post_path: Path) -> dict[str, str]:
    """Load Datawrapper chart ID cache for a post."""
    cache_path = post_path.with_name(post_path.stem + "_datawrapper.json")
    if cache_path.exists():
        return json.loads(cache_path.read_text())
    return {}


def save_cache(post_path: Path, cache: dict[str, str]) -> None:
    """Save Datawrapper chart ID cache."""
    cache_path = post_path.with_name(post_path.stem + "_datawrapper.json")
    cache_path.write_text(json.dumps(cache, indent=2))


def df_to_cache_key(df: pd.DataFrame) -> str:
    """Create a stable cache key from a DataFrame's content."""
    return df.to_csv(index=False).strip()


# ---------------------------------------------------------------------------
# Main table replacement logic
# ---------------------------------------------------------------------------

def process_tables(
    text: str,
    post_title: str,
    post_path: Path,
    dry_run: bool,
) -> str:
    """Find and replace all tables with Datawrapper embeds."""
    dw_client: DatawrapperClient | None = None
    cache: dict[str, str] = {}

    if not dry_run:
        load_dotenv()
        token = os.getenv("DATAWRAPPER_TOKEN")
        if not token:
            print("ERROR: DATAWRAPPER_TOKEN not found in .env", file=sys.stderr)
            print("Tables will be left as-is. Set the token and re-run.", file=sys.stderr)
            return text
        dw_client = DatawrapperClient(token)
        cache = load_cache(post_path)

    table_num = 0
    replacements: list[tuple[int, int, str]] = []

    # --- HTML tables ---
    for table_html, start, end in find_html_tables(text):
        table_num += 1
        if is_interactive_html_table(table_html, text) or has_nearby_script(text, end):
            print(f"  ⚠ Table {table_num}: Interactive HTML table — skipping")
            replacements.append((start, end, f"<!-- INTERACTIVE TABLE {table_num} — manually handle for Substack -->"))
            continue

        try:
            df = html_table_to_df(table_html)
        except Exception as e:
            print(f"  ⚠ Table {table_num}: Failed to parse HTML table — {e}")
            continue

        csv_data = df.to_csv(index=False)
        cache_key = csv_data.strip()
        chart_title = f"{post_title} — Table {table_num}"

        if dry_run:
            print(f"  Table {table_num} (HTML, {len(df)} rows): would upload to Datawrapper as \"{chart_title}\"")
            preview = df.to_string(index=False, max_rows=4)
            print(f"    Preview:\n    {preview.replace(chr(10), chr(10) + '    ')}")
            replacements.append((start, end, f"[DATAWRAPPER EMBED — Table {table_num}: \"{chart_title}\"]"))
        else:
            if cache_key in cache:
                chart_id = cache[cache_key]
                print(f"  Table {table_num}: Using cached chart {chart_id}")
            else:
                chart_id = dw_client.create_chart(chart_title)
                dw_client.upload_data(chart_id, csv_data)
                embed_url = dw_client.publish(chart_id)
                cache[cache_key] = chart_id
                print(f"  Table {table_num}: Created chart {chart_id}")

            embed_url = f"https://datawrapper.dwcdn.net/{cache[cache_key]}/1/"
            replacements.append((start, end, embed_url))

    # --- Markdown tables ---
    for table_text, start, end in find_markdown_tables(text):
        table_num += 1
        try:
            df = markdown_table_to_df(table_text)
        except Exception as e:
            print(f"  ⚠ Table {table_num}: Failed to parse markdown table — {e}")
            continue

        csv_data = df.to_csv(index=False)
        cache_key = csv_data.strip()
        chart_title = f"{post_title} — Table {table_num}"

        if dry_run:
            print(f"  Table {table_num} (Markdown, {len(df)} rows): would upload to Datawrapper as \"{chart_title}\"")
            preview = df.to_string(index=False, max_rows=4)
            print(f"    Preview:\n    {preview.replace(chr(10), chr(10) + '    ')}")
            replacements.append((start, end, f"[DATAWRAPPER EMBED — Table {table_num}: \"{chart_title}\"]"))
        else:
            if cache_key in cache:
                chart_id = cache[cache_key]
                print(f"  Table {table_num}: Using cached chart {chart_id}")
            else:
                chart_id = dw_client.create_chart(chart_title)
                dw_client.upload_data(chart_id, csv_data)
                embed_url = dw_client.publish(chart_id)
                cache[cache_key] = chart_id
                print(f"  Table {table_num}: Created chart {chart_id}")

            embed_url = f"https://datawrapper.dwcdn.net/{cache[cache_key]}/1/"
            replacements.append((start, end, embed_url))

    # Apply replacements in reverse order to preserve positions
    replacements.sort(key=lambda r: r[0], reverse=True)
    for start, end, replacement in replacements:
        text = text[:start] + replacement + text[end:]

    if not dry_run and dw_client:
        save_cache(post_path, cache)
        dw_client.close()

    return text


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------

def transform(text: str, post_path: Path, dry_run: bool) -> str:
    """Run all transformations on the post content."""
    fm, body = strip_frontmatter(text)
    title = fm.get("title", post_path.stem)

    print(f"Post: {title}")
    print(f"Processing tables...")
    body = process_tables(body, title, post_path, dry_run)

    print("Converting images...")
    body = convert_images(body, post_path)

    print("Converting math...")
    body = convert_math(body)

    print("Converting footnotes...")
    body = convert_footnotes(body)

    print("Stripping Nunjucks and HTML artifacts...")
    body = strip_nunjucks(body)
    body = strip_html_artifacts(body)

    # Clean up excessive blank lines
    body = re.sub(r"\n{4,}", "\n\n\n", body)

    return body.strip() + "\n"


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def markdown_to_html(text: str) -> str:
    """Convert the prepared markdown to an HTML page for rich-text copy-paste."""
    body_html = md_lib.markdown(text, extensions=["extra"])
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, Georgia, serif; max-width: 680px; margin: 2em auto; padding: 0 1em; line-height: 1.6; color: #1a1a1a; }}
  img {{ max-width: 100%; height: auto; }}
  a {{ color: #0366d6; }}
  hr {{ border: none; border-top: 1px solid #ddd; margin: 2em 0; }}
  p {{ margin: 1em 0; }}
</style>
</head>
<body>
{body_html}
</body>
</html>"""


def main() -> None:
    args = parse_args()

    if not args.post.exists():
        print(f"Error: {args.post} not found.", file=sys.stderr)
        sys.exit(1)

    text = args.post.read_text()
    result = transform(text, args.post, args.dry_run)

    # Determine output paths
    if args.output:
        out_path = args.output
    else:
        out_path = args.post.with_name(args.post.stem + "_substack.md")
    html_path = out_path.with_suffix(".html")

    # Write markdown
    out_path.write_text(result)
    print(f"\nMarkdown written to: {out_path}")

    # Write HTML for rich-text copy-paste
    html_content = markdown_to_html(result)
    html_path.write_text(html_content)
    print(f"HTML written to: {html_path}")

    if not args.no_copy:
        try:
            # Copy rich HTML to macOS clipboard so Cmd+V pastes formatted text
            hex_data = subprocess.run(
                ["xxd", "-p", str(html_path.resolve())],
                capture_output=True, text=True, check=True,
            ).stdout.replace("\n", "")
            subprocess.run(
                ["osascript", "-e", f'set the clipboard to «data HTML{hex_data}»'],
                check=True,
            )
            print("Rich text copied to clipboard — paste directly into Substack.")
        except Exception as e:
            print(f"Could not copy to clipboard: {e}")
            print("Open the HTML file manually and copy from there.")

    if args.open:
        webbrowser.open(f"file://{html_path.resolve()}")


if __name__ == "__main__":
    main()
