# 01 — Quote-with-comment (paper-rooted chains)

> Run the pre-flight checklist in `docs/forrt-form-fields.md` § Pre-flight checklist before drafting.
>
> If this is a question-rooted chain, use `01_pico.md` or `01_pcc.md` instead — see `docs/chain-decision-tree.md`.
>
> **After choosing the chain shape, delete the two step-1 alternates you aren't using.** Once you've decided this chain is paper-rooted and keep `01_quote.md`, run:
> ```bash
> rm nanopubs/drafts/01_pico.md nanopubs/drafts/01_pcc.md
> ```

**Form heading:** *"Annotate a paper quotation — Annotating a paper quotation with personal interpretation"*

## Field-by-field draft

<!-- field: paper -->
### Cited DOI (text input, required)

Format: starts with `10.` — bare DOI, **NOT** `https://doi.org/...` form.

```
10.1371/journal.pgph.0001995
```

### Quote mode (radio button)

- [x] **Quote whole text (less than 500 characters)**
- [ ] Quote start/end *(use this if the quote exceeds 500 chars)*

<!-- field: quotation -->
### The exact quotation from the paper (max. 500 characters) (textarea, required)

Verbatim from the paper PDF in `paper/`. Character-for-character. ≤ 500 chars in whole-text mode.

Source: Abstract, p. 1. Verification: matched verbatim against `pdftotext` extraction (whitespace-normalised); `verify_quote` (forrt-research MCP) was not available in the analysis session — **unverified by verify_quote; re-run before publishing**.

```
The mean difference in the mouth opening from admission to discharge was 6.9mm (95% CI: 5.4 to 8.3, p < 0.0001).
```

Character count: 112 / 500.

Alternative candidates (also matched against the extracted text):

- Abstract, p. 1: `Increased number of physiotherapy sessions and patient age above three years were significant predictors of improvement in mouth opening (p-value 0.011, 0.001 respectively).` (173 chars)
- Results, p. 7: `Being greater than age 3 accounted for a 4.8mm increase in mouth opening in the fully adjusted model (95% CI: 2.2 to 7.5mm).` (124 chars)

<!-- field: quotation-end -->
### End of quotation (optional - use when quoting beginning and end of a longer passage, max. 500 characters) (textarea, optional)

Only when quoting the beginning *and* end of a longer passage — set the mode above to
**Quote start/end**, put the opening phrase under the previous heading and the closing
phrase here. Leave empty for a single short quote.

```

```

<!-- field: comment -->
### Our interpretation and explanation of why this quotation is relevant (max. 800 characters) (textarea, required)

Why this quote matters and what the replication tests. Connect the paper's claim to the work this repo does. Don't repeat the quote.

```

```

## Publication note

After publishing, paste the resulting URI into `nanopubs/PUBLISHED.md` step 01.
