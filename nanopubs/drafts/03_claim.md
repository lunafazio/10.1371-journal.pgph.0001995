# 03 — FORRT Claim

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Form heading:** *"FORRT Claim — Declare an original claim according to FORRT, linking it to an AIDA sentence with a specific FORRT type."*

## Field-by-field draft

<!-- field: claim -->
### Short URI suffix as claim ID (text input, required)

Slug becomes part of the nanopub URI. Use kebab-case.

```
noma-physio-mouth-opening-increase
```

<!-- field: label -->
### Label of the claim, to find it later (text input, required)

A descriptive title (not a sentence). Used for searches/discovery.

```
Increase in mouth opening from admission to discharge in noma patients receiving physiotherapy (Oluwalomola et al. 2023)
```

<!-- field: aida -->
### Search for an AIDA sentence (search/select, required)

URI of the AIDA published in step 02. Pull from `nanopubs/PUBLISHED.md`.

> _If the AIDA was published via Nanodash (`w3id.org/np/...` namespace), the platform's search may not find it — paste the URI manually._

```
«URI of step 02 AIDA — filled by the chain wizard»
```

<!-- field: forrtType -->
### Type of FORRT claim (dropdown, required)

Pick one. See `docs/claim-type-vocabulary.md` for the seven options and how to choose.

- [ ] computational performance (Computational & Performance)
- [ ] data governance (access control, licensing, FAIR compliance)
- [ ] data quality (preprocessing, validation, normalization)
- [ ] descriptive pattern (distribution, trend, proportion)
- [ ] model performance (accuracy, F1 score, evaluation metrics)
- [ ] scalability (Computational & Performance)
- [x] statistical significance (significant difference, relationship, or effect)

<!-- field: source -->
### Source URI (text input, optional)

Full URL form: `https://doi.org/...` (NOT bare DOI).

```
https://doi.org/10.1371/journal.pgph.0001995
```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 03.
