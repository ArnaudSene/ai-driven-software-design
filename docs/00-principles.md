# 00 — Principles and conventions

| Key | Value |
|---|---|
| Status | Normative — applies to all phases |
| Readers | Human decision-maker, orchestrator agent, specialist agents |
| To load | Always, at the start of every session, before any phase file |

---

## 1. Purpose

This guide defines a complete software design process, **from the expressed need to the first slice of executable code**, conducted by an AI (artificial intelligence) in dialogue with a human decision-maker.

It pursues three objectives:

1. **Forget nothing.** Each phase covers a question that every project ends up asking — better to answer it before coding than in production.
2. **Trace every decision.** Every technical decision traces back to a need, every need traces down to a test.
3. **Divide the work according to each party's strengths.** The AI structures, asks questions, writes, checks consistency and proposes. The human knows the business, arbitrates and approves.

The guide is written to be read by a human **and** executed by an AI agent: stable sections, numbered lists, normative vocabulary, explicit output formats.

---

## 2. Roles

| Role | Nature | Responsibilities |
|---|---|---|
| **Decision-maker** | Human | Carries the product vision. Answers the questions, arbitrates between options, sets the thresholds, approves the gates. The only one entitled to resolve an OD (open decision). |
| **Consulted experts** | Humans | Business, legal, security, operations. Called on by the decision-maker when the agent recommends it. |
| **Orchestrator** | AI agent | Runs the process: keeps the state, chooses the phase, loads the specialist agent, applies the interaction loop, enforces the gates. Defined in [`AGENTS.md`](../AGENTS.md). |
| **Specialists** | AI agents | One per area of expertise (business analyst, architect, security…). Defined in [`prompts/`](../prompts/). |
| **Critical reviewer** | AI agent | Reviews the deliverables adversarially before each gate. Defined in [`prompts/critical-reviewer.md`](../prompts/critical-reviewer.md). |

RACI (Responsible, Accountable, Consulted, Informed — does the work, approves, is consulted, is informed) matrix:

| Activity | Decision-maker | Orchestrator | Specialist | Reviewer | Experts |
|---|---|---|---|---|---|
| Ask the questions | I | A | R | — | — |
| Answer on the business | A/R | I | I | — | C |
| Write the deliverables | I | A | R | — | — |
| Review before the gate | I | A | C | R | C |
| Approve a gate | A/R | C | C | C | C |
| Resolve an OD | A/R | C | C | — | C |

---

## 3. Normative vocabulary

The following keywords, inspired by RFC (Request For Comments) 2119, the IETF (Internet Engineering Task Force) standard on requirement levels, have a precise meaning throughout the guide:

| Term | Meaning |
|---|---|
| **must** / **must not** | Absolute obligation. A deviation is a non-conformity. |
| **should** / **should not** | Strong recommendation. A deviation must be justified in writing. |
| **may** | Option left to the judgment of the agent or the decision-maker. |

---

## 4. Process overview

The process has 13 **ordered** phases. Each phase answers a central question and ends with a **gate** (a human approval point).

| # | Phase | Central question | Agent | Main deliverable | Gate |
|---|---|---|---|---|---|
| 1 | [Scoping](01-scoping.md) | Why this project, for whom, within what limits? | Business analyst | `01-scoping.md` | G1 |
| 2 | [Functional analysis](02-functional-analysis.md) | What must the system do? | Business analyst | `02-functional-requirements.md` | G2 |
| 3 | [Quality requirements](03-quality-requirements.md) | At what level of quality? | Quality architect | `03-quality-requirements.md` | G3 |
| 4 | [Domain modeling](04-domain-modeling.md) | How is the business structured? | Domain modeler | `04-domain.md` | G4 |
| 5 | [Interaction design](05-interaction-design.md) | How does the user accomplish their tasks with the system? | Interaction designer | `05-interaction.md` + `prototypes/` | G5 |
| 6 | [Software architecture](06-software-architecture.md) | How should the system be organized? | Software architect | `06-architecture.md` + ADR (Architecture Decision Record) | G6 |
| 7 | [Technology choices](07-technology-choices.md) | With which languages, frameworks, products? | Technology advisor | `07-technology-choices.md` + ADR | G7 |
| 8 | [Data and contracts](08-data-contracts.md) | Which data, which interfaces? | Data and interface architect | `08-data-contracts.md` + `contracts/` | G8 |
| 9 | [Security and compliance](09-security-compliance.md) | What must be protected against, which obligations must be met? | Security specialist | `09-security.md` | G9 |
| 10 | [Infrastructure and operations](10-infrastructure-operations.md) | Where and how does the system run? | Platform reliability engineer | `10-operations.md` | G10 |
| 11 | [Test strategy](11-test-strategy.md) | How can conformance be proven? | Quality engineer | `11-test-strategy.md` | G11 |
| 12 | [Delivery plan](12-delivery-plan.md) | In what order should it be built, and how should it start? | Tech lead | `12-delivery-plan.md` | G12 |
| 13 | [Evolution](13-evolution.md) | How does the design stay true? | Orchestrator | Updates, superseding ADRs | — (continuous) |

**Order and dependencies.**

- Phases 1 to 3 describe the **problem**. They must contain **no technical solution choice**. A technical constraint imposed from outside ("the company only uses such-and-such cloud") is a **constraint** (`C-n`), not a choice.
- Phase 4 bridges the problem and the solution.
- Phases 5 to 12 describe the **solution**. Phase 5 designs the interaction with the user; phases 6 to 12 design the system that makes it possible. Every decision there cites the requirements that motivate it.
- Phase 13 starts with the first line of code and never ends.

**This process is not a waterfall cycle.** The order indicates which way information flows, not a ban on going back. A discovery in phase 8 can reopen a rule from phase 2: this is normal and governed (§ 14).

---

## 5. The interaction loop

Each phase follows the same seven-step loop. The orchestrator **must** apply it and **must** tell the decision-maker which step is under way.

```
 ┌────────┐   ┌────────────┐   ┌───────────┐   ┌────────────┐   ┌────────────┐   ┌──────────┐   ┌────────┐
 │ 1 LOAD │──►│ 2 QUESTION │──►│ 3 PROPOSE │──►│ 4 CRITIQUE │──►│ 5 VALIDATE │──►│ 6 RECORD │──►│ 7 GATE │
 └────────┘   └────────────┘   └───────────┘   └────────────┘   └────────────┘   └──────────┘   └────────┘
                     ▲                                                 │
                     └────────── corrections / new questions ──────────┘
```

| Step | Who acts | What happens |
|---|---|---|
| **1. Load** | AI | Reads `design/STATE.md`, this file, the phase file, the specialist prompt, then the deliverables of the upstream phases listed under "Inputs". Summarizes in 5 lines at most what it knows and what is missing. |
| **2. Question** | AI → human | Asks questions in **batches of 5 at most**, sorted by impact. Each question follows the format of § 5.1. |
| **3. Propose** | AI | Writes a draft of the deliverable from the answers. Everything the decision-maker has not confirmed is marked as a proposal or a hypothesis. |
| **4. Critique** | AI | Runs the phase checklist and, for the *Product* and *Critical* profiles, invokes the critical reviewer. Presents the gaps found. |
| **5. Validate** | Human | Amends, accepts or rejects each element. The AI loops back to step 2 or 3 as often as necessary. |
| **6. Record** | AI | Writes the files in `design/`, updates the traceability matrix, the OD register and `STATE.md`. |
| **7. Gate** | Human | The decision-maker explicitly declares the gate approved. The AI records it (§ 13). |

### 5.1 Format of a question

```markdown
**Q3.2 — Withdrawal period** · impact: high · blocks: BR-7, BR-9
Context: the law imposes a minimum period for certain distance sales; your offer seems to be concerned.
Options:
  a) 14 calendar days, the legal minimum — *recommended: legal obligation, no waiver cost*
  b) 30 days, a commercial selling point
  c) Other value: …
If you do not decide now: I open an OD and mark BR-7 [threshold to be set].
```

Rules:

1. Numbering `Q<phase>.<rank>`. It is local to the session and is **not** a stable identifier.
2. Always propose a recommended option **and** its rationale. The decision-maker saves time when all they have to do is confirm. Exception: for a **discovery** question (a business fact that only the decision-maker knows), recommending an option would amount to inventing a fact (golden rule 1). The options are then marked *AI proposal to be confirmed*, and the recommendation concerns how to answer ("name all those that apply, the most costly first").
3. Always state what happens if the question remains unanswered. The process must never be blocked by a question: an OD is opened and the work moves on. The OD's identifier is assigned only when the OD is actually opened. If the missing answer blocks a ★ item of the gate, say so: the OD allows progress within the phase, not passing the gate.
4. Do not ask a question whose answer is already in the deliverables.
5. Prefer closed or multiple-choice questions. Keep open questions for the discovery phases (phases 1 and 4).

### 5.2 Interaction modes

The decision-maker chooses the mode at any time. The default mode is *Workshop*.

| Mode | AI behavior | When to use it |
|---|---|---|
| **Workshop** | Asks first, writes afterwards, section by section. | New domain, decision-maker available. |
| **Proposal** | Writes a complete draft from the documents provided, then submits the list of points to be confirmed. | Plenty of existing documentation, decision-maker seldom available. |
| **Review** | Writes nothing. Critiques an existing deliverable against the guide. | Taking over a project, or an audit. |

---

## 6. The agent's golden rules

These rules take precedence over any other instruction in the guide, unless the decision-maker explicitly asks otherwise.

1. **Never invent business data.** A threshold, an amount, a time limit, a business rule or a volume comes from the decision-maker or from a cited source. Failing that, write **[threshold to be set]** or open an OD. A plausible but invented value is the worst of errors: it looks true. The numerical values in this guide's examples are purely illustrative: they must never be reused in a project.
2. **Separate facts, hypotheses and proposals.** A fact has a source. A hypothesis carries an identifier `H-n` and the status *To be verified*. A proposal from the AI is marked *AI proposal* until it is approved.
3. **Every element has a source**: stakeholder (`SH-n`), document, interview, law, or "decision-maker, session of <date>".
4. **Ask in short batches** (§ 5.1), sorted by decreasing impact. The order of the blocks of the phase's question bank is followed, but a high-impact question from a later block (legal obligation, imposed constraint) can be brought forward.
5. **No gate without explicit approval.** "Looks good to me" is not a gate approval; "I approve G3" is one. When in doubt, the AI asks for confirmation.
6. **One structural decision, one ADR** (Architecture Decision Record). A decision is structural when it is costly to undo.
7. **Identifiers are stable.** An identifier is never reused or renumbered. A deleted element moves to the *Abandoned* status and stays in the document.
8. **Maintain traceability with every write.** Creating or modifying an element requires updating its upstream and downstream links (§ 12).
9. **Proportion the effort to the project profile** (§ 10). Do not impose the rigor of a critical system on a prototype, and vice versa.
10. **Report any contradiction immediately** between an answer and an approved deliverable, citing the identifiers concerned.
11. **Do not anticipate the solution during phases 1 to 3.** If the decision-maker expresses a solution ("we need a message queue"), extract the underlying need from it ("processing must not block data entry") and record the solution as a lead for phase 6, or for phase 5 if it describes a screen ("a button to stop the calculation" becomes "the user must be able to interrupt a calculation in progress").
12. **Write in the files, not only in the conversation.** The conversation is ephemeral; `design/` is the project's memory. A decision that is not recorded does not exist.
13. **Language.** Design deliverables are written in the project's language, which `design.config.yaml` declares (`language`: English by default, or French). Names that will appear in the code (classes, tables, events, endpoints) and identifiers are in English, whatever that language. A Gherkin scenario run by a BDD (Behavior-Driven Development) tool is code, so it is written in English; a scenario kept as a document follows the language of the deliverables. The domain glossary maps the terms of the deliverables to the names in the code (phase 4).
14. **Name your uncertainties.** If the AI is not sure of a technical fact (a product's version, a library's behavior), it says so and proposes a verification, rather than asserting.

---

## 7. Conventions for writing requirements

We rely on the **Volere** framework (Suzanne and James Robertson) for requirements and on **Example Mapping** (Matt Wynne) for examples.

### 7.1 Structure of a rule

Each business rule (`BR-n`) and each quality scenario (`QS-n`) carries the following fields:

| Field | Content |
|---|---|
| **Rule** | A single, affirmative statement, with no "and" that would hide two rules. |
| **Fit criterion** | A measurable condition that makes it possible to write a test that fails **deterministically** when the rule is violated. |
| **Examples** | At least one nominal example and one boundary or failure example, in the form *Given / When / Then*. |
| **Source** | Where the rule comes from (`SH-n`, document, law, decision-maker on a given date). |
| **Rationale** | Why the rule exists. Without a rationale, nobody will ever dare to change or delete it. |
| **Priority** | *Must*, *Should*, *Could* or *Won't* (§ 7.3). |

### 7.2 Fit criterion and thresholds

A fit criterion must produce a test that fails deterministically. A criterion that cannot do so yet, because it is waiting for a value from the decision-maker, is marked **[threshold to be set]**. It is not disguised with a plausible value.

Each **[threshold to be set]** is linked to an OD. A deliverable can pass its gate with thresholds to be set, provided each has an OD, an owner and a due date (a phase or a date).

Recommended wording for the statements: the EARS (Easy Approach to Requirements Syntax) syntax:

| Template | Form |
|---|---|
| Ubiquitous | The system **must** <response>. |
| Event-driven | **When** <trigger>, the system **must** <response>. |
| State-driven | **While** <state>, the system **must** <response>. |
| Unwanted behavior | **If** <abnormal situation>, **then** the system **must** <response>. |
| Optional feature | **Where** <feature present>, the system **must** <response>. |

### 7.3 Priorities

We use the MoSCoW (Must, Should, Could, Won't — not this time) method. The priority follows from the **consequence of relaxing** the rule, not from how important it feels:

| Priority | Assignment criterion |
|---|---|
| **Must** | Relaxing the rule produces an **unrecoverable or silent** error: loss or corruption of data, undetected financial error, legal non-compliance, harm to people's safety. |
| **Should** | Relaxing the rule produces a **costly but visible** error: it is detected and corrected, at the cost of an intervention. |
| **Could** | Comfort or optimization. Its absence produces no error. |
| **Won't** | Explicitly outside the targeted version. Recorded so that nobody asks for it again. |

The decision-maker can refine this criterion in a project constraint (for example `C-4`), which the rules then cite as the arbiter.

### 7.4 Interaction requirements (`IR-n`)

An interaction requirement says what the user **must be able to do or see** to accomplish their task, never what the screen looks like. It follows the ISO (International Organization for Standardization) 25065:2019 standard, which distinguishes two kinds of user requirements:

| Kind (ISO 25065) | In the guide | Example |
|---|---|---|
| User-system interaction requirement | `IR-n`, phase 2 | **While** a calculation is in progress, the user **must be able to** interrupt it. |
| Quality-in-use requirement (effectiveness, efficiency, satisfaction) | Interaction capability `QS-n`, phase 3 | The tested users complete a booking without help in less than [threshold to be set] minutes. |

An `IR-n` carries the fields of § 7.1, the rule becoming the **requirement**, plus the `UC-n` it serves. Its fit criterion is verified by a journey test (phase 11).

Rules:

1. An `IR-n` cites the `UC-n` it serves.
2. An `IR-n` describes no appearance (color, position, component): "a red button at the top right" is a solution, which phase 5 will design.
3. A screen never carries a business rule: it displays and transmits. The rule lives in a `BR-n` and in the domain.
4. Every screen designed in phase 5 traces back to at least one `UC-n`, and every `IR-n` is satisfied by at least one screen.
5. An interaction need that is significant for the architecture (cancel, undo, follow progress, keep views consistent) becomes a `QS-n` in phase 3, receives its interaction response in phase 5 and its ADR in phase 6.
6. Without an end user, there is no `IR-n`.

---

## 8. Identifiers

### 8.1 Prefix register

| Prefix | Object | English term | Created in phase | File |
|---|---|---|---|---|
| `SH-n` | Stakeholder | Stakeholder | 1 | `01-scoping.md` |
| `BO-n` | Measurable business objective | Business Objective | 1 | `01-scoping.md` |
| `C-n` | Constraint (imposed, not negotiable by the team) | Constraint | 1+ | `01-scoping.md` |
| `H-n` | Hypothesis | Hypothesis | all | `STATE.md` (register) |
| `R-n` | Risk | Risk | all | `STATE.md` (register) |
| `OD-n` | Open decision | Open Decision | all | `STATE.md` (register) |
| `UC-n` | Use case | Use Case | 2 | `02-functional-requirements.md` |
| `BR-n` | Business rule | Business Rule | 2 | `02-functional-requirements.md` |
| `AC-n` | Acceptance criterion | Acceptance Criterion | 2 | `02-functional-requirements.md` |
| `IR-n` | Interaction requirement | Interaction Requirement | 2 | `02-functional-requirements.md` |
| `QS-n` | Quality attribute scenario | Quality Scenario | 3 | `03-quality-requirements.md` |
| `BC-n` | Bounded context | Bounded Context | 4 | `04-domain.md` |
| `ADR-nnnn` | Architecture decision | Architecture Decision Record | 6+ | `adr/ADR-nnnn-title.md` |
| `T-n` | Threat | Threat | 9 | `09-security.md` |
| `SLO-n` | Service level objective | Service Level Objective | 10 | `10-operations.md` |
| `FF-n` | Fitness function (architecture test) | Fitness Function | 11 | `11-test-strategy.md` |
| `INC-n` | Delivery increment | Increment | 12 | `12-delivery-plan.md` |
| `SRC-n` | Existing source document, read without being modified | Source | 1+ | `design.config.yaml` and `STATE.md` |

Each prefix is also an acronym — for example BR (Business Rule), UC (Use Case), QS (Quality Scenario) — whose full meaning is given in the [glossary](glossary.md). All the prefixes are initialisms of their English term; the "English term" column also gives the term to use in the code (golden rule 13).

### 8.2 Format rules

1. Form `PREFIX-n`, where `n` is an increasing integer with no leading zero (`BR-12`). Exception: ADRs are numbered on 4 digits (`ADR-0007`) so that the files sort in order.
2. An example is attached to its rule: `BR-3.E2` denotes the 2nd example of `BR-3`.
3. Identifiers are **stable**: never reused, never renumbered, even after abandonment.
4. Tests, commit messages and code comments that justify a behavior **must** cite the identifier (`// BR-12: ...`).

---

## 9. Statuses

| Object | Possible statuses |
|---|---|
| Deliverable (file) | Draft → Proposed → Approved (gate) → Revised *(after a change made after the gate)* |
| Element (BR, UC, QS…) | Proposed → Approved → Abandoned / Superseded by `X-n` |
| OD | Open → Resolved (points to `BR-n` or `ADR-nnnn`) / Lapsed |
| Hypothesis | To be verified → Confirmed / Refuted |
| Risk | Open → Mitigated / Accepted / Closed |
| ADR | Proposed → Accepted → Deprecated / Superseded by `ADR-nnnn` |

---

## 10. Project profiles (proportionality)

At scoping, the decision-maker chooses a profile. It determines the depth of each phase. The profile can change along the way: a prototype that becomes a product must go through the light phases again.

| Profile | Description |
|---|---|
| **Prototype** | Short or throwaway lifespan, restricted audience, learning objective. |
| **Product** | Standard case: real users, a life of several years, a small to medium team. |
| **Critical** | Sensitive data, regulated sector, high traffic, money at stake or people's safety. |

Abbreviations in the table below: ATAM (Architecture Tradeoff Analysis Method), C4 (Context, Containers, Components, Code — a model of architecture diagrams), DPIA (data protection impact assessment), DRP (disaster recovery plan). See the [glossary](glossary.md).

| Phase | Prototype | Product | Critical |
|---|---|---|---|
| 1 Scoping | Light | Full | Full |
| 2 Functional analysis | Light (`UC-n` + *Must* `BR-n`) | Full | Full |
| 3 Quality requirements | Light (3 to 5 `QS-n`) | Full | Full + ATAM review |
| 4 Domain | Glossary only | Full | Full |
| 5 Interaction | Light (screen map, *Must* screen states, responses to significant needs) | Full | Full + evaluation of the prototype with users |
| 6 Architecture | Light (C4 levels 1–2, 1 to 3 ADRs) | Full | Full + ATAM review |
| 7 Technologies | Light | Full | Full + proofs of concept |
| 8 Data and contracts | Light | Full | Full |
| 9 Security | Minimal checklist | Full | Full + DPIA if required |
| 10 Operations | Light | Full | Full + tested DRP |
| 11 Tests | Light | Full | Full |
| 12 Plan | Full | Full | Full |

"Light" means: the same sections, content reduced to the essentials, the gate checklist reduced to the items marked ★ in each phase.

Without an end user, that is, when the system only serves other systems or developers, phase 5 comes down to the ergonomics of the API (Application Programming Interface) or of the command line, whatever the profile.

---

## 11. Tree produced in the target project

All deliverables are written in the design directory, `DESIGN_DIR`. By default, it is `design/` at the root of the project being designed; it can be placed elsewhere, for example in a dedicated documentation repository, through the `design.config.yaml` file at the root of the project (see [`AGENTS.md` § 0](../AGENTS.md#0-establish-the-context)). Throughout the guide, `design/` denotes this directory. The templates are in [`templates/`](../templates/).

```
design/
├── STATE.md                          # Process state: phase, gates, OD/H/R registers, log
├── glossary.md                     # Domain language (term in the deliverables ↔ English name in the code) + acronyms
├── traceability.md                   # Traceability matrix
├── 01-scoping.md
├── 02-functional-requirements.md
├── 03-quality-requirements.md
├── 04-domain.md
├── 05-interaction.md                # Screens, journeys and states (phase 5)
├── prototypes/                      # Throwaway prototypes, never delivered
├── 06-architecture.md               # Architecture document (arc42 structure)
├── 07-technology-choices.md
├── 08-data-contracts.md
├── contracts/                        # openapi.yaml, asyncapi.yaml, schemas
├── 09-security.md
├── 10-operations.md
├── 11-test-strategy.md
├── 12-delivery-plan.md
├── adr/
│   ├── ADR-0001-short-title.md
│   └── …
└── diagrams/                      # Diagram sources (Mermaid, PlantUML, Structurizr)
```

Diagrams **should** be written as text (Mermaid preferably): the AI can read, produce and modify them, and they can be compared from one version to the next in Git.

---

## 12. Traceability

```
Problem                           Solution                                  Proof
───────                           ────────                                  ─────
BO-n ─► UC-n ─► AC-n ─────────────────────────────────────────────────────► acceptance test
          │
          ├───► IR-n ─► screen (phase 5) ─────────────────────────────────► journey test
          │
          └───► BR-n ─► BR-n.Ek (examples) ───────────────────────────────► domain test
                  │
                  └───────────────► ADR-nnnn ─► component / module ─► code

BO-n, C-n ─► QS-n ─────────────► ADR-nnnn ─► FF-n (architecture test)
                 └─────────────► SLO-n (production monitoring)

T-n (threat) ──────────────────► measure ─► ADR / BR-n / security test
BC-n ──────────────────────────► module or service
domain glossary ───────────────► names in the code
BO-n ──────────────────────────────────────────────────────────────────────► indicator measured in production
```

Rules:

1. Every `UC-n` traces back to at least one `BO-n`: otherwise, why build it?
2. Every *Must* `BR-n` has at least two examples (one nominal, one boundary or failure). Every `UC-n` has at least one `AC-n`. Every example and every `AC-n` traces down to a planned test (phase 11).
3. Every `ADR` cites at least one `QS-n`, `C-n` or `BR-n` that motivates it.
4. Every *Must* `QS-n` is covered by an `ADR`, an `FF-n` or an `SLO-n`.
5. `design/traceability.md` is updated at the *Record* step of each phase. Any orphan row (an element without an expected upstream or downstream link) is reported to the decision-maker.
6. Every `IR-n` traces back to a `UC-n`, is satisfied by at least one screen (phase 5) and traces down to a planned journey test (phase 11).

---

## 13. Gates

A gate is passed when:

1. all the items of the phase checklist are checked (or only the ★ items in a light profile), or expressly waived;
2. the critical reviewer has left no *blocking* objection unanswered (*Product* and *Critical* profiles);
3. the decision-maker has explicitly declared the approval.

Recording in `STATE.md`:

```markdown
| Gate | Date       | Decision | Waivers                    | Linked open ODs |
|------|------------|----------|----------------------------|-----------------|
| G3   | 2026-10-02 | Approved | QS-4: measurement deferred | OD-6, OD-7      |
```

An approved gate **freezes** the deliverable: any later change follows § 14.

---

## 14. Going back and change management

Discovering in phase *n* that an earlier phase is incomplete or wrong is **normal**. The procedure:

1. The AI reports the discrepancy, citing the identifiers affected ("ADR-0004 contradicts BR-9").
2. The AI lists the **downstream impact** using the traceability matrix.
3. The decision-maker chooses: correct upstream, adapt downstream, or open an OD.
4. The modified upstream element keeps its identifier and receives a dated revision note, and its deliverable moves to the *Revised* status.
5. If an accepted ADR is concerned, it is **not** modified: a new ADR is written that supersedes it.
6. The entry is recorded in the `STATE.md` log.

---

## 15. Resuming a session

The state of the process lives entirely in `design/`. A new agent, or the same one in a new conversation, **must** be able to resume by reading `STATE.md`, without the conversation history. At the end of a session, the orchestrator therefore writes in `STATE.md`:

- the current phase and loop step;
- the questions asked and left unanswered;
- the next planned action.

---

## 16. Working from existing material

The decision-maker often has documents written before applying the guide, and not necessarily following its methods: functional analysis, statement of requirements, user stories, specifications, rule spreadsheets. The guide does not replace them with an interrogation: it **transposes** them.

### 16.1 Declaring the sources

1. Each document is declared as a source, with a stable identifier `SRC-n`, a title and a location: a local path (including in another repository) or a web address. The declaration is made in `design.config.yaml` or in the decision-maker's message, then copied into the source register of `STATE.md`.
2. Sources are **read-only**: the agent never modifies, moves or copies them without an explicit request.
3. A source outside the project is not versioned with it. Its version (number, date, or commit identifier if it is a Git repository) is therefore recorded at the time of reading. If the source evolves, it is then possible to know what was transposed.
4. A remote repository is cloned locally, read-only, before being declared by its path: the agent does not depend on network access during the session.
5. The agent is launched from a **Git repository** (the code's, or a dedicated documentation repository), never from a folder that groups several repositories: otherwise neither the configuration nor the deliverables are versioned.
6. The paths in `design.config.yaml` are preferably **relative** (`../other-repo/…`), and the file is then versioned: anyone who clones the repositories side by side finds the configuration again. A file that contains absolute paths specific to one machine must not be versioned.

### 16.2 Transposition

1. The orchestrator proposes *Proposal* mode ([§ 5.2](#52-interaction-modes)).
2. The phase specialist reads the sources **in full** before any question, and extracts what belongs to its phase: scoping, use cases, business rules, quality requirements, etc. A single source often feeds several phases.
3. Each extracted element carries the precise reference in its **Source** field: `SRC-1 § 4.3`, `SRC-2 tab "Prices", row 12`. A rewording stays faithful to the meaning; when in doubt, the agent quotes the original passage.
4. The agent **fills no gap silently**. Everything the source does not say (boundary example, value, error case, rationale) is asked of the decision-maker or marked [threshold to be set] with an OD.
5. **Existing identifiers are kept.** If the source already numbers its elements in a compatible format (`BR-720`, `UC-12`), the agent reuses these identifiers instead of renumbering, and only assigns new numbers beyond the largest existing one. If the format is incompatible, the old → new identifier mapping is recorded in `traceability.md`.
6. Contradictions between sources, or within a source, are listed with both passages quoted, and resolved by the decision-maker.
7. Questions only concern what is missing, ambiguous or contradictory. Never ask again for what the source says clearly.

### 16.3 In-place adoption

If a source already satisfies the guide's conventions for the most part (rules with a fit criterion, examples, source, rationale, priority, stable identifiers), the agent does not copy it: duplicating it would create two truths. The phase deliverable, for example `02-functional-requirements.md`, then becomes an **index** that points to the source, and contains only:

- the mapping between the source's conventions and the guide's (fields, priorities, markers such as [to be set] or [to be measured]);
- the gaps found against the phase checklist, and how they are handled;
- the additions that the source does not cover.

The source adopted in place becomes a deliverable: it goes through the gate, and its later changes follow the change procedure. In-place adoption assumes that the source is versioned and that the team can modify it; otherwise, it is transposed.

### 16.4 What is authoritative

Until the gate of the phase concerned, the source is authoritative: a discrepancy between the transposition and the source is a transposition error. After the gate, **the deliverable is authoritative**, and the source becomes an archive. If the source is modified afterwards, the agent compares, lists the differences and applies the change procedure ([§ 14](#14-going-back-and-change-management)); it never resynchronizes automatically.
