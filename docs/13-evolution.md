# Phase 13 — Design evolution

| Key | Value |
|---|---|
| Central question | How does the design stay true throughout the life of the system? |
| Agent | Orchestrator ([`AGENTS.md`](../AGENTS.md)), supported by the specialist concerned by each change |
| Inputs | Complete `design/`, code, production results |
| Outputs | Revised deliverables, new ADR (Architecture Decision Record) entries, `STATE.md` log |
| Identifiers created | All, depending on the changes |
| Gate | No global gate; each structural change is approved by the decision-maker |

---

## 1. Why this phase

A design that is not maintained becomes **wrong**, and wrong documentation is worse than no documentation: it misleads humans and AI (artificial intelligence) agents alike, who will follow it to the letter.

Phase 13 starts with the first line of code and only stops when the system is retired.

## 2. Concepts and methods

### 2.1 Update triggers

| Trigger | Action |
|---|---|
| New business request | Lightweight rerun of phase 2 (new `UC-n` and `BR-n`), then of phases 3 to 11 depending on the impact |
| Business rule discovered during development | New `BR-n` approved by the decision-maker **before** it is coded |
| Necessary deviation from an ADR | New ADR that supersedes the old one; the old one moves to *Superseded by* |
| OD (open decision) resolved | Update of the elements marked [threshold to be set] and of the associated tests |
| Failure of a fitness function (`FF-n`) | Fix the code, **or** decide by ADR that the rule changes; never disable it silently |
| Production incident | Analysis; check of the `QS-n`, `SLO-n` and `T-n` concerned; update if the requirement or the measure was wrong |
| `SLO-n` regularly missed or always met by a wide margin | Review the original `QS-n` with the decision-maker |
| Measurement of the `BO-n` after release | Back to phase 1 if the objective is not met: was the problem well understood? |
| New vulnerability or new legal obligation | Phase 9, then impacts |
| End of support of a technology | Phase 7, new ADR |
| User feedback, usage measurements in production | Phase 5, and phase 2 if an `IR-n` changes. The ISO (International Organization for Standardization) 9241-210 standard provides for this follow-up over time (§ 7.5.6). |

### 2.2 Change procedure

It applies § 14 of the [principles](00-principles.md#14-going-back-and-change-management):

1. Identify the elements affected.
2. Walk through the traceability matrix to list the upstream and downstream impact.
3. Have the decision-maker decide.
4. Modify the deliverables (dated revision note), write the new ADRs, update the tests.
5. Record it in the `STATE.md` log.

### 2.3 Automatic guardrails against drift

The design stays true all the more easily when part of it is **verified by the machine**:

| Design element | Guardrail |
|---|---|
| Dependency rules, module boundaries | Blocking `FF-n` in the pipeline |
| Interface contracts | Contract tests, compatibility comparison |
| `BR-n` and `AC-n` | Tests that cite the identifiers; traceability matrix generated from the test tags |
| Performance `QS-n` | Periodic load tests, `SLO-n` in production |
| Diagrams | Generated from the code or the model when possible; otherwise, reviewed at each increment |

### 2.4 Work of the coding agents

During delivery, a coding agent that applies this guide **must**:

1. Before coding a feature, read the `UC-n`, `BR-n`, `AC-n`, ADRs and `FF-n` that concern it.
2. Use the glossary's names.
3. Write first the tests derived from the examples and the acceptance criteria.
4. Cite the identifiers in the tests, the commit messages and the pull request description.
5. Stop and ask the decision-maker instead of settling a business ambiguity alone; propose an OD (open decision).
6. Propose an ADR instead of working around an architecture decision.
7. Flag any divergence observed between the existing code and the design.

### 2.5 Periodic reviews

| Frequency | Review |
|---|---|
| At each increment | ODs resolved, `R-n` up to date, traceability, glossary |
| Each quarter (*Product* and *Critical* profiles) | ADRs still valid? `QS-n` still accurate in the light of production? Technical debt? |
| Each year | Threat model, dependencies and ends of support, test of the DRP (disaster recovery plan) |

### 2.6 Technical debt register

Deliberate technical debt is recorded as an `R-n` of type "debt", with: origin (ADR or decision that accepted it), estimated cost of keeping it, repayment trigger, planned increment.

## 3. Change checklist

- [ ] The elements affected and their upstream and downstream impact are listed.
- [ ] The decision-maker has approved the change.
- [ ] The superseded ADRs are not modified; a new ADR supersedes them.
- [ ] The tests and the `FF-n` concerned are updated.
- [ ] The traceability and the glossary are up to date.
- [ ] The `STATE.md` log contains the dated entry.

## 4. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Fossil documentation | `design/` describes a system that no longer exists | Triggers of § 2.1, automatic guardrails. |
| Rewritten ADR | The history of decisions is erased | An accepted ADR is not modified: it is superseded. |
| Rule coded on the sly | A business rule appears in the code without a `BR-n` | Golden rule 1 and development guidelines. |
| Disabled fitness function | Architecture test commented out "temporarily" | Fix it, or change the rule by ADR. |
