# Multi-Agent SDLC Governance Framework

## Setup Repository Structure
- [x] Create `project/` directories (`epics`, `stories`, `reviews`, `overrides`, `policies`)
- [x] Create `specs/` directories
- [x] Create `schemas/` directory
- [x] Create `agents/` directory
- [x] Create `logs/` directory
- [x] Create `.github/workflows/` directory

## Create JSON Schemas
- [x] Write `epic.schema.json`
- [x] Write `story.schema.json`
- [x] Write `review.schema.json`
- [x] Write `override.schema.json`

## Configure Governance & Actions
- [x] Define initial `review_policy.yaml`
- [x] Describe the Git-safe ID allocation strategy
- [x] Write a GitHub Actions Workflow (`governance.yml`) to validate schema, check ID allocation, state transition logic, and review thresholds.

## Agent System Setup
- [x] Provide boilerplate for Plan, Decompose, Review, and Aggregation agents
