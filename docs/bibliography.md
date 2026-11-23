# Bibliography

Works and references on which the guide relies, grouped by phase. Links and editions should be checked at the time of reading.

## Requirements (phases 1 to 3)

| Reference | Contribution to the guide |
|---|---|
| Suzanne Robertson, James Robertson — *Mastering the Requirements Process* | Volere framework, fit criterion, onion model of stakeholders |
| Alistair Cockburn — *Writing Effective Use Cases* | Use case format, goal levels, minimal guarantees |
| Matt Wynne — *Introducing Example Mapping* (article, 2015) | Rules / examples / questions workshop |
| Alistair Mavin et al. — *Easy Approach to Requirements Syntax* (article, 2009) | EARS (Easy Approach to Requirements Syntax) sentence templates |
| Gojko Adzic — *Specification by Example* | Examples as an executable specification |
| Geoffrey Moore — *Crossing the Chasm* | Vision statement template |
| Len Bass, Paul Clements, Rick Kazman — *Software Architecture in Practice* (3rd edition for the usability tactics) | Quality attribute scenarios, tactics, utility tree |
| ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25010:2023 | Quality model for software products |

## Domain (phase 4)

| Reference | Contribution to the guide |
|---|---|
| Eric Evans — *Domain-Driven Design* | Ubiquitous language, bounded contexts, context map, aggregates |
| Vaughn Vernon — *Implementing Domain-Driven Design* and *Domain-Driven Design Distilled* | Putting it into practice, aggregate design rules |
| Vlad Khononov — *Learning Domain-Driven Design* | Classification of subdomains and the associated strategies |
| Alberto Brandolini — *Introducing EventStorming* | Event Storming workshop |

## Interaction (phases 1, 2, 3 and 5)

| Reference | Contribution to the guide |
|---|---|
| ISO (International Organization for Standardization) 9241-210:2019 — [human-centred design for interactive systems](https://www.iso.org/standard/77520.html) | Human-centered design activities; testing with users (§ 7.5.4); follow-up over time (§ 7.5.6) |
| ISO 9241-11:2018 — [usability, definitions and concepts](https://www.iso.org/standard/63500.html) | Effectiveness, efficiency, satisfaction (phase 3) |
| ISO/TR (Technical Report) 25060:2023 — framework of the common usability formats | Specification of the user-system interaction and of the interface (phase 5) |
| ISO/IEC (International Electrotechnical Commission) 25063:2014 — [description of the context of use](https://www.iso.org/standard/35789.html), under revision | Sketch of the context of use (phase 1); evaluation from the earliest stages of the project |
| ISO/IEC 25064:2013 — [user needs report](https://www.iso.org/standard/35790.html) | Place of interaction design during architecture design |
| ISO 25065:2019 — [user requirements specification](https://www.iso.org/standard/72189.html) | Interaction requirements (`IR-n`) and use-related quality requirements (`QS-n`) |
| ISO 25062:2025 — [usability evaluation report](https://www.iso.org/standard/84255.html) | Format of evaluation reports (phase 11) |
| [WCAG (Web Content Accessibility Guidelines) 2.2](https://www.w3.org/TR/WCAG22/), 2023 recommendation | Accessibility levels (phase 3), audit (phase 11) |
| Len Bass, Bonnie E. John, Jesse Kates — [*Achieving Usability Through Software Architecture*](https://www.sei.cmu.edu/library/achieving-usability-through-software-architecture/), SEI (Software Engineering Institute) technical report, 2001 | Twenty-six usability needs that require support from the architecture (phases 3, 5 and 6) |
| Len Bass, Bonnie E. John — [*Linking usability to software architecture patterns through general scenarios*](https://doi.org/10.1016/S0164-1212(02)00076-6), *Journal of Systems and Software*, 2003 | Published version of these scenarios |
| Elspeth Golden, Bonnie E. John, Len Bass — [paper](https://doi.org/10.1109/ICSE.2005.1553589) at the *International Conference on Software Engineering*, 2005; Bonnie E. John et al. — [paper](https://doi.org/10.1145/1570433.1570437) at the *Engineering Interactive Computing Systems* conference, 2009 | Architecture patterns in the service of usability |
| Eelke Folmer, Jan Bosch — [*Architecting for usability: a survey*](https://doi.org/10.1016/S0164-1212(02)00159-0), *Journal of Systems and Software*, 2004 | How the architecture constrains usability |
| Ryan Singer — [*Shape Up*](https://basecamp.com/shapeup/1.3-chapter-04), Basecamp, 2019 | Screen map (*breadboarding*), fat-marker sketches (phase 5) |
| Karen Holtzblatt, Hugh Beyer — *Contextual Design: Design for Life*, 2nd edition | Observing users in their context, when the context of use is poorly known |
| Alan Cooper, Robert Reimann, David Cronin, Christopher Noessel — *About Face*, 4th edition | Goal-directed design: personas, scenarios, design framework |
| Jakob Nielsen — [*10 Usability Heuristics for User Interface Design*](https://www.nngroup.com/articles/ten-usability-heuristics/) | Heuristic evaluation (phases 5 and 11) |
| Kate Moran — [*Usability Testing 101*](https://www.nngroup.com/articles/usability-testing-101/), Nielsen Norman Group | Testing with users (phase 11) |
| John Brooke — SUS (System Usability Scale) questionnaire, presented in 1996; *SUS: A Retrospective*, *Journal of Usability Studies*, 2013 | Measuring user satisfaction (phases 3 and 11) |

## Architecture and technologies (phases 6 and 7)

| Reference | Contribution to the guide |
|---|---|
| Simon Brown — C4 (Context, Containers, Components, Code) model: *The C4 model for visualising software architecture* | Four-level architecture diagrams |
| Gernot Starke, Peter Hruschka — arc42 template | Structure of the architecture document |
| Michael Nygard — *Documenting Architecture Decisions* (article, 2011) | ADR (Architecture Decision Record) |
| Rick Kazman, Mark Klein, Paul Clements — ATAM (Architecture Tradeoff Analysis Method), SEI (Software Engineering Institute) technical report, 2000 | Lightweight architecture review |
| Mark Richards, Neal Ford — *Fundamentals of Software Architecture* | Catalog of styles and their trade-offs |
| Robert C. Martin — *Clean Architecture* | Dependency rule |
| Alistair Cockburn — *Hexagonal Architecture* (article, 2005) | Ports and adapters |
| Sam Newman — *Building Microservices* and *Monolith to Microservices* | Decomposition criteria, modular monolith |
| Martin Kleppmann — *Designing Data-Intensive Applications* | Consistency, replication, event streams |
| Sam Newman — [*Backends For Frontends*](https://samnewman.io/patterns/architectural/bff/) (article, 2015) | One access service per user interface (phases 6 and 8) |
| ThoughtWorks — *Technology Radar* | Classification of technologies (adopt, trial, assess, hold) |

## Data, security, operations, tests (phases 8 to 11)

| Reference | Contribution to the guide |
|---|---|
| Chris Richardson — *Microservices Patterns* | Saga, transactional *outbox* |
| CQRS (Command Query Responsibility Segregation): Udi Dahan — [*Clarified CQRS*](https://udidahan.com/2009/12/09/clarified-cqrs/) (article, 2009); Martin Fowler — [*CQRS*](https://martinfowler.com/bliki/CQRS.html) (article, 2011) | Read models tailored to the screens, and their limits (phase 8) |
| RFC (Request For Comments) 9457 — problem details for HTTP (Hypertext Transfer Protocol) APIs (Application Programming Interfaces) | Uniform error format for interfaces |
| Adam Shostack — *Threat Modeling: Designing for Security* | Four questions, STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege) |
| OWASP (Open Worldwide Application Security Project) — ASVS (Application Security Verification Standard), Top 10 | Levels of security requirements |
| CNIL (*Commission nationale de l'informatique et des libertés*, the French data protection authority) — GDPR (General Data Protection Regulation) practical guides | Protection of personal data |
| Betsy Beyer et al. — *Site Reliability Engineering* and *The Site Reliability Workbook* (Google) | SLO (Service Level Objective), error budget, alerting on symptoms |
| Jez Humble, David Farley — *Continuous Delivery* | Delivery pipeline, artifact promotion |
| Mike Cohn — *Succeeding with Agile* | Test pyramid |
| Neal Ford, Rebecca Parsons, Patrick Kua — *Building Evolutionary Architectures* | Fitness functions |

## Delivery (phases 12 and 13)

| Reference | Contribution to the guide |
|---|---|
| Alistair Cockburn — *Crystal Clear* | Walking skeleton |
| Jeff Patton — *User Story Mapping* | Story mapping, slicing into releases; journey map (phases 2 and 5) |
| Bill Wake — INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable) criteria, 2003 article | Quality of user stories |
| Melvin Conway — *How Do Committees Invent?* (article, 1968) | Conway's law |
