# Design state — <Project name>

<!-- File kept by the orchestrator agent. It is the memory of the process:
     an agent that resumes the project without any conversation history must be able to
     continue by reading this file alone. Update it at every "Record" step
     and at the end of each session. -->

## 1. Situation

| Key | Value |
|---|---|
| Project | <Project name, or "to be named"> |
| Design directory | <path of DESIGN_DIR> |
| Profile | To be chosen / Prototype / Product / Critical |
| Interaction mode | Workshop / Proposal / Review |
| Current phase | <n> — <name> |
| Loop step | <1 to 7> — <Load, Question, Propose, Critique, Validate, Record, Gate> |
| Next action | <precise action> |
| Last updated | <YYYY-MM-DD> |

## 2. Source register (`SRC-n`)

<!-- Existing documents read without being modified (principles § 16). Delete the example row at initialization. -->

| Id | Title | Location | Version read (number, date or commit) | Phases fed | Status (to be transposed, transposed, archived) |
|---|---|---|---|---|---|
| SRC-n (example) | | | | | |

## 3. Gates

| Gate | Date | Decision | Waivers | Linked open ODs (open decisions) |
|---|---|---|---|---|
| G1 | | | | |

## 4. Pending questions

<!-- Full text of the questions asked that are still unanswered, so that they can be asked again verbatim. -->

1. …

## 5. Open decision register (`OD-n`)

<!-- Delete the example row below at initialization. -->

| Id | Question | Options | Recommendation | Blocks | Owner | Due | Status | Resolution |
|---|---|---|---|---|---|---|---|---|
| OD-n (example) | | | | BR-n, QS-n, INC-n… | | Phase <n> or date | Open | → BR-n / ADR-nnnn |

## 6. Hypothesis register (`H-n`)

| Id | Hypothesis | Source | Planned verification (how, when) | Status |
|---|---|---|---|---|
| H-n (example) | | | | To be verified |

## 7. Risk register (`R-n`)

| Id | Risk | Type (project, technical, debt) | Probability | Impact | Response (avoid, reduce, transfer, accept) | Action | Increment | Status |
|---|---|---|---|---|---|---|---|---|
| R-n (example) | | | | | | | | Open |

## 8. Log

<!-- One dated entry per session and per notable decision. Never rewrite a past entry. -->

| Date | Phase | Event |
|---|---|---|
| <YYYY-MM-DD> | 1 | Design initialized. |
