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
# # 04 — Figures
#
# `figures/main_result.png`: left — paper vs reproduced headline paired
# t-test (mean admission, discharge, difference with 95% CI); right —
# per-patient admission vs discharge mouth opening.

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("seaborn-v0_8-whitegrid")
FIG = Path("../figures")
FIG.mkdir(parents=True, exist_ok=True)

summary = pd.read_csv("../results/summary.csv")
df = pd.read_csv("../data/processed/noma_clean.csv")
a = summary[summary.analysis == "a_paired_ttest"].set_index("statistic")


def val(stat: str, col: str) -> float:
    return float(a.loc[stat, col])


# %%
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))
labels = ["Admission", "Discharge", "Difference"]
keys = ["mean mouth opening at admission (mm)", "mean mouth opening at discharge (mm)",
        "mean difference (mm)"]
for off, col, name, c in [(-0.15, "paper_value", "Paper (R)", "tab:gray"),
                          (0.15, "reproduced_unrounded", "Reproduced (Python)", "tab:blue")]:
    ys = [val(k, col) for k in keys]
    ax1.bar([i + off for i in range(3)], ys, width=0.3, color=c, label=name)
    lo, hi = val("95% CI lower (mm)", col), val("95% CI upper (mm)", col)
    ax1.errorbar(2 + off, ys[2], yerr=[[ys[2] - lo], [hi - ys[2]]], color="k", capsize=4)
    for i, y in enumerate(ys):
        ax1.text(i + off, (hi if i == 2 else y) + 0.4, f"{y:.1f}", ha="center", fontsize=8)
ax1.set_xticks(range(3), labels)
ax1.set_ylabel("Mouth opening (mm)")
ax1.set_title("Paired t-test: paper vs reproduction (n = 91)")
ax1.legend()

for _, r in df.iterrows():
    ax2.plot([0, 1], [r.mo_admission_mm, r.mo_discharge_mm], color="tab:blue", alpha=0.2, lw=0.8)
ax2.boxplot([df.mo_admission_mm, df.mo_discharge_mm], positions=[0, 1], widths=0.3,
            showmeans=True)
ax2.axhline(20, color="tab:red", ls="--", lw=1, label="20 mm functional threshold")
ax2.set_xticks([0, 1], ["Admission", "Discharge"])
ax2.set_ylabel("Mouth opening (mm)")
ax2.set_title("Per-patient mouth opening")
ax2.legend(loc="upper left")
fig.tight_layout()
fig.savefig(FIG / "main_result.png", dpi=150)
plt.show()
