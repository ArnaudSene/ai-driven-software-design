# 11 — Test strategy — <Project name>

| Status | Version | Date | Gate |
|---|---|---|---|
| Draft | 0.1 | <YYYY-MM-DD> | G11: — |

## 1. From requirement to test

| Source | Test type | Level | Tool | Execution |
|---|---|---|---|---|
| Rule examples (BR-n.Ek) | Domain unit | | | On every change |
| Acceptance criteria (AC-n) | Acceptance | | | On every change |
| Contracts | Contract | | | On every change |
| Adapters | Integration | | | On every change |
| Performance QS-n | Load | | | |
| Availability and recovery QS-n | Resilience, restore | | | |
| T-n | Security | | | |
| Critical journeys | End-to-end | | | |
| Interaction requirements (IR-n) | Journey | | | |
| Interaction capability QS-n | Usability evaluation (heuristics, testing with users, SUS (System Usability Scale)) | | | |

## 2. Fitness functions

| Id | Rule checked | Requirement (QS-n, ADR (Architecture Decision Record)) | Tool | When | Failure threshold |
|---|---|---|---|---|---|
| FF-1 | | | | | |

## 3. Determinism and test data

## 4. Pipeline checks

| Check | Threshold | Blocking |
|---|---|---|
| | | |

## 5. Definitions of "ready" and "done"

**Ready**: …

**Done**: …

## 6. Test naming convention

Each test cites the identifier it verifies: `test_BR_7_E2_<description>`, tag `@AC-11`.
