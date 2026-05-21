## Project Overview

Personal blog built with **Eleventy (11ty) v2.0.1**, deployed to GitHub Pages at `https://tristinb.github.io/`.

## Tech Stack

- **SSG**: Eleventy 2.0.1 (Nunjucks templates, Markdown content)
- **Styling**: Custom CSS with CSS variables, dark mode via `prefers-color-scheme`
- **Markdown**: markdown-it with plugins: mathjax3, footnotes, anchors, attrs
- **Images**: `@11ty/eleventy-img` (auto-generates avif/webp, lazy loading)
- **Code highlighting**: Prism.js (Okaidia theme)
- **Comments**: Utterances (GitHub-based)
- **Analytics**: Google Analytics GA4
- **Python/UV**: Jupyter notebooks for data analysis that feeds blog posts

## Dev Commands

```bash
npm start          # Dev server with live reload (includes drafts)
npm run build      # Production build (excludes drafts)
```

Python (for notebooks/analysis scripts):
```bash
uv run word_counter.py --file content/blog/post/post.md
uv run jupyter notebook
```

## Project Structure

```
content/              # All source content (Eleventy input dir)
  blog/               # Blog posts, each in own subdirectory
    {post}/
      {post}.md       # Post content
      figures/         # Post-specific images
      research/        # Research notes (gitignored)
  drafts/             # Draft posts (dev only, excluded from prod)
_includes/layouts/    # Nunjucks layouts: base.njk, home.njk, post.njk
_data/metadata.js     # Site metadata (title, URL, author info)
public/css/           # Stylesheets (index.css is main)
public/img/           # Static images
eleventy.config.js    # Main config
_site/                # Build output (gitignored)
```

## Key Files for Styling

- `STYLE.md` — **Primary design reference.** Read this before making any visual or layout change. It defines design philosophy, typography, color tokens, component rules, and what to avoid.
- `public/css/index.css` — Main stylesheet, CSS variables, dark mode, responsive design
- `_includes/layouts/base.njk` — HTML shell, header, footer, nav
- `_includes/layouts/post.njk` — Blog post layout (prev/next nav, comments)
- `_includes/layouts/home.njk` — Homepage layout
- `_includes/postslist.njk` — Reusable post listing component
- `bundle.css` / `bundle.js` — Additional inline bundles

## Content Workflow

1. **Ideas/Scratch**: Loose ideas and exploration live in `content/drafts/{post-name}/`. These may or may not be committed.
2. **Research**: Save findings to `{post-folder}/research/` (e.g., `content/blog/stablecoin_interest/research/`). This folder is gitignored.
3. **In Progress**: Once committed to a post, move it to `content/blog/{post-name}/` with `draft: True`. It's version controlled but excluded from production builds.
4. **Publishing**: Set `draft: False` in frontmatter to publish.

## Blog Post Conventions

Frontmatter format:
```yaml
---
title: Post Title
description: Brief description
date: YYYY-MM-DD
draft: False
tags: [tag1, tag2]
---
```

Image shortcode: `{% image "./figures/name.png", "Alt text" %}`

### Title Guidelines (policy/econ/data posts)

When reviewing titles, evaluate against these principles and suggest improvements — do not replace the title outright.

**Core principles:**
1. **Take a position** — titles make an argument, not describe a topic. "The dollar's rally is about oil" not "An analysis of dollar movements."
2. **Establish stakes immediately** — "why now?" should be answerable from the title alone.
3. **Be concrete** — proper nouns, numbers, named mechanisms. Avoid vague nouns (geopolitics, reform, stability).
4. **Use active verbs** — "collapses," "reshapes," "exposes" over "examines" or "considers."
5. **Earn the surprise** — counterintuitive or contrarian framing pulls readers in.

**Reliable formats:**
- **Bold Claim**: "Dollar Dominance Is Over."
- **Corrective**: "NATO Isn't as Strong as You Think."
- **Paradox**: "The Austerity That Grows Debt."
- **Data Hook**: "The Chart That Explains the Trade War."

**Avoid:** hedging qualifiers ("Some Possible Considerations"), passive constructions, "may/might" titles, questions with obvious answers, academic caution in the title.

## Deployment

Push to `main` → GitHub Actions builds → deploys `_site/` to `gh-pages` branch.

## Working With the User

- **Design/styling**: The user will ask for help making the site look sleeker. Preview changes with `npm start` and verify visually.
- **Research**: The user may ask research questions — use web search to find current information.
- **Writing feedback**: The user has two critique modes. In both cases, do NOT rewrite, restructure, or significantly alter prose. Respect their voice. Provide targeted inline suggestions, not sweeping changes.
  - **Grammar check**: Quick pass for obvious mechanical issues only — incomplete sentences, misspellings, misused words, missing punctuation, subject-verb agreement. Flag each issue with the original text and a suggested fix. Do not touch style or word choice.
  - **Strunk & White check**: Deeper edit focused on vigorous, concise writing per *The Elements of Style*. Omit needless words. Prefer active voice. Use definite, specific, concrete language. Replace weak verbs. Cut hedging and qualifiers. Flag each suggestion with the original text, the proposed revision, and the Strunk & White principle it addresses.
