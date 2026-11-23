#!/usr/bin/env python3
"""Check that every local reference in the guide resolves.

The guide exists in two language trees that share their file names: English
at the repository root, French under fr/. In each tree, three kinds of
reference are checked:

1. Markdown links to a local file: the file exists, and an anchor names a
   heading of that file, spelled the way GitHub builds heading anchors.
2. Guide paths written in code spans (`docs/...`, `prompts/...`,
   `templates/...`): the file exists in the tree.
3. The `reads:` list in a prompt's front matter, which is what an agent
   opens: each path exists in the tree.

Fenced code blocks and URLs are ignored. Exit code is 1 when at least one
reference does not resolve.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class Tree:
    """A language version of the guide: where its paths resolve, and its files."""

    name: str
    root: Path
    readme: Path

    def files(self) -> list[Path]:
        if self.root == ROOT:
            found = [
                p for p in ROOT.rglob("*.md")
                if "fr" not in p.relative_to(ROOT).parts[:1]
                and p.name != "README.fr.md"
            ]
        else:
            found = list(self.root.rglob("*.md"))
            if self.readme.exists():
                found.append(self.readme)
        return sorted(p for p in found if ".git" not in p.parts)


TREES = [
    Tree("en", ROOT, ROOT / "README.md"),
    Tree("fr", ROOT / "fr", ROOT / "README.fr.md"),
]

FENCE = re.compile(r"^(```|~~~)")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CODE_PATH = re.compile(r"`((?:docs|prompts|templates)/[^`\s]+\.(?:md|ya?ml))`")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_ANCHOR = re.compile(r"<a\s+(?:id|name)=\"([^\"]+)\"")
PLACEHOLDER = re.compile(r"[<>*{}]|\bnn\b|\.\.\.")


def prose_lines(text: str) -> list[tuple[int, str]]:
    """Lines outside fenced code blocks, with their line numbers."""
    lines, fenced = [], False
    for number, line in enumerate(text.splitlines(), start=1):
        if FENCE.match(line.strip()):
            fenced = not fenced
            continue
        if not fenced:
            lines.append((number, line))
    return lines


def slug(heading: str) -> str:
    """GitHub's heading anchor: rendered text, lower-cased, punctuation dropped."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    text = text.replace("`", "").replace("*", "")
    text = text.strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def anchors(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    if path not in cache:
        found, seen = set(), {}
        for _, line in prose_lines(path.read_text(encoding="utf-8")):
            heading = HEADING.match(line)
            if heading:
                base = slug(heading.group(2))
                count = seen.get(base, 0)
                seen[base] = count + 1
                found.add(base if count == 0 else f"{base}-{count}")
            found.update(HTML_ANCHOR.findall(line))
        cache[path] = found
    return cache[path]


def front_matter_reads(text: str) -> list[str]:
    """The paths a prompt's front matter lists under `reads:`."""
    if not text.startswith("---\n"):
        return []
    end = text.find("\n---", 4)
    if end < 0:
        return []
    block = text[4:end].splitlines()
    paths: list[str] = []
    for i, line in enumerate(block):
        if not line.startswith("reads:"):
            continue
        inline = line[len("reads:"):].strip()
        if inline.startswith("["):
            paths.extend(p.strip() for p in inline.strip("[]").split(","))
        else:
            for item in block[i + 1:]:
                if not item.startswith(("  -", "- ")):
                    break
                paths.append(item.split("-", 1)[1])
    unquoted = (p.strip().strip("\"'") for p in paths)
    return [p for p in unquoted if p and not PLACEHOLDER.search(p)]


COUNTS = {"links": 0, "anchors": 0, "code paths": 0, "reads": 0}


def check_file(tree: Tree, path: Path, cache: dict[Path, set[str]]) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)

    for number, line in prose_lines(text):
        for target in LINK.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue
            COUNTS["links"] += 1
            file_part, _, anchor = target.partition("#")
            linked = (path.parent / file_part).resolve() if file_part else path
            if not linked.exists():
                errors.append(f"{rel}:{number}: link to missing file '{target}'")
                continue
            if anchor and linked.suffix == ".md":
                COUNTS["anchors"] += 1
            if anchor and linked.suffix == ".md" and anchor not in anchors(linked, cache):
                errors.append(f"{rel}:{number}: link to missing anchor '{target}'")
        for guide_path in CODE_PATH.findall(line):
            if PLACEHOLDER.search(guide_path):
                continue
            COUNTS["code paths"] += 1
            if not (tree.root / guide_path).exists():
                errors.append(f"{rel}:{number}: guide path '{guide_path}' does not exist")

    for guide_path in front_matter_reads(text):
        COUNTS["reads"] += 1
        if not (tree.root / guide_path).exists():
            errors.append(f"{rel}: front matter reads '{guide_path}', which does not exist")
    return errors


def main() -> int:
    errors, checked = [], 0
    cache: dict[Path, set[str]] = {}
    for tree in TREES:
        if not tree.root.is_dir():
            continue
        for path in tree.files():
            checked += 1
            errors.extend(check_file(tree, path, cache))
    for error in errors:
        print(error)
    counted = ", ".join(f"{n} {kind}" for kind, n in COUNTS.items())
    print(f"{len(errors)} broken reference(s) in {checked} file(s); checked {counted}.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
