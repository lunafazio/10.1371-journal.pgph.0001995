# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # 03 — Analysis
#
# Reproduces every reported statistic of Oluwalomola et al. 2023 from S1 Data.
# The authors used R (no code, version, or packages published); this notebook
# uses Python (scipy + statsmodels) — a recorded deviation. Tests used:
#
# - (a) paired t-test, admission vs discharge mouth opening (headline);
# - (b) independent two-sample t-test of change by age group (Student, equal
#   variances — the R `t.test` default is Welch, so both are reported);
# - (c) bivariate: one-way ANOVA for categorical factors, simple OLS for
#   continuous factors (Table 2);
# - (d) multivariable OLS: change ~ physio sessions + age group (Table 3);
# - (e) proportions with < 20 mm opening at admission / discharge.
#
# Each analysis uses complete cases for its variables; n is reported.
# The **primary** reproduction uses all 91 rows. Sensitivity analyses that
# reconstruct the paper's apparent n are reported separately and labelled.

# %%
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats

# %%
df = pd.read_csv("../data/processed/noma_clean.csv")
RESULTS = Path("../results")
RESULTS.mkdir(parents=True, exist_ok=True)
rows: list[dict] = []


def rec(analysis: str, statistic: str, paper: float | None, value: float,
        decimals: int, n: int, note: str = "") -> None:
    """Record a statistic; match = equal after rounding (or truncating) to the paper's precision."""
    rv = round(float(value), decimals)
    trunc = np.trunc(float(value) * 10**decimals) / 10**decimals
    if np.isclose(rv, paper):
        match = "match"
    elif np.isclose(trunc, paper):
        match = "match (truncated)"  # paper appears to truncate rather than round
    else:
        match = "mismatch"
    rows.append(dict(analysis=analysis, statistic=statistic, paper_value=paper,
                     reproduced_value=rv, reproduced_unrounded=float(value),
                     n=n, match=match, note=note))


# %% [markdown]
# ## (a) Paired t-test: admission vs discharge (headline)

# %%
a = df[["mo_admission_mm", "mo_discharge_mm"]].dropna()
n = len(a)
diff = a["mo_discharge_mm"] - a["mo_admission_mm"]
tt = stats.ttest_rel(a["mo_discharge_mm"], a["mo_admission_mm"])
ci = tt.confidence_interval(0.95)
print(f"n={n} adm={a.mo_admission_mm.mean():.3f} disc={a.mo_discharge_mm.mean():.3f} "
      f"diff={diff.mean():.3f} CI=({ci.low:.3f},{ci.high:.3f}) t={tt.statistic:.3f} "
      f"df={tt.df} p={tt.pvalue:.3g}")
A = "a_paired_ttest"
rec(A, "mean mouth opening at admission (mm)", 17.6, a.mo_admission_mm.mean(), 1, n)
rec(A, "mean mouth opening at discharge (mm)", 24.5, a.mo_discharge_mm.mean(), 1, n)
rec(A, "mean difference (mm)", 6.9, diff.mean(), 1, n)
rec(A, "95% CI lower (mm)", 5.4, ci.low, 1, n)
rec(A, "95% CI upper (mm)", 8.3, ci.high, 1, n)
rec(A, "t", 9.4, tt.statistic, 1, n)
rec(A, "df", 91, tt.df, 0, n, "paper reports df=91 with n=91; a paired t-test on 91 pairs has df=n-1=90")
rec(A, "p < 0.001 (1=yes)", 1, float(tt.pvalue < 0.001), 0, n, f"p={tt.pvalue:.2e}; also < 0.0001 (abstract)")

# %% [markdown]
# ## (b) Independent t-test of change by age group
#
# The data contain 91 patients with non-missing age (44 aged 0–3, 47 aged >3),
# whereas the paper reports n = 90 (44 / 46) and df = 88. One patient is aged
# 40 years — the only adult. Excluding that single patient reproduces the
# paper's 44 / 46 split exactly, so a sensitivity run with that exclusion is
# shown alongside the primary all-rows run.

# %%
def age_ttest(d: pd.DataFrame, label: str, note: str) -> None:
    y = d.loc[d.age_group == "0-3", "mo_change_mm"]
    o = d.loc[d.age_group == ">3", "mo_change_mm"]
    st = stats.ttest_ind(o, y, equal_var=True)
    we = stats.ttest_ind(o, y, equal_var=False)
    ci = st.confidence_interval(0.95)
    print(f"[{label}] n={len(y)}+{len(o)} mean0-3={y.mean():.3f} mean>3={o.mean():.3f} "
          f"diff={o.mean()-y.mean():.3f} CI=({ci.low:.3f},{ci.high:.3f}) "
          f"Student t={st.statistic:.3f} df={st.df} p={st.pvalue:.4f} | "
          f"Welch t={we.statistic:.3f} df={we.df:.1f} p={we.pvalue:.4f}")
    nn = len(y) + len(o)
    B = f"b_age_ttest[{label}]"
    rec(B, "n aged 0-3", 44, len(y), 0, nn, note)
    rec(B, "n aged >3", 46, len(o), 0, nn, note)
    rec(B, "mean change aged 0-3 (mm)", 4.5, y.mean(), 1, nn, note)
    rec(B, "mean change aged >3 (mm)", 8.9, o.mean(), 1, nn, note)
    rec(B, "difference in mean change (mm)", 4.5, o.mean() - y.mean(), 1, nn, note)
    rec(B, "95% CI lower (mm)", 1.7, ci.low, 1, nn, "Student pooled-variance CI")
    rec(B, "95% CI upper (mm)", 7.2, ci.high, 1, nn, "Student pooled-variance CI")
    rec(B, "t (Student)", 3.2, st.statistic, 1, nn)
    rec(B, "df (Student)", 88, st.df, 0, nn)
    rec(B, "p (Student)", 0.002, st.pvalue, 3, nn)
    rec(B, "t (Welch)", 3.2, we.statistic, 1, nn, "R t.test default")
    rec(B, "df (Welch)", 88, we.df, 0, nn, "R t.test default")
    rec(B, "p (Welch)", 0.002, we.pvalue, 3, nn, "R t.test default")


age_ttest(df, "all rows", "primary: all 91 rows")
df_no_adult = df[df.age_years <= 18]
age_ttest(df_no_adult, "excl. age-40 patient", "sensitivity: excludes the single 40-year-old")

# %% [markdown]
# ## (c) Bivariate analyses (Table 2)
#
# Categorical factors: one-way ANOVA of change. Group mean changes are
# compared with Table 2. Continuous factors: simple OLS of change on the factor.

# %%
TABLE2_MEANS = {
    "age_group": {"0-3": 4.47, ">3": 8.95},
    "sex": {"male": 6.97, "female": 6.78},
    "caregiver_group": {"Primary caregiver": 6.83, "Not primary caregiver": 6.00},
    "defect_site": {"Cheek": 7.22, "Lip": 6.54, "Nose": 4.33, "No defect": 4.00},
    "sequestrectomy": {"Yes": 5.92, "No": 6.49},
}
TABLE2_N = {"age_group": 90, "sex": 91, "caregiver_group": 80, "defect_site": 91,
            "sequestrectomy": 81}
TABLE2_COUNTS = {"age_group": {"0-3": 44, ">3": 46}, "sex": {"male": 44, "female": 47},
                 "caregiver_group": {"Primary caregiver": 72, "Not primary caregiver": 8},
                 "defect_site": {"Cheek": 72, "Lip": 11, "Nose": 6, "No defect": 2},
                 "sequestrectomy": {"Yes": 26, "No": 55}}
TABLE2_P = {"age_group": 0.002, "sex": 0.89, "caregiver_group": 0.75,
            "defect_site": 0.73, "sequestrectomy": 0.73}

for var, means in TABLE2_MEANS.items():
    d = df[[var, "mo_change_mm"]].dropna()
    groups = [g["mo_change_mm"].values for _, g in d.groupby(var)]
    f = stats.f_oneway(*groups)
    C = f"c_bivariate_anova[{var}]"
    rec(C, "n", TABLE2_N[var], len(d), 0, len(d))
    for lvl, pm in means.items():
        g = d.loc[d[var] == lvl, "mo_change_mm"]
        rec(C, f"count {lvl}", TABLE2_COUNTS[var][lvl], len(g), 0, len(d))
        rec(C, f"mean change {lvl} (mm)", pm, g.mean(), 2, len(d))
    rec(C, "ANOVA p", TABLE2_P[var], f.pvalue, 2 if TABLE2_P[var] >= 0.01 else 3, len(d))
    print(f"{var}: n={len(d)} F={f.statistic:.3f} p={f.pvalue:.4f} "
          + ", ".join(f"{k}={d.loc[d[var]==k,'mo_change_mm'].mean():.2f}" for k in means))

# Table 1 percentages: check which denominator was used.
for lvl, cnt in [("Female", 47), ("Male", 44), ("Cheek", 72), ("No defect", 2)]:
    print(f"Table 1 {lvl}: {cnt}/91={cnt/91:.1%}  {cnt}/92={cnt/92:.1%}")


# %%
def simple_ols(var: str, paper: tuple[float, float, float, float], paper_n: int,
               d: pd.DataFrame, label: str, note: str = "") -> None:
    dd = d[[var, "mo_change_mm"]].dropna()
    m = smf.ols(f"mo_change_mm ~ {var}", data=dd).fit()
    lo, hi = m.conf_int().loc[var]
    print(f"[{label}] {var}: n={len(dd)} b={m.params[var]:.4f} CI=({lo:.4f},{hi:.4f}) "
          f"p={m.pvalues[var]:.4f}")
    C = f"c_bivariate_ols[{var}; {label}]"
    rec(C, "n", paper_n, len(dd), 0, len(dd), note)
    rec(C, "coefficient (mm per unit)", paper[0], m.params[var], 2, len(dd), note)
    rec(C, "95% CI lower", paper[1], lo, 2, len(dd), note)
    rec(C, "95% CI upper", paper[2], hi, 2, len(dd), note)
    rec(C, "p", paper[3], m.pvalues[var], 3 if paper[3] < 0.01 else 2, len(dd), note)


simple_ols("physio_sessions", (0.28, 0.04, 0.53, 0.02), 20, df, "all rows",
           "paper's 'n = 20' is likely a typo")
simple_ols("length_of_stay_days", (0.14, 0.05, 0.22, 0.002), 75, df, "all rows")
simple_ols("length_of_stay_days", (0.14, 0.05, 0.22, 0.002), 75,
           df[df.length_of_stay_days > 0], "excl. stay = 0",
           "sensitivity: drops 5 rows with length of stay 0 days")

# %% [markdown]
# ## (d) Multivariable OLS (Table 3): change ~ physio sessions + age group

# %%
def multi(d: pd.DataFrame, label: str, note: str) -> None:
    dd = d[["mo_change_mm", "physio_sessions", "age_group"]].dropna().copy()
    dd["age_gt3"] = (dd.age_group == ">3").astype(int)
    m = smf.ols("mo_change_mm ~ physio_sessions + age_gt3", data=dd).fit()
    print(f"[{label}] n={int(m.nobs)}\n", m.summary().tables[1])
    ci = m.conf_int()
    D = f"d_multivariable[{label}]"
    paper = {"Intercept": (0.9, -2.6, 4.1, 0.589), "physio_sessions": (0.3, 0.1, 0.5, 0.011),
             "age_gt3": (4.8, 2.2, 7.5, 0.001)}
    for term, (b, lo, hi, p) in paper.items():
        nn = int(m.nobs)
        rec(D, f"{term} coefficient", b, m.params[term], 1, nn, note)
        rec(D, f"{term} 95% CI lower", lo, ci.loc[term, 0], 1, nn, note)
        rec(D, f"{term} 95% CI upper", hi, ci.loc[term, 1], 1, nn, note)
        rec(D, f"{term} p", p, m.pvalues[term], 3, nn, note)


multi(df, "all rows", "primary")
multi(df_no_adult, "excl. age-40 patient", "sensitivity")

# %% [markdown]
# ## (e) Proportion with < 20 mm opening

# %%
nE = int(df.mo_admission_mm.notna().sum())
adm_lt = int((df.mo_admission_mm < 20).sum())
dis_lt = int((df.mo_discharge_mm < 20).sum())
moved = int(((df.mo_admission_mm < 20) & (df.mo_discharge_mm >= 20)).sum())
back = int(((df.mo_admission_mm >= 20) & (df.mo_discharge_mm < 20)).sum())
print(f"<20 mm admission {adm_lt}/{nE}; discharge {dis_lt}/{nE}; "
      f"<20 -> >=20: {moved}; >=20 -> <20: {back}")
E = "e_proportions"
rec(E, "n < 20 mm at admission", 47, adm_lt, 0, nE)
rec(E, "% < 20 mm at admission", 52, 100 * adm_lt / nE, 0, nE)
rec(E, "n < 20 mm at discharge", 23, dis_lt, 0, nE)
rec(E, "% < 20 mm at discharge", 25, 100 * dis_lt / nE, 0, nE)
rec(E, "% moved from < 20 to >= 20 mm", 27, 100 * moved / nE, 0, nE,
    "paper: 27% went from non-functional to functional; 52%-25% also equals 27 if rounded percentages are subtracted")
rec(E, "net change in % < 20 mm (percentage points)", 27, 100 * (adm_lt - dis_lt) / nE, 0, nE)

# %% [markdown]
# ## Descriptives (Table 1)

# %%
T = "table1_descriptives"
rec(T, "mean age (years)", 5, df.age_years.mean(), 0, len(df))
rec(T, "SD age (years)", 5, df.age_years.std(), 0, len(df))
rec(T, "mean physio sessions", 11, df.physio_sessions.mean(), 0, int(df.physio_sessions.notna().sum()))
rec(T, "SD physio sessions", 6, df.physio_sessions.std(), 0, int(df.physio_sessions.notna().sum()))
rec(T, "mean length of stay (days)", 25, df.length_of_stay_days.mean(), 0, int(df.length_of_stay_days.notna().sum()))
rec(T, "SD length of stay (days)", 16, df.length_of_stay_days.std(), 0, int(df.length_of_stay_days.notna().sum()))

# %% [markdown]
# ## Comparison table

# %%
summary = pd.DataFrame(rows)
summary.to_csv(RESULTS / "summary.csv", index=False)
with pd.option_context("display.max_rows", None, "display.width", 200,
                       "display.max_colwidth", 40):
    print(summary[["analysis", "statistic", "paper_value", "reproduced_value", "n", "match"]])
print(summary.match.value_counts())
