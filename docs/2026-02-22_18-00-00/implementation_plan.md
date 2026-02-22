# Implementation Plan (Parallel, 8-week MVPs)

## Phase 1: Weeks 1–2 (Foundation)

### EP-0924: Payment Recovery
- Integrate Stripe Webhook API; ingest declined events (ChargeFailedError, AuthenticationRequired, etc.).
- Integrate Chargebee API for subscription metadata (plan, MRR, customer cohort).
- Parse failed transaction reasons into taxonomy (card expired, insufficient funds, 3D auth failure, issuer decline).

### EP-0925: Email Deliverability
- Integrate SendGrid Event Webhook API; ingest bounce/complaint/open events.
- Integrate Mailchimp/Campaign Monitor APIs.
- Parse bounce types (hard, soft, complaint); extract ISP feedback loop (FBL) signals.

### EP-0926: Course Analytics
- Integrate Canvas LMS API; ingest page views, quiz attempts, video watch events.
- Integrate Teachable/Kajabi APIs via Zapier/custom hooks.
- Create event schema: learner ID, lesson ID, event type, timestamp, duration.

---

## Phase 2: Weeks 3–4 (Core Logic)

### EP-0924: Payment Health Scoring + Retry Optimize
- Feature engineering: days-since-decline, customer age, MRR, plan type, prior decline history.
- Build payment health score (0–100%): decline risk prediction + recoverability.
- Train retry optimization model on historical data: "What timing/messaging recovers each cohort?"
  - Cohort A: 3-day delay + 20% discount → 50% recovery.
  - Cohort B: immediate retry + full amount → 35% recovery.
  - Cohort C: pause 14 days + new card prompt → 40% recovery.

### EP-0925: Authentication Audit + Reputation Scoring
- DNS lookup: Pull DKIM/SPF/DMARC records for customer domain; compare to best practices.
- Auto-generate: Corrected DKIM/SPF/DMARC records (template-based).
- Reputation scoring: ISP complaint rate, bounce rate, authentication pass rate → inbox placement risk.
- Model: Logistic regression; features = (DKIM_present, SPF_valid, DMARC_enforced, complaint_rate, bounce_rate, authentication_pass_rate) → P(inbox placement).

### EP-0926: Engagement Feature Engineering + Dropout Model
- Time-on-page, video completion %, quiz pass rate, days-since-last-engagement, cohort (new vs. returning), device type.
- Build gradient boosting dropout model: XGBOOST on labeled data (completed=1, refunded=0).
- Threshold tuning: Find decision threshold that maximizes (precision × recall), targeting 70%+ precision; 50%+ recall.

---

## Phase 3: Weeks 5–6 (Automation + Testing)

### EP-0924: Auto-Dunning + Win-Back
- Build state machine: NewDecline → ScorePaymentHealth → WaitOptimalTime → RetryPayment → CheckOutcome → Repeat or Escalate.
- Auto-trigger email/SMS based on cohort: "We tried charging on [date]; card was declined. Please update payment method."
- Implement outcome feedback: Track "retry_sent → payment_succeeded / payment_failed / customer_cancelled."

### EP-0925: Auto-Fix + Recovery Campaign
- Auto-generate DNS records for broken DKIM/SPF/DMARC; output as TXT records for customer to apply (or auto-apply via Route53 API if authorized).
- Build recovery campaign: Email to customer at risk of spam folder = reminder + bonus content unlock (e.g., "Exclusive video: [topic]").
- Resend flag emails via alternative pathway if model predicts >70% spam landing probability.

### EP-0926: Dropout Alert + Rescue Campaign
- When dropout probability >70%, trigger intervention:
  - Email: "We notice you've been away; here's a personalized resource: [bonus video / live Q&A link / tutor intro]."
  - Fallback: Offer 48-hour refund window + encouragement: "Our instructors are here to help; let's get you unstuck."
  - Win: If student re-engages, prevent refund; student completes course.

---

## Phase 4: Weeks 7–8 (Dashboard + Launch)

### All Three EPICs
- Build web dashboard:
  - EP-0924: Recovery metrics (attempted_retries, recovery_rate, MRR_saved, customer_breakdown).
  - EP-0925: Deliverability metrics (DMARC_pass_rate, inbox_placement_estimate, emails_recovered).
  - EP-0926: Completion metrics (dropouts_prevented, refunds_saved, engagement_uplift).
- Implement billing integration: Tiered/success-based pricing; auto-invoice via Stripe Billing API.
- Customer onboarding: API key setup, webhook validation, test campaign, go-live checklist.
- Launch with 2–3 pilot customers per EPIC:
  - EP-0924: 1 SaaS customer ($1M–$10M ARR); 1 marketplace (subscription-heavy).
  - EP-0925: 1 email marketing agency; 1 ecommerce brand.
  - EP-0926: 2–3 course creators (indie + courseware platform).

---

## Post-MVP (Weeks 9–12+)

### EP-0924
- Expand to additional payment platforms (Chargebee, Zuora, Paddle, Gumroad).
- Build predictive churn scoring; identify at-risk customers 30+ days before cancellation.
- Win-back campaigns: Personalized discount offers, feature highlights, usage reports.

### EP-0925
- Extend to SMS delivery recovery (Twilio, AWS Pinpoint).
- Build content-based spam prediction (subject line, CTA, links) → suggest rewrites.
- ISP relationship outreach: Partner with Gmail, Outlook feedback loop programs; integrate FBL directly.

### EP-0926
- Integrate mobile and video engagement (YouTube watch time, Vimeo session data).
- Cohort-specific predictions (first-time learner dropout vs. career-switcher vs. upskilling).
- Certification completion tracking (for regulated courses; compliance tracking).

---

## Success Metrics (Go/No-Go Criteria)

### EP-0924: Target 2-month ROI
- Recover 60%+ of failed payments (vs. standard 40–60%).
- Reduce churn by 5–15% in pilot cohorts (measurable within 60 days).
- Customer NPS >60 (willing to refer).

### EP-0925: Target 1.5-month ROI
- Predict inbox placement with 75%+ accuracy.
- Recover 10–20% of emails landing in spam.
- Improve customer open rates by 3–5% via authentication fixes + resend.

### EP-0926: Target 1.5-month ROI
- Predict dropouts 48–72 hours in advance (recall >60% at 70%+ precision).
- Prevent 15–25% of refund requests.
- Increase course completion rate by 10–20% in pilot courses.

---

## Resource Allocation (Parallel)
- **Engineers:** 2–3 FTE (distributed: 1 per epic + 1 shared infrastructure).
- **Founder:** 40% product, 60% sales/partnerships/pilots.
- **Timeline:** 8 weeks parallel; ships complete by 2026-04-17.
- **Cost:** ~$200K infrastructure + API integration (typical for SaaS MVP).
- **Breakeven:** Month 3–4 (first paying customers land); Y1 target $5.2M revenue.
