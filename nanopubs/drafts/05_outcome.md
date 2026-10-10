# 05 — FORRT Replication Outcome

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> **Verify the actual numerical results first** by reading `results/` and `notebooks/03_analysis.py`. Don't quote numbers from memory. See `docs/verify-before-drafting.md`.

## Field-by-field draft

<!-- field: outcome -->
### Short URI suffix for outcome ID (text input, required)

Slug. Use kebab-case.

```
noma-physio-mouth-opening-reproduction
```

<!-- field: label -->
### Plain-text label for the outcome (text input, required)

Descriptive title.

```
Computational reproduction of the admission-to-discharge mouth-opening change in noma patients receiving physiotherapy (Oluwalomola et al. 2023)
```

<!-- field: study -->
### Choose study (search/select, required)

URI of the Replication Study published in step 04. Pull from `nanopubs/PUBLISHED.md`.

```

```

<!-- field: repo -->
### Repository URL (text input, required)

Use the Zenodo **version DOI** URL for the release the results came from — not a
bare branch URL, and not the concept DOI.

> **Why not the bare repo URL.** `https://github.com/ORG/REPO` names a *moving
> branch*. This Outcome asserts "this code produced this number", in a signed,
> immutable record. A branch URL means that assertion points at whatever `main`
> happens to be years from now — code that may never have produced the number
> above. A concept DOI has the same flaw: it resolves to the latest version.
> The version DOI pins the exact release. `docs/chain-decision-tree.md` § Anchor
> ranks the options: SWHID > Zenodo DOI > repo URL > Wayback.
>
> Both DOIs and the SWHID are in `CITATION.cff` under `identifiers:`, recorded
> automatically at release by `.github/workflows/release-identifiers.yml`. Take
> the one described as *"Version DOI"*.

```
https://doi.org/{{ZENODO_VERSION_DOI}}
```

<!-- field: date -->
### Choose completion date (text input, required)

```
2026-10-10
```

<!-- field: validationStatus -->
### Choose validation status (dropdown, required)


This dropdown maps to the CiTO intention in step 06: Validated → `confirms`, PartiallySupported → `qualifies`, Contradicted → `disputes`.

- [ ] contradicted
- [ ] inconclusive
- [ ] not tested
- [ ] partially supported
- [x] validated

<!-- field: confidenceLevel -->
### Choose confidence level (dropdown, required)

_Vocabulary not yet captured._

```

```

- [x] high - Strong evidence, mostly agrees with original
- [ ] low - Limited evidence, significant disagreement
- [ ] moderate - Adequate evidence, partial agreement
- [ ] very high - Extensive evidence, high agreement with original
- [ ] very low - Minimal evidence, major disagreement

<!-- field: conclusion -->
### Describe the overall conclusion about the original claim (textarea, required)

Substantive interpretation. Headline comparison: replication's number vs the paper's number, sign + significance.

```
The headline result reproduces exactly from the authors' published data (S1 Data). Among 91 noma patients receiving physiotherapy during initial hospitalization, mean mouth opening increased from 17.6 mm at admission to 24.5 mm at discharge, a mean difference of 6.9 mm (95% CI 5.4 to 8.3; paired t = 9.4), matching the paper to the reported precision in direction, magnitude and significance. The one discrepancy is the reported degrees of freedom (paper: 91; correct for 91 pairs: 90), a reporting error that does not affect the result. Secondary analyses (age-group comparison, multivariable regression) reproduce only after excluding one 40-year-old patient, an exclusion the paper does not report; these are outside the scope of the claim tested here.
```

<!-- field: evidence -->
### Describe the evidence that supports your conclusion (textarea, required)

Numerical results, test statistics, model coefficients. Read directly from `results/`.

```
Paired t-test, n = 91: admission mean 17.637 mm, discharge mean 24.516 mm, mean difference 6.879 mm (95% CI 5.429 to 8.329), t = 9.424, df = 90, p = 4.5e-15 (paper: 6.9 mm, 95% CI 5.4 to 8.3, t = 9.4, df = 91, p < 0.001; abstract p < 0.0001 — both true). Patients below 20 mm mouth opening: 47/91 (52%) at admission, 23/91 (25%) at discharge, matching the paper; 25/91 (27%) moved from below 20 mm to 20 mm or above, matching the paper's 27%, with one patient moving the other way (net change 26.4 percentage points). Across all 120 statistics compared in results/summary.csv: 79 match, 9 match if the paper truncated rather than rounded, 32 mismatch; mismatches are confined to the age-dependent analyses (explained by the unreported exclusion of one adult) and to reporting errors (df, Table 1 percentage denominator of 92 instead of 91, "n = 20" in Table 2).
```

<!-- field: limitations -->
### Describe what limits the conclusions of the study (textarea, optional)

Honest caveats. If the result is partial or contradicted, say so plainly. Don't overclaim.

```
This is a computational reproduction on the same data, not an independent replication: it confirms the reported numbers follow from the published dataset, not that they generalise. The study has no comparison group without physiotherapy, so the admission-to-discharge change cannot be attributed causally to physiotherapy; natural recovery, other treatment and the length of hospitalization are not separated from it. The original analysis was run in R without published code; this reproduction uses Python (scipy, statsmodels), so variable recodings (primary caregiver, defect site) were inferred as the only mappings reproducing Table 1. The dataset contains data-quality irregularities that were logged but not corrected: five patients with a 0-day length of stay, four with more physiotherapy sessions than hospital days, missing values (sequestrectomy 10, caregiver 11), and one adult in a paediatric cohort. Length of stay in the data has n = 90, not the n = 75 reported, and no subset reproducing 75 was found.
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 05.
