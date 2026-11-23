# 03 — Quality requirements — <Project name>

| Status | Version | Date | Gate |
|---|---|---|---|
| Draft | 0.1 | <YYYY-MM-DD> | G3: — |

## 1. Load profile and data volumes

| Quantity | Today | In 1 year | In 3 years | Source |
|---|---|---|---|---|
| Registered users | | | | |
| Concurrent active users at peak | | | | |
| Key business operations per day | | | | |
| Hourly or seasonal peak | | | | |
| Volume of data created per year | | | | |
| Retention period | | | | |

## 2. Coverage of the quality characteristics

<!-- The nine characteristics of the ISO (International Organization for Standardization) / IEC (International Electrotechnical Commission) 25010 standard. -->

| Characteristic | Scenarios | Or "not applicable", with rationale |
|---|---|---|
| Functional suitability | | |
| Performance efficiency | | |
| Compatibility | | |
| Interaction capability | | |
| Reliability | | |
| Security | | |
| Maintainability | | |
| Flexibility | | |
| Safety | | |

## 3. Quality scenarios

### QS-1 — <Title>

- **Characteristic**: <characteristic › subcharacteristic>
- **Source**:
- **Stimulus**:
- **Environment**:
- **Artifact**:
- **Response**:
- **Response measure**: <numeric value or [threshold to be set]>
- **Rationale**:
- **Priority**: Must / Should / Could / Won't
- **Links**: BO-n, C-n, BR-n, IR-n
- **OD** (open decision): OD-n

## 4. Utility tree

| Scenario (QS) | Business importance (H/M/L) | Technical difficulty (H/M/L) | Architecturally significant |
|---|---|---|---|
| QS-1 | | | Yes / No |

## 5. Conflicts and trade-offs

| Scenarios in tension | Nature of the conflict | Options | Trade-off decision or OD |
|---|---|---|---|
| | | | |

## 6. Architecturally significant interaction needs

<!-- If the system has end users: list of the usability scenarios of the SEI (Software Engineering Institute),
     report `CMU/SEI-2001-TR-005`. Each need retained becomes a QS-n.
     One row per scenario of the report (twenty-six); the five rows below are examples. -->

| SEI scenario | Retained (yes / no) | Quality scenario (QS) | Rationale |
|---|---|---|---|
| Cancel an operation in progress | | | |
| Undo | | | |
| Observe the state of the system | | | |
| Aggregate data | | | |
| Remain consistent across views | | | |
