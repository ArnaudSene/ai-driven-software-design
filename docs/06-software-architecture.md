# Phase 6 — Software architecture

| Key | Value |
|---|---|
| Central question | How should the system be organized to satisfy the quality requirements? |
| Agent | [`prompts/software-architect.md`](../prompts/software-architect.md) |
| Inputs | Phases 1 to 5 approved; first of all the architecturally significant `QS-n`, the `BC-n` and the interaction responses from phase 5 |
| Outputs | `design/06-architecture.md` (arc42 structure), `design/adr/`, `diagrams/` |
| Identifiers created | `ADR-nnnn` |
| Templates | [`templates/06-architecture.md`](../templates/06-architecture.md), [`templates/adr.md`](../templates/adr.md) |
| Gate | G6 |

---

## 1. Why this phase

Architecture is the set of decisions that are **costly to undo**. This phase makes them deliberately, one by one, justifying each with a requirement, instead of letting them emerge by accident as the code grows.

Guiding principle: **the simplest architecture that satisfies the significant `QS-n`.** Any additional complexity (distribution, asynchrony, multiple databases) must be paid for by a precise quality scenario.

## 2. Concepts and methods

### 2.1 The dimensions of architecture are not mutually exclusive

Answers to different questions are often confused. Clean Architecture, event-driven architecture and DDD (Domain-Driven Design) **combine**:

| Dimension | Question | Typical options |
|---|---|---|
| Modeling | How is the business represented? | Rich model (tactical DDD), transaction script, simple CRUD (Create, Read, Update, Delete) |
| Internal organization of a module | How is a module's code arranged? | Layered, hexagonal (ports and adapters), Clean, onion, vertical slices |
| Decomposition and deployment | How many deployable units? | Monolith, modular monolith, services, microservices, serverless functions |
| Communication | How do the modules talk to each other? | Direct in-memory call, synchronous request-response, asynchronous messages or events |
| Data | Who owns which data? What consistency? | Shared database, database per module, strong or eventual consistency |
| User interfaces | How does each interface get its data? | A shared API (Application Programming Interface); one BFF (Backend for Frontend) per interface when their needs diverge |
| Reading and writing | A single model for reading and writing? | Single model, CQRS (Command Query Responsibility Segregation), event sourcing |

Modeling can **vary from one context to another**: a rich model and hexagonal architecture for a *Core* context, simple CRUD for a *Supporting* context.

### 2.2 Catalog of styles and their trade-offs

| Style | Favors | Costs | Choose when |
|---|---|---|---|
| **Modular monolith** | Simple operations, local transactions, easy refactoring, performance | Single deployment, scaling as a whole | **By default.** A team of fewer than about ten people; boundaries still shifting. |
| **Microservices** | Independent deployment and scaling, team autonomy | Distributed complexity: network, eventual consistency, observability, operations | Several autonomous teams; very different scaling needs between contexts; stable boundaries. |
| **Serverless (functions)** | No server to manage, cost proportional to usage | Cold start, provider dependency, hard local testing | Irregular load, short stateless processing. |
| **Event-driven** | Temporal decoupling, extensibility, resilience | Harder debugging and tracing, eventual consistency, message ordering | Chain reactions between contexts; tolerance for delay; absorbing peaks. |
| **CQRS** | Reads optimized independently of writes | Two models to maintain, synchronization lag | Reads and writes highly asymmetric in volume or shape. |
| **Event sourcing** | Complete, replayable history, built-in audit | High complexity, evolution of event schemas | Strong requirement for audit or state reconstruction; a domain naturally made of events. |
| **Hexagonal / Clean** | Testable domain, independent of infrastructure | More adapter code, indirections | *Core* contexts with rich logic and a long lifespan. |
| **Layered** | Simplicity, familiarity | The database leaks into the business logic | Simple *Supporting* contexts. |

Default recommendation, to be overturned by a quality scenario: a **modular monolith** whose modules are the `BC-n`, **hexagonal architecture** for the *Core* contexts, **in-memory calls** between modules through explicit interfaces, and **events** where eventual consistency is acceptable.

### 2.3 From quality scenarios to tactics

For each architecturally significant `QS-n`, the agent proposes **tactics** (in the SEI (Software Engineering Institute) sense) and compares them:

| Attribute | Usual tactics |
|---|---|
| Performance | Cache, precomputation, asynchronous processing, pagination, indexes, fewer round trips, parallelism |
| Availability | Redundancy, retry with increasing delay, circuit breaker, buffer queue, degraded mode, health check |
| Modifiability | Encapsulation, dependency inversion, external configuration, configurable rules, module boundaries |
| Security | Defense in depth, least privilege, validation at boundaries, encryption, audit logging |
| Testability | Dependency injection, pure domain without input/output, injectable clock, reproducible test data |
| Usability (interaction capability) | Support user initiative: cancel, undo, pause and resume, aggregate. Support system initiative: maintain a model of the task, of the user and of the system (*Software Architecture in Practice*, 3rd edition) |
| Consistency between modules | Local transaction, transactional *outbox* pattern, saga with compensation, idempotent consumers |

Each tactic retained is justified in an ADR (Architecture Decision Record). The significant interaction needs (phase 3), whose interaction was described in phase 5, are handled like any significant `QS-n`.

### 2.4 Architecture decision records (`ADR-nnnn`)

Format derived from Michael Nygard and from MADR (Markdown Architectural Decision Records). Full template: [`templates/adr.md`](../templates/adr.md).

| Section | Content |
|---|---|
| Status | Proposed, Accepted, Deprecated, Superseded by `ADR-nnnn` |
| Context | The problem and the forces at play, **with the identifiers** (`QS-n`, `C-n`, `BR-n`) |
| Options considered | At least two realistic options, often including "do nothing" or "the simplest" |
| Analysis | Advantages and drawbacks of each option **with regard to the requirements cited** |
| Decision | The option retained, stated in the affirmative |
| Consequences | Positive, negative, risks (`R-n`) and accepted debt |
| Verification | How we make sure the decision is respected: `FF-n`, review, `SLO-n` |

Criterion for writing an ADR: the decision is **costly to undo**, **non-obvious**, or **controversial**. An ADR runs one to two pages; beyond that, it hides several decisions.

### 2.5 C4 diagrams

Simon Brown's C4 (Context, Containers, Components, Code) model offers four zoom levels:

| Level | Shows | Mandatory |
|---|---|---|
| 1. System context | The system, its users, the external systems | Yes |
| 2. Containers | The deployable units and the stores (web application, service, database, message queue) and their protocols | Yes |
| 3. Components | The inside of a container: modules, ports, adapters | For *Core* contexts |
| 4. Code | Classes | No: the code is the source of truth |

The diagrams are written in Mermaid (or Structurizr DSL (Domain-Specific Language) for large systems) in `diagrams/`. At level 2, a "container" is not a Docker container: it is any separate executable unit or store.

### 2.6 arc42 architecture document

`06-architecture.md` follows the arc42 structure (Gernot Starke, Peter Hruschka), several sections of which are fed by other phases:

| arc42 § | Section | Fed by |
|---|---|---|
| 1 | Introduction and goals | Phases 1 and 3 (summary and cross-references) |
| 2 | Constraints | `C-n` |
| 3 | Context and scope | Context diagram, C4 level 1 |
| 4 | Solution strategy | **This phase**: style, decomposition, key choices |
| 5 | Building block view | C4 levels 2 and 3, `BC-n` → modules |
| 6 | Runtime view | Sequence diagrams of the *Must* `UC-n` and of the error scenarios |
| 7 | Deployment view | Phase 10 |
| 8 | Cross-cutting concepts | **This phase**: errors, transactions, idempotence, logging, configuration, time, internationalization |
| 9 | Architecture decisions | Index of the ADRs |
| 10 | Quality requirements | Reference to `03-quality-requirements.md` |
| 11 | Risks and technical debt | Technical `R-n` |
| 12 | Glossary | Reference to `glossary.md` |

### 2.7 Cross-cutting concepts to decide

The agent **must** examine each of these topics and settle it (in section 8 of arc42 or in an ADR):

1. **Error handling**: business or technical errors, propagation, message to the user.
2. **Transactions and consistency**: where is the transactional boundary? How is consistency between modules guaranteed?
3. **Idempotence**: what happens if a request or a message arrives twice?
4. **Concurrency**: optimistic or pessimistic locking for the concurrent accesses identified in phase 2.
5. **Time**: injectable clock, time zones, storage in Coordinated Universal Time.
6. **Configuration and secrets**: separation of code / configuration / secrets.
7. **Logging, metrics, traces**: groundwork for phase 10.
8. **Validation**: where are inputs validated (boundary) and invariants (domain)?
9. **Internationalization**, if required by a `QS-n`.
10. **Dependency rules** between modules and layers: which ones will be checked automatically (phase 11, `FF-n`).

### 2.8 Lightweight ATAM review (*Critical* profile, recommended for *Product*)

The ATAM (Architecture Tradeoff Analysis Method) confronts the architecture with the scenarios. Lightweight version led by the critical reviewer:

1. For each significant `QS-n`, walk the scenario through the diagrams: which components take part? Is the measure achievable?
2. Note the **sensitivity points**: decisions on which an attribute depends heavily.
3. Note the **trade-offs**: decisions that improve one attribute at the expense of another.
4. Note the **risks** (`R-n`) and the **non-risks** (sound, confirmed decisions).

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Lists the significant `QS-n`, the `C-n` and the `BC-n` that shape the architecture. | Confirms the priorities. |
| 2 | Proposes the **solution strategy**: decomposition style, internal organization by context type, communication mode. Writes the corresponding ADR with at least two options. | Arbitrates. |
| 3 | For each significant `QS-n`: tactics, options, ADR. | Arbitrates the trade-offs. |
| 4 | Draws C4 levels 1 and 2, then level 3 for the *Core* contexts. | Reviews. |
| 5 | Draws the runtime views of the *Must* `UC-n` and of at least one failure scenario. | Reviews. |
| 6 | Settles the cross-cutting concepts (§ 2.7). | Arbitrates if needed. |
| 7 | Leads the lightweight ATAM review if the profile requires it. | Arbitrates the risks. |
| 8 | Runs the checklist and invokes the critical reviewer. | Approves G6. |

**Product** choices (which database, which framework) are **not** made here. We decide "a transactional relational database" or "a message broker with ordering guaranteed per key", and phase 7 chooses the product. Exception: the `C-n` that already impose a product.

## 4. Question bank

1. How many people will develop and maintain this system? In how many teams? *(Conway's law: architecture tends to mirror the organization)*
2. Has the team already operated a distributed system in production?
3. Can this processing happen a few seconds later, or must the user see its result immediately?
4. Does this context have scaling needs very different from the others?
5. If this external system goes down, what must happen on our side?
6. Would you accept more complexity today in order to be able to split this module off later?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `06-architecture.md` | arc42 sections 1 to 6, 8, 9, 11 filled in; 7 waiting for phase 10 |
| `adr/ADR-0001-*.md` … | Solution strategy, one decision per significant `QS-n`, structuring cross-cutting concepts |
| `diagrams/` | C4 levels 1, 2, (3), sequences |

## 6. Gate G6 checklist

- [ ] ★ The solution strategy is the subject of an ADR that compares at least two options.
- [ ] ★ Each significant `QS-n` is addressed by an ADR or by a named section of the document.
- [ ] Each significant interaction need, whose interaction was described in phase 5, has its ADR.
- [ ] ★ The C4 level 1 and 2 diagrams exist and are consistent with the context map.
- [ ] Each ADR cites the requirements that motivate it and states how it will be verified.
- [ ] Each `BC-n` corresponds to an identified module or service.
- [ ] The ten cross-cutting concepts of § 2.7 are settled or explicitly deferred.
- [ ] At least one failure scenario is walked through as a runtime view.
- [ ] Any distributed complexity (several deployable units, asynchrony, several databases) is justified by a `QS-n` or a `C-n`.
- [ ] No product is chosen without a `C-n` that imposes it (products belong to phase 7).
- [ ] Lightweight ATAM review done if the profile is *Critical*.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Showcase architecture | Microservices, Kubernetes and event sourcing for three screens | Demand the `QS-n` that justifies each element of complexity. |
| Big-ball-of-mud monolith | No internal boundary, everything depends on everything | Modules = `BC-n`, dependencies checked by `FF-n`. |
| Shared-database microservices | Several services write to the same tables | One database (or one schema) per owner; integration through an interface or an event. |
| After-the-fact ADR | ADRs written afterwards to justify the code | Write the ADR before implementing, with status *Proposed*. |
| Single option | ADR without an alternative | Always at least two options, including the simplest. |
| Happy path only | No runtime view of a failure | Walk through at least one failure scenario per external dependency. |
