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
# # 01 — Data download
#
# Fetches S1 Data (XLSX) of Oluwalomola et al. 2023, PLOS Glob Public Health
# 3(9): e0001995 (doi:10.1371/journal.pgph.0001995), from PLOS. The supporting
# file has its own DOI, 10.1371/journal.pgph.0001995.s001. No credentials needed.
#
# The SHA-256 of the downloaded file is recorded in `data/raw/sources.json`;
# if `EXPECTED_SHA256` is set and the download differs, the notebook fails
# rather than silently analysing a changed file.

# %%
import hashlib
import json
import urllib.request
from datetime import date
from pathlib import Path

# %%
RAW_DIR = Path("../data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)
OUT = RAW_DIR / "pgph.0001995.s001.xlsx"

URL = (
    "https://journals.plos.org/globalpublichealth/article/file"
    "?type=supplementary&id=10.1371/journal.pgph.0001995.s001"
)
# Checksum observed on first download (2026-10-10).
EXPECTED_SHA256: str | None = "81dafc1d7ed0b3b5a97c98f6d0439c685f786e2e3f0773d58723aff84986a658"

# %%
req = urllib.request.Request(URL, headers={"User-Agent": "forrt-replication/1.0"})
with urllib.request.urlopen(req, timeout=120) as resp:
    payload = resp.read()
OUT.write_bytes(payload)
sha = hashlib.sha256(payload).hexdigest()
print(f"Wrote {OUT} ({len(payload)} bytes), sha256={sha}")
if EXPECTED_SHA256 and sha != EXPECTED_SHA256:
    raise RuntimeError(f"Checksum mismatch: expected {EXPECTED_SHA256}, got {sha}")

# %% [markdown]
# ## Source log

# %%
SOURCES = [
    {
        "name": "S1 Data — Oluwalomola et al. 2023 noma physiotherapy cohort",
        "doi": "10.1371/journal.pgph.0001995.s001",
        "url": URL,
        "file": OUT.name,
        "license": "CC-BY-4.0",
        "accessed_on": date.today().isoformat(),
        "sha256": sha,
    }
]
with open(RAW_DIR / "sources.json", "w") as f:
    json.dump({"sources": SOURCES}, f, indent=2)
print(f"Logged {len(SOURCES)} source(s) to {RAW_DIR / 'sources.json'}")
