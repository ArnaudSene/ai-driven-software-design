#!/usr/bin/env python3
"""Check that the French translation follows the current English guide.

English, at the repository root, is the authoritative version; fr/ holds its
French translation under the same file names (README.md is translated as
README.fr.md, beside it). The manifest fr/translated-from.sha256 records, for
each English file, the SHA-256 of the version its translation was last brought
up to date with. It uses the sha256sum format, so `shasum -a 256 -c
fr/translated-from.sha256`, run from the repository root, lists the English
files that changed since.

The check fails when:

1. an English file has no French counterpart, or a French file no English one;
2. an English file is missing from the manifest;
3. an English file no longer matches its recorded hash: it changed, and its
   translation has not been brought up to date since;
4. the manifest names a file that does not exist, or has a malformed line.

Once a translation is brought up to date, record it:

    python3 scripts/check_translation.py --stamp docs/00-principles.md

--stamp takes English or French paths, and checks the whole guide afterwards.
Exit code is 1 when at least one problem is found.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FRENCH = ROOT / "fr"
MANIFEST = FRENCH / "translated-from.sha256"
TRANSLATED_DIRS = ("docs", "prompts", "templates")
TRANSLATED_FILES = ("AGENTS.md", "README.md")
ENTRY = re.compile(r"^([0-9a-f]{64})  (\S.*)$")


def visible_files(directory: Path) -> list[Path]:
    """Files under a directory, without hidden files or Python caches."""
    return [
        p for p in directory.rglob("*")
        if p.is_file()
        and not any(part.startswith(".") or part == "__pycache__"
                    for part in p.relative_to(ROOT).parts)
    ]


def english_files() -> list[str]:
    """The English files that have a translation, relative to the root."""
    found = [name for name in TRANSLATED_FILES if (ROOT / name).is_file()]
    for name in TRANSLATED_DIRS:
        found += [p.relative_to(ROOT).as_posix() for p in visible_files(ROOT / name)]
    return sorted(found)


def french_of(english: str) -> str:
    return "README.fr.md" if english == "README.md" else f"fr/{english}"


def english_of(french: str) -> str:
    return "README.md" if french == "README.fr.md" else french.removeprefix("fr/")


def french_files() -> list[str]:
    """The French files, relative to the root, without the manifest."""
    found = [p.relative_to(ROOT).as_posix() for p in visible_files(FRENCH) if p != MANIFEST]
    if (ROOT / "README.fr.md").is_file():
        found.append("README.fr.md")
    return sorted(found)


def digest(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def read_manifest(errors: list[str]) -> dict[str, str]:
    """English path -> recorded hash; malformed lines are reported."""
    recorded: dict[str, str] = {}
    if not MANIFEST.exists():
        return recorded
    rel = MANIFEST.relative_to(ROOT)
    for number, line in enumerate(MANIFEST.read_text(encoding="utf-8").splitlines(), start=1):
        entry = ENTRY.match(line)
        if not entry:
            errors.append(f"{rel}:{number}: malformed line, expected '<sha256>  <English path>'")
            continue
        recorded[entry.group(2)] = entry.group(1)
    return recorded


def write_manifest(recorded: dict[str, str]) -> None:
    lines = [f"{recorded[path]}  {path}\n" for path in sorted(recorded)]
    MANIFEST.write_text("".join(lines), encoding="utf-8")


def check() -> int:
    errors: list[str] = []
    english = english_files()
    french = set(french_files())
    recorded = read_manifest(errors)
    rel = MANIFEST.relative_to(ROOT)

    for path in english:
        translation = french_of(path)
        if translation not in french:
            errors.append(f"{path}: no French translation at {translation}")
            continue
        stamp = f"python3 scripts/check_translation.py --stamp {path}"
        if path not in recorded:
            errors.append(f"{translation}: not recorded in {rel}; once it follows {path}, run: {stamp}")
        elif recorded[path] != digest(path):
            errors.append(
                f"{translation}: behind {path}, which changed since the translation was last "
                f"brought up to date; update it (see git log -p -- {path}), then run: {stamp}"
            )
    for path in sorted(french - {french_of(p) for p in english}):
        errors.append(f"{path}: no English source at {english_of(path)}")
    for path in sorted(set(recorded) - set(english)):
        errors.append(f"{rel}: entry for {path}, which is not an English file of the guide")

    for error in errors:
        print(error)
    print(f"{len(errors)} problem(s); checked {len(english)} translated file(s).")
    return 1 if errors else 0


def relative_to_root(given: str) -> str:
    """A path given on the command line, from the current directory or the root."""
    path = Path(given)
    if not path.is_absolute():
        path = path if path.exists() else ROOT / path
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return given


def stamp(paths: list[str]) -> int:
    errors: list[str] = []
    recorded = read_manifest(errors)
    if errors:
        for error in errors:
            print(error)
        return 1
    english = set(english_files())
    for given in paths:
        relative = relative_to_root(given)
        source = english_of(relative) if relative in french_files() else relative
        if source not in english or not (ROOT / french_of(source)).is_file():
            print(f"{given}: not a translated file of the guide (English source and French translation)")
            return 1
        recorded[source] = digest(source)
        print(f"stamped {french_of(source)} as following {source}")
    write_manifest(recorded)
    return check()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--stamp", nargs="+", metavar="PATH",
        help="record that these translations follow the current English version",
    )
    args = parser.parse_args()
    return stamp(args.stamp) if args.stamp else check()


if __name__ == "__main__":
    sys.exit(main())
