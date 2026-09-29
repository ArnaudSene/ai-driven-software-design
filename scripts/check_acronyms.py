#!/usr/bin/env python3
"""Check acronym usage across the guide.

Two rules are enforced on every Markdown file except the glossary itself:

1. Every all-caps token must be declared in docs/glossaire.md (or allow-listed).
2. The first prose occurrence (headings excluded) of each glossary acronym
   in a file must be
   expanded, i.e. immediately followed by "(" or written inside parentheses
   right after its long form, e.g. "intelligence artificielle (IA)".

Fenced code blocks, inline code spans and link targets are ignored, as are
stable identifiers such as BR-12 or ADR-0007.

Exit code is 1 when at least one violation is found.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "docs" / "glossaire.md"
ACRONYM_SECTION = "## 1. Acronymes"

# Tokens that look like acronyms but are file names or local numbering.
ALLOWLIST = {
    "README", "AGENTS", "CLAUDE", "ETAT", "CONTRIBUTING", "LICENSE", "SKILL",
    "AAAA", "MM", "JJ",  # date placeholder: AAAA-MM-JJ
}
ALLOWLIST_PATTERNS = [
    re.compile(r"^G\d+$"),  # gates: G1..G11
    re.compile(r"^Q\d+$"),  # session question numbers: Q3.2
    re.compile(r"^E\d+$"),  # example suffix: BR-3.E2
]

GLOSSARY_ROW = re.compile(r"^\|\s*\*\*(?P<acr>[^*]+)\*\*\s*\|")
CAPS_TOKEN = re.compile(r"(?<![\w-])[A-Z][A-Z0-9]+(?![\w])")
IDENTIFIER_SUFFIX = re.compile(r"-(\d|n\b|x\b|nnnn\b|NNNN\b)")


def load_glossary() -> set[str]:
    """Read the bold first cells of the glossary's acronym section only."""
    acronyms = set()
    in_section = False
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = line.startswith(ACRONYM_SECTION)
            continue
        match = GLOSSARY_ROW.match(line)
        if in_section and match:
            acronyms.add(match.group("acr").strip())
    return acronyms


def strip_non_prose(text: str) -> str:
    """Blank out code and link targets while preserving line numbers."""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", " ", text)
    text = re.sub(r"\]\([^)]*\)", "]", text)
    # Emphasis markers would otherwise sit between an acronym and its expansion.
    return text.replace("*", "")


def is_identifier(text: str, end: int) -> bool:
    return bool(IDENTIFIER_SUFFIX.match(text, end))


def is_allowed(token: str, glossary: set[str]) -> bool:
    # Multi-word entries such as "PCI DSS" declare each of their parts.
    known = {part for acronym in glossary for part in acronym.split()}
    if token in known or token in ALLOWLIST:
        return True
    return any(p.match(token) for p in ALLOWLIST_PATTERNS)


def is_expanded(text: str, start: int, end: int) -> bool:
    after = text[end:end + 3]
    if re.match(r"\s?\(", after):
        return True
    before = text[max(0, start - 1):start]
    return before == "("


def is_heading(text: str, index: int) -> bool:
    """Headings are titles: the expansion is expected in the body below."""
    line_start = text.rfind("\n", 0, index) + 1
    return text.startswith("#", line_start)


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_file(path: Path, glossary: set[str]) -> list[str]:
    errors = []
    text = strip_non_prose(path.read_text(encoding="utf-8"))
    rel = path.relative_to(ROOT)

    for match in CAPS_TOKEN.finditer(text):
        token = match.group(0)
        if is_identifier(text, match.end()) or is_allowed(token, glossary):
            continue
        errors.append(f"{rel}:{line_of(text, match.start())}: undeclared acronym '{token}'")

    for acronym in sorted(glossary):
        pattern = re.compile(rf"(?<![\w-]){re.escape(acronym)}(?![\w])")
        for match in pattern.finditer(text):
            if is_identifier(text, match.end()) or is_heading(text, match.start()):
                continue
            if not is_expanded(text, match.start(), match.end()):
                errors.append(
                    f"{rel}:{line_of(text, match.start())}: first use of '{acronym}' is not expanded"
                )
            break
    return errors


def main() -> int:
    glossary = load_glossary()
    if not glossary:
        print(f"No acronym found in {GLOSSARY}", file=sys.stderr)
        return 1

    errors = []
    for path in sorted(ROOT.rglob("*.md")):
        if path == GLOSSARY or ".git" in path.parts:
            continue
        errors.extend(check_file(path, glossary))

    for error in errors:
        print(error)
    print(f"{len(errors)} violation(s), {len(glossary)} acronyms in glossary.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
