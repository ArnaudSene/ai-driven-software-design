#!/usr/bin/env python3
"""Check acronym usage across the guide.

The guide exists in two language trees, English at the repository root and
French under fr/, each with its own glossary: an English acronym is not always
the French one (AI and IA). Two rules are enforced on every Markdown file of a
tree except its glossary:

1. Every all-caps token must be declared in that tree's glossary (or
   allow-listed).
2. The first prose occurrence (headings excluded) of each glossary acronym
   in a file must be
   expanded, i.e. immediately followed by "(" or written inside parentheses
   right after its long form, e.g. "artificial intelligence (AI)".

Fenced code blocks, inline code spans and link targets are ignored, as are
stable identifiers such as BR-12 or ADR-0007.

Exit code is 1 when at least one violation is found.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Tree:
    """A language version of the guide: its glossary and its files."""

    name: str
    root: Path
    readme: Path
    acronym_section: str

    @property
    def glossary(self) -> Path:
        return self.root / "docs" / "glossary.md"

    def files(self) -> list[Path]:
        if self.root == ROOT:
            found = [
                p for p in ROOT.rglob("*.md")
                if p.relative_to(ROOT).parts[0] != "fr" and p.name != "README.fr.md"
            ]
        else:
            found = list(self.root.rglob("*.md"))
            if self.readme.exists():
                found.append(self.readme)
        return sorted(p for p in found if ".git" not in p.parts and p != self.glossary)


TREES = [
    Tree("en", ROOT, ROOT / "README.md", "## 1. Acronyms"),
    Tree("fr", ROOT / "fr", ROOT / "README.fr.md", "## 1. Acronymes"),
]

# Tokens that look like acronyms but are file names or local numbering.
ALLOWLIST = {
    "README", "AGENTS", "CLAUDE", "STATE", "CONTRIBUTING", "LICENSE", "SKILL",
    "AAAA", "MM", "JJ",  # French date placeholder: AAAA-MM-JJ
    "YYYY", "DD",  # English date placeholder: YYYY-MM-DD
}
ALLOWLIST_PATTERNS = [
    re.compile(r"^G\d+$"),  # gates: G1..G12
    re.compile(r"^Q\d+$"),  # session question numbers: Q3.2
    re.compile(r"^E\d+$"),  # example suffix: BR-3.E2
]

GLOSSARY_ROW = re.compile(r"^\|\s*\*\*(?P<acr>[^*]+)\*\*\s*\|")
CAPS_TOKEN = re.compile(r"(?<![\w-])[A-Z][A-Z0-9]+(?![\w])")
IDENTIFIER_SUFFIX = re.compile(r"-(\d|n\b|x\b|nnnn\b|NNNN\b)")


def load_glossary(tree: Tree) -> set[str]:
    """Read the bold first cells of the glossary's acronym section only."""
    acronyms = set()
    in_section = False
    for line in tree.glossary.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            in_section = line.startswith(tree.acronym_section)
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
    errors, summary = [], []
    for tree in TREES:
        if not tree.glossary.exists():
            print(f"No glossary at {tree.glossary.relative_to(ROOT)}", file=sys.stderr)
            return 1
        glossary = load_glossary(tree)
        if not glossary:
            print(f"No acronym found in {tree.glossary.relative_to(ROOT)}", file=sys.stderr)
            return 1
        files = tree.files()
        for path in files:
            errors.extend(check_file(path, glossary))
        summary.append(f"{tree.name}: {len(files)} files, {len(glossary)} acronyms")

    for error in errors:
        print(error)
    print(f"{len(errors)} violation(s); {'; '.join(summary)}.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
