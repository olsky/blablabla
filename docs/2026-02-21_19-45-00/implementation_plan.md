# Implementation Plan: EP-0140 – EP-0149 ($100M+ Y1 Batch)

**Session:** 2026-02-21_19-45-00  
**Agent:** planner (claude-opus-4)

## Phase 1 – Setup (this session)

| Step | Action | Status |
|------|--------|--------|
| 1.1 | Scan existing EPIC titles for uniqueness | ✅ Done |
| 1.2 | Create session folder `docs/2026-02-21_19-45-00/` | ✅ Done |
| 1.3 | Write `task.md` | ✅ Done |
| 1.4 | Write `walkthrough.md` | ✅ Done |
| 1.5 | Write `implementation_plan.md` | ✅ This file |

## Phase 2 – EPIC Authoring

Create 10 EPIC YAMLs under `project/epics/`:

| Step | EPIC ID | Working Title | Target Y1 Earnings |
|------|---------|---------------|---------------------|
| 2.1 | EP-0140 | Mining Royalty & Production Under-Reporting Detection Fabric | $150M+ |
| 2.2 | EP-0141 | Commercial Real Estate CAM & Opex Overcharge Recovery Network | $180M+ |
| 2.3 | EP-0142 | Automotive Warranty & Recall Reimbursement Optimization Engine | $130M+ |
| 2.4 | EP-0143 | Timber Concession Compliance & Yield Optimization Mesh | $140M+ |
| 2.5 | EP-0144 | Seafarer Payroll, Social Security & Tax Compliance Fabric | $120M+ |
| 2.6 | EP-0145 | Specialty Chemical Toll-Manufacturing Capacity Exchange | $160M+ |
| 2.7 | EP-0146 | Hospital Implant & High-Cost Device Charge Capture Engine | $170M+ |
| 2.8 | EP-0147 | Heavy Equipment Idle Capacity Liquidity & Rental Mesh | $150M+ |
| 2.9 | EP-0148 | Airport Ground-Handling SLA & Irregular Ops Compensation Recovery Platform | $110M+ |
| 2.10 | EP-0149 | Livestock Health Early-Warning & Parametric Coverage Network | $120M+ |

Each EPIC will follow the standard YAML structure:

```yaml
id: EP-014X
title: "..."
description: |
  **Idea:** ...

  **Why "WOW":** ...

  **ROI (Time In vs Cash Out):**
  - Time In: ...
  - Cash Out: ...

  **First Year Projections:**
  - [TAM + capture assumptions]
  - Users / customers in Y1
  - **Total Estimated Earnings: $XXX,XXX,XXX**

  **Feasibility Score:** X.X/10

  **Risk Analysis:**
  - High: ...
  - Medium: ...
  - Low: ...

  **Legal & Ethical:** ...

created_at: "2026-02-21"
created_by:
  agent: planner
  model: claude-opus-4
  provider: anthropic
status: draft
linked_stories: []
review_policy:
  min_reviews: 4
  approval_threshold: 0.90
  require_blocking_clearance: true
```

## Phase 3 – Validation

After EP-0140..EP-0149 are created:

1. Run schema validation:
   - `python3 agents/validators/schema_validator.py`
2. Run integrity validation:
   - `python3 agents/validators/integrity_validator.py`
3. Confirm all 10 EPICs pass without modification.

## Hand-off Plan

Once this plan is complete and EPICs are validated:

- **Decomposer agents** can generate user stories and low-level requirements from each EPIC.
- **Planner/aggregator agents** can prioritize EPICs based on feasibility and ROI.
- **Implementation agents** can later generate code and infrastructure plans for selected EPICs.

No code is written in this session; the output is purely EPIC-level artifacts, ready for downstream agents.
