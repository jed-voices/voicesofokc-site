#!/usr/bin/env python3
"""
Extract above-the-fold (critical) CSS rules from final-overrides.css.

Strategy:
- Always keep :root blocks (CSS custom properties everything depends on).
- Keep any rule whose selector list contains at least one critical token.
- Preserve @media blocks, keeping only the critical rules inside them
  (and dropping the @media block entirely if it has no critical rules).
- Keep @font-face and @import as-is (rare, but safe).

The full stylesheet still loads (deferred) after paint, so anything missed
here just resolves a beat later rather than breaking permanently.
"""
import re
import sys

SRC = "assets/css/final-overrides.css"
OUT = "assets/css/critical.css"

# Critical above-the-fold selector tokens. A rule is kept if any of its
# selectors contains one of these as a class/element token.
CRITICAL_TOKENS = [
    # Layout primitives
    ".container",
    # Skip link (a11y, top of DOM)
    ".skip-link",
    # Header
    ".site-header", ".header-inner", ".header-cta",
    ".brand", ".brand-mark", ".brand-lockup", ".brand-name", ".brand-tag",
    ".nav",
    # Hero (homepage)
    ".hero", ".hero-platform", ".hero-card", ".home-hero",
    ".hero-content", ".hero-copy", ".hero-media", ".hero-media-card",
    ".hero-panel", ".hero-episode-card", ".hero-episode-link",
    # Page intro (hero on inner pages)
    ".page-intro",
    # Headings + Azure rule
    ".title-xl", ".title-lg", ".title-md", ".title-with-rule", ".rule-target",
    ".episode-card-title",
    # Hero supporting text
    ".eyebrow", ".lede",
    # Buttons (hero CTAs)
    ".button", ".button-row", ".button-secondary", ".button-ghost",
    ".button-outline", ".button-primary",
    # Base typography elements often above the fold
    "body", "html", ":root",
]

def tokenize_selectors(selector_blob):
    """Split a selector list on commas into individual selectors."""
    return [s.strip() for s in selector_blob.split(",") if s.strip()]

def selector_is_critical(selector_blob):
    """True if any selector in the list contains a critical token."""
    # :root is always critical (variables)
    if ":root" in selector_blob:
        return True
    for sel in tokenize_selectors(selector_blob):
        for tok in CRITICAL_TOKENS:
            if tok == ":root":
                continue
            # Match the token as a whole class/element token boundary.
            # e.g. ".hero" should match ".hero", ".hero-content"? We want
            # word-ish boundaries: token followed by end, space, comma,
            # combinator, colon, bracket, or another dot is fine.
            # Simplest robust check: token present AND next char (if any)
            # is not an alphanumeric/hyphen that would make it a different class.
            idx = 0
            while True:
                pos = sel.find(tok, idx)
                if pos == -1:
                    break
                after = sel[pos + len(tok): pos + len(tok) + 1]
                # Acceptable boundary chars after the token
                if after == "" or after in " \t>+~:,.[)#":
                    return True
                idx = pos + 1
    return False

def parse_blocks(css):
    """
    Yield top-level constructs as (kind, header, body, raw).
    kind: 'at' for @media/@supports (has nested rules), 'rule' for normal,
          'atstatement' for @import/@charset (no block).
    This is a simple brace-depth parser (CSS has no nested braces except
    inside at-rules, which we handle).
    """
    i = 0
    n = len(css)
    while i < n:
        # skip whitespace
        while i < n and css[i] in " \t\r\n":
            i += 1
        if i >= n:
            break
        # comment
        if css[i:i+2] == "/*":
            end = css.find("*/", i+2)
            if end == -1:
                break
            i = end + 2
            continue
        # at-statement ending with ; (e.g. @import url(...);)
        if css[i] == "@":
            # find first of { or ;
            brace = css.find("{", i)
            semi = css.find(";", i)
            if semi != -1 and (brace == -1 or semi < brace):
                stmt = css[i:semi+1]
                yield ("atstatement", stmt, "", stmt)
                i = semi + 1
                continue
            # at-rule with block (@media, @supports, @font-face, @keyframes)
            header = css[i:brace].strip()
            # find matching close brace
            depth = 0
            j = brace
            while j < n:
                if css[j] == "{":
                    depth += 1
                elif css[j] == "}":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            body = css[brace+1:j]
            raw = css[i:j+1]
            yield ("at", header, body, raw)
            i = j + 1
            continue
        # normal rule: selector { ... }
        brace = css.find("{", i)
        if brace == -1:
            break
        header = css[i:brace].strip()
        depth = 0
        j = brace
        while j < n:
            if css[j] == "{":
                depth += 1
            elif css[j] == "}":
                depth -= 1
                if depth == 0:
                    break
            j += 1
        body = css[brace+1:j]
        raw = css[i:j+1]
        yield ("rule", header, body, raw)
        i = j + 1

def extract_critical(css):
    out = []
    for kind, header, body, raw in parse_blocks(css):
        if kind == "atstatement":
            # keep @import/@charset (safe, rare)
            out.append(raw)
        elif kind == "rule":
            if selector_is_critical(header):
                out.append(raw)
        elif kind == "at":
            at_name = header.split("(")[0].split("{")[0].strip().lower()
            if at_name.startswith("@font-face") or at_name.startswith("@keyframes"):
                # keep font-face/keyframes wholesale (safe)
                out.append(raw)
            elif at_name.startswith("@media") or at_name.startswith("@supports"):
                # recurse into the block, keep only critical inner rules
                inner = []
                for k2, h2, b2, r2 in parse_blocks(body):
                    if k2 == "rule" and selector_is_critical(h2):
                        inner.append(r2)
                    elif k2 == "atstatement":
                        inner.append(r2)
                if inner:
                    out.append(f"{header} {{\n" + "\n".join(inner) + "\n}")
            else:
                # unknown at-rule, keep to be safe
                out.append(raw)
    return "\n".join(out)

def main():
    with open(SRC, encoding="utf-8") as f:
        css = f.read()
    critical = extract_critical(css)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("/* Critical above-the-fold CSS, auto-extracted from final-overrides.css */\n")
        f.write("/* Do not edit by hand; regenerate via scripts/extract_critical_css.py */\n")
        f.write(critical)
        f.write("\n")
    print(f"Wrote {OUT}")
    print(f"Source size:   {len(css):,} bytes")
    print(f"Critical size: {len(critical):,} bytes")
    print(f"Reduction:     {100*(1-len(critical)/len(css)):.1f}% of final-overrides deferred")

if __name__ == "__main__":
    main()
