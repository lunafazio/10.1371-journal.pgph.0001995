# 04 — FORRT Replication Study

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify code first:** read the actual reproduction script in `notebooks/03_analysis.py` before writing the methodology field. See `docs/verify-before-drafting.md`.

## Field-by-field draft

<!-- field: study -->
### Short URI suffix for study ID (text input, required)

Slug. Use kebab-case.

```
noma-physio-mouth-opening-reproduction-study
```

<!-- field: label -->
### Label/name of replication study (text input, required)

Human-readable title.

```
Computational reproduction of Oluwalomola et al. (2023): admission-to-discharge mouth opening change in noma patients receiving physiotherapy
```

<!-- field: type -->
### Choose the study type (dropdown, required)

- [ ] Replication Study - replication with different methodology or conditions
- [ ] Reproduction/Replication Study - study that is both, reproduction and replication
- [x] Reproduction Study - direct reproduction: same methodology, same tools

<!-- field: claim -->
### Choose FORRT claim (search/select, required)

URI of the Claim published in step 03. Pull from `nanopubs/PUBLISHED.md`.

```
«URI of step 03 Claim — filled by the chain wizard»
```

<!-- field: scope -->
### Describe what part of the claim is reproduced/replicated. (textarea, required)

The **scope** of the claim being tested. Which aspect, what's in/out of scope. NOT methodology. NOT results. See `docs/pico-study-outcome-levels.md`.

```
The headline claim of Oluwalomola et al. (2023): among the 91 noma patients (WHO stages 3 and 4) who received physiotherapy during initial hospitalization at Noma Children Hospital, Sokoto, mouth opening at discharge was greater than at admission. In scope is the within-patient admission-to-discharge comparison of mouth opening (mean difference, its confidence interval and significance) and the proportions of patients below 20 mm opening at admission and discharge. The paper's secondary analyses (age-group comparison, bivariate and multivariable predictors of change) were also re-run and are reported as context, but are not part of the claim tested. Out of scope: whether physiotherapy causes the change (the study has no comparison group) and generalisation beyond this cohort.
```

<!-- field: methodology -->
### Describe how the claim is reproduced/replicated. (textarea, required)

The **method** in plain prose. Read `notebooks/03_analysis.py` and any config files first. NOT exact numerical results.

```
Computational reproduction on the authors' own published patient-level data (S1 Data, https://doi.org/10.1371/journal.pgph.0001995.s001, 91 rows). No analysis code was published, so the analysis was reconstructed from the paper's methods description in Python (pandas, scipy, statsmodels) and orchestrated with Snakemake as jupytext notebooks: download and checksum S1 Data; tidy it without dropping rows or repairing values (missing values kept; each analysis uses complete cases and reports its n); then re-run every reported test. Headline: paired t-test of discharge versus admission mouth opening. Secondary: independent two-sample t-test of change by age group (0-3 vs >3 years); bivariate one-way ANOVA for categorical factors and simple linear regression for continuous factors; multivariable linear regression of change on number of physiotherapy sessions and age group; proportions below 20 mm at admission and discharge. Each reproduced statistic is compared against the paper's reported value at the paper's precision. Code and results are archived at https://doi.org/10.5281/zenodo.23281226.
```

<!-- field: deviation -->
### Describe any deviations from original methodology. (textarea, optional)

What's different from the original method. Verify against the actual code, don't guess.

```
(1) The original analysis was run in R with no code, version or packages published; this reproduction uses Python (scipy, statsmodels) with code reconstructed from the methods text. (2) The paper does not define how raw caregiver labels map to "primary caregiver", nor how the raw "Particularities" defect site is grouped; the mappings used were inferred as the only ones that reproduce the Table 1 counts. (3) The secondary age-dependent analyses (age-group t-test and multivariable regression) reproduce the paper only after excluding one 40-year-old patient, an exclusion the paper does not report; the primary run uses all rows and the exclusion is reported as a separately labelled sensitivity run. (4) Because R's t.test defaults to Welch while the paper does not state which variant was used, both Student (equal variances) and Welch t-tests are reported for the age-group comparison.
```

<!-- field: keyword -->
### Search keywords (Wikidata) (search/select, optional)

Provide labels (not QIDs) — the Wikidata search picks up labels.

```
noma (Q994794)
physiotherapy (Q16643870)
trismus (Q936070)
reproducibility (Q1425625)
```

<!-- field: discipline -->
### Search discipline (Wikidata) (search/select, optional)

Provide labels.

```
global health (Q2725393)
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 04.
