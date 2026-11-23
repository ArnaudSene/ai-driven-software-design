# Phase 3 — Quality requirements (non-functional)

| Key | Value |
|---|---|
| Central question | At what level of quality must the system operate? |
| Agent | [`prompts/quality-architect.md`](../prompts/quality-architect.md) |
| Inputs | `01-scoping.md` (G1), `02-functional-requirements.md` (G2) |
| Outputs | `design/03-quality-requirements.md` |
| Identifiers created | `QS-n`, additional `C-n`, `OD-n` |
| Template | [`templates/03-quality-requirements.md`](../templates/03-quality-requirements.md) |
| Gate | G3 |

---

## 1. Why this phase

Two systems that offer exactly the same functions can require radically different architectures. What sets them apart is their **quality attributes**: performance, availability, security, ease of modification…

**It is these attributes, not the features, that dictate the architecture.** An architecture chosen without explicit quality requirements is chosen out of habit or fashion. This phase is therefore the main input to phases 5 to 10.

## 2. Concepts and methods

### 2.1 ISO/IEC 25010 quality model

The ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25010 standard, 2023 version, serves as a **checklist** so that no family of requirements is forgotten:

| Characteristic | Useful sub-characteristics | Typical question |
|---|---|---|
| Functional suitability | Completeness, correctness, appropriateness | Must calculations be exact to the cent? |
| Performance efficiency | Time behaviour (response time), capacity, resource utilization | How many simultaneous users? What delay is acceptable? |
| Compatibility | Co-existence, interoperability | Which systems to exchange with, in which formats? |
| Interaction capability | Learnability, user error protection, inclusivity and user assistance (in 2023, the accessibility of the 2011 version was split into these last two) | Will people with disabilities use it? Can the user follow and interrupt a long operation? |
| Reliability | Availability, fault tolerance, recoverability | How much downtime is tolerable? How much data can be lost? |
| Security | Confidentiality, integrity, non-repudiation, accountability, authenticity | Which data is sensitive? Must it be possible to prove who did what? |
| Maintainability | Modularity, testability, modifiability | Which parts will change often? |
| Flexibility | Adaptability, installability, scalability | Will the hosting provider have to change, or the system be deployed at customers' sites? |
| Safety | Fail safe, hazard warning | Could a failure injure someone or cause material damage? |

### 2.2 Quality attribute scenario (`QS-n`)

The formalism of the SEI (Software Engineering Institute, Carnegie Mellon University), taken from *Software Architecture in Practice* (Bass, Clements, Kazman). A scenario makes a quality attribute **measurable**:

| Part | Question | Example |
|---|---|---|
| **Source** | Who or what triggers it? | 500 customers |
| **Stimulus** | What happens? | submit a booking simultaneously |
| **Environment** | What state is the system in? | under normal load, on a Saturday morning |
| **Artifact** | Which part is concerned? | the booking service |
| **Response** | What must the system do? | records each booking and confirms it |
| **Response measure** | How is it verified? | 95% of confirmations in less than [threshold to be set: 300 ms?], no double booking |

Each `QS-n` also carries the common fields of [00-principles § 7.1](00-principles.md#71-structure-of-a-rule): Source (where the requirement comes from), Rationale, Priority, and the link to the `BO-n`, `C-n` or `BR-n` that motivate it.

Full example:

```markdown
### QS-4 — Maximum data loss after an incident

- **Characteristic**: Reliability › recoverability
- **Source**: hardware failure of the primary hosting
- **Stimulus**: total loss of the primary storage
- **Environment**: normal operations, during the day
- **Artifact**: booking and payment data
- **Response**: the service is restored from the backups
- **Measure**: data loss ≤ [threshold to be set] minutes (RPO); service restored in ≤ [threshold to be set] hours (RTO)
- **Rationale**: a lost booking means a wronged customer and a dispute (BO-2).
- **Priority**: Must — the loss would go unnoticed until the customer complains.
- **Links**: BO-2, BR-3, C-5
- **OD**: OD-9 (RPO/RTO values to be weighed against the cost of the infrastructure)
```

RPO (Recovery Point Objective) is the maximum acceptable data loss, RTO (Recovery Time Objective) the maximum acceptable interruption time.

### 2.3 Load profile and data volumes

No performance scenario makes sense without orders of magnitude. The agent **must** obtain them from the decision-maker, even approximate ones, and **must not** invent them:

| Quantity | Today | In 1 year | In 3 years | Source |
|---|---|---|---|---|
| Registered users | | | | |
| Concurrent active users at peak | | | | |
| Key business operations per day (by type) | | | | |
| Hourly or seasonal peak | | | | |
| Volume of data created per year | | | | |
| Legal retention period | | | | |

A range ("between 100 and 1,000") is better than a blank: it is often enough to decide between two architectures.

### 2.4 Utility tree and prioritization

Each `QS-n` is ranked on two axes, rated H/M/L (high, medium, low):

- **business importance**, set by the decision-maker;
- **technical difficulty**, estimated by the agent.

The (H, H) and (H, M) scenarios are **architecturally significant**: phase 6 must answer each of them explicitly with an ADR (Architecture Decision Record) or a documented choice of style.

### 2.5 Cross-cutting requirements that are often forgotten

| Topic | Question to ask |
|---|---|
| Accessibility | Is the service subject to the RGAA (*Référentiel général d'amélioration de l'accessibilité*, the French accessibility standard), which transposes the WCAG (Web Content Accessibility Guidelines)? Which level should be targeted (`A`, `AA` or `AAA`), and in which version of the WCAG (2.2 is the most recent)? |
| Internationalization | Languages, date and number formats, time zones, currencies? |
| Auditability | Must it be possible to reconstruct who did what, when, and with which value before and after? For how long? |
| Archiving and purging | Legal retention periods; the right of individuals to erasure. |
| Degraded mode | What must keep working when an external system is unavailable? |
| Offline | Must the application work without a network? |
| Operating cost | Monthly ceiling for hosting and licenses? |
| Environmental footprint | A digital sobriety objective? |
| Operability | Who monitors the system, at what hours? Who gets woken up at night? |

### 2.6 Interaction needs that are significant for the architecture

Some interaction needs cannot be met by the screen alone: they require support from the architecture, and are expensive to add once the architecture is frozen. The SEI identified twenty-six of them, each described as a scenario with a stimulus, a response and an architectural pattern (Len Bass, Bonnie E. John, Jesse Kates, report `CMU/SEI-2001-TR-005`, 2001). The report offers them as a checklist for verifying that the requirements miss no important need. Examples:

| SEI scenario | Question for the decision-maker |
|---|---|
| Aggregating data (*Aggregating Data*) | Must the user act on several items at once? |
| Canceling an operation in progress (*Canceling Commands*) | Must they be able to interrupt a process in progress? |
| Observing the state of the system (*Observing System State*) | Must they see the progress of an operation, or be warned when a piece of data changes? |
| Undoing (*Supporting Undo*) | Which actions must be undoable, and until when? |
| Staying consistent across views (*Operating Consistently Across Views*) | Do they see several views of the same data, which must stay synchronized? |

The agent goes through the report's full list with the decision-maker. Each need retained becomes an interaction capability `QS-n`, or a performance one if it concerns a delay, with its six parts; the utility tree (§ 2.4) says whether it is significant. Phase 5 describes the interaction that answers it, phase 6 the architectural tactic.

**Quality in use** can be measured too: the ISO 9241-11:2018 standard defines usability by the effectiveness, efficiency and satisfaction of given users, for given goals, in a given context of use. A `QS-n` can set a target for each of them. For satisfaction, John Brooke's SUS (System Usability Scale) questionnaire gives a score from 0 to 100; it is in common use, but has never been standardized.

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Rereads phases 1 and 2 and extracts the implicit quality attributes from them ("the branches open at 8:00" → availability in the morning). | — |
| 2 | Collects the load profile (§ 2.3). | Gives the orders of magnitude. |
| 3 | Goes through the ISO/IEC 25010 characteristics one by one and asks the relevant questions. | Answers, points out what does not apply. |
| 4 | Goes through the SEI list of interaction needs (§ 2.6), if the system has end users. | Retains those that apply. |
| 5 | Writes a `QS-n` for each requirement expressed, with its six parts. | Sets the thresholds or leaves them [threshold to be set]. |
| 6 | Proposes the difficulty of each `QS-n`. | Sets the importance. |
| 7 | Identifies the **conflicts** between scenarios (security versus usability, consistency versus availability, cost versus redundancy) and presents them as trade-offs. | Arbitrates or opens open decisions (OD). |
| 8 | Runs the checklist and invokes the critical reviewer. | Approves G3. |

## 4. Question bank

1. Can the system be unavailable? When (at night, at the weekend) and for how long without serious consequences?
2. If the system lost the data of the last hour, what would the consequence be?
3. After how many seconds of waiting does a user give up?
4. Which data would be the most serious to see leaked? To see modified without anyone noticing?
5. Which parts of the business change most often (prices, rules, forms)? Who must be able to change them: a developer or an authorized user?
6. What is the expected lifetime of the system? Who will maintain it?
7. Will the system be deployed once, or for several customers (multi-tenant, on-premises installation)?
8. Are there predictable peaks (sales, month-end closing, back to school)?
9. What monthly operating budget is acceptable?
10. Which standards or certifications do customers or the sector require?
11. Does an operation last long enough for the user to want to follow it or interrupt it?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `03-quality-requirements.md` | Load profile, complete `QS-n`, retained interaction needs, utility tree, conflicts and trade-offs |
| `STATE.md` | `OD-n` on the thresholds; technical `R-n` that came to light |

## 6. Gate G3 checklist

- [ ] ★ The load profile is filled in, at least as orders of magnitude, or each gap is an OD.
- [ ] ★ Every `QS-n` has a quantified response measure or a [threshold to be set] attached to an OD.
- [ ] ★ Availability and acceptable data loss (RPO and RTO) have been explicitly asked about.
- [ ] ★ The architecturally significant `QS-n` are identified.
- [ ] Each of the nine ISO/IEC 25010 characteristics has been examined, and those judged not applicable are recorded as such.
- [ ] Conflicts between scenarios are listed with their trade-off or their OD.
- [ ] The accessibility, auditability and retention obligations are addressed.
- [ ] If the system has end users, the interaction needs on the SEI list are examined; those retained are `QS-n` whose significance is assessed.
- [ ] No `QS-n` prescribes a technology ("use a cache" is a solution; "95% of reads in less than 100 ms" is a requirement).

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Adjective without a measure | "The system must be fast, secure and scalable" | Turn each adjective into a six-part scenario. |
| Everything is a priority | All `QS-n` are *Must* and (H, H) | Force a relative ranking: "if you had to sacrifice one of the two?". |
| Magic availability | "100% availability" | Show the cost of each additional "9" and ask for the real cost of an hour of downtime. |
| Invented figures | 10,000 simultaneous users assumed by the AI (artificial intelligence) | Apply golden rule 1. |
| Disguised solution | "The system must use Kubernetes" | If it is imposed, it is a `C-n`; otherwise, extract the underlying need. |
