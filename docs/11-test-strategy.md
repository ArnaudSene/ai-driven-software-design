# Phase 11 — Test and quality strategy

| Key | Value |
|---|---|
| Central question | How can we prove, automatically and repeatably, that the system conforms? |
| Agent | [`prompts/quality-engineer.md`](../prompts/quality-engineer.md) |
| Inputs | All previous phases, in particular `BR-n.Ek`, `AC-n`, `IR-n`, `QS-n`, `T-n`, ADR (Architecture Decision Record), `SLO-n`, contracts |
| Outputs | `design/11-test-strategy.md`, `traceability.md` completed down to the tests |
| Identifiers created | `FF-n` |
| Template | [`templates/11-test-strategy.md`](../templates/11-test-strategy.md) |
| Gate | G11 |

---

## 1. Why this phase

The previous phases produced fit criteria designed to fail deterministically. This phase decides **which type of test verifies what, where and when**, so that each requirement has an automatic proof.

It is also the phase that protects the architecture over time: without architecture tests, the boundaries drawn in phase 6 fade away within a few months.

## 2. Concepts and methods

### 2.1 From requirement to test

| Source | Test type | Level | Run |
|---|---|---|---|
| `BR-n.Ek` (examples of the rules) | Domain unit test | Pure domain, without input/output | On every change |
| `AC-n` (acceptance criteria) | Acceptance test (*Given / When / Then*) | Application, through its ports or its API (Application Programming Interface) | On every change |
| Contracts (`contracts/`) | Contract test (provider and consumers) | Boundary between contexts or with third parties | On every change |
| Adapters (database, messages, third parties) | Integration test with real components (real database in a container) | Adapter | On every change |
| Performance `QS-n` | Load and endurance test | System in pre-production | Before each release, or nightly |
| Availability and recovery `QS-n` | Resilience test (fault injection), restore test | System | Periodically |
| `T-n` (threats) | Automated security test; penetration test for the *Critical* profile | System | On every change (automated), periodically (manual) |
| Accessibility `QS-n` | Automated scan + manual audit | Interface | On every change (automated), before release (audit) |
| `IR-n` (interaction requirements) | Journey test on the interface, with simulated services; end-to-end only for critical journeys | Interface | On every change |
| Interaction capability `QS-n` | Usability evaluation (§ 2.9) | Prototype, then interface | In phase 5 on the prototype, then before release |
| ADRs and structural rules | Fitness function (`FF-n`) | Code and system | On every change |
| `SLO-n` | Production monitoring | Production | Continuously |
| Critical journeys | End-to-end test (few of them) | Complete system | Before release |

### 2.2 Distribution of tests

The test pyramid (Mike Cohn) remains the reference: **many** fast unit tests, **fewer** integration tests, **very few** end-to-end tests, which are slow and brittle.

For a hexagonal architecture, this naturally gives:

- the domain tested exhaustively, without database or network (examples of the `BR-n`);
- each adapter tested against the real technology;
- the use cases tested through the ports, with in-memory adapters (`AC-n`);
- a few end-to-end journeys to check the assembly.

### 2.3 Fitness functions (`FF-n`)

A fitness function (Neal Ford, Rebecca Parsons, Patrick Kua — *Building Evolutionary Architectures*) is an **automated test that verifies a characteristic of the architecture**:

| Example | Verifies | Possible tools |
|---|---|---|
| `FF-1`: the `domain` package imports nothing from `infrastructure` | Hexagonal dependency rule (strategy ADR) | ArchUnit, import-linter, dependency-cruiser |
| `FF-2`: no dependency cycle between modules | Boundaries of the `BC-n` | Same tools |
| `FF-3`: a module accesses only its own tables | Data ownership (phase 8) | Test on the queries, database permissions per module |
| `FF-4`: 95th percentile of `POST /bookings` < [QS-3 threshold] under nominal load | `QS-3` | Load-testing tool in the pipeline |
| `FF-5`: no incompatible change to the published contracts | Compatibility rules (phase 8) | OpenAPI / AsyncAPI contract comparator |
| `FF-6`: no dependency with a known critical vulnerability | Dependency policy (phases 7 and 9) | Dependency analysis |

`FF-n` sheet: requirement verified (`QS-n`, ADR), rule, tool, when it runs, failure threshold.

### 2.4 Requirement-driven tests

- **The name or tag of each test cites the identifier it verifies**: `test_BR_7_E2_late_cancellation_at_exact_limit` or `@AC-11`. The traceability matrix can then be generated from the code.
- Acceptance tests can be written in Gherkin and run by a BDD (Behavior-Driven Development) tool, in English since they are then code (golden rule 13), or written directly in the test language, keeping the *Given / When / Then* structure.
- TDD (Test-Driven Development) is recommended for the domain of the *Core* contexts: the examples of the `BR-n` are already the first tests.
- **Tests written by an AI (artificial intelligence)**: they must be derived from the specification (`BR-n.Ek`, `AC-n`), **not** from the existing code. A test inferred from the code confirms the code, errors included.

### 2.5 Determinism

A test that fails "sometimes" destroys confidence in the whole suite. Rules:

1. Injectable clock: no test depends on the real time.
2. Controlled randomness: fixed seeds, identifiers generated reproducibly.
3. Isolation: each test prepares and cleans up its own data.
4. No arbitrary waits: wait for a condition, not for a duration.
5. A flaky test is quarantined **and** fixed within a set deadline; it is never simply rerun until it passes.

### 2.6 Test data

- Synthetic datasets, built by readable test factories or builders.
- Boundary data taken from the examples of the `BR-n`.
- Never real personal data, except with verified anonymization (phase 9).

### 2.7 Quality checks in the pipeline

| Check | Threshold | Blocking |
|---|---|---|
| All tests pass | 100% | Yes |
| Fitness functions | No violation | Yes |
| Code coverage | Trend indicator; no absolute target imposed | No (alert if it drops) |
| Mutation tests on the *Core* domain | Minimum score [threshold to be set] | Depending on profile |
| Security analyses | No untreated critical or high vulnerability | Yes |
| Formatting and static analysis | No deviation | Yes |

Coverage measures what has been **executed**, not what has been **verified**. Mutation tests (deliberately introducing errors and checking that the tests detect them) better measure the quality of the domain tests.

### 2.8 Definition of "done" and of "ready"

- **DoR** (Definition of Ready): an increment can start when its `UC-n`, `BR-n` and `AC-n` are approved, its blocking ODs (open decisions) are resolved and its contracts are written.
- **DoD** (Definition of Done): an increment is done when its tests (examples, `AC-n`, `FF-n` concerned) pass in the pipeline, the traceability is up to date, the modified documentation has been reviewed, and it is deployed to pre-production.

### 2.9 Usability evaluation

| Method | What it provides | Reference |
|---|---|---|
| Heuristic evaluation | Three to five evaluators, each working separately, check the interface against Jakob Nielsen's ten heuristics | Nielsen Norman Group |
| Test with users | A facilitator, tasks, a participant: you observe where they stumble | ISO (International Organization for Standardization) 9241-210, § 7.5.4 |
| SUS (System Usability Scale) questionnaire | Satisfaction score from 0 to 100, to be compared with the `QS-n` target; in common use, never standardized | John Brooke |
| Accessibility audit | Automated scan and manual review at the target level | WCAG (Web Content Accessibility Guidelines) 2.2 |

The first evaluations are done on the phase 5 prototype, when fixing costs almost nothing. The report of an evaluation can follow the common format of the ISO 25062:2025 standard.

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Builds the requirement → test type table (§ 2.1) for the project. | Approves. |
| 2 | Sets the distribution of tests and the tools per level (consistently with phase 7). | Approves. |
| 3 | Writes the `FF-n` from the ADRs and the significant `QS-n`. | Approves. |
| 4 | Defines the determinism and test data rules. | — |
| 5 | Defines the pipeline checks and their thresholds. | Sets the thresholds. |
| 6 | Writes the DoR and the DoD. | Approves. |
| 7 | Completes `traceability.md` up to the "planned test" column. | — |
| 8 | Runs the checklist and invokes the critical reviewer. | Approves G11. |

## 4. Question bank

1. Who functionally validates an increment before its release?
2. Is there a test environment at each integrated third party?
3. Which functions, if they broke in production, would be the most serious? *(they deserve an end-to-end test)*
4. Is an accessibility audit or an external penetration test required or budgeted?
5. What maximum time do you accept for the integration pipeline?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `11-test-strategy.md` | Requirement → test table, distribution and tools, `FF-n`, determinism, data, pipeline checks, DoR, DoD |
| `traceability.md` | "Planned test" column filled in for each `BR-n.Ek`, `AC-n`, `IR-n`, *Must* `QS-n`, `T-n` |

## 6. Gate G11 checklist

- [ ] ★ Each `AC-n` and each example of a *Must* `BR-n` has a planned test.
- [ ] ★ The architecture's dependency rules are verified by at least one `FF-n`.
- [ ] ★ The DoD is written.
- [ ] Each *Must* `QS-n` is covered by a test, an `FF-n` or an `SLO-n`.
- [ ] Each mitigated `T-n` has a verification.
- [ ] The contracts are verified by contract tests.
- [ ] The determinism rules are written.
- [ ] The blocking pipeline checks are listed with their thresholds.
- [ ] A restore test is planned (phase 10).
- [ ] Each `IR-n` has a planned journey test; each interaction capability `QS-n` has its evaluation method.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Inverted pyramid | Mostly slow, unstable end-to-end tests | Push the checks down to the lowest possible level. |
| Coverage cult | "80% coverage" required, assertions missing | Coverage as an indicator; mutation tests on the core. |
| Mirror tests | Tests generated from the code, which reproduce its errors | Derive the tests from the examples and the criteria. |
| Mocks everywhere | Database and network simulated in every test | Test the adapters against the real technology. |
| Unguarded architecture | Dependency rules in a document nobody reads | Turn them into blocking `FF-n`. |
