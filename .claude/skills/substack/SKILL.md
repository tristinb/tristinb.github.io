---
name: substack
description: Convert a blog post to Substack format and copy rich text to clipboard.
argument-hint: <path-to-post>
user-invocable: true
allowed-tools: Bash, Read
---

Convert a blog post to Substack-ready rich text.

## Steps

1. Build the site first (needed for image URL resolution):
   ```bash
   npm run build
   ```
   If the build fails but the error is unrelated to the target post, proceed anyway.

2. Run the substack prep script on the provided file:
   ```bash
   uv run substack_prep.py <path-to-post>
   ```

3. The script copies rich text to the clipboard. Inform the user they can paste directly into Substack's editor.

4. Remind the user:
   - Replace superscript footnote markers with Substack's native footnotes (Cmd+Shift+8)
   - The generated `*_substack.md` and `*_substack.html` files are gitignored and can be deleted

## Usage

```
/substack content/blog/stablecoin_interest/stablecoin_interest.md
```
