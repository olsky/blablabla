# Implementation Plan: 12-Week MVP Execution Roadmap

## Phase Overview
This document provides a detailed 12-week build, test, and pilot roadmap for launching 5 autonomous agents across untapped sectors. Each EPIC targets 3-month MVP completion with single-engineer buildability.

---

## EPIC #1: Medical Coding Denial Appeal Automation (EP-0905)

### MVP Scope (3 Months)
**Goal:** Autonomously generate appeal letters for denied healthcare claims with 80%+ medical coder validation accuracy.

### Week-By-Week Roadmap

#### Weeks 1–2: Data Ingestion & Normalization
**Milestones:**
- Ingest CPT/ICD-10/HCPCS code databases (nucc.org, CMS)
- Normalize 20 major payer denial reason codes (Aetna, UHC, Cigna, Anthem, Medicare, Medicaid)
- Build mapping: `{denial_reason_code} → {likely_policy} → {appeal_strategy}`
- Ingest final Medicare LCD/NCD libraries (>5,000 local coverage determinations)
- Connect to 1 EHR API (Epic FHIR preferred; fallback Cerner HL7)

**Deliverables:**
- `code_lookup.py` – CPT/ICD-10 validation & code description retrieval
- `payer_policy_db.json` – Normalized 20-payer denial reason mapping
- `ehr_connector.py` – Epic FHIR query wrapper (gets clinical notes for claim)

#### Weeks 3–4: EHR & Claim Data Pipeline
**Milestones:**
- Connect to hospital's EHR system (pilot: 1 mid-size hospital system)
- Build claim ingestion from payer EDI Stream (837 remittance or payer API)
- Extract: claim ID, patient demographics, ICD-10 codes, billed procedures (CPT), denial reason, payer policy reference
- Link claim → EHR clinical notes (match via MRN + DOS + CPT code)
- Build data validation pipeline (reject malformed claims early)

**Deliverables:**
- `claim_ingestion.py` – Parse EDI 835 (remittance advice) or payer API JSON
- `clinical_lookup.py` – Query EHR for patient records + clinical notes
- `claim_validation.py` – Validate claim structure, flag missing data

#### Weeks 5–6: LLM-Powered Appeal Generation
**Milestones:**
- Fine-tune LLM on 1,000+ de-identified denied claim appeals (from prior litigation databases, CMS samples)
- Build prompt engineering for medical necessity appeal letters
- Generate appeals that cite: specific payer policy, relevant LCD/NCD, clinical evidence from patient record
- Implement fact-checking layer (verify cited CPT codes are accurate, dates align, etc.)
- Output: Human-readable appeal letter (ready for signature + submission)

**Deliverables:**
- `appeal_generator.py` – LLM prompt + generation logic
- `appeal_validator.py` – Fact-check generated claims against clinical notes
- `appeal_templates/` – JSON templates per payer (Aetna, UHC, etc.) with variable substitution

#### Weeks 7–8: Payer Integration & Submission
**Milestones:**
- Integrate with payer submission portals (most accept secure EDI or API)
- Build submission wrapper (auto-format appeal letter as PDF, bundle with evidence docs, submit via payer portal)
- Implement tracking mechanism (poll payer for submission status)
- Handle payer response parsing (accept/deny/request more info)
- Build audit trail (log every appeal, outcome, evidence chain)

**Deliverables:**
- `payer_submission.py` – Format appeal + submit via payer API or EDI
- `status_tracker.py` – Poll for appeal status; parse payer responses
- `audit_log.json` – Immutable transaction log per claim

#### Weeks 9–10: Human-in-the-Loop Review & Deployment
**Milestones:**
- Build hospital-facing dashboard (display pending appeals, flagged cases requiring human review)
- Implement confidence scoring (flag low-confidence appeals for manual review before submission)
- Train hospital coding team (2-day workshop on tool usage, escalation workflows)
- Deploy to hospital production (claims live from their payer feeds)
- Set up daily monitoring (accuracy tracking, appeal win rate trending)

**Deliverables:**
- `dashboard.py` – Flask/Streamlit UI for hospital admins
- `escalation_logic.py` – Route low-confidence appeals to human reviewer
- `monitoring.py` – Daily accuracy + win-rate reports

#### Weeks 11–12: Validation & Scaling
**Milestones:**
- Measure accuracy against human coder validation (blind comparison: did AI's reasoning match coder's?)
- Target: 80%+ coders agree with AI-generated appeal reasoning
- If <80%, iterate on LLM fine-tuning
- Test scaling: 100 claims/day (typical mid-size hospital denial traffic)
- Plan Phase 2 (connect to 2nd EHR system; expand payer coverage to 50 payers)

**Deliverables:**
- `validation_report.pdf` – Accuracy benchmarking vs manual coders
- `scaling_test.log` – Load test at 100 claims/day; monitor latencies
- `phase2_roadmap.md` – Plan for 2nd hospital + expanded payer network

### Revenue Model
- **Contingency:** 25–35% of appeal recovery (if claim's appeal succeeds, hospital pays % of recovered amount)
- **Volume mechanics:** 
  - Mid-size hospital (500-bed system): 3,000 claims/month × 15% denial rate = 450 denied claims/month
  - Assume 35% appeal win rate (higher than human because AI finds better evidence) = 157 successful appeals
  - Average claim value $5,000 → $785k recovered/month
  - 30% contingency fee = $235k/month = $2.8M/year per hospital
  - **1 pilot hospital = $235k/month starting Day 1 of production deployment**

### Success Metrics
- Accuracy: 80%+ coder agreement with appeal reasoning
- Appeal submission success: 95%+ (properly formatted, received by payer)
- Appeal win rate: 40%+ (initial; iterate to 50%+ as system learns)
- Deployment: Live with 1 hospital by Week 12; processing 100 claims/day by end of Month 2

---

## EPIC #2: Import Duty & Tariff Minimization (EP-0906)

### MVP Scope (3 Months)
**Goal:** Autonomously classify HS codes and calculate optimal tariff + trade agreement savings for imported goods.

### Week-By-Week Roadmap

#### Weeks 1–2: Tariff Data Ingestion
**Milestones:**
- Ingest ITC HS Code database (10,000+ product categories with tariff rates)
- Normalize tariff rates per country (US, EU, Mexico, China, India, Vietnam, etc.)
- Ingest US trade agreement schedules (USMCA origin rules, EU GSP, etc.)
- Build real-time tariff lookup (query HS code → return applicable duty rate per origin country)
- Version control tariff data (capture monthly updates from ITC)

**Deliverables:**
- `hs_code_db.json` – Complete HS code hierarchy + tariff rates
- `tariff_lookup.py` – Fast query engine (HS code → duty rate)
- `tariff_updater.py` – Auto-sync with ITC monthly releases

#### Weeks 3–4: HS Code Classification
**Milestones:**
- Build rules-based HS code classifier (decision trees: Is it "finished goods"? Contains <50% material X? Final assembly location?)
- Ingest 10k historical HS classifications from customs rulings (ITC, CBP APHIS databases)
- Fine-tune LLM on custom HS classification task (many ambiguous cases require judgment)
- Implement fallback logic: if rules-based classifier <70% confident, escalate to LLM or human broker
- Output: `{product_description} → {HS_code} @ {confidence_score}`

**Deliverables:**
- `hs_classifier_rules.py` – Decision tree logic for common products
- `hs_classifier_llm.py` – LLM-powered ambiguous case resolution
- `classification_confidence.py` – Scoring logic; flags for human review

#### Weeks 5–6: ERP & BOM Integration
**Milestones:**
- Connect to ERP APIs (SAP, Oracle NetSuite, Coupa — prioritize 2 of 3)
- Extract purchase orders + BOM structures (products, quantities, supplier origin)
- Map supplier master data → country of origin
- Build supplier product history (track: this supplier has shipped "USB cables from China" 100x; they match HS 8471)
- Pre-populate HS classification suggestions (new order: auto-suggest HS code based on supplier history + product name)

**Deliverables:**
- `erp_connector_sap.py` – SAP API integration for POs + BOMs
- `erp_connector_coupa.py` – Coupa procurement integration
- `supplier_history.py` – Track historical HS classifications per supplier product combo

#### Weeks 7–8: Trade Agreement Logic & Duty Calculation
**Milestones:**
- Ingest USMCA certificate rules (origin requirements, content thresholds, processing rules)
- Implement trade agreement eligibility logic (if good originating in Mexico + <50% non-originating content = USMCA eligible = duty waived)
- Build duty calculator: `{HS_code} × {origin_country} × {quantity} × {tariff_rate} → {total_duty}`
- Implement savings identifier: compare standard duty vs reduced duty (USMCA, GSP, special waivers)
- Output: duty estimate with confidence; identify duty minimization opportunities

**Deliverables:**
- `trade_agreement_checker.py` – Verify USMCA/GSP eligibility
- `duty_calculator.py` – Compute total duty + identify savings opportunities
- `duty_report.py` – Generate summary report (SKU-level savings potential)

#### Weeks 9–10: Port Integration & Customs Submission
**Milestones:**
- Connect to port APIs (LA/LB, NYC, Houston offer SCOS integration; fallback to EDI 322)
- Build customs documentation generator (invoice, packing list, HS certificate, USMCA origin declaration if applicable)
- Implement pre-clearance logic (submit documentation before shipment arrives; shorten port dwell time)
- Build audit trail (log all HS classifications, duty calculations, submissions)
- Set up feedback loop (when shipment clears customs, store actual HS code applied by CBP; compare vs our prediction)

**Deliverables:**
- `port_api_connector.py` – Integrate with port SCOS systems
- `customs_doc_generator.py` – Create compliant customs declarations
- `feedback_loop.py` – Track CBP rulings; improve classifier over time

#### Weeks 11–12: Validation & Pilot Deployment
**Milestones:**
- Partner with 1 importer (target: $500M+ annual imports, diverse product portfolio)
- Classify 1,000 pilot SKUs (historical purchases); compare our HS codes vs importer's current classifications
- Measure: # of misclassifications found, $ savings potential
- Deploy to live PO stream (flag high-savings opportunities; generate duty minimization recommendations)
- Set up monthly reconciliation (actual vs predicted duties; measure impact on financials)

**Deliverables:**
- `pilot_analysis.pdf` – HS classification accuracy benchmarking vs importer's historical data
- `savings_report.pdf` – Quantified duty savings potential ($ per month, $ per year)
- `live_deployment.log` – Monitor real POs; track accuracy over 4 weeks

### Revenue Model
- **Contingency:** 40% of duty savings (importer pays platform 40% of the duty $ saved)
- **Volume mechanics:**
  - Enterprise importer with $1B annual import spend @ 3.2% avg tariff = $32M annual duty burden
  - Assume 3.5% of purchases are misclassified (overpaying duty) = $1.12M annual overpayment
  - Assume further 2% of purchases are tariff-eligible (USMCA, GSP) but importer unaware = $640k missed savings opportunity
  - Total annual savings identified: ~$1.76M
  - 40% capture = $700k Year 1
  - **1 pilot importer = $58k/month starting Month 2 of production**

### Success Metrics
- HS code accuracy: 85%+ match with importer's current classifications (establishes baseline trust)
- Savings identification: $1M+ annual duty savings per customer
- False positive rate: <5% (flag legitimate ambiguities for human broker, not wrong classifications)
- Deployment: Live with 1 importer by Week 12; processing new POs real-time by Month 2

---

## EPIC #3: Published Research Data Monetization (EP-0907)

### MVP Scope (3 Months)
**Goal:** Autonomously identify valuable academic datasets from published papers; broker licensing to pharmaceutical companies.

### Week-By-Week Roadmap

#### Weeks 1–2: Paper Indexing & Scraping
**Milestones:**
- Ingest arXiv, PubMed Central, bioRxiv, medRxiv APIs (500k papers in scope: life sciences, medical, biotech)
- Build paper metadata extractor: title, authors, institution, journal, publication date, citation count
- Scan full-text PDFs for dataset mentions/URLs (regex: "Data available at...", "Supplementary data", "GitHub repo")
- Extract supplementary data file URLs (many papers host supplementary data on Zenodo, Figshare, OSF)
- Build initial dataset catalog (500 datasets identified in Week 2)

**Deliverables:**
- `paper_scraper.py` – Query arXiv/PubMed/bioRxiv APIs; fetch PDFs
- `dataset_extractor.py` – NLP-based extraction of dataset mentions + URLs
- `dataset_catalog.json` – Initial 500-dataset index (title, publication, authors, URL, metadata)

#### Weeks 3–4: Dataset Valuation & Classification
**Milestones:**
- Classify datasets by commercial value (pharma interest, meta-analysis utility, indication potential)
- Build valuation heuristics: 
  - Paper citations (high citations = high interest = higher licensing value)
  - Author h-index (high h-index researchers = their data is valuable)
  - Cohort size (larger trials = more valuable for meta-analysis)
  - Specificity (rare disease data = more valuable than common domain)
- Flag datasets with >$50k estimated annual licensing potential
- Estimate: ~50 datasets meet $50k+ threshold from 500 initial catalog

**Deliverables:**
- `dataset_valuation.py` – Scoring algorithm (citations × h-index × cohort-size × specificity)
- `valuation_report.json` – Ranked datasets by estimated value
- `high_value_subset.json` – Top 50 datasets for outreach

#### Weeks 5–6: De-identification & Compliance
**Milestones:**
- Screen datasets for HIPAA compliance (clinical data requires de-identification or explicit public dataset status)
- Build automatic de-identifier (remove PHI: names, MRNs, exact dates; replace with time-offsets)
- Verify dataset compliance: Is it published open-source? Is it de-identified per HIPAA? Does it have explicit consent for secondary use?
- Classify into tiers:
  - Tier 1: Published open-source, fully de-identified (ready to license immediately)
  - Tier 2: Published but with restrictions (need author consent to broker license)
  - Tier 3: Sensitive data (requires IRB waiver or explicit consent)
- Prioritize Tier 1 for MVP (zero friction; can start licensing Day 1)

**Deliverables:**
- `deidentifier.py` – HIPAA-compliant PHI removal
- `compliance_checker.py` – Verify open-source + de-identification status
- `dataset_tiers.json` – Classify all 500 datasets; prioritize Tier 1 (expect ~100 Tier 1 datasets)

#### Weeks 7–8: Researcher Outreach & Licensing Portal
**Milestones:**
- For Tier 1 datasets: Auto-generate licensing offer emails to corresponding authors
- For Tier 2 datasets: Auto-generate consent request emails
- Build researcher portal (secure upload area; version control; usage analytics; royalty tracking)
- Set up licensing agreement templates (researcher grants platform right to broker licensing; researcher receives 70% of licensing revenue)
- Implement royalty tracking (per dataset: # licensees, annual licensing revenue, researcher payout)
- Estimate engagement rate: ~30% of outreach researchers respond positively within 30 days

**Deliverables:**
- `researcher_outreach.py` – Auto-generate personalized licensing offer emails
- `researcher_portal.py` – Secure upload + license management interface
- `licensing_agreement_template.md` – Legal document (researcher + platform terms)
- `royalty_tracker.py` – Track per-dataset licensing revenue + researcher splits

#### Weeks 9–10: Pharma Buyer Outreach & Licensing
**Milestones:**
- Identify pharma buyers (licensing managers at Pfizer, Novartis, GSK, J&J, Roche, etc.)
- Auto-generate licensing offers to pharma (curated datasets matching their therapeutic area)
- Build pricing model: 
  - Tier 1 (common domains, large cohorts): $25k/year per licensee
  - Tier 2 (rare disease, specialized data): $50k/year per licensee
  - Tier 3 (unique biomarkers, proprietary cohorts): $100k+/year per licensee
- Set up licensing portal (pharma company can browse datasets, request access, execute licensing agreements)
- Launch with 5 pharma pilot customers (target: oncology, immuno, rare disease specialties)

**Deliverables:**
- `pharma_outreach.py` – Auto-generate personalized licensing offers based on therapeutic area
- `pharma_portal.py` – Dataset discovery + licensing UI for pharma buyers
- `licensing_agreement.json` – Standardized pharma license terms
- `pricing_engine.py` – Dynamic pricing based on dataset tier + exclusivity period

#### Weeks 11–12: Validation & Scaling
**Milestones:**
- Deploy with 5 pilot researchers + 3 pilot pharma customers
- Launch with 20 Tier 1 datasets (fully compliant; ready for immediate licensing)
- Measure: # of licensing agreements executed, $ revenue generated, researcher satisfaction
- Target: 1–2 pharma licensing agreements by end of Week 12 ($25k–$50k in Year 1 revenue)
- Plan Phase 2 (tier 2 researcher onboarding + direct dataset hosting on platform)

**Deliverables:**
- `pilot_results.pdf` – Researcher + pharma engagement metrics
- `revenue_report.json` – Licensing revenue (expect $25k–$50k from 2–3 pharma licenses in MVP window)
- `phase2_roadmap.md` – Plan to expand to Tier 2 + Tier 3 datasets + direct researcher support

### Revenue Model
- **Licensing Revenue:** Platform takes 30% of licensing fees; researcher gets 70%
- **Volume mechanics:**
  - Launch with 20 Tier 1 datasets
  - Target 2–3 pharma customers licensing datasets (assume 3–5 datasets per customer)
  - Average licensing fee: $35k/dataset/year
  - 6 licenses × $35k = $210k gross licensing revenue
  - Platform take: 30% = **$63k Year 1** (conservative MVP forecast)
  - By Year 2 (scaling to 100 datasets, 20 pharma customers): **$2–3M/year platform revenue**

### Success Metrics
- Datasets onboarded: 20 Tier 1 datasets by end of Week 12
- Pharma engagement: 3+ licensing offers accepted; 2–3 pharma customers signed
- Researcher engagement: 5+ researchers signed researcher agreements
- Revenue: $25k–$75k Year 1 (from pilot licensing agreements)
- Deployment: Live pharma licensing portal by Week 11; 2–3 active licenses by Week 12

---

## EPIC #4: Government RFP Automation at Scale (EP-0908)

### MVP Scope (3 Months)
**Goal:** Autonomously generate 50-page government proposal responses matching RFP requirements and evaluation criteria.

### Week-By-Week Roadmap

#### Weeks 1–2: RFP Data Ingestion
**Milestones:**
- Ingest SAM.gov RFP feed (real-time; 50k+ active RFPs in XML/JSON format)
- Parse RFP structure: requirements section, evaluation criteria, compliance/FAR clauses, deadlines
- Extract: NAICS code, estimated contract value, agency, keywords
- Build historical RFP database (10k past RFPs with outcomes; used for precedent matching + win-rate analysis)
- Set up real-time RFP monitoring (new RFPs matching customer criteria auto-flagged)

**Deliverables:**
- `sam_gov_ingester.py` – Real-time SAM.gov RFP feed integration
- `rfp_parser.py` – Extract structure, requirements, evaluation criteria, FAR clauses
- `rfp_database.json` – 10k+ historical RFPs with win/loss outcomes
- `rfp_monitor.py` – Real-time new RFP alerts matching customer criteria

#### Weeks 3–4: Compliance & FAR Clause Library
**Milestones:**
- Ingest FAR (Federal Acquisition Regulation) clause library (~6,000 clauses)
- Normalize clauses into templates (52.200-series, 52.202, 52.219, etc. — most RFPs reuse same clauses)
- Build FAR clause matcher (given RFP, identify which FAR clauses are required)
- Auto-populate compliance section of proposals (boilerplate text for each required clause)
- Reduce manual effort: FAR compliance drops from "4 hours human work" to "template instantiation"

**Deliverables:**
- `far_clause_library.json` – 6,000+ FAR clauses with standard language
- `clause_matcher.py` – Given RFP, identify required FAR clauses
- `compliance_generator.py` – Auto-populate compliance sections from templates

#### Weeks 5–6: Proposal Writing Engine
**Milestones:**
- Fine-tune LLM on 10k past winning proposals (government contracts with published reports)
- Train on government writing style (formal, requirement-focused, repetitive, jargon-heavy but clear)
- Build proposal structure generator:
  - Technical approach (maps firm capabilities → RFP requirements)
  - Past performance (pulled from FPDS; auto-formatted for gov evaluation)
  - Cost estimate (benchmarked against historical similar contracts)
  - Management plan (org chart, timeline, risk mitigation)
- Implement requirement traceability (each proposal section explicitly states which RFP requirement it addresses)

**Deliverables:**
- `proposal_generator.py` – LLM-powered proposal writing
- `requirement_traceability.py` – Map proposal sections to RFP requirements
- `proposal_templates/` – Modular sections (technical, past perf, mgmt, cost)

#### Weeks 7–8: Past Performance & Cost Integration
**Milestones:**
- Ingest FPDS (Federal Procurement Data System) to retrieve customer's contract history
- Auto-populate "Past Performance" section (pull customer's prior contracts, dollar values, completion dates)
- Build cost estimation engine:
  - Benchmark against FPDS awarded prices for similar contracts
  - Apply scaling factors (complexity, timeline, labor rates, overhead)
  - Generate realistic cost estimate matching RFP evaluation expectations
  - Flag if customer's cost proposal is suspiciously low/high vs benchmarks
- Validate proposal competitiveness (does cost + technical approach beat median for similar contracts?)

**Deliverables:**
- `fpds_connector.py` – Retrieve customer's past performance data
- `past_performance_generator.py` – Format historical contracts for proposal
- `cost_estimator.py` – Benchmark + estimate cost; flag outliers

#### Weeks 9–10: Proposal Quality & Human Review
**Milestones:**
- Build proposal quality scorer (readability, grammar, requirement coverage, compliance completeness)
- Generate initial proposal draft (50+ pages, complete sections, compliance language)
- Create human review UI (highlight sections flagged for review, allow editing, approval workflow)
- Implement version control (track edits; enable re-generation if customer updates requirements)
- Set up submission workflow (final PDF generation; auto-submit to SAM.gov or agency portal if enabled)
- Target: Reduce proposal writing time from 100 hours (manual) to 10 hours (with AI + human review)

**Deliverables:**
- `proposal_scorer.py` – Quality metrics (coverage, grammar, compliance)
- `human_review_ui.py` – Streamlit interface for proposal review + editing
- `submission_module.py` – Format proposal; submit to SAM.gov or agency portals
- `version_control.py` – Track edits; enable re-generation

#### Weeks 11–12: Pilot Deployment & Outcome Tracking
**Milestones:**
- Deploy with 5 pilot SMBs (IT services, construction, logistics, consulting, manufacturing verticals)
- Generate proposals for 3–5 RFPs per SMB (15–25 total proposals in MVP window)
- Track outcomes: submitted proposals, win/loss results, evaluation feedback (if available)
- Measure: 
  - Proposal submission success (95%+ accepted by agencies; zero compliance rejections)
  - Win rate vs historical SMB average (SMBs typically 5–10% win rate; target: demonstrate 15%+ with better writing)
  - Time-to-submission (goal: 8 hours from RFP release to final proposal)
- Build feedback loop (capture eval scores if available; use to improve LLM scoring + targeting)

**Deliverables:**
- `pilot_results.pdf` – Pilot SMB engagement metrics, proposal submission success, preliminary win rate
- `outcome_tracker.json` – Per-proposal: submitted, won/lost, evaluation score if available
- `feedback_loop.py` – Ingest agency feedback; retrain LLM on higher-scoring proposals
- `phase2_roadmap.md` – Scale to 50–100 SMB customers; expand to DoD + state/local RFPs

### Revenue Model
- **Per-Proposal Fee:** $5,000 per RFP response (vs $15k–$50k manual writing costs)
- **Volume mechanics:**
  - 5 pilot SMBs × 4 RFPs/month/SMB × $5k per proposal = $100k/month
  - Assume 30% adoption (out of addressable SMB gov contractor market): 500 customers
  - 500 customers × 3 proposals/month × $5k = **$7.5M/year revenue** (mature state)
  - **MVP window (Weeks 11–12): $75k–$125k from pilot 5 SMBs** (if they do 3–5 RFPs each in first month)

### Success Metrics
- Proposal generation success: 95%+ submission completion (properly formatted, all required sections)
- Compliance quality: 100% (zero agency rejections for missing FAR clauses or non-responsive sections)
- Win rate: Target 15%+ (vs SMB historical 5–10%)
- Time reduction: 10 hours human effort per proposal (vs 100 hours historically)
- Deployment: Live with 5 SMBs by Week 12; processing 3–5 RFPs/month per customer by Month 3

---

## EPIC #5: Supply Chain ESG & Sustainability Compliance (EP-0909)

### MVP Scope (3 Months)
**Goal:** Autonomously calculate Scope 3 emissions, generate regulatory disclosures (CSRD/CBAM), and flag non-compliant suppliers.

### Week-By-Week Roadmap

#### Weeks 1–2: Emissions Factor Database
**Milestones:**
- Ingest emissions factor databases (GHG Protocol Scope 3, EPA, IPCC, EcoInvent)
- Normalize across databases (kgCO2e per unit: kg material, mile shipped, kWh energy, etc.)
- Build lookup engine: `{material_type} × {quantity} × {supplier_location} → {emissions}`
- Create material-specific factors (steel = 2.1 kgCO2e/lb, aluminum = 12.5, plastic = 5.3, etc.)
- Version control (update with annual IPCC revisions)

**Deliverables:**
- `emissions_db.json` – Normalized emissions factors across all material types
- `emissions_calculator.py` – Fast lookup + multiplication
- `emissions_updater.py` – Auto-sync with GHG Protocol/EPA annual updates

#### Weeks 3–4: Supply Chain Data Integration
**Milestones:**
- Connect to procurement systems (Ariba, Coupa, SAP — prioritize 2 of 3)
- Extract supplier master data (name, industry, country, size)
- Pull transaction history (PO history: what, from whom, when, how much)
- Map suppliers to industry sectors (classify supplier: Tier 1 manufacturer, logistics, raw material, etc.)
- Build supplier carbon profile lookup (many suppliers already have published ESG footprints; query: CDP, SCI, SASB databases)
- Fallback: Estimate supplier emissions from industry benchmark + supplier size

**Deliverables:**
- `procurement_connector_ariba.py` – Ariba API integration
- `procurement_connector_coupa.py` – Coupa integration
- `supplier_carbon_lookup.py` – Query CDP/SCI for published carbon footprints
- `supplier_baseline_estimator.py` – Industry benchmark × supplier size for unknown suppliers

#### Weeks 5–6: Scope 3 Emissions Calculation
**Milestones:**
- Implement GHG Protocol Scope 3 calculation logic (standard methodology)
- For each PO: 
  - Scope 3 Category 1 (Purchased goods): `supplier_emissions × order_quantity`
  - Scope 3 Category 4 (Upstream transport): `transport_mode × distance × weight`
  - Sum across all suppliers for comprehensive Scope 3 footprint
- Build transaction logging (every PO → emissions calculation → stored in ledger)
- Validate precision (track confidence: high confidence if supplier has published data; low if estimated)
- Monthly rollup (sum all October transactions; report October Scope 3 total)

**Deliverables:**
- `scope3_calculator.py` – Scope 1/2/3 calculation per GHG Protocol
- `transaction_logger.py` – Log every PO + related emissions calculation
- `monthly_rollup.py` – Aggregate per-period emissions totals

#### Weeks 7–8: Regulatory Reporting (CSRD/CBAM/TCFD)
**Milestones:**
- Ingest CSRD reporting requirements (EU standard; mandatory 2026–2027)
- Ingest CBAM reporting framework (carbon border adjustment mechanism; mandatory Q1 2026)
- Ingest TCFD disclosure guidelines (Task Force on Climate-Related Financial Disclosure; US pending)
- Build report generators:
  - CSRD report: Scope 1/2/3 totals, emissions intensity, supplier engagement plan
  - CBAM report: Scope 3 emissions per imported product; carbon passport generation per product
  - TCFD report: Climate risk assessment, emissions targets, mitigation strategies
- Auto-populate with live data from procurement + emissions database
- Output: PDF reports ready for regulatory submission

**Deliverables:**
- `csrd_report_generator.py` – Generate CSRD disclosure (Scope 1/2/3, supplier strategy, targets)
- `cbam_report_generator.py` – Generate CBAM carbon passport per SKU; declare import duties
- `tcfd_report_generator.py` – Generate TCFD climate risk disclosure
- `regulatory_submission.py` – Format for EU/SEC filing; track submission status

#### Weeks 9–10: Supplier Engagement & Scoring
**Milestones:**
- Build supplier carbon scorecard (rank: high/medium/low carbon intensity)
- Auto-identify outlier suppliers (top 20% emitters; flag for engagement)
- Generate supplier engagement templates (auto-email high-emitter suppliers: "Your carbon intensity is X; industry average is Y; here's how to reduce...")
- Implement carbon reduction opportunity identification (flag: this supplier could reduce emissions by 20% if they switch to green energy; cost impact: $X)
- Build incentive mechanism (offer: if supplier reduces emissions by 15%, we'll increase PO volume by 5%)

**Deliverables:**
- `supplier_scorecard.py` – Rank suppliers by carbon intensity
- `supplier_outlier_detector.py` – Flag high-emitter suppliers for engagement
- `supplier_engagement_templates.py` – Auto-generate outreach emails
- `reduction_opportunity_finder.py` – Identify cost-effective emissions cuts per supplier

#### Weeks 11–12: Deployment & Validation
**Milestones:**
- Deploy with 2–3 pilot enterprises (target: $1B+ revenue; EU-listed or SEC-listed; facing CSRD/CBAM compliance deadlines)
- Ingest 6 months of historical PO data (backfill emissions calculations; track trends)
- Generate mock CSRD/CBAM reports (validate regulatory compliance; get feedback from pilot's sustainability team)
- Measure: 
  - Data completeness (% of suppliers with carbon data vs estimated)
  - Emissions accuracy (compare calculated totals vs pilot's manual estimate; target: <10% delta)
  - Regulatory readiness (do reports pass sustainability team review?)
- Plan Phase 2 (expand to 10–20 enterprises; integrate with compliance/audit systems)

**Deliverables:**
- `pilot_results.pdf` – Enterprise engagement metrics, emissions accuracy validation, regulatory report acceptance
- `emissions_report.json` – 6-month retrospective emissions totals + trends
- `csrd_cbam_reports.pdf` – Sample regulatory reports (show pilot's sustainability team)
- `phase2_roadmap.md` – Plan for enterprise scaling + integration with auditors

### Revenue Model
- **SaaS Subscription:** Annual contract, $250k–$500k per enterprise (varies by # of suppliers, regions, compliance scope)
- **Contingency/Incentive:** 10% of documented emissions reduction costs saved (if supplier reduces emissions by $1M, platform gets $100k)
- **Volume mechanics:**
  - Target 3 pilot enterprises in MVP → $1M Year 1 (assuming 2–3 signed)
  - Enterprise SAC duration: 3-year typical (CSRD 3-year compliance timeline)
  - Scale Year 2: 20 customers × $350k ACV = $7M/year
  - Scale Year 3: 50 customers × $400k ACV = $20M/year

### Success Metrics
- Data completeness: 80%+ suppliers with published or estimated carbon data
- Emissions accuracy: <10% delta vs manually calculated totals
- Regulatory readiness: Generated CSRD/CBAM reports pass sustainability team review
- Deployment: Live with 2–3 enterprises by Week 12; processing monthly emissions reports, generating regulatory disclosures

---

## Cross-EPIC Timeline & Resource Allocation

### Total Build Resource Requirements
- **Engineers Required:** 7–8 Full-Time Equivalent for 12 weeks
  - EPIC #1 (Medical Coding): 1.5 FTE
  - EPIC #2 (Import Duty): 1.5 FTE
  - EPIC #3 (Research Data): 1 FTE
  - EPIC #4 (Government RFP): 2 FTE
  - EPIC #5 (Supply Chain ESG): 1.5 FTE
  
- **Specialists Required:** 3–4 FTE
  - Medical/healthcare coder (EPIC #1): 0.5 FTE
  - Trade/customs specialist (EPIC #2): 0.5 FTE
  - Research/pharma domain expert (EPIC #3): 0.3 FTE
  - Gov contracting specialist (EPIC #4): 0.4 FTE
  - ESG/sustainability expert (EPIC #5): 0.3 FTE

- **Total 12-Week Budget:** ~$800k–$1.2M (contract labor + tools + cloud infrastructure)

### Parallel Work Streams
**Weeks 1–4:** Data ingestion + normalization (all 5 EPICs in parallel)
**Weeks 5–8:** Core logic + ML model training (all 5 EPICs in parallel)
**Weeks 9–10:** Integration + human workflows (all 5 EPICs in parallel)
**Weeks 11–12:** Pilot deployment + validation (all 5 EPICs in parallel)

### Expected MVP Deployment Schedule
- **Week 12 End State:** 
  - EPIC #1: Live with 1 hospital; 100 claims/day processing
  - EPIC #2: Live with 1 importer; $58k/month potential revenue
  - EPIC #3: 5 researchers + 3 pharma customers; $25k–$75k Year 1 expected
  - EPIC #4: 5 SMBs; 3–5 RFPs/month × 5 = 15–25 proposals in first month
  - EPIC #5: 2–3 enterprises; monthly ESG reporting live

### Phase 2 Roadmap (Months 4–12)
**EPIC #1 (Medical Coding):** Expand to 5 hospital systems; add 30 payers; measure 50%+ appeal success rate
**EPIC #2 (Import Duty):** Expand to 5 importers; refine HS classifier; add export duty optimization
**EPIC #3 (Research Data):** Onboard Tier 2 researchers; expand to 100+ datasets; target $500k Year 1 revenue
**EPIC #4 (RFP):** Scale to 50 SMBs; add DoD RFP support; measure 20%+ win rate
**EPIC #5 (ESG):** Scale to 20 enterprises; integrate with audit firms; target $7M Year 2 revenue

---

## Success Criteria & KPIs

### Technical Metrics
| EPIC | MVP Target Accuracy | MVP Feasibility | MVP Deployment Week |
|------|-------------------|-----------------|-------------------|
| Medical Coding | 80% coder agreement | 8.5/10 | Week 12 |
| Import Duty | 85% HS code match | 8.2/10 | Week 12 |
| Research Data | 20 Tier-1 datasets | 7.8/10 | Week 11 |
| Govt RFP | 95% submission success | 8.6/10 | Week 12 |
| Supply Chain ESG | 80% data completeness | 8.1/10 | Week 12 |

### Business Metrics
| EPIC | Month 1 Revenue | Month 3 Projection | Year 1 Projection |
|------|---------------|-------------------|------------------|
| Medical Coding | $235k | $400k | $2.8M |
| Import Duty | $58k | $200k | $840k |
| Research Data | $0 (waiting for licensing) | $25k | $63k |
| Govt RFP | $100k | $300k | $2M |
| Supply Chain ESG | $250k | $500k | $1M |
| **PORTFOLIO TOTAL** | **$643k** | **$1.4M** | **$6.7M** |

---

## Risk Mitigation & Contingency Plans

### EPIC #1: Medical Coding — Payer Integration Delays
**Risk:** Hospital payers slow to integrate APIs; manual submission required longer than expected
**Mitigation:** Start with EDI submission (electronic data interchange) via hospital's existing EDI vendor; avoid direct payer API dependency in MVP
**Contingency:** Allow human submission of appeals if payer integration not ready; still automates 80% of work

### EPIC #2: Import Duty — HS Code Ambiguity
**Risk:** 15–20% of HS classifications are genuinely ambiguous; can't automate 100%
**Mitigation:** Position as "duty optimization advisor"; flag ambiguous cases (confidence <70%) for humans (customs broker)
**Contingency:** Land 2 customers with simpler product portfolios (electronics vs machinery); expand to complex products in Phase 2

### EPIC #3: Research Data — Researcher Engagement Friction
**Risk:** Academic researchers slow to respond; many don't want to commercialize their data
**Mitigation:** Start with already-open-source datasets (Zenodo, Figshare, OSF); no researcher consent needed
**Contingency:** Begin licensing from public datasets; add researcher onboarding once demand is proven

### EPIC #4: Government RFP — SMB Sales Friction
**Risk:** SMBs are small, fragmented; hard to sell; long sales cycles
**Mitigation:** Launch with low-price-point ($5k per proposal); position as "insurance" (reduce RFP writing risk)
**Contingency:** Target larger mid-market contractors ($50M+ revenue) with more efficient procurement processes

### EPIC #5: Supply Chain ESG — Data Quality
**Risk:** Many suppliers don't have published carbon data; estimates are unreliable
**Mitigation:** Start with tier-1 suppliers (large, published ESG data); tier-2/3 suppliers get industry benchmarks + manual engagement
**Contingency:** Offer concurrent "supplier engagement" service (charge to help suppliers get certified ESG data)

---

## Conclusion

This 12-week roadmap delivers 5 autonomous agents targeting $630M+ Year 1 revenue across untapped sectors with <1% automation penetration. By leveraging existing data, regulatory tailwinds, and deep domain expertise, the portfolio achieves:

- **Average feasibility: 8.2/10** (solo-founder buildable)
- **Average time-to-revenue: 2 months** (1.5–3 month range)
- **Portfolio payback: 2–4 weeks** (cost vs Year 1 revenue)
- **Phase 2 revenue: $8–10M/year** (scaling to 20–50 customers per EPIC)

The key to success is **parallel execution** (all 5 EPICs simultaneously) and **ruthless prioritization** (focus on MVP; defer nice-to-haves to Phase 2).
