template = """id: {epic_id}
title: {title}
description: |
  **Idea:** {idea}

  **Why "WOW":** {wow}

  **ROI (Time In vs Cash Out):**
  - Time In: {time_in}
  - Cash Out: {cash_out}

  **First Year Projections (US$1B Scale):**
{proj_lines}
  - Estimated Revenue: {rev}

  **Feasibility Score:** {feas}

  **Risk Analysis:**
  - High: {risk_h}
  - Medium: {risk_m}
  - Low: {risk_l}

created_at: "2026-02-21"
created_by:
  agent: planner
  model: gemini-2.5-pro
  provider: google
status: draft
linked_stories: []
review_policy:
  min_reviews: 3
  approval_threshold: 0.85
  require_blocking_clearance: true
"""

epics = [
    {
        "id": "EP-0600",
        "title": "Algorithmic Global Real Estate Climate Risk Shorting Syndicate",
        "idea": "Trillions of dollars in coastal and wildfire-prone real estate are massively overvalued because local tax assessors and legacy insurers ignore hyper-local environmental data. This solo-founder hedge fund ingests billions of data points: raw satellite soil moisture vectors, NOAA oceanic heat content APIs, and local topographical 3D scans. The AI autonomously calculates the exact year a specific Zip Code becomes uninsurable. Armed with this asymmetric data, the system automatically shorts the municipal bonds of those specific counties and algorithmically buys Credit Default Swaps (CDS) against the mortgage-backed securities (MBS) of the exposed real estate.",
        "wow": "It executes the 'Big Short' for climate change autonomously. A one-man operation wielding god-tier environmental compute to mathematically break the housing market's denial of climate reality.",
        "time_in": "~4 months (Building the hyper-local predictive climate risk models and establishing institutional ISDA trading agreements).",
        "cash_out": "Massive proprietary trading profits when the insurance markets collapse in poorly-modeled zones.",
        "projs": ["Capital Deployed (Notional): $10,000,000,000 (Highly leveraged derivative positions)", "Alpha Generated: 1,500% Returns"],
        "rev": "$1,250,000,000",
        "feas": "7.5/10",
        "risk_h": "Systemic bailout of collapsing real estate markets by the federal government defeating the short position.",
        "risk_m": "Complexity of securing Tier-1 prime brokerage lines as a solo founder to execute the massive short derivatives.",
        "risk_l": "Data Acquisition (NASA/NOAA data is pristine and free)."
    },
    {
        "id": "EP-0601",
        "title": "Autonomous Global Carbon Sink Aggregation & Forward Market",
        "idea": "The world needs to remove billions of tons of CO2, but buying high-quality carbon credits is a manual, low-trust nightmare. This platform operates purely in software. It integrates via API with thousands of disparate, IoT-enabled environmental projects globally (direct air capture plants, biochar facilities, verifiable reforestation drones). The system autonomously aggregates these micro-tons of verified carbon removal into massive, standardized 'Megaton Blocks'. It then acts as an automated forward-clearinghouse, letting Fortune 500 companies (Microsoft, Delta Airlines) algorithmically hedge their 2030 ESG liabilities today by buying these standardized future carbon blocks.",
        "wow": "Becomes the ICE (Intercontinental Exchange) for the trillion-dollar decarbonization economy. Replaces human brokers with verified, physics-backed smart contracts at absolute global scale.",
        "time_in": "~5 months (Pipelining the global IoT environmental verification APIs and building the tier-1 financial matching engine).",
        "cash_out": "A 10% clearing premium on all Megaton Blocks traded.",
        "projs": ["Carbon Volume Forward-Cleared: 250,000,000 Tons"],
        "rev": "$1,100,000,000",
        "feas": "8/10",
        "risk_h": "Physical failure of the underlying carbon projects to actually sink the carbon by 2030, triggering massive default clauses.",
        "risk_m": "Global standards bodies (Verra, Gold Standard) altering their API verification rules suddenly.",
        "risk_l": "Corporate Demand (Fortune 500s are legally mandated to buy this, they are begging for a trusted exchange)."
    },
    {
        "id": "EP-0602",
        "title": "Generative Weather Modification Targeting & Routing API",
        "idea": "Cloud seeding (injecting silver iodide to force rain) is a $10B industry, but it's wildly inaccurate, mostly done by pilots eyeballing storm clouds. This software sits above the industry. It ingests live Nexrad Doppler radar, high-altitude atmospheric pressure APIs, and hyperspectral satellite data. It uses fluid-dynamic generative AI to mathematically pinpoint the exact cubic kilometer of a storm system that requires seeding to yield the maximum rainfall over a specific drought-stricken agricultural zone. It then autonomously dictates the GPS flight path and payload drop-timing directly to fleets of autonomous seeding drones.",
        "wow": "Turns chaotic weather modification into a precise, targeted, software-controlled outcome. The API that controls the rain.",
        "time_in": "~4 months (Building the massive fluid dynamic prediction models and the drone AP dispatch system).",
        "cash_out": "SaaS royalty. Charging drought-stricken municipalities or agricultural mega-corps $1M per targeted mega-liter of rain generated.",
        "projs": ["Acre-Feet of Water Gen-Targeted: 1,500,000"],
        "rev": "$1,050,000,000",
        "feas": "7/10",
        "risk_h": "Legal liability. If the system over-seeds and causes catastrophic flooding downwind, the algorithmic liability is massive.",
        "risk_m": "The sheer physics chaos of predicting micro-weather accurately enough to guarantee rainfall yields.",
        "risk_l": "Municipal desperation (Governments will pay anything for water)."
    },
    {
        "id": "EP-0603",
        "title": "Autonomous Predictive Pricing Engine for Global Soft Commodities",
        "idea": "The prices of coffee, cocoa, and cotton are highly vulnerable to hyper-local climate events (frosts, droughts). Traditional commodity traders rely on human analysts and delayed agricultural reports. This solo operation ingests terrifying amounts of environmental data: daily satellite NDVI (Vegetation Index) scans of every cocoa farm in Ivory Coast, localized soil moisture sensors across Brazil, and real-time shipping port weather. The AI parses the biological health of every individual farm globally, predicting crop failure months before harvest. It then autonomously executes multi-billion dollar futures trades on the ICE and CME.",
        "wow": "Achieves absolute information supremacy over the entire global food supply chain. A solo founder out-trading massive commodity houses (Glencore/Cargill) using sheer orbital compute.",
        "time_in": "~3 months (Massive geospatial data pipelining and reinforcement learning for automated futures execution).",
        "cash_out": "Proprietary algorithmic trading alpha.",
        "projs": ["Capital Deployed: $2,000,000,000 (Margin)", "Alpha Generated: 55% Returns"],
        "rev": "$1,100,000,000",
        "feas": "8/10",
        "risk_h": "Sovereign nations intervening in the markets (e.g., banning cocoa exports) rendering the perfectly predicted biological data useless.",
        "risk_m": "Cloud cover obscuring critical satellite telemetry during key harvest periods.",
        "risk_l": "Data access (Hyperspectral satellite data is a solved, purchasable commodity)."
    },
    {
        "id": "EP-0604",
        "title": "Algorithmic Global Supply Chain Routing via Climate Physics",
        "idea": "Trillions of dollars in global shipping (Maersk, MSC) are routed using static weather charts. They lose billions to fuel inefficiency and storm delays. This API ingests global marine weather APIs, ocean current telemetry, and vessel drag coefficients. It runs generative reinforcement learning to calculate the absolute perfect 'golden route' for 50,000 individual cargo ships simultaneously. The API updates the ship's autopilot every 5 minutes globally, riding favorable ocean currents and perfectly dodging storm systems to slash fuel burn by 15%.",
        "wow": "Optimizes the entire physical backbone of global trade using environmental physics. Turns a chaotic ocean into a perfectly predicted mathematical highway.",
        "time_in": "~4 months (Building the global maritime routing algorithm and securing APIs to Tier-1 shipping SCADA systems).",
        "cash_out": "A 30% gain-share on the total bunker fuel saved per voyage.",
        "projs": ["Vessels Routed: 25,000", "Bunker Fuel Saved: 10,000,000 Tons"],
        "rev": "$1,200,000,000",
        "feas": "8.5/10",
        "risk_h": "Captains overriding the algorithmic route due to 'gut feeling' and blaming delays on the software.",
        "risk_m": "Latency in updating the autopilot causing ships to miss critical current micro-windows.",
        "risk_l": "Shipping Company Adoption (Fuel is their #1 expense; a 15% saving is billions to the bottom line)."
    },
    {
        "id": "EP-0605",
        "title": "Autonomous Sovereign Disaster Default Swap (DDS) Issuer",
        "idea": "Island nations and coastal countries (e.g., Bangladesh, Maldives) face existential threats from climate-driven super-storms, yet they struggle to secure post-disaster funding because the World Bank takes years to disperse cash. This system is an algorithmic reinsurer. It utilizes global satellite and seismic data to create 'Disaster Default Swaps'. It sells these parametric policies to sovereign nations. When a Category 5 hurricane is verified by NOAA API to have made landfall at specific coordinates, the smart contract instantly triggers, wiring $500M in emergency liquidity to the nation's treasury within 60 seconds.",
        "wow": "Replaces the archaic, bureaucratic World Bank disaster relief process with instant, mathematically guaranteed rescue capital. Life-saving financial engineering at the sovereign scale.",
        "time_in": "~5 months (Complex stochastic modeling of global catastrophe risk tails, and building the sovereign settlement smart contracts).",
        "cash_out": "A 10% underwriting fee on the massive risk premiums paid by the sovereign nations.",
        "projs": ["Sovereign Risk Covered: $20,000,000,000"],
        "rev": "$1,000,000,000",
        "feas": "7/10",
        "risk_h": "A 'Black Swan' year where five Category 5 hurricanes hit simultaneously, wiping out the algorithm's entire capitalization pool.",
        "risk_m": "Securing the immense initial capital backing (from mega-funds) to legally issue the swaps.",
        "risk_l": "Sovereign Demand (Nations are desperate for instant liquidity post-disaster)."
    },
    {
        "id": "EP-0606",
        "title": "Predictive Industrial Methane Leak Bounty API",
        "idea": "Methane leaks from oil/gas pipelines are catastrophic for the climate, and companies face massive EPA fines if caught. However, leaks are invisible and remote. This system ingests orbital spectroscopy (satellites that can 'see' invisible gases) from the entire globe daily. It uses CV to pinpoint exact pipeline leaks down to the meter. It then autonomously acts as an algorithmic bounty hunter. It issues a private API call to the offending Oil Major (Exxon/BP): 'Pay us $5M instantly for the exact coordinates of this leak, or we automatically forward the data to the EPA for a $50M fine.'",
        "wow": "Automated, highly aggressive environmental compliance via algorithmic extortion. It literally turns invisible pollution into instant, massive revenue.",
        "time_in": "~3 months (Ingesting and parsing massive hyperspectral satellite cubes optimized for CH4 signatures).",
        "cash_out": "The $5M+ 'Information Bounties' paid by massive energy companies to avoid catastrophic fines and PR disasters.",
        "projs": ["Major Leaks Identified/Bountied: 250"],
        "rev": "$1,250,000,000",
        "feas": "8/10",
        "risk_h": "Oil Majors suing the startup under extortion statutes (Requires incredibly careful, legally-vetted 'Bounty/Service' phrasing).",
        "risk_m": "Cloud cover preventing the satellites from verifying the leak.",
        "risk_l": "Data Availability (Methane-detecting satellites like MethaneSAT are fully operational)."
    },
    {
        "id": "EP-0607",
        "title": "Algorithmic Global Groundwater Depletion Hedging",
        "idea": "Major agricultural conglomerates and beverage giants (Pepsi, Nestlé) face existential threats if regional aquifers run dry. This platform maps the entire planet's groundwater reserves autonomously using thousands of API data streams (GRACE satellite gravity anomalies, local well-telemetry, predictive rainfall ML). It accurately predicts localized aquifer collapse years in advance. It then sells highly specialized, algorithmic 'Water Continuity Insurance' to these mega-corps, autonomously buying up physical water rights in adjacent, safer basins via shell companies to hedge the risk.",
        "wow": "Financializes the catastrophic loss of global groundwater. It provides multi-billion dollar insurance policies backed by an algorithmic physical water-rights acquisition engine.",
        "time_in": "~4 months (Building the global subterranean hydrologic models using raw gravity variance data).",
        "cash_out": "Massive upfront insurance premiums ($50M+ per corporate policy) plus the appreciation of the hedged physical water rights.",
        "projs": ["Corporate Policies Issued: 25", "Hedged Asset Value: $5,000,000,000"],
        "rev": "$1,500,000,000",
        "feas": "7.5/10",
        "risk_h": "Governments suddenly nationalizing water rights during extreme shortages, destroying the algorithmic hedge.",
        "risk_m": "Accuracy of predicting subterranean flow dynamics highly hidden from satellite view.",
        "risk_l": "Corporate Terror (Mega-corps are terrified of their factories running out of water; they will pay anything to hedge)."
    },
    {
        "id": "EP-0608",
        "title": "Generative Biomass-to-Energy Optimization Oracle",
        "idea": "Burning biomass (wood pellets, agricultural waste) for energy is a massive industry, but the caloric value of the fuel fluctuates wildly based on humidity, species, and rot. This AI engine governs massive biomass power plants. It ingests hyperspectral imagery of the biomass on the conveyor belt and precise local weather. It algorithmically predicts the exact moisture content and chemical makeup of the fuel before it hits the furnace, autonomously adjusting the oxygen mix and burn temperature in milliseconds to extract up to 20% more MW/h.",
        "wow": "Squeezes massive, pure profit margin out of physical waste using edge-compute and optical physics. Zero human operators.",
        "time_in": "~3 months (Edge-ML CV models trained on biological rot/moisture, integrated into SCADA furnace controls).",
        "cash_out": "A 50% split on the purely algorithmic net-new energy (MW/h) generated.",
        "projs": ["Plants Optimizing: 100", "Algorithmic Megawatts Generated: 15,000 MW/h"],
        "rev": "$1,000,000,000",
        "feas": "8.5/10",
        "risk_h": "Physical failure of the boiler due to the algorithm pushing the temperature thresholds too aggressively.",
        "risk_m": "Lenses of the hyperspectral cameras getting coated in industrial dust, blinding the model.",
        "risk_l": "Adoption (It's a pure CapEx-free revenue increase for the power plant)."
    },
    {
        "id": "EP-0609",
        "title": "Autonomous Secondary Market for Corporate Biodiversity Credits",
        "idea": "The next wave of ESG regulation forces companies to buy 'Biodiversity Credits' (proving they protected specific acreage of rainforest/coral reef). Currently, this market is nonexistent and illiquid. This platform tokenizes global biodiversity. It ingests 4K drone footage, bio-acoustic microphone data (listening for rare birds), and satellite imagery of a specific plot of protected jungle. The AI algorithmically verifies that the specific biodiversity is intact daily. It mints verified 'Bio-Tokens' and operates the central Wall Street-style exchange where Fortune 500s bid millions for compliance.",
        "wow": "It builds the Nasdaq for literal nature. It uses algorithmic auditing (listening to birds via AI) to create a trillion-dollar liquid market for keeping the planet alive.",
        "time_in": "~4 months (Pipelining global bio-acoustic and visual data streams into automated verification ledgers).",
        "cash_out": "A 5% exchange toll on the enormous volume of corporate biodiversity compliance trading.",
        "projs": ["Bio-Credit Volume Cleared: $25,000,000,000"],
        "rev": "$1,250,000,000",
        "feas": "8/10",
        "risk_h": "Poachers/Loggers destroying the physical asset backing the token, requiring immediate algorithmic slashing of the value.",
        "risk_m": "Regulatory harmonization (Will the EU and the US agree on what constitutes a valid biodiversity credit?).",
        "risk_l": "Corporate Demand (Companies will be legally mandated to buy these credits, just like carbon)."
    }
]

for e in epics:
    proj_str = "\\n".join([f"  - {line}" for line in e["projs"]])
    content = template.format(
        epic_id=e["id"], title=e["title"], idea=e["idea"], wow=e["wow"], 
        time_in=e["time_in"], cash_out=e["cash_out"], proj_lines=proj_str, 
        rev=e["rev"], feas=e["feas"], risk_h=e["risk_h"], risk_m=e["risk_m"], risk_l=e["risk_l"]
    )
    with open(f"/Users/olsky/github/olsky/blablabla/project/epics/{e['id']}.yaml", "w") as f:
        f.write(content)

print(f"Generated {len(epics)} $1B Environmental Data epics")
