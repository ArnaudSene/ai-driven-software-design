# Phase 7 — Technology choices

| Key | Value |
|---|---|
| Central question | With which languages, frameworks, products and services should the chosen architecture be built? |
| Agent | [`prompts/technology-advisor.md`](../prompts/technology-advisor.md) |
| Inputs | `06-architecture.md` and ADR (Architecture Decision Record) entries approved (G6), `05-interaction.md` (journeys, states, needs per screen), `C-n`, `QS-n` |
| Outputs | `design/07-technology-choices.md`, choice ADRs, proof-of-concept reports |
| Identifiers created | `ADR-nnnn` |
| Template | [`templates/07-technology-choices.md`](../templates/07-technology-choices.md) |
| Gate | G7 |

---

## 1. Why this phase

The architecture says **what** ("a transactional relational database", "a message broker"). This phase says **with what**. It comes after the architecture so that the technology serves the design, and not the other way round.

The best technical choice is rarely the most powerful in absolute terms: it is the one the team will be able to **master, operate and evolve** throughout the system's lifetime.

## 2. Concepts and methods

### 2.1 Inventory of the choices to make

The agent draws up the list of the choices needed from the containers of the C4 (Context, Containers, Components, Code) level 2 diagram and from the cross-cutting concepts:

Hosting models mentioned: IaaS (Infrastructure as a Service), PaaS (Platform as a Service), SaaS (Software as a Service).

| Category | Examples of decisions |
|---|---|
| Languages | Language of the server, of the client, of the scripts |
| Frameworks | Server web framework, interface framework and component system, which sets the look (colors, typography) when no brand guidelines are imposed (`C-n`), test framework |
| Persistence | DBMS (database management system), schema migration tool, data access layer |
| Communication | Interface format and protocol, message broker |
| Cross-cutting services | Identity provider, email sending, file storage, full-text search, cache |
| Hosting | Model (self-managed servers, IaaS, PaaS, SaaS, serverless functions), provider, region |
| Tooling | Version control, continuous integration (CI) and continuous delivery (CD), dependency management, code analysis |
| Observability | Logs, metrics, traces, alerts |

### 2.2 Selection method

For each structuring choice:

1. **Elimination filter.** Any option incompatible with a `C-n` (imposed or forbidden technology, license, sovereign hosting, budget) or with a *Must* `QS-n` is ruled out.
2. **Shortlist.** Two to four realistic options. Beyond that, the analysis becomes superficial.
3. **Weighted grid.** The decision-maker sets the weights, the agent proposes the scores **and justifies them**.
4. **Proof of concept** if the gap is small or if a technical uncertainty remains (§ 2.4).
5. **ADR** that records options, grid, decision and consequences.

### 2.3 Evaluation criteria

| Criterion | What we look at |
|---|---|
| Fit with the requirements | Are the `QS-n` and `C-n` concerned satisfied, and with what margin? |
| Team skills | Does the team master the tool? Cost and duration of upskilling? |
| Maturity and longevity | Age, project governance, release frequency, long-term support (LTS) policy, number of active maintainers |
| Ecosystem | Libraries, integrations, documentation, community |
| Hiring | Ease of finding profiles in the target market |
| Total cost | Licenses, hosting, training, operations: the TCO (Total Cost of Ownership) |
| Security | Track record of published vulnerabilities (CVE (Common Vulnerabilities and Exposures)) and responsiveness of fixes |
| License | Compatibility with the product's distribution model (permissive or reciprocal licenses) |
| Reversibility | Exit cost: open formats, standards, dependency on a provider |
| Operability | Monitoring, backup, updates, operations skills available |
| Frugality | Resource consumption, if a `QS-n` asks for it |

Example grid:

| Criterion | Weight | Option A | Option B | Option C |
|---|---|---|---|---|
| Fit with `QS-2`, `QS-5` | 5 | 4 — justification | 5 — justification | 3 — justification |
| Team skills | 4 | 5 | 2 | 3 |
| Reversibility | 2 | 4 | 3 | 5 |
| … | | | | |
| **Weighted total** | | | | |

The grid informs the decision, it does not make it. If the result contradicts the decision-maker's intuition, a criterion or a weight is missing: look for it rather than ignore one or the other.

### 2.4 Proof of concept

A proof of concept (a *spike*, or PoC (Proof of Concept)) is a **throwaway, time-boxed prototype** that answers **one** question:

| Section | Example |
|---|---|
| Question | Does framework X meet `QS-3` (500 requests per second under 300 ms at the 95th percentile) on our data model? |
| Maximum duration | 2 days |
| Success criterion | Measurement of the 95th percentile under simulated load |
| Result | Recorded in the ADR, "Analysis" section |
| Fate of the code | Thrown away. It is never promoted to production. |

### 2.5 Buy, reuse or build

For each *Generic* subdomain identified in phase 4, the default option is to **buy or reuse** (managed service, product, library). Building a generic subdomain must be justified by an ADR.

### 2.6 Dependency policy

Recorded in `07-technology-choices.md`:

1. Admission criteria for a third-party library: license, maintenance activity, popularity, number of transitive dependencies.
2. Version pinning and automated update tool.
3. Production of an SBOM (Software Bill of Materials) if the profile is *Critical* or if a customer requires it.
4. Frequency of dependency reviews.

### 2.7 Verify rather than remember

An AI (artificial intelligence) model's knowledge has a cutoff date. For any claim about a specific **version**, **end of support**, **license** or **feature**, the agent **must** either verify it (official documentation, the project's repository) or mark it "to be verified" (golden rule 14). An invented or outdated version in an ADR is a silent error.

## 3. Workshop flow

| Step | The agent | The decision-maker |
|---|---|---|
| 1 | Draws up the inventory of choices (§ 2.1) and marks those already imposed by a `C-n`. | Completes it. |
| 2 | Surveys the team's skills and the organization's preferences. | Answers. |
| 3 | For each structuring choice: filter, shortlist, proposed grid. | Sets the weights, discusses the scores. |
| 4 | Proposes the proofs of concept needed, with their question and their duration. | Accepts or refuses. |
| 5 | Writes the ADRs. | Arbitrates. |
| 6 | Consolidates `07-technology-choices.md`: chosen stack, versions, dependency policy. | Reviews. |
| 7 | Runs the checklist and invokes the critical reviewer. | Approves G7. |

## 4. Question bank

1. Which languages and frameworks does the team really master, that is, having already put a system into production with them?
2. Does the organization impose or forbid certain providers, languages or licenses?
3. Who will maintain the system in three years? The same team, a contractor, an internal team still to be hired?
4. What is the monthly budget for hosting and licenses?
5. Must the data stay in one country or with a certified hosting provider?
6. Are you ready to depend on a cloud provider's proprietary service in exchange for simpler operations?

## 5. Deliverables

| File | Minimum content |
|---|---|
| `07-technology-choices.md` | Stack table: category, choice, version, ADR, alternatives ruled out; dependency policy |
| `adr/` | One ADR per structuring choice, with the grid |
| `STATE.md` | Technical hypotheses and risks |

## 6. Gate G7 checklist

- [ ] ★ Each container of the C4 level 2 has a designated technology.
- [ ] ★ Each structuring choice has an ADR that compares at least two options.
- [ ] ★ No choice violates a `C-n`.
- [ ] The team's skills have been taken into account explicitly.
- [ ] The versions and ends of support cited have been verified or marked "to be verified".
- [ ] Each generic subdomain is bought or reused, or building it is justified.
- [ ] The planned proofs of concept have been carried out and their result is recorded.
- [ ] The dependency policy is written.
- [ ] The estimated monthly operating cost is compared with the budget.

## 7. Anti-patterns

| Anti-pattern | Symptom | Correction |
|---|---|---|
| Novelty for novelty's sake | Choice of a tool nobody knows, with no `QS-n` that requires it | Upskilling cost in the grid; prefer the proven. |
| Choice by habit | "We've always done it this way", with no alternative | At least two options in the ADR. |
| Promoted proof of concept | The prototype becomes the product | The proof-of-concept code is thrown away by definition. |
| Unnoticed lock-in | Proprietary service adopted without evaluating the exit | Reversibility criterion in every grid. |
| Hallucinated versions | Version or feature asserted by the AI without verification | Golden rule 14. |
