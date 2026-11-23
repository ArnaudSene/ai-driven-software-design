# Phase 1 — Scoping

| Key | Value |
|---|---|
| Central question | Why this project, for whom, within what limits? |
| Agent | [`prompts/business-analyst.md`](../prompts/business-analyst.md) |
| Inputs | Initial idea or request, existing documents declared as sources `SRC-n` (requirements specification, functional analysis, mockups, emails, studies) |
| Outputs | `design/01-scoping.md`, `design/STATE.md` initialized, `design/glossary.md` seeded |
| Identifiers created | `SH-n`, `BO-n`, `C-n`, first `H-n`, `R-n`, `OD-n` |
| Template | [`templates/01-scoping.md`](../templates/01-scoping.md) |
| Gate | G1 |

---

## 1. Why this phase

A project without explicit scoping is built on misunderstandings: everyone imagines a different product, audience and ambition. Scoping sets **the problem to solve, the people concerned, the expected success and the limits** before a single feature is discussed.

This is also where the **project profile** is chosen (*Prototype*, *Product* or *Critical*, see [00-principles § 10](00-principles.md#10-project-profiles-proportionality)), which calibrates the effort of every following phase.

## 2. Concepts and methods

### 2.1 Vision statement

A sentence that fits in an elevator ride, following Geoffrey Moore's template:

> **For** <target customer> **who** <need or problem>, **<product name>** is a <product category> **that** <key benefit>. **Unlike** <current alternative>, our product <essential difference>.

If the decision-maker cannot fill in this template, the project is not yet ready for what follows. That is valuable information, not a failure.

### 2.2 Stakeholders (`SH-n`)

Any person or organization that **uses** the system, is **affected** by it, **funds** it, **operates** it or may **oppose** it. Volere's onion model helps to leave no one out:

| Layer | Examples |
|---|---|
| The product | Direct users, operators, administrators |
| The business system | Internal services that consume or produce the data |
| The organization | Sponsor, management, legal, security, support |
| The environment | End customers, regulators, partners, competitors, the general public |

For each stakeholder, record their role, their interest, their influence, and the **representative** who can be interviewed.

### 2.3 Measurable business objectives (`BO-n`)

An objective describes an **observable change in the real world**, not a feature. Each one carries an indicator, a baseline, a target and a deadline.

| Bad | Good |
|---|---|
| "Have an online claims portal" | `BO-1`: reduce the average processing time of an insurance claim from 10 days to 3 days, within 6 months of launch. *(illustrative values)* |
| "Be fast" | This is not a business objective. It is a quality attribute, handled in phase 3. |

If the decision-maker does not know the baseline, write **[threshold to be set]** and open an OD (open decision) whose action is to measure it.

### 2.4 Scope

- **In scope**: what the target version covers.
- **Out of scope**: what is **explicitly** excluded. This is the most useful list, because it defuses implicit expectations.
- **Later**: what is considered for a later version.

A **business context diagram** shows the system as a black box surrounded by its actors and by the external systems it exchanges with. It is drawn in Mermaid, without any internal technical detail.

### 2.5 Constraints (`C-n`)

A constraint is a limit **imposed** on the team, which it has no power to negotiate: budget, deadline, legal obligation, technology imposed by the company, available skills, mandatory hosting in a given country, an existing system to keep.

A constraint is not a choice: "we must use the company's cloud" is a constraint; "we prefer such-and-such a language" is a choice, to be examined in phase 7.

### 2.6 Initial hypotheses and risks

- Hypothesis (`H-n`): what is held to be true without having been verified ("users have a recent smartphone"). Record how and when to verify it.
- Risk (`R-n`): an uncertain event that would jeopardize the project. Record its probability, its impact and a response (avoid, reduce, transfer, accept).

### 2.7 What already exists

Systems, data, manual processes or spreadsheets that the project replaces or coexists with. What already exists is the best source of implicit business rules: a spreadsheet used for ten years contains rules that nobody has ever written down.

### 2.8 Context of use (sketch)

For each group of end users, sketch the **context of use**, in the manner of the ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25063 standard (§ 4.2):

| Element | Question |
|---|---|
| Characteristics | Who are they? How comfortable are they with the business and with digital tools? |
| Goals | What are they trying to achieve? |
| Main tasks | What do they do, and how often? |
| Environment | Where, on which device, under which conditions: in the office, on the move, under pressure, often interrupted? |

The sketch sizes phase 5 (interaction design). If the system has no end user (it serves only other systems, or developers through an API (Application Programming Interface) or a command line), write it down: phase 5 will be reduced to the ergonomics of that API or of that command line.

## 3. Workshop flow

| Step | The AI (artificial intelligence) | The decision-maker |
|---|---|---|
| 1 | Creates `design/` from the templates, initializes `STATE.md` (phase 1, *Load* step). | — |
| 2 | Reads every document provided and writes a factual summary of them: facts, unclear areas, contradictions. | Provides the documents, corrects the summary. |
| 3 | Asks the questions on the problem and the vision (§ 4, block A). Proposes a vision statement. | Answers, rephrases the vision. |
| 4 | Inventories the stakeholders (block B) and proposes an `SH-n` list, then sketches the context of use of each user group (§ 2.8). | Completes the list and names the representatives. |
| 5 | Turns the stated expectations into measurable `BO-n` objectives (block C). | Sets the targets or leaves them [threshold to be set]. |
| 6 | Delimits the scope and draws the context diagram (block D). | Decides what is in and what is out. |
| 7 | Lists the constraints, what already exists, the hypotheses and the risks (blocks E and F). | Confirms. |
| 8 | Recommends a project profile, justified by the answers. | Chooses the profile. |
| 9 | Seeds the glossary with the business terms encountered. | Corrects the definitions. |
| 10 | Writes `01-scoping.md`, runs the checklist, presents the gate summary. | Approves G1. |

## 4. Question bank

The AI picks from this bank the questions that are still unanswered and asks them in batches of at most 5, in the format of [00-principles § 5.1](00-principles.md#51-format-of-a-question).

**A. Problem and vision**
1. What concrete problem are we solving? Who suffers from it today, and how do they work around it?
2. What happens if we do nothing?
3. Why now?
4. What does success look like in a year? What will have changed for the users?
5. Is there a competing solution or a current tool? What is wrong with it?

**B. Stakeholders**
1. Who will use the system day to day? How often, on which device, with what level of digital proficiency?
2. Who pays? Who decides? Who can block the project?
3. Who will operate the system and provide support?
4. Are third parties (partners, regulators, your customers' customers) affected?
5. Who can answer detailed business questions?
6. Under which conditions do users use the system: in the office, on the move, under pressure, often interrupted?

**C. Objectives**
1. Which indicators do you already track, and which ones must the project move?
2. What baseline, what target, what deadline?
3. What is the order of magnitude of the number of users today and in three years?

**D. Scope**
1. What are the three functions without which the product is pointless?
2. What is explicitly excluded from the first version?
3. Which external systems must it exchange with (payment, messaging, directory, business management software)?

**E. Constraints and what already exists**
1. Budget, deadline, team size and skills?
2. Known legal or regulatory obligations (personal data, health, finance, accessibility)?
3. Technologies, hosting providers or suppliers that are imposed or forbidden?
4. Which systems, data or manual processes exist today? Must data be migrated?

**F. Risks**
1. What keeps you up at night about this project?
2. Which hypothesis, if it turned out to be false, would kill the project?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `01-scoping.md` | Vision, `SH-n`, context of use, `BO-n`, scope (in, out, later), context diagram, `C-n`, what already exists, chosen profile and its justification |
| `STATE.md` | Current phase, profile, `H-n`, `R-n` and `OD-n` registers, log |
| `glossary.md` | First business terms (term, definition, synonyms to avoid) |

## 6. Gate G1 checklist

The items marked ★ are enough in a light profile.

- [ ] ★ The vision statement is filled in and approved by the decision-maker.
- [ ] ★ Every `BO-n` has an indicator, a target and a deadline, or a [threshold to be set] attached to an OD.
- [ ] ★ The out-of-scope list is explicit (at least 3 items).
- [ ] ★ The project profile is chosen and justified.
- [ ] Every `SH-n` has a role, an interest, an influence and a representative (or "to be identified").
- [ ] The context of use of each group of end users is sketched, or the absence of any end user is written down.
- [ ] The context diagram shows every actor and external system mentioned.
- [ ] Legal constraints have been explicitly asked about, even if the answer is "none".
- [ ] Every `R-n` has a probability, an impact and a response.
- [ ] No technical choice appears in the document, except in the form of a `C-n`.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Feature as objective | "Objective: have a dashboard" | Ask "to change what?" until a measurable effect is reached. |
| Forgotten stakeholder | Support or legal discovers the project at go-live | Go through the four layers of the onion. |
| Implicit scope | No out-of-scope list written | Require at least three explicit exclusions. |
| Solution disguised as a need | "The need is to have microservices" | Apply golden rule 11: extract the need, note the idea for phase 6. |
| Invented figure | A "reasonable" target proposed by the AI and never approved | Apply golden rule 1: [threshold to be set] + OD. |
