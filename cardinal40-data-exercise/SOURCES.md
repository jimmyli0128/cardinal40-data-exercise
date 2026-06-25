# Cardinal40 — "Founders as the Next Offset" | Data Sources & Provenance

**Purpose:** This document is the verification spine for the data behind the three exhibits. Every figure below is tagged with its primary source, an exact URL, the access date, how the variable is constructed, and the single most important caveat — what the writer must *not* claim from it. Open each URL and check the number against the cited table/section.

**Access date for all sources:** 2026-06-23
**Extraction status legend:** `TRANSCRIBED` = figure read from a free, public report/release and recorded by hand (no API). `API` = pulled programmatically from an open endpoint; checkpoint values below should match the script output in `/scripts/pull_api_sources.py`.

---

## Verification index

| # | Dataset | Maps to | Primary source | Extraction |
|---|---------|---------|----------------|------------|
| 1 | ASPI Critical Technology Tracker — the "flip" | Q1 | ASPI (Australian Strategic Policy Institute) | TRANSCRIBED |
| 2 | Stanford HAI AI Index 2026 — US/China AI | Q1 + Q2 | Stanford HAI | TRANSCRIBED |
| 3 | Hurun Global Unicorn Index 2025 — scoreboard | Q2 | Hurun Research Institute | TRANSCRIBED |
| 4 | NFAP Immigrant Founders 2026 | Q2 + Q3 | National Foundation for American Policy | TRANSCRIBED |
| 5 | World Bank — China household consumption %GDP | Q3 | World Bank WDI | API |
| 6 | UN WPP 2024 — working-age population | Q3 | UN DESA Population Division | API |
| 7 | IMF COFER — reserve-currency shares | Q3 | IMF Statistics Dept | API |
| 8 | China EV "involution" / overcapacity | Q3 | AlixPartners (via Reuters/SCMP) + CSIS/Rhodium | TRANSCRIBED |

---

## 1. ASPI Critical Technology Tracker — the research-leadership "flip"  `TRANSCRIBED`

**The data (64-technology dataset, the last fully-public complete release):**

| Period | Technologies China leads (of 64) | Technologies US leads (of 64) |
|--------|----------------------------------|-------------------------------|
| 2003–2007 | 3 | 60 |
| 2019–2023 | 57 | 7 |

Supporting: prior-year tracker had China leading 52; Chinese Academy of Sciences alone leads 31 of 64; "high-risk" (monopoly-risk) technologies rose from 14 to 24 in one update; US still leads quantum computing, vaccines & medical countermeasures, nuclear medicine, atomic clocks, small satellites, genetic engineering, NLP.

**2025 update (for currency):** expanded to **74 technologies**, five-year window **2020–2024**; ASPI reports the leadership trajectory is "remarkably stable" vs. the prior two years. Use the 64-tech figures above as the flip anchor (complete public counts); cite the 74-tech update to show it still holds.

**Primary source:**
- Report: *ASPI's two-decade Critical Technology Tracker: the rewards of long-term research investment* (Aug 2024) — https://www.aspi.org.au/report/aspis-two-decade-critical-technology-tracker/
- Report PDF (figures + Appendix 1 country snapshots): https://ad-aspi.s3.ap-southeast-2.amazonaws.com/2024-08/ASPIs%20two-decade%20Critical%20Technology%20Tracker_1.pdf
- 2025 update (74 tech): https://www.aspistrategist.org.au/aspis-critical-technology-tracker-2025-updates-and-10-new-technologies/
- Interactive tool (membership-gated): https://techtracker.aspi.org.au/

**Variable construction:** Country share of the **top 10% most highly-cited research publications** in each technology, five-year rolling windows. "Leads" = highest share of high-impact papers.

**CAVEAT — the most important one in the whole project:** This measures **research output**, i.e. a *leading indicator* of future capability — NOT current commercialization, manufacturing capacity, deployment, or military capability. "China leads 57 of 64" ≠ "China dominates 57 of 64 industries." Also, the 2003–2007 baseline partly reflects that some of the 64 technologies barely existed then (ASPI flags low/insignificant credit counts in early years), so the "3 → 57" jump slightly overstates the cleanliness of the flip. Do not write that China "controls" or "owns" these technologies.

---

## 2. Stanford HAI AI Index 2026 — where the US still leads, and where China has closed  `TRANSCRIBED`

**The data (2025 calendar-year unless noted):**

| Metric | United States | China | Note |
|--------|---------------|-------|------|
| Private AI investment, 2025 | $285.9B | $12.4B | Ratio 23.1× (was 11.7× in 2024) |
| — US YoY | +162% from $109.1B (2024) | — | |
| — California alone | $218B (>75% of US total) | — | |
| Notable AI models, 2025 | 50 | 30 | China up from 15 in 2024 |
| Newly funded AI companies, 2025 | 1,953 | 161 | US >10× next country |
| Top model quality gap (US lead) | — | — | Collapsed to **2.7%** (Mar 2026); was 17.5–31.6 pp (May 2023) |
| — MMLU benchmark | — | — | US lead 17.5 pp (end-2023) → 0.3 pp (end-2024) |
| AI patents (share of global) | — | 69.7% | |
| AI publications / citations | 12.6% (cit.) | 23.2% pubs / 20.6% cit. | |
| Industrial robot installs | 34,200 | 295,000 | China ~9× |
| Data centers | 5,427 | — | US >10× any country |
| AI researchers migrating *to* US | down 89% since 2017 | — | 80% of that drop in the last year |

**Primary source:**
- Landing: https://hai.stanford.edu/ai-index/2026-ai-index-report
- Full report PDF (~400pp, free): https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- "12 Takeaways" summary: https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report

**Variable construction:** Private investment from **Quid** (proprietary deal database); models from **Epoch AI**; benchmarks (MMLU, MMMU, MATH, HumanEval) from published leaderboards. Report PDF is free; underlying chart data is published by the AI Index team.

**CAVEAT:** Private-investment figures **understate China's true AI spend** — the report itself notes China channels capital through government guidance funds (estimated ~$184B into AI through 2023; ~$912B across all industries 2000–2023), plus a new ~$138B state VC fund announced 2025. So the 23× gap is a *private-capital* gap, not a total-national-effort gap. This is exactly the founder-financing asymmetry the thesis wants — frame it that way, not as "the US out-spends China 23× on AI."

---

## 3. Hurun Global Unicorn Index 2025 — the founder scoreboard  `TRANSCRIBED`

**The data (cut-off 1 Jan 2025; valuations updated to mid-2025 release):**

| Country | Unicorns | Share | New "faces" this year |
|---------|----------|-------|------------------------|
| United States | 758 | 49.8% | 108 |
| China | 343 | ~23% | 36 (net +3; 19 IPO'd out) |
| India | 64 | — | — |
| United Kingdom | 61 | — | — |
| Germany | 36 | — | — |
| France | 30 | — | — |
| Canada | 28 | — | — |
| **World total** | **1,523** | 100% | 203 (record) |

Supporting: EU combined = 112 unicorns (<8% of world, vs ~20% of global GDP). Most valuable: SpaceX $350B, ByteDance (China), OpenAI $300B, xAI $115B (debut), Anthropic, Revolut (UK). US by state: California 395–396 cos ($2.1T), New York 141 ($362B), Massachusetts 44 ($100B), Texas 32 ($75B).

**Primary source:** Hurun Research Institute, *Global Unicorn Index 2025* — https://www.hurun.net/en-us/info/detail?num=2DVQ51ORRGTH

**Variable construction:** Privately-held companies founded in the 2000s, valued ≥ US$1B, not yet listed. Valuations are Hurun estimates. Companies exit by "promotion" (IPO/acquisition) or "demotion" (value < $1B).

**CAVEAT:** Valuations are **private estimates**, not audited. Unicorns are the **survivor tail**, not the business-formation rate — don't conflate "more unicorns" with "more entrepreneurship" generally. **Figure to standardize:** the primary Hurun release says the US added **108** new faces; several secondary aggregators report **55** (likely net-of-exits or a misread). Use 108 (gross new faces) and footnote the discrepancy.

---

## 4. NFAP — Immigrants and U.S. Billion-Dollar Companies (June 2026)  `TRANSCRIBED`

**The data (US unicorns as of April 2026):**

| Metric | Value |
|--------|-------|
| US unicorns total | 775 |
| With ≥1 immigrant founder | 455 (**59%**) |
| Founded/cofounded by immigrants OR children of immigrants | **66%** |
| With immigrant founder OR immigrant in key leadership | **~80%** |
| With a founder who arrived as an international student | **24%** (183 companies) |
| Combined value of the 455 immigrant-founded | **$5.0 trillion** |
| — incl. those gone public since 2016 | ~$5.8T |
| Immigrant-founded with *only* immigrant founder(s) | 55% |

**Top countries of origin for immigrant founders:** India (largest — NFAP lists #1; confirm exact count in brief table), Israel 60, UK 47, **China 41**, Canada 30, Russia 23, France 21, Germany 18, Ukraine 16, Australia 14, Pakistan 10, Romania 10.

**Primary source:** NFAP Policy Brief, *Immigrants and U.S. Billion-Dollar Companies* (June 2026) — https://nfap.com/wp-content/uploads/2026/06/IMMIGRANTS-AND-US-BILLION-DOLLAR-COMPANIES.NFAP-Policy-Brief.2026-3.pdf

**Variable construction:** Universe = ~775 US unicorns tracked by **CB Insights** (private, ≥$1B, not yet public), valuations as of April 2026. "Immigrant founder" = at least one founder born outside the US.

**CAVEAT:** "Founded or cofounded" counts any company with ≥1 immigrant founder — not that immigrants are *sole* founders of 59% (the sole-founder figure is the 55%-of-immigrant-founded subset). The standout point for the thesis: **India is the #1 source and China is #4** — i.e. the US founder engine is partly powered by foreign-born (including Chinese-born) talent. That's a structural advantage about the *system*, not about native-born Americans specifically.

---

## 5. World Bank WDI — China household consumption as % of GDP  `API`

**Checkpoint values (to be confirmed by the pull):**

| Series | Value |
|--------|-------|
| China, household consumption % of GDP, 2023 | 39.6% (39.57) |
| World average, 2023 | ~63.6% |
| United States | pull via API (typically high-60s%) |

**Primary source:** World Bank, Households & NPISHs final consumption expenditure (% of GDP), indicator **`NE.CON.PRVT.ZS`** — https://data.worldbank.org/indicator/NE.CON.PRVT.ZS?locations=CN
**API:** `https://api.worldbank.org/v2/country/CHN;USA;WLD/indicator/NE.CON.PRVT.ZS?format=json` (open, free)

**Variable construction:** Market value of all goods/services bought by households (incl. imputed rent for owner-occupied dwellings; incl. NPISHs), as a share of GDP.

**CAVEAT:** Two distinct World Bank indicators exist — *household* consumption (`NE.CON.PRVT.ZS`) vs. *total final* consumption (`NE.CON.TOTL.ZS`, which adds government). Pick one and stay consistent; the demand-suppression story uses **household** consumption. This is the cleanest, fully-reproducible series in the whole package.

---

## 6. UN World Population Prospects 2024 — working-age population (15–64)  `API`

**Checkpoint values:**

| Country | 2024 | 2050 | Change |
|---------|------|------|--------|
| China (15–64) | 984M | 745M | −239M (≈ −24%) |
| India (15–64) | 990M | 1.13B | +144M |

Supporting: China's working-age population peaked in 2015 and has fallen since; old-age dependency ratio projected to rise from ~18% (2020) toward ~50%+ by 2050.

**Primary source:** UN DESA Population Division, *World Population Prospects 2024*, Medium variant — https://population.un.org/wpp/
**Bulk CSV:** https://population.un.org/wpp/downloads?folder=Standard+Projections&group=CSV+format
**API:** `https://population.un.org/dataportalapi/` (open)

**Variable construction:** Population aged 15–64 ("working age," standard international definition), medium-fertility projection variant, single-year and 5-year age groups available.

**CAVEAT:** Mind the age band — different sources use 15–64 vs 15–59 vs 20–64; standardize on **15–64**. These are projections (medium variant) — present the 2050 figure as a UN central scenario, not a certainty. The 984M→745M checkpoint traces to UN WPP 2024; the API pull will reproduce it exactly.

---

## 7. IMF COFER — currency composition of FX reserves  `API`

**Checkpoint values (2025Q4):**

| Currency | Share |
|----------|-------|
| US dollar | 56.77% |
| Euro | 20.25% |
| Japanese yen | 5.56% |
| British pound | 4.64% |
| Canadian dollar | 2.49% |
| Australian dollar | 2.01% |
| Chinese renminbi | 1.95% |
| Swiss franc | 0.19% |

Context: total reserves $13.14T (2025Q4); USD peaked ~72% (2001), now ~57%.

**Primary source:** IMF Statistics Dept, *Currency Composition of Official Foreign Exchange Reserves (COFER)* — https://data.imf.org/en/datasets/IMF.STA:COFER
**Data brief (2025Q4):** https://data.imf.org/en/news/imf%20data%20brief%20march%2027
**Dashboard:** https://data.imf.org/en/dashboards/cofer%20dashboard

**Variable construction:** Voluntary, confidential reports from 149 reporting economies; holdings reported in USD using end-of-period exchange rates, expressed as % of allocated reserves.

**CAVEAT — two big ones:** (1) **Exchange-rate effects, not active diversification, drive nearly all the recent decline** in the dollar's share (IMF's own blog says so) — because shares are valued in USD, a stronger euro mechanically lifts the euro's share. (2) The dollar's lost share has gone to *nontraditional* currencies and **gold**, NOT the renminbi (RMB stuck at ~2%). Also note: from 2025Q3 the IMF removed the "unallocated" portion (revised back to 2000Q1), so the series now sums to 100% — older charts may differ. The structural point is the **absence of a Chinese alternative**, not dollar strength per se.

---

## 8. China EV "involution" / overcapacity — the cost of the state-mobilization model  `TRANSCRIBED`

**The data:**

| Metric | Value |
|--------|-------|
| EV / plug-in-hybrid brands in China (2024) | 129 (across ~50 carmakers) |
| Forecast financially viable by 2030 | 10–15 (AlixPartners) → ~114 brands exit/merge |
| Survivors' projected market share by 2030 | ~75% |
| Auto-plant capacity utilization, 2024 | 50% (lowest in a decade) |
| Profitable EV makers (mid-2025) | ~3, amid record ~16.8% discounts |
| Govt financial support to EV sector, 2009–2023 (CSIS est.) | >$230B |
| Car-sale subsidies as share of central fiscal revenue (Rhodium est.) | ~3% |

Counter-nuance (do not omit): AlixPartners also credits China's "New Operating Model" with bringing vehicles to market ~2× faster, with 40–50% less investment and a ~30% cost advantage.

**Primary / best-available sources:**
- AlixPartners 2025 Global Automotive Outlook (China): https://www.alixpartners.com/newsroom/2025-alixpartners-global-automotive-outlook-china/
- Reuters (129 brands → 15 by 2030): https://www.globalbankingandfinance.com/UK-CHINA-AUTOS-9391e7b5-7da3-4fcb-93ba-5ff07ecb983a
- SCMP (10–15 viable; "<10% profitable"): https://www.scmp.com/business/china-business/article/3316864/chinas-ev-price-war-dashes-profit-hopes-90-brands-alixpartners-says
- CSIS ($230B subsidy estimate) & Rhodium (3% of fiscal revenue): cited via reporting above.

**Variable construction:** Brand counts and viability forecasts are **AlixPartners consultancy estimates**; subsidy totals are CSIS/Rhodium analytical estimates. The structural root (consumption <40% / investment ~40% of GDP) traces back to World Bank data in #5 — i.e. this is the same demand-suppression story, told through one industry.

**CAVEAT:** This is a **"cost of the model" story, not a "the model failed" story.** China still produces the majority of the world's EVs and leads the sector. The defensible claim is that state-directed capital allocation produces overcapacity and destroys profitability ("involution"); the indefensible claim is that China's approach "doesn't work." Subsidy and brand-survival figures are estimates (private consultancy / think-tank), so attribute them as such — they are weaker, less reproducible evidence than #5–7.

---

## How to verify quickly
1. Open each **Primary source** URL above and match the bolded figure against the cited table/section.
2. For `API` items (#5–7), run `python scripts/pull_api_sources.py` — the printed checkpoints should match the tables here.
3. Anything that doesn't reconcile, flag it and we hold before designing the exhibit.

---

## EXHIBIT 3 — THE RETURNS ANGLE ("backing America's founder ecosystem → extraordinary returns")
Pivot from macro-moats to realized equity returns (adjacent to the fund's book; uses public-market receipts, never the fund's own performance). Distinct from Exhibit 2 (which used VC/unicorns/ROE/demand) — this is about REALIZED INVESTOR RETURNS over time.

### Panel A — the growth-vs-returns paradox (the hook)
- **Shanghai Composite is still ~33% BELOW its 2007 peak** (peak ~6,092 in Oct 2007; ~4,113 in May 2026) — i.e., an investor who bought at the 2007 top is down ~33% eighteen years later. [Yahoo Finance, "Chinese Economy Is Booming, But Stock Markets Haven't Recovered in 20 Years," May 2026, citing TradingView; levels corroborated by macrotrends.net/2592]
- **China nominal GDP expanded ~7× over the same ~two-decade stretch.** [same Yahoo/NBS]
- **US benchmark (S&P 500) delivered 600%+ total return over that period** (≈ $100 → ~$700). [same source; corroborated: S&P 500 ~10–12% annualized long-run, ~13.7% last 5yr — tradethatswing/slickcharts]
- One-line: economic growth ≠ investor returns. China grew the economy; America compounded the equity. (Academic backing: Jay Ritter / U. Florida — no stable GDP↔equity-return relationship; CNBC 2012.)
- **CAVEAT (must note on-chart):** 2007 was a Shanghai bubble peak, so a 2007-start flatters the US somewhat. Fair framing = "still below its 2007 level after 18 yrs," which is the widely-cited, defensible fact. Optional cleaner cross-check: MSCI China total-return vs S&P 2010–25 (pull if we want a non-peak window).

### Panel B — it's the founders (ties returns to FOUNDERS specifically, not just "US > China")
- **Bain & Company (2025/26): since 2015, founder-led companies beat non-founder-led peers by 2.1× in total shareholder return; 2.6× among tech; still 1.4× even excluding tech.** [bain.com, "The Magic of Founder-led Companies"]
- **Bain/HBR (2016): founder-led S&P 500 firms returned 3.1× the rest, 1990–2014.** [HBR 3/24/16]
- **Founder-led firms = <5% of S&P 500 by count but ~15% of total market cap** — disproportionate value creation. [HBR/AInvest 2025]
- Credit Suisse: founder-led companies globally ~3% annual sector-adjusted alpha since 2006.
- The giants driving US returns are founder-built: Nvidia (Huang), Apple, Microsoft, Amazon (Bezos), Meta (Zuckerberg), Alphabet, Tesla (Musk).
- Purdue (2016): founder-CEO S&P 500 firms generate 31% more patents; market values their innovation ~4× higher (Tobin's Q). [HBR]

### Narrative role
Ex1 = the threat (China leads critical-tech). Ex2 = America's edge (it builds companies). Ex3 = THE PAYOFF (backing those founders compounds extraordinarily) → makes the fund's thesis feel inevitable without citing the fund.

### Panel B reframed — FOUNDER-LED COMPANIES WIN TWICE (returns + society) — the patriotic double bottom line
Drop the economy/paradox angle. Exhibit 3 = founder-led companies deliver MORE for shareholders AND more for the country.

**FOR INVESTORS (returns):**
- **2.1× total shareholder return** vs non-founder peers since 2015 (2.6× in tech, 1.4× ex-tech). [Bain & Company, 2025/26]
- **7 of the 10 most valuable S&P 500 companies are founder-built — ~33% of the entire index by weight**: Nvidia 7.90%, Apple 6.78%, Alphabet 6.03%, Microsoft 4.37%, Amazon 3.71%, Meta 1.96%, Tesla 1.75% (top-10 ≈ 38% of index). [S&P Dow Jones Indices float weights, June 2026 — PRIMARY, recomputable. Replaces the unsourced <5%/15% aggregator stat, now DROPPED.] (“founder-built” umbrella: Nvidia/Meta/Tesla still founder-led; Apple/Alphabet/MSFT/Amazon founder-built.)
- The giants driving US returns are founder-built: Nvidia, Apple, Microsoft, Amazon, Meta, Tesla.
- (Historical: 3.1× the rest, 1990–2014, Bain/HBR; ~3% annual alpha since 2006, Credit Suisse.)

**FOR AMERICA (societal benefit):**
- **Innovation:** founder-CEO S&P 500 firms generate **31% more patents**, of higher value, and invest more in R&D. [Purdue/HBR 2016; Wiedower via Anchor Capital]
- **Jobs (structural):** net new US job creation occurs **only through startups** — new firms add **~3M jobs in year one** while existing firms net-destroy **~1M/yr** combined; 1-yr-old firms create ~1M jobs vs ~300k for 10-yr-olds. [Kauffman/Tim Kane, U.S. Census BDS 1977–2005 — PRIMARY; date honestly]
- **Jobs (recent anchor, pattern holds):** ~**6.6M Americans started a new business in 2025** (back to pre-pandemic levels); startup early job creation 4.7 jobs/1,000 people (2021, latest per-capita reading; 5.1 in 2019; peak 7.9 in 1997). [Kauffman Indicators / National Report 2025, May 2026 — PRIMARY]
- **Long-term investment:** founder-CEOs invest more in R&D / the future and hold longer horizons vs quarter-driven professional CEOs. [Ohio State/Fahlenbrach; Purdue]

**HONESTY NOTE (unit difference — keep clear):** returns + patents = founder-LED *public companies*; job-creation = *startups/young firms* (the broader founder ecosystem). Frame the societal column as "the founder ecosystem," not "founder-led mega-caps create all the jobs." The fund backs founders *early*, so both apply across the founder lifecycle.

**MESSAGE:** Backing American founders aligns profit and patriotism — it's the rare bet that pays shareholders and strengthens the country at the same time. Makes the fund's thesis feel virtuous + inevitable without citing the fund.
