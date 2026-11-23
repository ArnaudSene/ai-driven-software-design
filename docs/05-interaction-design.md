# Phase 5 — Interaction design

| Key | Value |
|---|---|
| Central question | How does the user accomplish their tasks with the system? |
| Agent | [`prompts/interaction-designer.md`](../prompts/interaction-designer.md) |
| Inputs | Phases 1 to 4 approved; first and foremost the context of use (phase 1), the `UC-n`, the `IR-n` and the journeys (phase 2), the interaction capability `QS-n` and the interaction needs that are significant for the architecture (phase 3), the domain glossary (phase 4) |
| Outputs | `design/05-interaction.md`, `design/prototypes/` |
| Identifiers created | No new prefix; the screens are named and linked to the `UC-n` and to the `IR-n` |
| Template | [`templates/05-interaction.md`](../templates/05-interaction.md) |
| Gate | G5 |

---

## 1. Why this phase

Phases 2 and 3 say what the user must be able to do or see (`IR-n`, interaction requirements) and with what quality (`QS-n`, quality scenarios). This phase designs the answer: which screens, in which sequence, with which states.

It comes **before the architecture**, for two reasons:

1. Some interaction needs commit the architecture: canceling a command, undoing an action, following the progress of a long operation, keeping several views consistent. The work of the SEI (Software Engineering Institute) shows that they require support from the architecture, and that architectural decisions are the hardest to change as design progresses (Bass, John, Kates, 2001; Bass and John, 2003). This work then proposed architectural patterns that serve usability (Golden, John, Bass, 2005; John et al., 2009), and Folmer and Bosch (2004) produced a synthesis of it. Discovered during coding, these needs are expensive.
2. The ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25063 and 25064 standards, which accompany the ISO 9241-210 standard on human-centered design, place the activity "producing design solutions" during architectural design, implementation and integration, not after them (introduction to both standards).

Guiding principle: **interaction before appearance, low fidelity before detail.** Colors, typography and the choice of a component system come in phase 7, once the journeys are approved.

If the system has no end user (context of use from phase 1) and serves only other systems or developers, the phase is reduced to the ergonomics of its API (Application Programming Interface) or of its command line: naming, error messages, consistency of the commands.

## 2. Concepts and methods

### 2.1 What the phase produces

The technical report ISO/TR (Technical Report) 25060:2023 names this deliverable the "user-system interaction and user interface specification". The guide breaks it down as follows:

| Deliverable | Content | Reference method |
|---|---|---|
| Screen map | The screens ("places"), what can be done on them ("affordances": buttons, fields), and the links between them | *Breadboarding* from *Shape Up* (Ryan Singer) |
| Screen sketches | A rough layout, without color or style, drawn "with a fat marker" so that no detail can be added to it | *Fat-marker sketches* from *Shape Up* |
| Interaction specification | For each journey: steps, information displayed, possible actions, system feedback, errors | ISO/TR 25060:2023, § 5.5 |
| Screen states | What each screen shows in each of the states of § 2.3 | — |
| Answers to significant needs | The interaction that answers each interaction need that is significant for the architecture (§ 2.4) | SEI usability scenarios |
| Per-screen needs | The data each screen reads and the actions it sends | Input to phase 8 |
| Throwaway prototype | Clickable HTML (HyperText Markup Language) prototype of the *Must* journeys | § 2.5 |

### 2.2 Start from the journeys, not from the screens

No screen is drawn before the journey it serves is known. The journey map from phase 2 (the user's activities, in the order in which they carry them out, in the manner of Jeff Patton's *story map*) provides the backbone; each screen hangs from it.

When the context of use is poorly known, user research comes before the phase: observation in context (*Contextual Design*, Karen Holtzblatt and Hugh Beyer), or personas and scenarios (*Goal-Directed Design*, Alan Cooper).

Rules (details in [00-principles § 7.4](00-principles.md#74-interaction-requirements-ir-n)):

1. Every screen traces back to at least one `UC-n` (use case); every `IR-n` is satisfied by at least one screen.
2. A screen never carries a business rule: it displays and transmits. A validation that would exist only in the screen is a forgotten `BR-n` (business rule): it is sent back up to phase 2.
3. The labels use the terms of the domain glossary (phase 4): the ubiquitous language goes all the way to the screen; it does not stop at the code.

### 2.3 The states of a screen

A screen does not have just one state. Forgotten states are a classic source of defects: the agent **must** enumerate them for each screen.

| State | Question to settle |
|---|---|
| Empty | What does the user see the first time, when there is nothing yet? What are they offered? |
| Loading | What do they see while waiting? Beyond what duration are they shown the progress? Can they cancel? |
| Error | What are they told, in what words? What can they do next? Is their input kept? |
| Partial | Only part of the data is available: is it displayed, and how is that signaled? |
| Stale | The data displayed is no longer up to date: can they see that? Since when? |
| Insufficient permissions | What does a role that has no access to an action see (role × action matrix from phase 2)? |
| Success | How do they know their action succeeded? Can they undo it? |

### 2.4 The interaction needs that are significant for the architecture

Phase 3 went through the list of SEI usability scenarios and turned each need retained into a `QS-n` ([03 § 2.6](03-quality-requirements.md#26-interaction-needs-that-are-significant-for-the-architecture)). Here, the agent describes the interaction that answers it, for example:

| Need (SEI scenario) | Interaction to describe | What phase 6 will have to make possible |
|---|---|---|
| Canceling an operation in progress (*Canceling Commands*) | Cancel button during a long process; the state after cancellation | Interrupt a process in progress and return to a consistent state |
| Observing the state of the system (*Observing System State*) | Progress, state of a launched task, alert when a piece of data changes | Expose the progress and push the changes, or allow them to be queried |
| Undoing (*Supporting Undo*) | "Undo" action, its scope and its duration | Keep what is needed to go back |
| Aggregating (*Aggregating Data*) | Act on several items at once | Process a batch as a single operation |
| Staying consistent across views (*Operating Consistently Across Views*) | Several views of the same data, synchronized | Propagate a change to every view |

Each answer is passed on to phase 6, which handles it with an ADR (Architecture Decision Record). If the answer reveals a need that phase 3 had not seen, go back to that phase ([00-principles § 14](00-principles.md#14-going-back-and-change-management)).

### 2.5 Throwaway prototype

In the *Propose* step, the agent **should** generate a clickable HTML prototype of the *Must* journeys, in `design/prototypes/`. The decision-maker approves by handling it rather than by reading: an interaction is judged by using it.

The prototype is **throwaway**: it contains no business rule, it is never reused in the product, and its data is fictitious and flagged as such (golden rule 1). It can serve for a first evaluation: the "evaluate" activity starts at the earliest stages of the project (ISO/IEC 25063, introduction), for example with a few users from the context of use (ISO 9241-210, § 7.5.4).

### 2.6 What the phase does not do

| Topic | Where it is handled |
|---|---|
| Business rules | Phase 2 (`BR-n`) |
| Measures of quality in use (effectiveness, efficiency, satisfaction) | Phase 3 (`QS-n`) |
| Mechanisms that make cancellation, progress or synchronization possible | Phase 6 (ADR) |
| Interface framework, component system, appearance | Phase 7 |
| API contracts served to the screens | Phase 8, from the per-screen needs |
| Usability tests on the product | Phase 11 |

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Rereads the context of use, the `UC-n`, the `IR-n`, the journeys, the interaction capability `QS-n` and the glossary. Lists the significant interaction needs. | Confirms. |
| 2 | Proposes the map of the screens and of the navigation, linked to the `UC-n`. | Corrects. |
| 3 | For each *Must* `UC-n`: writes the interaction specification and draws the screen sketches. | Corrects the flow. |
| 4 | Enumerates the states of each screen (§ 2.3). | Settles each case. |
| 5 | Describes the interaction answer to each significant need and what it requires from the architecture (§ 2.4). | Arbitrates. |
| 6 | Generates the throwaway prototype of the *Must* journeys (§ 2.5). | Handles it, corrects. |
| 7 | Lists, per screen, the data read and the actions sent. | — |
| 8 | Runs the checklist and invokes the critical reviewer, who also checks the prototype against Jakob Nielsen's ten heuristics. | Approves G5. |

## 4. Question bank

1. Does the context of use from phase 1 hold for this screen, or does the screen serve a particular situation?
2. What must the user see first in order to decide?
3. When an operation lasts more than a few seconds, what must they be able to do: wait, carry on elsewhere, cancel?
4. Which actions must be undoable, and until when?
5. What must they see when the data displayed is no longer up to date?
6. Which errors can they make here? Must the system prevent them, signal them or allow them to be corrected?
7. Must they see several views of the same data at the same time? Must those views stay synchronized?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `05-interaction.md` | Screen map, interaction specification of the *Must* `UC-n`, screen states, answers to the significant needs, per-screen needs |
| `prototypes/` | Throwaway prototype of the *Must* journeys |
| `STATE.md` | `OD-n` (open decisions) arising from the phase |
| `traceability.md` | Links `IR-n` → screen |

## 6. Gate G5 checklist

- [ ] ★ Every screen traces back to at least one `UC-n`, and every `IR-n` is satisfied by at least one screen.
- [ ] ★ Every interaction need that is significant for the architecture has its interaction answer, passed on to phase 6.
- [ ] ★ Every screen of the *Must* `UC-n` has its states described (§ 2.3), or marked "not applicable".
- [ ] No screen carries a business rule.
- [ ] The labels use the terms of the domain glossary.
- [ ] The decision-maker has handled the *Must* journeys on the prototype, or has explicitly chosen not to.
- [ ] The accessibility requirements of phase 3 are taken into account in the sketches.
- [ ] The data read and the actions sent by each screen are listed for phase 8.
- [ ] No choice of appearance or of framework is made (phase 7).
- [ ] The critical reviewer has checked the prototype against Jakob Nielsen's ten heuristics (*Product* and *Critical* profiles); this single-evaluator review does not replace the evaluation of phase 11.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Screen before journey | Screens are drawn before the `UC-n` and the `IR-n` are known | Start from the journey map (§ 2.2). |
| Rule hidden in the screen | A business validation exists only in a sketch | Send it back up as a `BR-n` (phase 2). |
| Happy path only | No error, loading or stale-data state | Enumerate the states of each screen (§ 2.3). |
| Premature visual polish | Colors are debated before the journeys are approved | Low fidelity; appearance comes in phase 7. |
| Prototype turned product | The prototype's code is reused as it is | Throwaway prototype, in `prototypes/`, never delivered. |
| Significant need discovered during coding | "We should be able to cancel this calculation", once the architecture is frozen | SEI list in phase 3, interaction answer here, ADR in phase 6. |
