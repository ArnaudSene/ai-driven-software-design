# 12 — Delivery plan — <Project name>

| Status | Version | Date | Gate |
|---|---|---|---|
| Draft | 0.1 | <YYYY-MM-DD> | G12: — |

## 1. Risks to address first

| Element (R-n, H-n, QS-n) | Criticality | Increment that addresses it |
|---|---|---|
| | | |

## 2. Walking skeleton — INC-0

| Element | Content |
|---|---|
| Minimal use case | |
| Layers crossed | |
| Modules created | BC-n → … |
| Delivery pipeline | |
| Observability | |
| Active fitness functions | FF-n |
| Authentication | |
| Decisions (ADR) validated by the skeleton | ADR-nnnn |

## 3. Increments

| Id | Title | Objective (BO-n) | Content (UC-n, BR-n, AC-n) | Risks reduced | Prerequisites (increments, open decisions (OD)) | Completion criterion |
|---|---|---|---|---|---|---|
| INC-1 | | | | | | Definition of "done" + … |

**Minimum viable product**: INC-0 to INC-n (to be specified).

## 4. Breakdown of the first increments

| Backlog item | Implements | Increment |
|---|---|---|
| | UC-n, BR-n, AC-n | INC-1 |

## 5. Development guidelines

Files created at the project root: `AGENTS.md` (guidelines) and `CLAUDE.md` (`@AGENTS.md`).

Expected structure of the project's `AGENTS.md`:

```markdown
# Development guidelines

## Design
- The design is authoritative: `<DESIGN_DIR>` (by default `design/`). Before coding a feature, read the relevant use cases (UC, Use Case), business rules (BR, Business Rule), acceptance criteria (AC, Acceptance Criterion), architecture decisions (ADR, Architecture Decision Record) and fitness functions (FF, Fitness Function).
- Any business ambiguity: stop and ask; propose an open decision (OD) in `design/STATE.md`.
- Any deviation from an architecture decision: propose a new ADR, never work around it silently.
- Never hard-code a value marked [threshold to be set]: make it configurable and flag it.

## Language
- Code names in English, consistent with `design/glossary.md`; no synonyms.

## Structure
- One module per bounded context: <list>.
- Dependency rules: <summary>; checked by <FF-n>.

## Traceability
- Tests: the name or tag cites the verified identifier (BR-7.E2, AC-11).
- Commits and pull requests: cite the identifiers delivered.

## Conventions
- Style, commits, branches, review: <…>
```

## 6. Overall consistency review

| # | Severity | Element | Objection | Decision |
|---|---|---|---|---|
| | | | | |
