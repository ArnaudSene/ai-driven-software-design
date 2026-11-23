# Phase 12 — Delivery plan and walking skeleton

| Key | Value |
|---|---|
| Central question | In what order should we build, and how do we start without risk? |
| Agent | [`prompts/tech-lead.md`](../prompts/tech-lead.md) |
| Inputs | All approved phases, the `OD-n` and `R-n` registers of `STATE.md` |
| Outputs | `design/12-delivery-plan.md`, development guidelines for coding agents, global consistency review |
| Identifiers created | `INC-n` |
| Template | [`templates/12-delivery-plan.md`](../templates/12-delivery-plan.md) |
| Gate | G12 — end of the initial design |

---

## 1. Why this phase

A design only has value if it turns into code without getting lost along the way. This phase:

1. splits delivery into **increments** that each bring an observable value;
2. puts first what **reduces the most risk**;
3. defines a **walking skeleton** that validates the architecture end to end before investing in features;
4. prepares the **guidelines** that the developers, human or AI (artificial intelligence) agents, will follow;
5. checks the **global consistency** of all the deliverables before closing the initial design.

## 2. Concepts and methods

### 2.1 Walking skeleton (`INC-0`)

The walking skeleton (Alistair Cockburn) is the **smallest implementation that crosses the whole architecture**: a trivial function, but one that goes through the interface, the domain, persistence and the delivery pipeline, all the way to a production-like environment.

Typical content of `INC-0`:

| Element | Example |
|---|---|
| A minimal use case | Create and read back a booking, without complex rules |
| All the layers | Interface → API (Application Programming Interface) → domain → database |
| A minimal screen | If the system has end users, one screen of a *Must* journey from phase 5, unpolished |
| Module structure | One module per `BC-n`, even empty ones, with their boundaries |
| Continuous integration (CI) and continuous delivery (CD) pipeline | Build, tests, analyses, automatic deployment to pre-production |
| Observability | Structured logs, one metric, one trace, one dashboard |
| Fitness functions | Dependency `FF-n` active and blocking |
| Security | Real authentication, even with a single role |
| Schema migration | First versioned migration |

The skeleton **validates the riskiest ADR** (Architecture Decision Record) entries at the lowest cost. If it reveals a problem, we go back to phase 6 or 7 (§ 14 of the principles): that is exactly its role.

### 2.2 Splitting into increments (`INC-n`)

Each increment is a **vertical slice**: it delivers one or more complete `UC-n`, with their `BR-n`, their `AC-n` and their tests, from the interface to the database.

Ordering criteria, in this order:

1. **Risk**: what can invalidate the architecture or the project first (integration with a poorly known third party, a difficult `QS-n`, a vague business rule).
2. **Value**: the *Must* `UC-n` that serve the main `BO-n`.
3. **Dependencies**: what unblocks the rest.
4. **Learning**: what makes it possible to check a hypothesis `H-n` with users early.

Story mapping (Jeff Patton) helps to visualize the split: the user's activities as columns, the increments as horizontal rows. The first complete row forms the MVP (Minimum Viable Product): the smallest version that lets you learn whether the product reaches its objectives.

Increment sheet:

| Section | Content |
|---|---|
| Identifier and title | `INC-3` Cancellation and credit notes |
| Objective | Value delivered, `BO-n` served |
| Content | `UC-n`, `BR-n`, `AC-n`, `IR-n`, `FF-n` and `SLO-n` concerned |
| Risks reduced | `R-n`, `H-n` verified |
| Prerequisites | Increments, `OD-n` to resolve before starting |
| Completion criterion | DoD (Definition of Done) from phase 11 + a criterion specific to the increment |

### 2.3 From use case to tasks

The `UC-n` are split into product backlog items (user stories) of reasonable size, following the INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable) criteria. Each item **must** cite the identifiers it implements.

Techniques for splitting a case that is too big: by scenario (main scenario first, extensions next), by rule, by data variant, by role, by level of automation (manual first).

### 2.4 Development guidelines

The design is translated into working rules, written in the code repository so that developers **and coding agents** apply them. The agent writes a guidelines file (`AGENTS.md` and, for Claude Code, `CLAUDE.md`) at the root of the project, which contains at least:

1. **Where the design is**: `design/`, and which files to read before working on a feature (the `BR-n`, `AC-n` and ADRs concerned).
2. **Language**: use the glossary's names; do not invent synonyms.
3. **Structure**: one module per `BC-n`; dependency rules (reference to the `FF-n`).
4. **Traceability**: tests and commit messages cite the identifiers (`BR-7`, `AC-11`); pull requests list the identifiers implemented.
5. **Deviations**: any necessary divergence from an ADR or a rule is handled through a proposed ADR or an OD (open decision), never silently in the code.
6. **Business values**: never hard-code a value marked [threshold to be set]; make it configurable and flag it.
7. **Conventions**: code style, commit conventions, branching strategy, code review.

### 2.5 Global consistency review

Before G12, the critical reviewer leads a cross-cutting review:

| Check | Method |
|---|---|
| Orphan elements | Walk through `traceability.md`: `UC-n` without a `BO-n`, *Must* `BR-n` without a test, `IR-n` without a screen or a test, *Must* `QS-n` without an ADR, `FF-n` or `SLO-n`, ADR without a requirement |
| Contradictions | Between `BR-n` and ADRs, between `QS-n` and topology, between data classification and security measures |
| Pending ODs | Each open OD has an owner, a due date, and the increment it blocks |
| Risks | Each open `R-n` has a response and an increment that addresses it |
| Glossary | Each term used in the deliverables appears in it |

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Ranks the `R-n`, the `H-n` and the difficult `QS-n` by criticality. | Confirms. |
| 2 | Defines `INC-0` (walking skeleton). | Approves. |
| 3 | Proposes the split into `INC-n` and their order, with a risk / value justification. | Reorders according to their priorities. |
| 4 | Delimits the MVP. | Decides. |
| 5 | Writes the development guidelines (the project's `AGENTS.md` / `CLAUDE.md`). | Reviews. |
| 6 | Leads the global consistency review with the critical reviewer. | Arbitrates the discrepancies. |
| 7 | Sets `STATE.md` to the status "initial design closed" and switches to phase 13. | Approves G12. |

## 4. Question bank

1. What is the very first thing real users should be able to do?
2. Which hypothesis do you want to check with users as early as possible?
3. Is there an imposed date (trade show, legal obligation, end of contract of a legacy system)?
4. Who will develop: a team, AI agents, both? Who will review the code?
5. What delivery and demonstration cadence do you want?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `12-delivery-plan.md` | `INC-0`, ordered `INC-n`, MVP, split of the first increments into stories, result of the consistency review |
| `AGENTS.md` / `CLAUDE.md` (project root) | Development guidelines |
| `STATE.md` | Initial design closed, remaining ODs and risks with due dates |

## 6. Gate G12 checklist

- [ ] ★ `INC-0` crosses all the layers and the delivery pipeline.
- [ ] ★ Each *Must* `UC-n` is assigned to an increment.
- [ ] ★ The development guidelines exist in the project's repository.
- [ ] ★ The global consistency review leaves no untreated *Must* orphan.
- [ ] The order of the increments is justified by risk and value.
- [ ] Each open OD has an owner, a due date and an identified blocked increment.
- [ ] The MVP is delimited.
- [ ] The first increments are split into items that meet the INVEST criteria.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Horizontal slicing | "Increment 1: the database; increment 2: the API; increment 3: the interface" | Vertical slices that each bring value. |
| Fun first | The easy, visible features first, the risks at the end | Risk comes before value in the ordering. |
| Forgotten skeleton | Features developed before the delivery pipeline exists | `INC-0` first, always. |
| Abandoned design | `design/` never reread once coding has started | Development guidelines and phase 13. |
