# 10 — Infrastructure and operations — <Project name>

| Status | Version | Date | Gate |
|---|---|---|---|
| Draft | 0.1 | <YYYY-MM-DD> | G10: — |

## 1. Environments

| Environment | Role | Data | Deployment |
|---|---|---|---|
| Local | | Synthetic | |
| Integration | | Synthetic | Automatic |
| Pre-production | | Synthetic or anonymized | Automatic |
| Production | | Real | After approval |

## 2. Deployment topology

| Container | Hosting | Instances | Zones | Scaling | Requirement (QS-n) |
|---|---|---|---|---|---|
| | | | | | |

Diagram: see `06-architecture.md` § 7.

## 3. Integration and delivery pipeline

| Stage | Content | Blocking |
|---|---|---|
| | | |

Release strategy: … — Rollback: …

## 4. Observability

| Signal | Tool | Content | Retention |
|---|---|---|---|
| Logs | | | |
| Metrics | | | |
| Traces | | | |

| Alert | Symptom | Threshold | Procedure |
|---|---|---|---|
| | | | |

## 5. Service level objectives

| Id | Indicator | Target | Window | Originating requirement |
|---|---|---|---|---|
| SLO-1 | | | Rolling 30 days | QS-n |

## 6. Backup and recovery

| Data | Frequency | Location | Retention | Restore test | Objectives (data loss, downtime) |
|---|---|---|---|---|---|
| | | | | Frequency, last date | QS-n |

Disaster recovery plan: …

## 7. Day-to-day operations

| Subject | Organization |
|---|---|
| Runbooks | |
| On-call | |
| Incident management | |
| Capacity monitoring | |
| Cost monitoring | |
