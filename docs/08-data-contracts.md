# Phase 8 — Data and interface contracts

| Key | Value |
|---|---|
| Central question | Which data, owned by whom, and which interfaces between the parts of the system and with the outside world? |
| Agent | [`prompts/data-interface-architect.md`](../prompts/data-interface-architect.md) |
| Inputs | `02-functional-requirements.md`, `04-domain.md`, `05-interaction.md` (needs per screen), `06-architecture.md`, `07-technology-choices.md` |
| Outputs | `design/08-data-contracts.md`, `design/contracts/` |
| Identifiers created | No new prefix; contracts are identified by their name and their version |
| Template | [`templates/08-data-contracts.md`](../templates/08-data-contracts.md) |
| Gate | G8 |

---

## 1. Why this phase

Data outlives code: a program can be rewritten, a badly designed database drags on for years. Interfaces, for their part, are **promises** made to others; breaking them is costly for everyone who depends on them.

This phase therefore settles, **before** implementation, what is the most costly to change afterwards: the structure and ownership of the data, and the interface contracts.

## 2. Concepts and methods

### 2.1 Data ownership

Fundamental rule: **each piece of data has one and only one owning context** (`BC-n`), the only one allowed to write it. The other contexts read it through an interface, receive it through an event, or keep a local read-only copy of it.

| Data | Owner | Consumers | Consumers' access mode |
|---|---|---|---|
| Booking | `BC-1` | `BC-2`, `BC-3` | Events `BookingConfirmed`, `BookingCancelled` |

### 2.2 Data model per context

Three levels, not to be confused:

| Level | Content | When |
|---|---|---|
| Conceptual | Business concepts and relationships, without technical attributes | Already started in phase 4 |
| Logical | Entities, attributes, abstract types, keys, cardinalities, integrity constraints | **This phase** |
| Physical | Tables, indexes, partitioning, DBMS (database management system) types | This phase for the critical structures; the rest is left to implementation |

The diagrams are written in Mermaid `erDiagram`. Each integrity constraint that embodies a business rule cites its `BR-n`.

### 2.3 Cross-cutting choices on data

The agent **must** have each of these points settled:

| Topic | Options and default recommendation |
|---|---|
| Identifiers | Generated technical identifier (version 7 UUID (Universally Unique Identifier), time-ordered) rather than a business key that may change; the business key remains unique through a constraint. |
| Amounts | Exact decimal or integer in the smallest unit (cents), **never** a floating-point number; currency stored with the amount. |
| Dates and times | Instants stored in Coordinated Universal Time; time zone kept when it has a business meaning ("2 p.m. Paris time"); ISO (International Organization for Standardization) 8601 format, the standard for representing dates in data interchange. |
| Deletion | Physical, logical (flagging) or archiving: to be decided per data type, consistently with erasure obligations. |
| History and audit | Audit table, row versioning, event log: depending on the auditability `QS-n`. |
| Multi-tenancy | If the system serves several client organizations: database per client, schema per client, or discriminator column. A major decision, which justifies an ADR (Architecture Decision Record). |
| Text | UTF-8 (Unicode Transformation Format, 8-bit) encoding everywhere; collation and sorting rules. |

### 2.4 Classification and lifecycle

Each dataset receives:

| Section | Values |
|---|---|
| Sensitivity | Public, Internal, Confidential, Secret |
| Personal data | No, Yes, Yes and sensitive within the meaning of the GDPR (General Data Protection Regulation): health, opinions, biometrics… |
| Retention period | Duration and basis (law, contract, consent) |
| End of life | Archiving, anonymization or purge, and who triggers it |
| Estimated volume | Taken from the load profile of phase 3 |

This classification feeds directly into phase 9.

### 2.5 Schema evolution

1. Every schema change goes through a **versioned migration**, replayable, kept in the repository.
2. For a release without downtime, apply the **expand and contract** pattern: add the new structure, write to both, migrate the data, switch reads over, then remove the old structure in a later version.
3. Migrations of large data volumes are designed to be interrupted and resumed.

### 2.6 Migrating existing data

If the existing material identified in phase 1 contains data to be migrated: inventory of the sources, field mapping, transformation and cleansing rules, handling of rejects, volumes, cutover strategy, success criteria (counts, checksums, samples checked by the business).

### 2.7 Interface contracts

**The interface is designed before its implementation**: the contract is a design deliverable, written in a standard format, reviewed, versioned, and used to generate tests and documentation.

| Type of exchange | Contract format |
|---|---|
| Request-response over HTTP (Hypertext Transfer Protocol), REST (Representational State Transfer) style | OpenAPI 3.x (`contracts/openapi.yaml`) |
| High-performance remote procedure calls | gRPC (gRPC Remote Procedure Calls) + Protocol Buffers (`.proto`) |
| Events and messages | AsyncAPI 3.x (`contracts/asyncapi.yaml`) + JSON (JavaScript Object Notation) Schema |
| Flexible client-side queries | GraphQL schema |
| Files exchanged in batches | Format specification + JSON Schema or description of the columns |

YAML (YAML Ain't Markup Language) is the recommended writing format for OpenAPI and AsyncAPI contracts.

Design rules for an HTTP API (Application Programming Interface), to be recorded and applied uniformly:

1. **Naming** of resources: plural nouns, in English, consistent with the glossary.
2. **Errors**: a uniform format, preferably that of RFC (Request For Comments) 9457, *Problem Details for HTTP APIs*; stable business error codes that cite the violated `BR-n` when relevant.
3. **Pagination, sorting, filtering**: a single mechanism for all collections.
4. **Idempotence**: an idempotency key is mandatory on non-idempotent creations (payment, order).
5. **Concurrency**: optimistic control (`ETag` / `If-Match` headers) on resources that several actors can modify.
6. **Versioning**: a single strategy (in the path, a header, or no version and only compatible changes).
7. **Compatibility**: adding an optional field is compatible; removing, renaming or making mandatory is not, and requires a new version and an announced deprecation period.
8. **Security**: authentication mechanism of each endpoint, specified in phase 9.

**Screen-driven contracts.** The needs per screen from phase 5 (data read, actions sent) are an input to the contracts, just like the use cases:

- when a screen needs a shape of data very different from the domain model, it is served a **read model** tailored to its view (Udi Dahan); this is a form of CQRS (Command Query Responsibility Segregation), to be reserved for the parts of the system where it is justified (Martin Fowler);
- errors have a **model designed for the user**: each business error code corresponds to a message and to the possible next action, consistent with the error states of phase 5;
- a **BFF** (Backend for Frontend: one access service per interface, after Sam Newman) is justified only if several interfaces have diverging needs, and is decided in phase 6;
- what the screen must see change without asking for it (progress, modified data) has its contract, for events or for polling, according to the mechanism decided in phase 6.

### 2.8 Events

| Topic | Rule |
|---|---|
| Naming | Past tense, in English, in the domain language: `BookingConfirmed` |
| Envelope | Unique identifier, type, schema version, instant of occurrence, correlation identifier, emitting context |
| Content | Minimal notification (identifier and type), or state transfer (data useful to the consumer): to be chosen per event |
| Delivery guarantee | "At least once" by default; consumers **must** be idempotent |
| Ordering | Guaranteed per key (for example per booking) only if an invariant requires it |
| Reliable publication | Transactional *outbox* pattern: the event is recorded in the same transaction as the change |
| Evolution | Same compatibility rules as for APIs; schema registry if there are several teams |

### 2.9 External integrations

For each external system: contract used (provided by the third party or to be negotiated), anti-corruption layer, authentication, call limits, behavior when unavailable (link with the degraded-mode `QS-n`), test environment provided by the third party.

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Draws up the data ownership table (§ 2.1). | Approves. |
| 2 | Produces the logical model of each context, citing the `BR-n` carried by constraints. | Reviews the cardinalities and the rules. |
| 3 | Has the cross-cutting choices settled (§ 2.3). | Arbitrates. |
| 4 | Classifies the data and sets their lifecycle (§ 2.4). | Gives the legal durations or opens ODs (open decisions). |
| 5 | Designs the migration of existing data if needed. | Provides the samples. |
| 6 | Writes the API design rules, then the contracts of the *Must* `UC-n` and of the needs per screen (phase 5). | Reviews. |
| 7 | Writes the event catalog and the AsyncAPI contract. | Reviews. |
| 8 | Describes each external integration. | Provides the third parties' documentation. |
| 9 | Runs the checklist and invokes the critical reviewer. | Approves G8. |

## 4. Question bank

1. How long must each type of data be kept, and why?
2. Must it be possible to retrieve the state of a record as it was on a past date?
3. Who, outside the application, reads this data (business intelligence, accounting, partners)?
4. Does some of the data come from an existing system? In what state of quality?
5. Will the system serve several client organizations whose data must be kept separate?
6. Will third-party applications consume our APIs? Can you require them to follow our changes?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `08-data-contracts.md` | Ownership, logical models, cross-cutting choices, classification and lifecycle, migration strategy, migration of existing data, API rules, event catalog, integrations |
| `contracts/openapi.yaml` | Endpoints of the *Must* `UC-n` |
| `contracts/asyncapi.yaml` | Events published between contexts |
| `diagrams/` | Mermaid data models |

## 6. Gate G8 checklist

- [ ] ★ Each piece of data has a single owning context.
- [ ] ★ Amounts, dates and identifiers follow the cross-cutting choices that were settled.
- [ ] ★ Each personal dataset has a retention period and an end of life.
- [ ] ★ The contracts of the *Must* `UC-n` exist in the standard format and are valid against their schema.
- [ ] Each screen of the *Must* `UC-n` (phase 5) finds the data it reads and its actions in a contract.
- [ ] The integrity constraints cite the `BR-n` they guarantee.
- [ ] The API design rules are written (errors, pagination, idempotence, versioning, compatibility).
- [ ] Each event has an envelope, an owner, a delivery guarantee and identified consumers.
- [ ] Reliable publication of events is addressed (*outbox* or equivalent).
- [ ] Each external integration has a defined behavior when unavailable.
- [ ] The migration of existing data is designed if the existing system requires it.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Integration database | Several contexts write to the same tables | One owner per piece of data; integration through an interface or an event. |
| Monetary floats | Amount stored as a floating-point number | Exact decimal or integer in cents. |
| Ambiguous local time | Dates stored without a time zone | Coordinated Universal Time + explicit business time zone. |
| API mirroring the database | Endpoints that expose the tables as they are | Design the API from the `UC-n`, not from the schema. |
| Contract after code | Documentation generated afterwards, never reviewed | Contract first, reviewed, then implemented and tested. |
| Naive consumer | Non-idempotent event consumer | Deduplication by event identifier. |
