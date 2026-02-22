# 12-Week MVP Implementation Roadmaps
**Session ID:** 2026-02-22_01-39-11  
**Prepared for:** Solo founder + 2–3 engineers  

---

## Overview

Each EPIC has a **12-week = 3-month MVP build timeline** ending in "first paying customer" or "alpha revenue." Below are detailed week-by-week roadmaps.

---

## EP-0910: Telecom Billing Dispute Automation

**MVP Goal:** Ingest 5 real telecom bills from Fortune 500 companies, extract line items, cross-reference contracts, generate dispute documents, deliver 90% accuracy on extracted charges.

### Roadmap

| Week | Milestone | Tasks | Resources |
|------|-----------|-------|-----------|
| 1–2 | **Data Collection & Training** | Acquire 10 real telecom bills (ask pilot customers), 5 service agreements | Founder + Customer relationships |
| | | Extract bill structure patterns manually | Founder, 5 hrs |
| | | Extract contract structure patterns manually | Founder, 5 hrs |
| 3–4 | **LLM Extraction Pipeline V1** | Implement Claude API bill parsing ("extract all line items, dates, amounts") | 1 engineer, 30 hrs |
| | | Implement Claude API contract parsing ("extract service terms, rates, discounts") | 1 engineer, 20 hrs |
| | | Build basic validation layer (sanity checks on extracted amounts) | 1 engineer, 10 hrs |
| | | Test on 5 sample bills; measure accuracy | Founder, 5 hrs |
| 5–6 | **Matching Logic & Dispute Template** | Build matching algorithm: "Is this charge in contract X?" | 1 engineer, 25 hrs |
| | | Build dispute document templating (PDF generation) | 1 engineer, 20 hrs |
| | | Add historical anomaly detection (flag charges appearing <3 months) | 1 engineer, 15 hrs |
| | | Test with 10 bills + contracts; refine accuracy | Founder, 5 hrs |
| 7–8 | **Customer Dashboard & Delivery** | Build basic web dashboard (list disputes, download PDFs, mark submitted) | 1 engineer, 40 hrs |
| | | Build email delivery (auto-send dispute PDFs to customer) | 1 engineer, 10 hrs |
| | | Add authentication + onboarding (file upload, contract registration) | 1 engineer, 20 hrs |
| | | Test with 2 pilot customers | Founder + Engineer, 10 hrs |
| 9–10 | **Legal Review & Case Building** | Engage telecom attorney part-time (5 hrs/week) to review 5 dispute templates | Attorney, 10 hrs |
| | | Build "reasoning document" (why this charge is likely an error) | Founder + Attorney, 10 hrs |
| | | Add credibility signals (cite contract article, show comparable carrier rates) | 1 engineer, 15 hrs |
| | | Test with pilot customers; iterate | Founder, 10 hrs |
| 11–12 | **Launch & Revenue** | Finalize 3–5 pilot customer disputes for submission | Founder, 10 hrs |
| | | Submit disputes to carriers; track responses | Founder + Customers, 5 hrs |
| | | Document case results (amount disputed, amount recovered, timeline) | Founder, 5 hrs |
| | | Close first paid customer; deliver recoveries | Founder + Customers, 10 hrs |
| | | **Target:** Revenue from first 3–5 customers ($150K–$500K) by end of week 12 | |

**Total effort:** ~280 engineer-hours + 40 founder-hours + 10 attorney-hours

**Risks & Mitigations:**
- Risk: Bill extraction accuracy <80% → Mitigation: Loop iterations with human review; build feedback loop
- Risk: Carriers dispute findings → Mitigation: Engage attorney early; build airtight legal reasoning
- Risk: Slow contract acquisition from customers → Mitigation: Start with 1–2 customers; iterate quickly

---

## EP-0911: Cryptocurrency Tax Compliance Engine

**MVP Goal:** Auto-ingest Coinbase + Kraken transaction history, calculate FIFO cost basis, generate IRS Form 8949 + Schedule D, achieve >95% accuracy on test returns.

### Roadmap

| Week | Milestone | Tasks | Resources |
|------|-----------|-------|-----------|
| 1–2 | **Coinbase & Kraken API Integration** | Set up Coinbase OAuth (get test API credentials) | 1 engineer, 15 hrs |
| | | Set up Kraken API (get test credentials) | 1 engineer, 15 hrs |
| | | Build transaction ingestion pipeline (fetch buys, sells, transfers) | 1 engineer, 20 hrs |
| | | Test with 5 sample accounts | Engineer + Founder, 5 hrs |
| 3–4 | **Price History & Cost Basis Calculation** | Source historical price data (CoinGecko API) | 1 engineer, 15 hrs |
| | | Implement FIFO cost basis calculation algorithm | 1 engineer, 30 hrs |
| | | Implement LIFO + average-cost options | 1 engineer, 15 hrs |
| | | Test with 10 sample crypto portfolios (varying complexity) | Engineer + Founder, 10 hrs |
| 5–6 | **Form 8949 & Schedule D Generation** | Build Form 8949 PDF templating (line-item sale records) | 1 engineer, 25 hrs |
| | | Build Schedule D PDF templating (summary gains/losses) | 1 engineer, 15 hrs |
| | | Add Schedule 1 (for staking income, airdrops) | 1 engineer, 10 hrs |
| | | Test with 5 sample returns; validate IRS form structure | Founder + CPA consultant, 10 hrs |
| 7–8 | **Dashboard & User Experience** | Build SaaS dashboard (onboarding, wallets, forms, export) | 1 engineer, 40 hrs |
| | | Add stripe.com integration for payment processing | 1 engineer, 15 hrs |
| | | Build email delivery (PDF forms auto-emailed to customer) | 1 engineer, 10 hrs |
| | | Build CSV export (for accountant review) | 1 engineer, 10 hrs |
| 9–10 | **Tax Law Accuracy & Validation** | Engage CPA/tax professional part-time (10 hrs/week) | CPA, 20 hrs |
| | | Validate wash-sale detection algorithm (complex tax rule) | CPA + Engineer, 10 hrs |
| | | Validate staking income treatment (evolving IRS guidance) | CPA + Engineer, 10 hrs |
| | | Test with 10 real user returns; compare to accountant hand-calculation | Founder + CPA, 10 hrs |
| 11–12 | **Launch & Revenue** | Open beta (free/discounted access for 1K users) | Founder, 10 hrs |
| | | Market via crypto Twitter, Reddit, Discord (organic outreach) | Founder, 20 hrs |
| | | GA launch (full pricing, production SaaS) | Founder + Engineer, 10 hrs |
| | | Close first 500–1K beta customers (free/discounted) | Founder, 10 hrs |
| | | **Target:** First 100 paid customers by end of week 12 ($10K–$30K revenue) | |

**Total effort:** ~225 engineer-hours + 30 founder-hours + 20 CPA-hours

**Risks & Mitigations:**
- Risk: Crypto exchange API changes → Mitigation: Build versioned integrations; monitor API docs
- Risk: IRS guidance evolving (wash-sale treatment, staking income) → Mitigation: Partner with CPA early; plan quarterly updates
- Risk: Tax law interpretation uncertainty → Mitigation: Conservative approach (flag ambiguous cases for manual review); clearly disclose limitations

---

## EP-0912: Retail Shrinkage Intelligence Engine

**MVP Goal:** Ingest POS + inventory data from 3 pilot retailers, segment shrinkage into 4 categories (supplier error, register, theft, waste), generate per-location dashboard, achieve >80% accuracy on high-loss-location identification.

### Roadmap

| Week | Milestone | Tasks | Resources |
|------|-----------|-------|-----------|
| 1–2 | **POS Integration Framework** | Partner with 3 pilot retailers (agreement to share data) | Founder, 20 hrs |
| | | Research POS system APIs (NCR, Oracle, Shopify, Toast) | Engineer, 15 hrs |
| | | Build generic POS API adapter (query transactions, reconciliation) | 1 engineer, 30 hrs |
| | | Test with pilot retailer #1 (pull 3 months of transaction history) | Engineer + Founder, 10 hrs |
| 3–4 | **Inventory Ingestion** | Integrate with inventory systems (API or manual upload) | 1 engineer, 25 hrs |
| | | Build inventory reconciliation logic (received qty vs. on-hand) | 1 engineer, 20 hrs |
| | | Ingest supplier invoices (EDI or email) | 1 engineer, 15 hrs |
| | | Test data pipeline with all 3 pilot retailers | Engineer + Founder, 10 hrs |
| 5–6 | **Shrinkage Segmentation ML** | Build unsupervised clustering model (segment losses by type) | 1 engineer, 40 hrs |
| | | Train on 3 months of historical data from pilots | Engineer + Founder, 10 hrs |
| | | Validate accuracy (manual review of 50 samples from each cluster) | Founder, 15 hrs |
| | | Iterate on model performance (target: 80% confidence on segmentation) | Engineer, 20 hrs |
| 7–8 | **Dashboard & Alerting** | Build per-location shrinkage dashboard (loss %, by category) | 1 engineer, 40 hrs |
| | | Build alerting engine (flag high-variance stores, anomalies) | 1 engineer, 20 hrs |
| | | Add peer benchmarking (compare location X to system average) | 1 engineer, 15 hrs |
| | | Build data quality scoring (flag low-confidence alerts) | 1 engineer, 10 hrs |
| 9–10 | **Feedback & Iteration** | Deploy dashboard to 3 pilot retailers for feedback | Founder, 10 hrs |
| | | Gather loss prevention director feedback (validation of recommendations) | Founder, 20 hrs |
| | | Iterate on dashboard UX, refine segmentation based on feedback | Engine + Founder, 20 hrs |
| | | Validate that recommendations actually improved shrinkage (pilot stores) | Founder, 10 hrs |
| 11–12 | **Launch & Revenue** | Finalize 2–3 case studies from pilots (dollar impact) | Founder, 10 hrs |
| | | Build sales collateral + pricing page | Founder + Engineer, 10 hrs |
| | | Outreach to retail groups (LinkedIn, industry conferences) | Founder, 20 hrs |
| | | Close first 2–3 paying customers (small chains, 10–50 locations) | Founder, 10 hrs |
| | | **Target:** Revenue from first 3–5 customers ($15K–$50K/month) by end of week 12 | |

**Total effort:** ~290 engineer-hours + 50 founder-hours

**Risks & Mitigations:**
- Risk: Inconsistent POS data quality → Mitigation: Build data quality scoring; flag low-confidence segmentations
- Risk: Retailers slow to grant data access → Mitigation: Lead with 1–2 large retailers who are motivated; use as references for others
- Risk: Shrinkage segmentation inaccuracy → Mitigation: Involve retail operations expert in model validation; conservative alert thresholds initially

---

## EP-0913: Healthcare Lab Order Optimization Engine

**MVP Goal:** Integrate with Epic EHR, ingest orders + clinical context, build guideline knowledge base for 10 most common lab panels, deploy at 1 beta hospital, achieve >90% accuracy on "medically necessary" vs. "low-value" classification.

### Roadmap

| Week | Milestone | Tasks | Resources |
|------|-----------|-------|-----------|
| 1–2 | **Clinical Guideline Research & Compilation** | Compile 10 most common lab panel guidelines (ACCP, AHA, IDSA) | Founder + Clinical consultant, 20 hrs |
| | | Map guideline indications (diagnoses → recommended panels) | Founder, 15 hrs |
| | | Build guideline knowledge base structure (JSON/YAML) | 1 engineer, 15 hrs |
| | | Test guideline matching logic manually | Founder, 10 hrs |
| 3–4 | **Epic EHR FHIR Integration** | Set up Epic FHIR developer environment (credentials, sandbox) | 1 engineer, 15 hrs |
| | | Build order intercept API (capture lab orders pre-phlebotomy) | 1 engineer, 25 hrs |
| | | Build patient context fetcher (diagnosis, vitals, recent labs) | 1 engineer, 20 hrs |
| | | Test with 10 sample order records | Engineer + Founder, 10 hrs |
| 5–6 | **LLM-based Guideline Matching** | Implement Claude API matching ("Is this order appropriate?") | 1 engineer, 30 hrs |
| | | Add confidence scoring and reasoning extraction | 1 engineer, 15 hrs |
| | | Build alert generation (pop-up message for ordering physician) | 1 engineer, 15 hrs |
| | | Test with 50 sample orders; validate accuracy >90% | Founder + Clinical consultant, 10 hrs |
| 7–8 | **Clinical Validation & Safety** | Partner with beta hospital (1 hospital system) | Founder + CMO relationship, 10 hrs |
| | | Deploy in "advisory mode" (no order blocking; silent logging only) | Engineer, 10 hrs |
| | | Collect 2 weeks of order data; validate guideline matching | Founder + Hospital CMO, 15 hrs |
| | | Iterate on guideline logic (improve accuracy, reduce false positives) | Engineer + CMO, 20 hrs |
| 9–10 | **Dashboard & Feedback Loop** | Build physician feedback dashboard (per-physician % low-value orders) | 1 engineer, 30 hrs |
| | | Build hospital-wide analytics (cost savings, safety metrics) | 1 engineer, 20 hrs |
| | | Deploy intervention mode (soft alert to ordering physician) | Engineer, 15 hrs |
| | | Test with 2–3 beta units (departments) at hospital | Founder + Hospital CMO, 10 hrs |
| 11–12 | **Clinical Outcome Validation & Launch** | Measure clinical outcomes (order prevention rate, readmission rate, safety) | Founder + Hospital quality team, 10 hrs |
| | | Build case study (hospital Y reduced unnecessary tests by 15%, saved $5M) | Founder, 10 hrs |
| | | Complete IRB/compliance review (if required) | Founder + Legal, 5 hrs |
| | | Prepare for wider hospital rollout (2–3 additional systems) | Founder, 10 hrs |
| | | **Target:** First 1–2 paying hospital systems signed by end of week 12 ($50K–$100K) | |

**Total effort:** ~255 engineer-hours + 40 founder-hours + 20 clinical consultant-hours

**Risks & Mitigations:**
- Risk: Hospital legal/compliance skepticism → Mitigation: Deploy in advisory-only mode initially; rigorous safety validation
- Risk: Guideline interpretation incorrect → Mitigation: Partner with hospital CMO; conservative confidence thresholds
- Risk: EHR integration complexity → Mitigation: Focus on Epic first (largest market); Cerner integration later

---

## EP-0914: Supply Chain Counterfeiting Detection Platform

**MVP Goal:** Build CV model for 1 product category (luxury watches or pharma packaging), integrate blockchain supply chain tracking, deploy at 2–3 checkpoints (ports or manufacturer facilities), detect counterfeits with >95% confidence on known fakes.

### Roadmap

| Week | Milestone | Tasks | Resources |
|------|-----------|-------|-----------|
| 1–2 | **Computer Vision Model Training** | Acquire 1,000+ images of authentic product (collaborate with 1–2 brand pilots) | Founder + Brand partnerships, 20 hrs |
| | | Acquire 500+ images of counterfeit samples (from law enforcement, investigators) | Founder, 10 hrs |
| | | Label dataset (1,500 images total) | Founder + Contractor, 20 hrs |
| | | Train baseline CV model (YOLOv8 or similar) | 1 engineer, 30 hrs |
| 3–4 | **CV Model Accuracy & Validation** | Test model accuracy on holdout test set (target >90% on known fakes) | Engineer + Founder, 15 hrs |
| | | Identify failure cases (confusing authentic vs. fake) | Engineer, 10 hrs |
| | | Fine-tune model with augmented data | 1 engineer, 25 hrs |
| | | Achieve >95% accuracy (or accept 90% + human review) | Engineer, 10 hrs |
| 5–6 | **Blockchain Supply Chain Integration** | Build blockchain ledger (Hyperledger or custom) | 1 engineer, 30 hrs |
| | | Implement lot-tracking schema (product SKU, serial, path from mfg → retail) | 1 engineer, 20 hrs |
| | | Build API for checkpoint scanning (upload image, cross-check against ledger) | 1 engineer, 25 hrs |
| | | Test with 10 sample scanning scenarios | Engineer + Founder, 10 hrs |
| 7–8 | **Checkpoint Deployment & UI** | Design checkpoint scanning station (camera + screen + backend) | 1 engineer + UX, 20 hrs |
| | | Deploy cameras + scanning infrastructure at 2 pilot checkpoints | Founder + IT contractor, 15 hrs |
| | | Build scanning dashboard (capture image, trigger CV model, display confidence) | 1 engineer, 25 hrs |
| | | Test live scanning with 100+ real product samples | Founder + Checkpoint teams, 15 hrs |
| 9–10 | **Law Enforcement Integration & Fulfillment** | Build law enforcement alerting (auto-notify authorities of detected counterfeits) | 1 engineer, 20 hrs |
| | | Partner with customs/police (engage local authorities) | Founder, 15 hrs |
| | | Build analytics dashboard (heat maps, supply chain forensics) | 1 engineer, 20 hrs |
| | | Test alert workflow with law enforcement | Founder + LE contacts, 10 hrs |
| 11–12 | **Launch & Revenue** | Document pilot results (counterfeits detected, supply chain traces, LE seizures) | Founder, 10 hrs |
| | | Build case study + landing page | Founder, 10 hrs |
| | | Outreach to brands + law enforcement | Founder, 15 hrs |
| | | Close first brand pilot contract (2–3 checkpoints, $100K–$300K) | Founder, 10 hrs |
| | | **Target:** First paid customer + deployed checkpoints by end of week 12 ($50K–$100K revenue) | |

**Total effort:** ~315 engineer-hours + 50 founder-hours

**Risks & Mitigations:**
- Risk: CV accuracy <90% on real fakes → Mitigation: Use ensemble methods (CV + blockchain signals); escalate low-confidence to human review
- Risk: Supply chain coordination complex → Mitigation: Start with manufacturers + warehouses (easier to deploy); retail later
- Risk: Counterfeiting techniques evolve → Mitigation: Plan for quarterly model retraining; maintain relationship with LE for new fake samples

---

## Cross-Cutting Build Infrastructure

**All 5 EPICs require:**
- Cloud hosting (AWS, GCP, or Azure): $5K–$20K/month across all 5 projects
- LLM API credits (Claude, GPT-4): $10K–$30K/month (shared across 3+ projects)
- Data storage + processing (database, object storage): $2K–$5K/month
- **Total monthly infrastructure:** $17K–$55K (highest in months 2–3; lower Y1 average $25K)

---

## Resource Allocation Across All 5 EPICs (12 weeks)

**Total engineering capacity needed:** ~1,365 hours = ~3.3 FTE engineers for 12 weeks

**Recommendation:**
- Hire 3 engineers (full-time) for weeks 1–12
- Founder: Full-time (technical + customer relationships)
- Consultants (2–3): Part-time (legal, CPA, clinical, compliance) as needed

**Staffing cost (12 weeks):**
- Senior engineer × 3: $150K × 3 × (12 wks / 52 wks) = ~$103K
- Founder salary (opportunity cost): $0 (equity sweat equity)
- Consultants (legal, CPA, clinical): ~$15K total
- **Total staffing:** ~$120K for 12-week MVP period

**Total MVP investment (12 weeks):**
- Staffing: $120K
- Infrastructure: $300K (assuming ~$25K/month × 12)
- Contingency (10%): $42K
- **Total:** ~$462K

**Expected break-even:** First customer revenue ($100K–$500K depending on EPIC) by week 12–14, recovering MVP cost by month 4–5.

---

## Go/No-Go Decision Gates

**Week 4:** If any EPIC shows <70% accuracy on core hypothesis, pivot or kill it
- **EP-0910:** Bill parsing must achieve >80% accuracy
- **EP-0911:** Cost basis calculation must match > CPA hand-calc
- **EP-0912:** Shrinkage segmentation must be >75% accurate in manual validation
- **EP-0913:** Guideline matching must be >85% accurate compared to hospital CMO
- **EP-0914:** CV model must detect >90% of known counterfeits

**Week 8:** If pilot customers aren't showing measurable ROI or engagement, deprioritize that EPIC
- Prioritize: All 5 EPICs showing strong pilot traction
- Maintain: Any 1–2 projects that show medium traction
- Pause: Any projects <50% of expected engagement metric

**Week 12:** Measure revenue progress per EPIC; allocate Year 2 resourcing accordingly
- **All-in:** Any EPIC generating >$50K by end of week 12
- **Maintain:** Any EPIC generating $10K–$50K
- **Pivot/wind-down:** Any EPIC <$10K

