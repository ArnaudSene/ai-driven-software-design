# Phase 9 — Security and compliance

| Key | Value |
|---|---|
| Central question | What must the system protect itself against, and which obligations must it meet? |
| Agent | [`prompts/security-specialist.md`](../prompts/security-specialist.md) |
| Inputs | `01-scoping.md` (legal `C-n`), `02` (role × action matrix), `03` (security `QS-n`), `06` (C4 (Context, Containers, Components, Code) level 2), `07`, `08` (data classification, contracts) |
| Outputs | `design/09-security.md`, security ADR (Architecture Decision Record) entries, additional `BR-n` and `QS-n` |
| Identifiers created | `T-n` |
| Template | [`templates/09-security.md`](../templates/09-security.md) |
| Gate | G9 |

---

## 1. Why this phase

Security added after the fact is expensive and stays fragile. Handled at design time, it often comes down to a few well-placed decisions: trust boundaries, authorization model, secrets management, logging.

This phase comes **after** the architecture and the data, because threats can only be modeled for a system whose flows and data are known. But it can **reopen** those phases: a threat can force a change of architecture (§ 14 of the principles).

## 2. Concepts and methods

### 2.1 Threat modeling

A method based on Adam Shostack's four questions:

1. **What are we working on?** A data flow diagram, built from the C4 level 2: processes, stores, flows, external actors and **trust boundaries** (any point where one passes from one trust level to another: Internet → application, application → database, application → third party).
2. **What can go wrong?** Applying STRIDE (the threat classification detailed below) to each element and to each flow that crosses a boundary.
3. **What do we do about it?** One measure per threat retained: avoid, reduce, transfer or accept.
4. **Did we do a good job?** Security review and tests (phase 11).

STRIDE (Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege):

| Category | Threat | Property violated | Typical question |
|---|---|---|---|
| **S**poofing | Identity spoofing | Authenticity | Can someone pass themselves off as a user or a service? |
| **T**ampering | Alteration | Integrity | Can a piece of data be modified in transit or at rest? |
| **R**epudiation | Repudiation | Non-repudiation | Can a user deny an action for lack of proof? |
| **I**nformation disclosure | Disclosure | Confidentiality | Can a piece of data leak (an interface's response, logs, error message, backup)? |
| **D**enial of service | Denial of service | Availability | Can a resource be exhausted or the service blocked? |
| **E**levation of privilege | Elevation of privilege | Authorization | Can a user do what their role does not allow? |

### 2.2 Threat sheet (`T-n`)

| Section | Content |
|---|---|
| Element or flow | Component or flow concerned, boundary crossed |
| STRIDE category | S, T, R, I, D or E |
| Scenario | How the attack unfolds, concretely |
| Likelihood | Low, Medium, High |
| Impact | Low, Medium, High, citing the data (classification from phase 8) |
| Response | Avoid, Reduce, Transfer, Accept (with the decision-maker's signature) |
| Measure | Control retained, with a reference to `ADR`, `BR-n` or `QS-n` |
| Verification | Test or check that proves the measure works |
| Status | Open, Mitigated, Accepted |

### 2.3 Security requirement level

Security requirements are based on the ASVS (Application Security Verification Standard) published by the OWASP (Open Worldwide Application Security Project), rather than reinvented:

| Profile | Target ASVS level |
|---|---|
| Prototype | Level 1 on the authentication, access control and input validation chapters |
| Product | Level 2 |
| Critical | Level 2 minimum, level 3 for the components that handle the most sensitive data |

The OWASP Top 10 serves as an awareness list, not as a requirements standard.

### 2.4 Security decisions to make

| Topic | Decisions |
|---|---|
| **Authentication** | Delegation to an identity provider via OIDC (OpenID Connect) or internal management; multi-factor authentication, known as MFA (Multi-Factor Authentication), for which roles; SSO (Single Sign-On) with the company directory; password policy or passwordless login |
| **Sessions and tokens** | Lifetime, renewal, revocation, client-side storage |
| **Authorization** | Model: RBAC (Role-Based Access Control), ABAC (Attribute-Based Access Control), relationship-based; built from the role × action matrix of phase 2; check **on the server side** on every request; isolation between client organizations |
| **Input validation** | At each trust boundary; output encoding |
| **Encryption** | In transit: TLS (Transport Layer Security) everywhere, including internally if the boundary justifies it. At rest: according to the data classification. Key management and rotation. |
| **Secrets** | Secrets vault; no secret in the code, the versioned configuration or the logs |
| **Security logging** | Events traced (logins, failures, permission changes, access to sensitive data); integrity and retention period of the logs; **no** sensitive data or secret logged |
| **Abuse protection** | Rate limiting, protection against automation, quotas |
| **Supply chain** | Dependency analysis, known as SCA (Software Composition Analysis); static code analysis, known as SAST (Static Application Security Testing); dynamic analysis, known as DAST (Dynamic Application Security Testing); SBOM (Software Bill of Materials); artifact signing |
| **Incident management** | Who is alerted, who decides, how individuals and authorities are notified, within what time limits |

Each structuring decision is the subject of an ADR.

### 2.5 Personal data protection

If the system processes personal data (classification from phase 8), the GDPR (General Data Protection Regulation) applies. The agent checks with the decision-maker:

| Item | Deliverable or decision |
|---|---|
| Purposes and legal basis | For each processing: why, and on what basis (contract, legal obligation, consent, legitimate interest…) |
| Minimization | Is each piece of data collected necessary for a purpose? |
| Retention periods | Taken from phase 8 |
| Data subject rights | Access, rectification, erasure, portability, objection: which `UC-n` implements them? |
| Processors | Hosting provider, service providers: contracts, location, transfers outside the European Union |
| Record of processing activities | Entry to be created or updated by the controller |
| DPIA (data protection impact assessment) | Mandatory in case of high risk for individuals (sensitive data on a large scale, systematic monitoring, profiling…) |
| Data protection officer | To be consulted if the organization has appointed one |

The agent **gives no legal advice**: it flags the likely obligations and recommends consulting a lawyer or the data protection officer. Official references, such as the recommendations of the CNIL (*Commission nationale de l'informatique et des libertés*, the French data protection authority) for France, must be checked at the source.

### 2.6 Other common compliance requirements

To be asked about depending on the sector, without claiming to be exhaustive; each obligation retained becomes a `C-n`:

| Domain | Examples of standards |
|---|---|
| Health | Hosting that is approved or certified under HDS (*Hébergeur de données de santé*, the French health data hosting certification) in France |
| Card payment | PCI DSS (Payment Card Industry Data Security Standard): often avoided by delegating card entry to the payment provider |
| Essential and important services | European NIS (Network and Information Security) 2 directive |
| Financial sector | European DORA (Digital Operational Resilience Act) regulation |
| Public services | RGAA (*Référentiel général d'amélioration de l'accessibilité*, the French accessibility standard, based on WCAG (Web Content Accessibility Guidelines)), the government's security standards |
| Sensitive cloud computing | SecNumCloud qualification issued by the ANSSI (*Agence nationale de la sécurité des systèmes d'information*, the French national cybersecurity agency) |

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Builds the data flow diagram and marks the trust boundaries. | Approves. |
| 2 | Applies STRIDE to each element and each flow crossing a boundary; writes the `T-n`. | Assesses the business impact. |
| 3 | Proposes a response and a measure for each `T-n`. | Accepts or refuses; signs off the accepted risks. |
| 4 | Sets the ASVS level and extracts the applicable requirements from it as `QS-n` or `BR-n`. | Approves. |
| 5 | Has the security decisions settled (§ 2.4) and writes the ADRs. | Arbitrates. |
| 6 | Leads the personal data protection review (§ 2.5). | Answers; consults the lawyer if needed. |
| 7 | Surveys the other compliance requirements (§ 2.6) and adds them as `C-n`. | Confirms. |
| 8 | Flags the upstream phases to reopen, if any. | Decides. |
| 9 | Runs the checklist and invokes the critical reviewer. | Approves G9. |

## 4. Question bank

1. What would be the worst possible data leak? And the worst silent modification?
2. Who are the plausible attackers: opportunists, competitors, malicious employees, fraudsters, states?
3. Is there a company directory or an identity provider to use?
4. Can a user belong to several organizations, with different permissions?
5. Must it be legally proven that a user performed an action (signature, timestamping)?
6. Does personal data leave the European Union, even for support or backup?
7. Does the organization have a security policy, a security officer, a data protection officer?
8. Who must be notified, and how quickly, in the event of a security incident?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `09-security.md` | Flow diagram and trust boundaries, register of the `T-n`, ASVS level, security decisions, data protection review, compliance |
| `adr/` | Authentication, authorization, secrets management, encryption |
| `02`, `03`, `01` | `BR-n`, `QS-n` and `C-n` added, marked "from phase 9" |

## 6. Gate G9 checklist

- [ ] ★ The trust boundaries are identified on a diagram.
- [ ] ★ The authorization model covers the whole role × action matrix and the check is done on the server side.
- [ ] ★ Secrets management is decided; no secret is planned in the code or the versioned configuration.
- [ ] ★ The presence of personal data is established and, where applicable, the GDPR review is done.
- [ ] Each flow crossing a boundary has been screened with STRIDE.
- [ ] Each `T-n` has a response; each accepted risk carries the decision-maker's explicit decision.
- [ ] Each measure has a planned verification (test, analysis, review).
- [ ] The ASVS level is set and its applicable requirements are carried over.
- [ ] Security logging and incident management are defined.
- [ ] The software supply chain is covered (dependencies, analyses, artifacts).
- [ ] Sector-specific compliance has been asked about.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Security through the interface | Buttons hidden for unauthorized roles, with no server-side check | Authorization checked on the server side, on every request. |
| Home-grown authentication | Custom-built password storage and verification | Delegate to a proven identity provider, unless justified by an ADR. |
| Chatty logs | Tokens, passwords or personal data in the logs | Explicit list of forbidden fields, automatic filtering. |
| Risk accepted by default | Threats without a response | One response per threat; acceptance is a signed decision. |
| Assumed compliance | "The GDPR does not concern us", without analysis | Go through the data classification of phase 8. |
| Lawyer agent | Definitive legal advice given by the AI (artificial intelligence) | Flag, recommend a lawyer or the data protection officer. |
