# Implementation Plan

## Phase 1 (Weeks 1-2)
- Build normalized event graph from shipping, customs, invoice, and payment feeds.
- Ship policy/rules engine for document checks, sanctions, and trigger conditions.

## Phase 2 (Weeks 3-6)
- Launch autonomous decision loops: detect -> decide -> execute -> settle.
- Integrate payout/collection rails (bank APIs, PSPs, insurer APIs).

## Phase 3 (Weeks 7-10)
- Add pricing/risk models for dynamic fees and underwriting.
- Add self-serve onboarding and API keys.

## Phase 4 (Weeks 11-12)
- Production hardening, audit logs, explainability reports.
- Corridor-by-corridor rollout with contingency-based pricing.

## GTM
- Start with importers/exporters, freight forwarders, and specialty lenders.
- Sell via API + contingency economics; minimal enterprise sales overhead.

## Risk controls
- Human override for high-severity financial actions in pilot mode.
- Multi-source data verification for payouts.
- Jurisdiction-aware legal and sanctions policy checks.
