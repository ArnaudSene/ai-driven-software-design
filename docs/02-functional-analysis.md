# Phase 2 — Functional analysis

| Key | Value |
|---|---|
| Central question | What must the system do? |
| Agent | [`prompts/business-analyst.md`](../prompts/business-analyst.md) |
| Inputs | `01-scoping.md` approved (G1), `glossary.md`, business documents |
| Outputs | `design/02-functional-requirements.md`, enriched `glossary.md`, `traceability.md` |
| Identifiers created | `UC-n`, `BR-n`, `BR-n.Ek`, `AC-n`, `IR-n`, `OD-n` |
| Template | [`templates/02-functional-requirements.md`](../templates/02-functional-requirements.md) |
| Gate | G2 |

---

## 1. Why this phase

It turns an intention ("manage bookings") into a **verifiable** set of expected behaviors. At the end of this phase, it must be possible to write the acceptance tests **before** a single tool has been chosen.

The success criterion is simple: if two teams read the requirements, they must produce systems that behave the same way on every example.

## 2. Concepts and methods

### 2.1 The three levels of functional requirement

| Level | Identifier | Answers | Example |
|---|---|---|---|
| Use case | `UC-n` | What goal does an actor achieve with the system? | `UC-3`: a customer cancels a booking. |
| Business rule | `BR-n` | What rule does the system apply, whatever the case? | `BR-7`: a cancellation less than 24 h before the slot is not refunded. |
| Acceptance criterion | `AC-n` | Under what condition is the use case considered delivered? | `AC-11`: given a booking three days ahead, when the customer cancels, then they receive a credit note and the slot becomes free again. |

A business rule is **cross-cutting**: `BR-7` applies to cancellation by the customer (`UC-3`) just as it does to cancellation by an advisor (`UC-8`). It is therefore written once and referenced from the use cases.

### 2.2 Use cases (`UC-n`)

Format inspired by Alistair Cockburn, at the "user goal" level (a task that an actor accomplishes in one sitting and that brings them value):

| Section | Content |
|---|---|
| Primary actor | An `SH-n` or an external system |
| Goal | What the actor wants to obtain, in one sentence |
| Business objective | `BO-n` served |
| Preconditions | What is true before |
| Success guarantees | What is true after a success |
| Minimal guarantees | What remains true even in case of failure (nothing is half-saved, for example) |
| Main success scenario | Numbered steps, alternating between the actor and the system |
| Extensions | Variants and errors, numbered after the step they branch from (`3a`, `3b`) |
| Rules applied | `BR-n` |
| Priority | *Must*, *Should*, *Could* or *Won't* |

User stories ("As a…, I want…, so that…") can complement the use cases when the work is split up in phase 12. They do not replace them: a story describes neither the errors nor the guarantees.

### 2.3 Business rules (`BR-n`)

Each rule carries the six fields of [00-principles § 7.1](00-principles.md#71-structure-of-a-rule): Rule, Fit criterion, Examples, Source, Rationale, Priority.

Full example:

```markdown
### BR-7 — Late cancellation not refunded

- **Rule**: If a customer cancels a booking less than [threshold to be set: 24 h?] before the start
  of the slot, then the system must issue neither a refund nor a credit note.
- **Fit criterion**: for any cancellation whose timestamp is strictly later than
  (start of the slot − time limit), the amount refunded is 0 and no credit note is created.
- **Examples**:
  - BR-7.E1 (nominal) — Slot on March 10 at 14:00, cancellation on March 9 at 13:59 → full credit note.
  - BR-7.E2 (boundary) — Same slot, cancellation on March 9 at 14:00:00 → full credit note (bound included?) → OD-3
  - BR-7.E3 (failure) — Cancellation on March 10 at 09:00 → no credit note.
- **Source**: SH-2 (branch manager), interview on 2026-10-01; terms and conditions § 4.
- **Rationale**: a slot released late can no longer be resold.
- **Priority**: Must — a refund error is financial and silent (C-4).
- **Use cases**: UC-3, UC-8.
```

Note: the time limit stays **[threshold to be set]** until the decision-maker has confirmed it, and the question of the bound (included or excluded?) becomes an OD (open decision) instead of being settled at random by the AI (artificial intelligence) or by the developer.

### 2.4 Example Mapping

Matt Wynne's technique for bringing rules and examples to light in a workshop. One use case (or one story) is worked on at a time, with four types of cards:

| Card | Customary color | Becomes |
|---|---|---|
| The story or case under study | Yellow | `UC-n` |
| A rule | Blue | `BR-n` |
| A concrete example, with real values | Green | `BR-n.Ek` or `AC-n` |
| An unanswered question | Red | `OD-n` |

Reading heuristics:

- Many red cards: the subject is not mature; the business must be questioned before going further.
- Many blue cards: the case is too big; it must be split.
- A rule without an example: it is not understood.

The AI simulates the workshop: for each `UC-n`, it **proposes** rules and concrete examples, and above all **boundary examples** (bounds, null values, duplicates, concurrency, cancellation in the middle of processing), then the decision-maker confirms, corrects or turns them into a question.

### 2.5 Acceptance criteria (`AC-n`)

Written in the *Given / When / Then* format (Gherkin) so that they can be carried directly into automated tests in phase 11. Their language follows golden rule 13. Run by a BDD (Behavior-Driven Development) tool, a scenario is code and is written in English, as below. Kept as a document, it follows the language of the deliverables; in a language other than English, its first line is the `# language: <code>` directive (for example `# language: fr`), without which Gherkin tools do not recognize the keywords:

```gherkin
# AC-11 — verifies UC-3, BR-7
Given a booking confirmed for March 10 at 14:00
  And it is March 7 at 10:00
When the customer cancels the booking
Then a credit note of €45.00 is issued
  And the slot on March 10 at 14:00 is available again
```

### 2.6 Functional supplements

Depending on the project, the phase also covers:

| Supplement | Form |
|---|---|
| Life cycle of business objects | State diagram (Mermaid `stateDiagram`) for each object that has states: order, case file, contract |
| Cross-cutting business processes | Activity or sequence diagram when a process spans several use cases |
| Roles and permissions | Role × action matrix (who can do what). The technical mechanisms come in phase 9. |
| Notifications | Triggering event, recipient, channel, content |
| Documents and reports | Content, recipient, frequency |
| User journeys | For each user group, the sequence of its activities, linked to the `UC-n`, in the manner of a *story map* (Jeff Patton). The screens and their sketches are designed in phase 5. |
| Data migration | Existing data to migrate and transformation rules |

### 2.7 Interaction requirements (`IR-n`)

For each use case whose actor is human, write what the user **must be able to do or see**, never what the screen looks like. Format and rules: [00-principles § 7.4](00-principles.md#74-interaction-requirements-ir-n).

Example:

```markdown
### IR-4 — Interrupt a long calculation

- **Requirement**: While a calculation is running, the user must be able to interrupt it.
- **Fit criterion**: after the interruption request, the user sees the calculation stopped in less than [threshold to be set] seconds.
- **Examples**:
  - IR-4.E1 (nominal) — Given a running calculation, when the user interrupts it, then the calculation stops and the user is back in the situation from before the calculation.
  - IR-4.E2 (boundary) — Given a calculation that finishes at the moment the user interrupts it, when the interruption arrives, then the result is kept and the user is informed of it.
- **Source**: SH-3 (main user), workshop on 2026-10-01.
- **Rationale**: a calculation can last several minutes; without interruption, a parameter error blocks the user.
- **Priority**: Should — a costly error, but a visible one.
- **Use cases**: UC-6
```

Seeing the progress of the calculation is another requirement (`IR-5`): an `IR-n` contains only one. That nothing partial is saved belongs to the minimal guarantees of `UC-6`, not to the `IR-n`. This need also commits the architecture: phase 3 turns it into a `QS-n`, phase 5 designs the interaction, phase 6 makes it possible.

## 3. Workshop flow

**If a functional analysis already exists** (source `SRC-n`), the flow below applies in *Proposal* mode: each step starts with the transposition of the source, and the questions cover only its gaps. See [00-principles § 16](00-principles.md#16-working-from-existing-material).

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Lists the actors from the `SH-n` and proposes the inventory of the `UC-n` (title, actor, goal, `BO-n`). | Completes, prioritizes. |
| 2 | For each *Must* `UC-n`, in order of priority: writes the main success scenario and the extensions. | Corrects the flow. |
| 3 | For that same `UC-n`, runs the Example Mapping: rules, nominal and boundary examples, questions. | Gives the real values, decides or leaves open. |
| 4 | Factors the rules shared by several cases into single `BR-n`. | — |
| 5 | Writes the `AC-n`. | Approves. |
| 6 | For each `UC-n` whose actor is human, starting with the *Must* ones, writes the `IR-n` (§ 2.7). | Approves. |
| 7 | Covers the supplements (§ 2.6) that are relevant to the project, including the user journeys. | Answers. |
| 8 | Takes up the *Should* and *Could* `UC-n` with a proportionate level of detail. | Prioritizes. |
| 9 | Enriches the glossary with every business term that has come up. | Corrects. |
| 10 | Updates the traceability, runs the checklist, invokes the critical reviewer. | Approves G2. |

## 4. Question bank

**For each use case**
1. Who triggers this case? Can it be triggered automatically (by a date, by another system)?
2. What must be true before? What happens if it is not?
3. What must be true at the end, even in case of failure?
4. What happens if the actor gives up halfway through?
5. Can two people do the same thing at the same time on the same object? Which one wins?

**For each rule**
1. Give me a concrete example with real values.
2. What happens exactly at the boundary (equality, zero, empty, maximum)?
3. Are there exceptions? Who can override the rule, and how is that traced?
4. Where does this rule come from (law, contract, habit)? Can it change, and how often?
5. If the system applied it wrongly, how and when would anyone notice? *(used to set the priority)*

**For each use case whose actor is human**
1. What must the user see to decide at this step?
2. Do they sometimes have to wait? What must they be able to do in the meantime: follow, carry on elsewhere, interrupt?
3. Which input or handling errors are likely, and how must they be able to correct them?

**Cross-cutting**
1. Must the history of changes be kept? Who did what, when?
2. Which amounts, dates, time zones, currencies, rounding, languages?
3. What must be possible to cancel, and until when?
4. Which entered data may be wrong, and how is it corrected?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `02-functional-requirements.md` | Actors, inventory of the `UC-n`, `UC-n` sheets, complete `BR-n`, `AC-n`, `IR-n`, user journeys, relevant supplements |
| `STATE.md` | `OD-n` arising from the red cards |
| `glossary.md` | Business terms added |
| `traceability.md` | Links `BO-n` → `UC-n` → `BR-n` / `AC-n` / `IR-n` |

## 6. Gate G2 checklist

- [ ] ★ Every `UC-n` traces back to a `BO-n`.
- [ ] ★ Every *Must* `BR-n` carries the six fields, including at least one nominal example and one boundary or failure example.
- [ ] ★ No business value has been invented: every threshold is confirmed or marked [threshold to be set] with an OD.
- [ ] ★ Every *Must* `UC-n` has at least one `AC-n`.
- [ ] ★ Every `IR-n` cites the `UC-n` it serves, and every *Must* `UC-n` whose actor is human has at least one `IR-n`.
- [ ] Every `UC-n` has error extensions and minimal guarantees.
- [ ] Every `BR-n` has a rationale and a source.
- [ ] Concurrent access and cancellation during processing have been examined for every *Must* `UC-n`.
- [ ] Business objects that have states have a state diagram.
- [ ] The role × action matrix is filled in.
- [ ] No business term is used without appearing in the glossary.
- [ ] No requirement mentions a technology (database, framework, protocol).
- [ ] No `IR-n` describes an appearance (color, position, component).

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Rule without an example | "The system calculates the discount according to the sales policy" | Require three examples with figures, including a boundary. |
| Compound rule | "… and … and …" in a single statement | Split it into several `BR-n`. |
| Unverifiable criterion | "The system must be intuitive" | This is a quality attribute: move it to phase 3 with a measure. |
| Happy path only | No error extension | Systematically ask questions 3 to 5 of the "use case" block. |
| Interface disguised as a requirement | "A green button at the top right" | Go back to the intention and write it as an `IR-n`; the screen is designed in phase 5. |
| Bound settled at random | "≤" or "<" chosen by the AI | Open an OD. |
