# Multi-Agent SDLC System Setup Walkthrough

This document outlines the foundation for a governed, multi-agent SDLC system established inside the GitHub repository located at `/Users/olsky/github/olsky/blablabla`. 

The system provides deterministic tracking, automated policy evaluation, JSON schema adherence, and multi-model agent collaboration. 

## Repository Architecture Implemented

The following directory structure categorizes artifacts:

*   `project/epics/`: Storage for Epics (High-level business capabilities) (`EP-XXXX.yaml`).
*   `project/stories/`: Storage for User Stories (Implementation details) (`US-XXXX.yaml`).
*   `project/reviews/EP-XXXX/`: Dedicated folders storing review artifacts per epic (`RV-EP-XXXX-YYY.yaml`).
*   `project/overrides/`: Explicit human override logs (`OV-XXXX.yaml`).
*   `project/policies/`: Configuration files mapping governance rules (e.g., `review_policy.yaml`).
*   `schemas/`: Contains the strict JSON Schema (Draft 2020-12) files enforcing the shape of Epics, Stories, Reviews, and Overrides.
*   `agents/`: Houses initial boilerplate and validation logic representing the agent system.
    *   `agents/validators/`: Contains Python scripts defining the Git-safe ID allocation algorithm, schema validations, requirement integrities, and policy enforcements.
    *   `agents/planners/`, `agents/decomposers/`, `agents/reviewers/`, `agents/aggregators/`: Python modules with boilerplate simulation logic outlining inputs, transformations, and outputs for the respective AI agents.
*   `.github/workflows/`: Houses the Github Action `governance.yml` to trigger pipeline validation on pull requests and commits.

## ID Allocation Strategy

A robust, Git-safe ID allocation mechanism was implemented in `agents/validators/id_allocator.py`.

It does not rely on a centralized counter file, which would be susceptible to merge conflicts and lock contention. Instead, the algorithm scans the corresponding artifact directory (`project/epics/`, `project/stories/`, etc.), extracts existing numerical IDs using regex, calculates the `max()` present, and increments it by `+1`, zero-padding the result. 

## CI/CD Governance & Validations

The `governance.yml` GitHub actions file triggers a series of python scripts to enforce data integrity:
1.  **Schema Validation**: Ensures all YAML artifacts comply strictly with their respective JSON schemas (`agents/validators/schema_validator.py`).
2.  **Reference Integrity**: Ensures that artifact relations are valid. For instance, an Epic's `linked_stories` array must only reference existing user stories on the disk (`agents/validators/integrity_validator.py`).
3.  **Policy Enforcement**: Validates that state transitions strictly align with configurations in `project/policies/review_policy.yaml`. The current logic defines metrics like the 0.75 approval threshold and mandatory resolving of blocking issues before entering an `approved` state (`agents/validators/policy_evaluator.py`).

## Next Steps

1.  **Integrate LLMs**: The provided boilerplates in `agents/` (e.g., `planner_agent.py`, `reviewer_agent.py`) should be hooked up to actual LLM API providers (OpenAI, Gemini). Prompts must be developed telling models to natively output the defined YAML structured format without excess Chain-of-Thought (since CoT is discarded for storage).
2.  **State Machine Refinement**: Enhance `policy_evaluator.py` to formally block git merges during Github Actions if state transitions skip required sequential phases (e.g., `draft` -> `approved` without `in_review` and passing the aggregator's evaluation score). 
3.  **Cross-layer Alignments**: Start passing contextual schema contexts into the Agent prompts to assure features remain aligned transversally (Backend <-> Gateway <-> UI). Mismatches identified during multi-model reviews must correctly classify the review artifact as `blocking`.
