# 02 — AIDA Sentence

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.

**Form heading:** *"AIDA Sentence — Make structured scientific claims following the AIDA model"*

## Field-by-field draft

<!-- field: aida -->
### AIDA sentence (text input, required)

Atomic, Independent, Declarative, Absolute. One empirical finding. Must end with a full stop.

> _If your draft AIDA contains "and" linking two distinct findings, split into two AIDA nanopubs._

```
Mouth opening increases between hospital admission and discharge in noma patients who receive physiotherapy during their initial hospitalization.
```

<!-- field: topic -->
### Select related topics/tags (search/select, optional)

Predefined topic vocabulary — list the labels you intend to pick from the dropdown.

```
noma (Q994794)
physiotherapy (Q16643870)
```

<!-- field: project -->
### Relates to this nanopublication (search/select, required)

URI of the nanopub the AIDA derives from.

- For paper-rooted chains: the Quote-with-comment URI (from step 01).
- For question-rooted chains: the PICO or PCC URI (from step 01).

Pull the URI from `nanopubs/PUBLISHED.md`.

```
«URI of step 01 PICO — filled by the chain wizard»
```

<!-- field: dataset -->
### Supported by datasets (text input, optional)

DOIs/URLs of datasets that ground the AIDA claim.

*(skip — optional; S1 Data is cited in the Study and Outcome, and leaving this empty avoids the platform bug below)*

<!-- field: publication -->
### Supported by other publications (text input, optional)

DOIs/URLs of publications that support the AIDA claim — e.g. peer-reviewed methods papers, or the original paper if not already cited via the Quote.

- https://doi.org/10.1371/journal.pgph.0001995

> **Known platform bug (2026-04-26):** if both *Supported by datasets* AND *Supported by other publications* are populated and publishing fails, fall back to publishing this AIDA via Nanodash. The URI namespace becomes `https://w3id.org/np/...` (still valid and citable).

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 02.
