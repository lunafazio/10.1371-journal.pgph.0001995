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
# # 02 — Data clean
#
# Tidies S1 Data (one sheet, 91 rows x 10 columns) into
# `data/processed/noma_clean.csv`. **No rows are dropped and no values are
# repaired.** Missing values stay missing; each analysis in 03 uses complete
# cases for the variables it needs and reports its own n.
#
# ## Variable mapping (raw column -> tidy column)
#
# | Raw | Tidy | Transformation |
# |---|---|---|
# | `Age` | `age_years` | as-is (integer years) |
# | — | `age_group` | `"0-3"` if age <= 3 else `">3"` (paper: 0–3 vs >3) |
# | `Sex` | `sex` | lower-case male/female |
# | `Physio Sessions` | `physio_sessions` | as-is (float; NaN kept) |
# | `Stay No` | `length_of_stay_days` | as-is (float; NaN kept; zeros kept and flagged) |
# | `Sequestrum` | `sequestrectomy` | Yes/No; NaN kept |
# | `Relationship` | `caregiver_raw` | as-is |
# | — | `caregiver_group` | Mother, Grandmother, "Father and Mother" -> "Primary caregiver"; Aunty, Father, Brother, Sister -> "Not primary caregiver"; NaN kept. **Inferred**: the paper does not define "primary caregiver"; this is the only grouping of the raw labels that reproduces Table 1 counts (72 / 8). |
# | `Defect Site` | `defect_site_raw` | as-is |
# | — | `defect_site` | Cheeks->Cheek; Lips/lips->Lip; Nasal->Nose; "No defect"->No defect; **"Particularities" -> No defect (inferred)** — the only mapping that reproduces Table 1 (72/11/6/2). |
# | `MO Adm` | `mo_admission_mm` | as-is (mm) |
# | `MO Disc` | `mo_discharge_mm` | as-is (mm) |
# | `MO Change` | `mo_change_raw_mm` | as-is; checked against discharge − admission |
# | — | `mo_change_mm` | `mo_discharge_mm - mo_admission_mm` |

# %%
from pathlib import Path

import pandas as pd

# %%
RAW = Path("../data/raw/pgph.0001995.s001.xlsx")
OUT_DIR = Path("../data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

raw = pd.read_excel(RAW, sheet_name=None)
print("Sheets:", {k: v.shape for k, v in raw.items()})
assert list(raw) == ["Sheet1"], "unexpected sheet layout"
raw = raw["Sheet1"]
raw.info()

# %% [markdown]
# ## Missingness and value audit (raw)

# %%
print(raw.isna().sum().to_string())
for col in ["Sex", "Sequestrum", "Relationship", "Defect Site"]:
    print(f"\n{col}:\n{raw[col].value_counts(dropna=False).to_string()}")
print("\nAge distribution:\n", raw["Age"].value_counts().sort_index().to_string())

# %% [markdown]
# ## Build tidy dataset

# %%
PRIMARY = {"Mother", "Grandmother", "Father and Mother"}
NOT_PRIMARY = {"Aunty", "Father", "Brother", "Sister"}
DEFECT = {"Cheeks": "Cheek", "Lips": "Lip", "lips": "Lip", "Nasal": "Nose",
          "No defect": "No defect", "Particularities": "No defect"}

unknown_rel = set(raw["Relationship"].dropna()) - PRIMARY - NOT_PRIMARY
unknown_def = set(raw["Defect Site"].dropna()) - set(DEFECT)
assert not unknown_rel and not unknown_def, (unknown_rel, unknown_def)


def caregiver(v: object) -> object:
    if pd.isna(v):
        return pd.NA
    return "Primary caregiver" if v in PRIMARY else "Not primary caregiver"


clean = pd.DataFrame({
    "patient_row": range(1, len(raw) + 1),
    "age_years": raw["Age"].astype(int),
    "age_group": raw["Age"].map(lambda a: "0-3" if a <= 3 else ">3"),
    "sex": raw["Sex"].str.lower(),
    "physio_sessions": raw["Physio Sessions"],
    "length_of_stay_days": raw["Stay No"],
    "sequestrectomy": raw["Sequestrum"],
    "caregiver_raw": raw["Relationship"],
    "caregiver_group": raw["Relationship"].map(caregiver),
    "defect_site_raw": raw["Defect Site"],
    "defect_site": raw["Defect Site"].map(DEFECT),
    "mo_admission_mm": raw["MO Adm"],
    "mo_discharge_mm": raw["MO Disc"],
    "mo_change_raw_mm": raw["MO Change"],
})
clean["mo_change_mm"] = clean["mo_discharge_mm"] - clean["mo_admission_mm"]

# %% [markdown]
# ## Consistency checks and flags (logged, not repaired)

# %%
n_change_mismatch = int((clean["mo_change_mm"] != clean["mo_change_raw_mm"]).sum())
print(f"Rows where raw 'MO Change' != discharge - admission: {n_change_mismatch}")
flags = {
    "length_of_stay == 0": int((clean["length_of_stay_days"] == 0).sum()),
    "physio_sessions > length_of_stay": int(
        (clean["physio_sessions"] > clean["length_of_stay_days"]).sum()),
    "negative mouth-opening change": int((clean["mo_change_mm"] < 0).sum()),
    "age > 18 years (adult in a children's cohort)": int((clean["age_years"] > 18).sum()),
}
for k, v in flags.items():
    print(f"{k}: {v}")
print(f"\nRows in: {len(raw)}; rows out: {len(clean)}; rows excluded: 0")
print(clean["age_group"].value_counts().to_string())

# %%
clean.to_csv(OUT_DIR / "noma_clean.csv", index=False)
print(f"Wrote {OUT_DIR / 'noma_clean.csv'} ({clean.shape})")
