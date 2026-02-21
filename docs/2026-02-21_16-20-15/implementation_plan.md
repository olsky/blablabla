# Governed Multi-Agent SDLC System Plan

This document outlines the approach for setting up the multi-agent SDLC governance framework inside a GitHub repository.

## Proposed Changes

### Directory Structure Initialization
We will create the following directories:
- `project/epics/`
- `project/stories/`
- `project/reviews/`
- `project/overrides/`
- `project/policies/`
- `specs/canonical_feature_specs/`
- `schemas/`
- `agents/`
- `logs/`
- `.github/workflows/`

### JSON Schemas
We will implement the provided JSON Schema 2020-12 drafts for the entities to ensure strict validation.
- **[NEW]** `schemas/epic.schema.json`
- **[NEW]** `schemas/story.schema.json`
- **[NEW]** `schemas/review.schema.json`
- **[NEW]** `schemas/override.schema.json`

Because the `epic.schema.json` requires strict ID routing `EP-[0-9]{4}`, validation will easily hook into CI using standard tools `ajv` or Python `jsonschema`.

### ID Allocation Strategy
We will implement the provided Git-safe Directory-Scan strategy. Instead of a central counter, ID allocation will loop over `project/<entity>/`, parse `[A-Z]+-(\d{4}).yaml`, calculate `max() + 1`, and format it back pad-zeroed. This makes the system robust against branching and merging, avoiding central lock contention. 

### CI/CD Governance Workflows
We will construct a GitHub Action `governance.yml`. This workflow will execute on Pull Requests and Pushes and perform:
1. **Schema Validation**: Verify all updated/modified YAML files in `project/` against their corresponding JSON schema.
2. **State Transition Validation**: Reject PRs that skip required states (e.g. `draft` -> `approved` without `in_review`).
3. **Review Checks**: For an epic to transition to `approved`, CI will enforce the `review_policy` (min reviews count, approval threshold, no blocking issues).
4. **Link / Reference Integrity**: Ensure `US-XXXX` mapped in `EP-YYYY` actually exist and don't refer to deleted endpoints.

## User Review Required
> [!IMPORTANT]
> The exact logic to run the CI validations (Python script vs existing GitHub action plugins) has not been detailed in full. I am planning on adding a Python script (`agents/validators/governance_validator.py`) to the repository which will be invoked by `.github/workflows/governance.yml`. Please confirm if this is the desired path.

## Verification Plan
### Automated Tests
- Create sample valid and invalid Epics, Stories, and Reviews. Run the schema validation script to ensure invalid components are caught.
- Attempt state transition from `in_review` to `approved` without enough reviews, forcing it to fail.

### Manual Verification
- Review the generated JSON schemas.
- Examine the python validation logic and GitHub action workflow file.
