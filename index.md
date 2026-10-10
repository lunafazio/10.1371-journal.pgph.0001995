# 10.1371-journal.pgph.0001995

> **Physiotherapy and associated factors affecting mouth opening changes in noma patients during initial hospitalization at an MSF-supported hospital in Northwest Nigeria—A retrospective cohort study** — computational reproduction with reconstructed code.
>
> Reference paper: [10.1371/journal.pgph.0001995](https://doi.org/10.1371/journal.pgph.0001995)

This repository is a self-contained computational reproduction of the headline claim from the reference paper above: the authors' published data (S1 Data) re-analysed with code reconstructed from the paper's methods description (no original code was published). It produces:

- A reproducible computational pipeline (Snakefile + notebooks).
- A FORRT-tagged nanopublication chain on the [Science Live platform](https://platform.sciencelive4all.org), documenting the claim, the reproduction design, and the outcome with full provenance.
- A Zenodo-archived release (source + container image) with a citable DOI.

## Quick start

```bash
git clone https://github.com/lunafazio/10.1371-journal.pgph.0001995.git
cd 10.1371-journal.pgph.0001995
pixi install
pixi run snakemake --cores 1
```

Or with Docker:

```bash
docker run --rm ghcr.io/lunafazio/10.1371-journal.pgph.0001995:latest
```

## Structure

- `paper/` — the source paper PDF (drop yours in there).
- `notebooks/` — jupytext `.py` notebooks that drive the pipeline.
- `data/` — downloaded by `notebooks/01_data_download.py`, never committed.
- `nanopubs/` — drafts of the FORRT chain field-by-field, plus the published-URI registry.
- `docs/` — operating manuals (FORRT form fields, chain decision tree, claim-type vocabulary).
- `figures/` — curated figures used in the Jupyter Book.

## Nanopublication chain

The published chain is listed in [`nanopubs/PUBLISHED.md`](nanopubs/PUBLISHED.md). Each step links to its viewer URL on the Science Live platform.

## Citation

If you use this work, please cite both:

- This software: [`CITATION.cff`](CITATION.cff) → DOI [{{ZENODO_DOI}}]({{ZENODO_DOI}}).
- The original paper: [10.1371/journal.pgph.0001995](https://doi.org/10.1371/journal.pgph.0001995).
