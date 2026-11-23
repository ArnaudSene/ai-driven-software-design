# Phase 10 — Infrastructure and operations

| Key | Value |
|---|---|
| Central question | Where does the system run, how does it get there, and how do we know it is healthy? |
| Agent | [`prompts/platform-reliability-engineer.md`](../prompts/platform-reliability-engineer.md) |
| Inputs | `03-quality-requirements.md` (availability, RPO (Recovery Point Objective), RTO (Recovery Time Objective), load), `06`, `07`, `09` |
| Outputs | `design/10-operations.md`, section 7 of `06-architecture.md`, infrastructure ADR (Architecture Decision Record) entries |
| Identifiers created | `SLO-n` |
| Template | [`templates/10-operations.md`](../templates/10-operations.md) |
| Gate | G10 |

---

## 1. Why this phase

Software only has value in production. The way it is deployed, monitored, backed up and repaired follows directly from the quality requirements: an availability `QS-n` without monitoring or a recovery procedure is nothing but a wish.

This phase applies the principles of reliability engineering, known as SRE (Site Reliability Engineering): **measure what matters to the user, automate what repeats, prepare for what will break**.

## 2. Concepts and methods

### 2.1 Environments

| Environment | Role | Data |
|---|---|---|
| Local | Development and fast tests | Synthetic datasets |
| Integration | Automatic assembly on every change | Synthetic |
| Pre-production (staging) | Business validation, load tests, release rehearsals | Synthetic or anonymized, **never** unprotected real personal data |
| Production | Service to users | Real |

Parity principle: environments differ in their size and their configuration, not in their nature. The same artifact is promoted from one environment to the next, without being rebuilt.

### 2.2 Deployment topology

For each container of the C4 (Context, Containers, Components, Code) level 2: where it runs, how many instances, in which zones, how it scales. Redundancy is **sized by the availability `QS-n`**, not on principle:

| Target availability | Maximum annual downtime | Typical implication |
|---|---|---|
| 99% | ~3.65 days | One instance, fast restart, backups |
| 99.9% | ~8.8 hours | Several instances, database with a replica, zero-downtime deployment |
| 99.95% | ~4.4 hours | Several availability zones, automatic failover |
| 99.99% | ~53 minutes | Several zones, or even several regions, 24/7 operations — very high cost |

Deployment diagram in Mermaid in `diagrams/`, carried over into section 7 of `06-architecture.md`.

### 2.3 Infrastructure described as code

The infrastructure is described as versioned code: this is called IaC (Infrastructure as Code). No manual change in production: every change goes through the repository, a review and an automated apply. Benefits: reproducibility, history, rebuilding after a disaster.

### 2.4 Integration and delivery pipeline

Continuous integration (CI) and continuous delivery (CD) form a pipeline whose typical stages are:

```
change ─► build ─► unit tests ─► analyses (quality, SCA, SAST, secrets)
       ─► integration tests ─► build of the signed artifact
       ─► deployment to integration ─► acceptance tests
       ─► deployment to pre-production ─► (approval) ─► production
```

The SCA (Software Composition Analysis, dependency analysis) and SAST (Static Application Security Testing, static security analysis) analyses are defined in phase 9.

Release strategies:

| Strategy | Principle | When |
|---|---|---|
| Progressive (*rolling*) | Replacement instance by instance | By default |
| Blue / green | Two environments, instant switchover | Immediate rollback required |
| Canary | New version on a fraction of the traffic, then widening | High traffic, high regression risk |
| Feature flags | Code deployed but disabled, activated separately | Decouple deployment from release |

**Rollback** is designed at the same time as deployment, including for schema migrations ("expand then contract" pattern from phase 8).

### 2.5 Observability

| Signal | Content | Rules |
|---|---|---|
| **Logs** | Structured events (key-value or JSON (JavaScript Object Notation) format) | Correlation identifier in every line; consistent levels; no sensitive data (phase 9) |
| **Metrics** | Aggregated numerical series | RED (Rate, Errors, Duration) method for services; USE (Utilization, Saturation, Errors) method for resources |
| **Traces** | Path of a request through the components | Recommended open standard: OpenTelemetry |

**Alert on symptoms, not on causes**: alert when users suffer (error rate, latency), not when a processor is at 80% load. Every alert must be **actionable** and point to a runbook.

### 2.6 Service level objectives (`SLO-n`)

| Term | Definition |
|---|---|
| SLI (Service Level Indicator) | Measure of the service as seen by the user: proportion of successful requests, proportion of requests served in under *x* ms |
| SLO (Service Level Objective) | Internal target on an indicator, over a window: "99.9% of requests successful over a rolling 30 days" |
| SLA (Service Level Agreement) | Contractual commitment to a customer, with penalties. Always less demanding than the SLO. |
| Error budget | 100% − SLO. As long as budget remains, we ship; once it is exhausted, reliability takes priority. |

Each `SLO-n` **derives** from a `QS-n` and cites it. A *Must* performance or availability `QS-n` without an `SLO-n` is a gap.

### 2.7 Backup, restore and recovery

| Element | Content |
|---|---|
| Backups | What, how often, where (another zone or region, offline or immutable copy), for how long |
| Restore | A written **and tested** procedure; a backup that has never been restored is not a backup |
| DRP (disaster recovery plan) | Disaster scenarios, procedure, roles, meeting the RPO and RTO of phase 3 |
| BCP (business continuity plan) | If the service must never stop: degraded operation during the incident |

### 2.8 Day-to-day operations

1. **Runbooks**: one per alert and per routine operation (restart, secret rotation, restore).
2. **On-call**: who is called, when, with what access. Must be consistent with the `QS-n` ("weekend availability" implies weekend on-call).
3. **Incident management**: roles, communication, then a **blameless** analysis and tracked corrective actions.
4. **Capacity**: tracking growth against the load profile of phase 3; scaling thresholds.
5. **Costs**: monthly estimate, resource tagging, budget alerts.

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Translates the availability, performance and recovery `QS-n` into infrastructure needs. | Confirms. |
| 2 | Proposes the environments and the deployment topology; writes the ADRs. | Arbitrates the cost / redundancy balance. |
| 3 | Proposes the integration and delivery pipeline and the release strategy. | Approves. |
| 4 | Defines observability and derives the `SLO-n` from the `QS-n`. | Approves the targets. |
| 5 | Designs backup, restore and, if the profile requires it, the DRP. | Approves. |
| 6 | Defines day-to-day operations: procedures, on-call, incidents, costs. | Appoints the people responsible. |
| 7 | Writes section 7 of arc42. Runs the checklist, invokes the critical reviewer. | Approves G10. |

## 4. Question bank

1. Who will operate the system: the development team, an operations team, a contractor?
2. Is there a hosting platform or monitoring tools imposed by the organization?
3. During what hours must the service be monitored? Who can be woken up at night?
4. How much does an hour of downtime cost? *(used to weigh the cost of redundancy)*
5. How often do you want to release to production?
6. What is the monthly hosting cost ceiling?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `10-operations.md` | Environments, topology, delivery pipeline, observability, `SLO-n`, backup and recovery, operations, costs |
| `06-architecture.md` § 7 | Deployment view |
| `adr/` | Hosting, topology, deployment strategy |

## 6. Gate G10 checklist

- [ ] ★ Each availability or recovery `QS-n` has a concrete translation in the topology and the backup.
- [ ] ★ The backup and the restore procedure are defined, with a scheduled restore test.
- [ ] ★ The delivery pipeline is described, rollback included.
- [ ] Each *Must* performance or availability `QS-n` has at least one `SLO-n`.
- [ ] Logs, metrics and traces are defined, with a correlation identifier.
- [ ] Alerts are on symptoms and point to a procedure.
- [ ] The infrastructure is described as code.
- [ ] On-call is consistent with the required availability hours.
- [ ] The estimated monthly cost fits the budget, or the gap has been arbitrated.
- [ ] The DRP exists if the profile is *Critical*.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Snowflake server | Configuration done by hand, impossible to reproduce | Infrastructure described as code, no manual change. |
| Schrödinger's backup | Backups never restored | Periodic restore test, timed against the RTO. |
| Alert storm | Dozens of non-actionable alerts | Alert on symptoms and on the `SLO-n`; remove any alert without an action. |
| Availability without on-call | 99.9% required, nobody available on the weekend | Align the organization with the `QS-n`, or revise the `QS-n`. |
| Production data in staging | Raw copy of production in pre-production | Synthetic or anonymized data. |
