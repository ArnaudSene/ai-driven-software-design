# Guide glossary

This glossary defines the acronyms and terms used **in the guide**. The business vocabulary of a project designed with the guide goes in that project's own `design/glossary.md` (phase 4).

Writing rule applied to the whole repository: **at the first occurrence of an acronym in each file, its long form is given in parentheses.** The rule applies file by file, because an agent may load only a single file. The script [`scripts/check_acronyms.py`](../scripts/check_acronyms.py) checks it.

---

## 1. Acronyms

| Acronym | Expansion | Definition |
|---|---|---|
| **ABAC** | Attribute-Based Access Control | Access control based on the attributes of the user, the resource and the context. |
| **AC** | Acceptance Criterion | Acceptance criterion: a condition, expressed as *Given / When / Then*, under which a use case is considered delivered. Prefix `AC-n`. |
| **ACL** | Anti-Corruption Layer | Anti-corruption layer: translates the model of an external system to protect the domain model. *Not to be confused with Access Control List, which this guide does not use.* |
| **ADR** | Architecture Decision Record | Architecture decision record: a short document that records a decision, its context, the options and the consequences. |
| **AI** | Artificial Intelligence | Here: the agent, based on a large language model, that drives the process. |
| **ANSSI** | Agence nationale de la sécurité des systèmes d'information | The French national cybersecurity agency. |
| **API** | Application Programming Interface | Programming interface through which a piece of software exposes its services to others. |
| **ASVS** | Application Security Verification Standard | Catalog of application security requirements published by the OWASP, in three levels. |
| **ATAM** | Architecture Tradeoff Analysis Method | SEI method for evaluating an architecture against its quality scenarios. |
| **BC** | Bounded Context | Bounded context: a boundary within which a model and its language are consistent. Prefix `BC-n`. |
| **BCP** | Business Continuity Plan | Arrangements that keep the service running, possibly in degraded mode, during a disaster. |
| **BDD** | Behavior-Driven Development | Behavior-driven development: specifications in the form of executable examples. |
| **BFF** | Backend for Frontend | Pattern that gives each user interface its own data access service, when their needs diverge (Sam Newman). |
| **BO** | Business Objective | Business objective: a measurable change expected in the real world. Prefix `BO-n`. |
| **BR** | Business Rule | Business rule. Prefix `BR-n`. |
| **C4** | Context, Containers, Components, Code | Simon Brown's model of architecture diagrams, in four zoom levels. |
| **CD** | Continuous Delivery / Continuous Deployment | Continuous delivery (every version is ready to be deployed) or continuous deployment (every version is deployed automatically). |
| **CI** | Continuous Integration | Continuous integration: every change is automatically built and tested. |
| **CNIL** | Commission nationale de l'informatique et des libertés | The French data protection authority. |
| **CQRS** | Command Query Responsibility Segregation | Separation of the write (command) and read (query) models. |
| **CRUD** | Create, Read, Update, Delete | The four elementary operations on data; denotes a model without rich business logic. |
| **CVE** | Common Vulnerabilities and Exposures | Public catalog of known vulnerabilities. |
| **DAST** | Dynamic Application Security Testing | Security testing of a running application. |
| **DBMS** | Database Management System | Software that stores and queries data. |
| **DDD** | Domain-Driven Design | Domain-driven design (Eric Evans). |
| **DoD** | Definition of Done | Definition of "done": the conditions for considering an increment complete. |
| **DoR** | Definition of Ready | Definition of "ready": the conditions for starting an increment. |
| **DORA** | Digital Operational Resilience Act | European regulation on the digital operational resilience of the financial sector. |
| **DPIA** | Data Protection Impact Assessment | Assessment required by the GDPR for processing that carries a high risk for individuals. |
| **DRP** | Disaster Recovery Plan | Procedure for restarting the service after a disaster. |
| **DSL** | Domain-Specific Language | Language dedicated to a particular domain. |
| **EARS** | Easy Approach to Requirements Syntax | Sentence templates for writing unambiguous requirements. |
| **FF** | Fitness Function | Fitness function: an automated test of a characteristic of the architecture. Prefix `FF-n`. |
| **GDPR** | General Data Protection Regulation | European regulation 2016/679 on personal data. |
| **gRPC** | gRPC Remote Procedure Calls | Remote procedure call protocol based on HTTP/2 and Protocol Buffers. |
| **HDS** | Hébergeur de données de santé | French certification required to host health data. |
| **HTML** | HyperText Markup Language | Language that describes web pages; the format of the throwaway prototypes of phase 5. |
| **HTTP** | Hypertext Transfer Protocol | The web's transfer protocol. |
| **IaaS** | Infrastructure as a Service | Infrastructure (machines, network, storage) rented on demand. |
| **IaC** | Infrastructure as Code | Infrastructure described by versioned code and applied automatically. |
| **IEC** | International Electrotechnical Commission | International electrotechnical commission, co-publisher of standards with the ISO. |
| **IETF** | Internet Engineering Task Force | Standards body for Internet protocols. |
| **INC** | Increment | Vertical slice of delivery. Prefix `INC-n`. |
| **INVEST** | Independent, Negotiable, Valuable, Estimable, Small, Testable | Quality criteria for a user story. |
| **IR** | Interaction Requirement | Interaction requirement: what the user must be able to do or see, without saying anything about the look of the screen. Prefix `IR-n`. |
| **ISO** | International Organization for Standardization | International standardization organization. |
| **JSON** | JavaScript Object Notation | Text format for exchanging structured data. |
| **LTS** | Long-Term Support | Version that receives extended support. |
| **MADR** | Markdown Architectural Decision Records | ADR template in Markdown format. |
| **MFA** | Multi-Factor Authentication | Multi-factor authentication. |
| **MIT** | Massachusetts Institute of Technology | Name of the permissive free license under which the guide is distributed. |
| **MoSCoW** | Must, Should, Could, Won't | Prioritization method: must, should, could, not this time. |
| **MVP** | Minimum Viable Product | Minimum viable product: the smallest version that makes it possible to learn whether the product meets its objectives. |
| **NIS** | Network and Information Security | European directive (version 2) on the security of network and information systems. |
| **OD** | Open Decision | Open decision: a question awaiting a ruling by the decision-maker. Prefix `OD-n`. |
| **OHS** | Open Host Service | Open host service: a stable interface exposed to all the consumers of a context. |
| **OIDC** | OpenID Connect | Federated authentication protocol based on OAuth 2. |
| **OWASP** | Open Worldwide Application Security Project | Foundation that publishes application security reference standards. |
| **PaaS** | Platform as a Service | Managed execution platform, rented on demand. |
| **PCI DSS** | Payment Card Industry Data Security Standard | Security standard for payment card data. |
| **PL** | Published Language | Published language: a documented exchange format shared between contexts. |
| **PoC** | Proof of Concept | Proof of concept: a throwaway prototype that answers a technical question. |
| **QS** | Quality Scenario | Six-part quality attribute scenario (source, stimulus, environment, artifact, response, measure). Prefix `QS-n`. |
| **RACI** | Responsible, Accountable, Consulted, Informed | Responsibility matrix: does the work, approves, is consulted, is informed. |
| **RBAC** | Role-Based Access Control | Role-based access control. |
| **RED** | Rate, Errors, Duration | Method for monitoring a service: rate, errors, duration. |
| **REST** | Representational State Transfer | Architectural style for interfaces over HTTP, centered on resources. |
| **RFC** | Request For Comments | Series of IETF standardization documents. |
| **RGAA** | Référentiel général d'amélioration de l'accessibilité | French digital accessibility standard, based on the WCAG. |
| **RPO** | Recovery Point Objective | Maximum acceptable data loss, expressed as a duration. |
| **RTO** | Recovery Time Objective | Maximum acceptable interruption time. |
| **SaaS** | Software as a Service | Software provided as an online service. |
| **SAST** | Static Application Security Testing | Security analysis of the source code, without executing it. |
| **SBOM** | Software Bill of Materials | Software bill of materials: an inventory of components and dependencies. |
| **SCA** | Software Composition Analysis | Analysis of third-party dependencies (vulnerabilities, licenses). |
| **SEI** | Software Engineering Institute | Carnegie Mellon University institute, author of quality scenarios and of the ATAM. |
| **SH** | Stakeholder | Stakeholder: a person or organization concerned by the system. Prefix `SH-n`. |
| **SLA** | Service Level Agreement | Contractual service level agreement. |
| **SLI** | Service Level Indicator | Service level indicator, measured from the user's point of view. |
| **SLO** | Service Level Objective | Service level objective. Prefix `SLO-n`. |
| **SRE** | Site Reliability Engineering | Engineering of the reliability of systems in production. |
| **SRC** | Source | Existing document read without being modified, cited by its identifier `SRC-n` (principles § 16). |
| **SSO** | Single Sign-On | Single authentication for several applications. |
| **STRIDE** | Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege | Threat classification: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. |
| **SUS** | System Usability Scale | Ten-question questionnaire that gives a satisfaction score from 0 to 100 (John Brooke); in common use, never standardized. |
| **TCO** | Total Cost of Ownership | Total cost of ownership. |
| **TDD** | Test-Driven Development | Test-driven development: the test is written before the code. |
| **TLS** | Transport Layer Security | Protocol for encrypting communications. |
| **TR** | Technical Report | ISO technical report: a reference document that does not have the status of a standard. |
| **UC** | Use Case | Use case. Prefix `UC-n`. |
| **URL** | Uniform Resource Locator | Address of a resource on the web. |
| **USE** | Utilization, Saturation, Errors | Method for monitoring a resource: utilization, saturation, errors. |
| **UTF** | Unicode Transformation Format | Family of Unicode character encodings; UTF-8 is the reference. |
| **UUID** | Universally Unique Identifier | 128-bit unique identifier; version 7 is time-ordered. |
| **WCAG** | Web Content Accessibility Guidelines | International guidelines for the accessibility of web content. |
| **YAML** | YAML Ain't Markup Language | Readable text serialization format, used for contracts and configuration. |

## 2. Single-letter identifier prefixes

| Prefix | English term | Meaning |
|---|---|---|
| `C-n` | Constraint | Constraint |
| `H-n` | Hypothesis | Hypothesis |
| `R-n` | Risk | Risk |
| `T-n` | Threat | Threat |

The full register of prefixes is in [00-principles § 8](00-principles.md#8-identifiers).

## 3. Terms

| Term | Definition |
|---|---|
| **Aggregate** | Group of domain objects modified as a whole, which guarantees invariants. A transaction modifies only one aggregate. |
| **arc42** | Architecture documentation template in twelve sections (Gernot Starke, Peter Hruschka). |
| **Architecturally significant** | Said of a quality scenario of high importance and high difficulty, which the architecture must address explicitly. |
| **Clean Architecture** | Variant of hexagonal architecture formalized by Robert C. Martin, based on the rule that dependencies point toward the center. |
| **Context map** | Diagram of the bounded contexts and of the relationship patterns between them. |
| **Context of use** | The users, their goals, their tasks and the environment in which they use the system (ISO/IEC 25063). Sketched in phase 1. |
| **Decision-maker** | The human who carries the product vision, arbitrates and approves the gates. |
| **Error budget** | Share of unavailability or errors tolerated by an SLO (Service Level Objective) over a time window. |
| **Event sourcing** | Persisting state as the sequence of events that produced it. |
| **Event Storming** | Modeling workshop based on business events (Alberto Brandolini). |
| **Example Mapping** | Workshop for discovering rules and examples using four types of cards (Matt Wynne). |
| **Fit criterion** | Measurable condition that makes it possible to write a test that fails deterministically when a rule is violated. |
| **Gate** | Human approval point that closes a phase. |
| **Gherkin** | *Given / When / Then* syntax for describing test scenarios. |
| **Hexagonal architecture** | Code organization in which the domain depends on nothing and communicates with the outside through *ports* implemented by *adapters* (Alistair Cockburn). Also called "ports and adapters". |
| **Idempotence** | Property of an operation whose repetition produces the same effect as a single execution. |
| **Modular monolith** | Application deployed as a single unit but split into modules with strict boundaries. |
| **Orchestrator** | AI (artificial intelligence) agent that drives the design process. |
| **Per-screen needs** | The data a screen reads and the actions it sends; described in phase 5, they feed the contracts of phase 8. |
| **Saga** | Sequence of local transactions with compensating actions in case of failure. |
| **Screen map** | The screens of a system, what can be done on them and the links between them; drawn up in phase 5. |
| **Screen sketch** | Low-fidelity sketch of a screen, without color or style, that shows what can be seen and done on it. |
| **Screen states** | What a screen shows when it is empty, loading, in error, partial, stale, without sufficient rights or after a success. Described in phase 5. |
| **Subdomain** | Part of the business, classified as *Core*, *Supporting* or *Generic*. |
| **Tactic** | Design technique that acts on a quality attribute (cache, redundancy, circuit breaker…). |
| **Threshold to be set** | The "[threshold to be set]" marker for a value expected from the decision-maker; always attached to an OD (Open Decision). |
| **Throwaway prototype** | Clickable prototype of the user journeys, generated in phase 5 to validate the interaction, never reused in the product. |
| **Transactional outbox** | Pattern that records an event in the same transaction as the business change, then publishes it reliably. |
| **Trust boundary** | Point where data or a request passes from one trust level to another. |
| **Ubiquitous language** | Vocabulary shared by the business, the documentation and the code within a bounded context. |
| **Volere** | Requirements specification framework by Suzanne and James Robertson. |
| **Walking skeleton** | Minimal implementation that runs through the whole architecture end to end. |
