# Paper summary

> This is a working scratchpad for the paper-analysis phase. The output of this file feeds the Quote / AIDA / Claim drafts. It is not itself a nanopub.

**Reference paper:** Physiotherapy and associated factors affecting mouth opening changes in noma patients during initial hospitalization at an MSF-supported hospital in Northwest Nigeria—A retrospective cohort study

**DOI:** 10.1371/journal.pgph.0001995

**Authors:** Oluwole Victor Oluwalomola, Emily Briskin, Michael Olaleye, Joseph Samuel, Bukola Oluyide, Mark Sherlock, Adeniyi Semiyu Adetunji, Mohana Amirtharajah

**Year:** 2023 (PLOS Glob Public Health 3(9): e0001995, published 1 September 2023)

## Headline claim

> The mean difference in the mouth opening from admission to discharge was 6.9mm (95% CI: 5.4 to 8.3, p < 0.0001).

(Abstract, p. 1.) Status: matched verbatim against `pdftotext` extraction after whitespace normalisation. The `forrt-research` MCP `verify_quote` tool was NOT available in the analysis session, so this is formally **unverified by verify_quote** — re-run `verify_quote` before publishing.

Alternative candidates (see `01_quote.md`): abstract p. 1 predictors sentence; Results p. 7 age-coefficient sentence.

## Methodology summary

- **Data sources:** Routinely collected clinical data (MSF noma database) for patients admitted to Noma Children Hospital, Sokoto, Northwest Nigeria, 1 May 2018 – 1 May 2020. Variables exported to an Excel spreadsheet: sociodemographics, mouth-opening measurements (admission, discharge), length of stay, number of physio sessions, caregiver relationship, defect site, sequestrectomy.
- **Data availability:** "All relevant data are within the manuscript and its Supporting Information files." S1 Data (XLSX), DOI 10.1371/journal.pgph.0001995.s001 — resolves and downloads openly (checked 2026-10-10; served as `pgph.0001995.s001.xlsx`). Contents not yet inspected.
- **Eligibility:** WHO stage 3 (gangrene) and 4 (scarring) noma patients, no prior reconstructive/trismus-release surgery, received physiotherapy during initial hospitalization. Age dichotomised 0–3 vs >3 years.
- **Statistical models:** (1) paired t-test, admission vs discharge mouth opening; (2) independent t-test of change by age group; (3) bivariate one-way ANOVA (categorical) and simple linear regression (continuous) on change in mouth opening; (4) multivariable linear regression: change ~ number of physio sessions + age group (length of stay dropped for multicollinearity with sessions); (5) proportions <20 mm vs >=20 mm at admission/discharge.
- **Software:** R (R Core Team 2020); no package list, version, or code shared.
- **Sample sizes:** n = 91 included (47 female; age n = 90: 44 aged 0–3, 46 >3; Fig 2 states n = 88); caregiver n = 80; sequestrectomy n = 81; length of stay n = 75; Table 2 reports "n = 20" for physio sessions (likely a typo).
- **Headline numerical results:** mean mouth opening 17.6 mm admission → 24.5 mm discharge; mean difference 6.9 mm (95% CI 5.4–8.3; t = 9.4, df = 91, p < 0.001 [abstract: p < 0.0001]). Age >3 vs 0–3: 8.9 vs 4.5 mm, difference 4.5 mm (95% CI 1.7–7.2; t = 3.2, df = 88, p = 0.002). Multivariable: +0.3 mm per session (95% CI 0.1–0.5, p = 0.011); age >3: +4.8 mm (95% CI 2.2–7.5, p = 0.001); constant 0.9 (−2.6 to 4.1). Bivariate: sessions coef 0.28 (0.04–0.53, p = 0.02); length of stay 0.14 (0.05–0.22, p = 0.002). <20 mm: 47 (52%) at admission → 23 (25%) at discharge.

## Replication design choice

- [x] **Reproduction Study** — direct reproduction: same methodology, same tools.
- [ ] **Replication Study** — replication with different methodology or conditions.
- [ ] **Reproduction/Replication Study** — both.

The user has specified a reproduction. The authors deposited the patient-level data as S1 Data (open XLSX), and the analyses are standard tests (paired/independent t-tests, ANOVA, OLS) in R, so the same data and same methods can be re-run directly to check the reported numbers. No independent noma cohort is available, so a replication on new data is not feasible.

## Notes for downstream drafts

- Internal inconsistencies to watch during reproduction: p < 0.0001 (abstract) vs p < 0.001 (results); paired t-test df = 91 with n = 91 (expected df = 90); age-group n = 90 (Table 1/2) vs n = 88 (Fig 2) vs df = 88 in the t-test; Table 2 "n = 20" for physio sessions; Table 1 percentages use a denominator of ~92.
- No comparison (no-physiotherapy) group — the paper's design cannot attribute the change causally to physiotherapy; AIDA wording should state the pre/post change, not a causal effect.
- Geographic scope: single site, Noma Children Hospital, Sokoto, Northwest Nigeria (see `09_geo_coverage.md`).
