# Pretrial Detention Decisions in New York: Case, Record, Place and Race

SE_POL 408 (Applied Data Science and Application in Social Policy), Northwestern University, Fall 2026 — Final Project

**Research question.** How much of New York's pretrial detention decisions is explained by the case and the defendant's record, how much by where and before whom the case is arraigned and by the defendant's race, and do these differences track the actual risk of failing to appear?

**Data.** New York State Office of Court Administration, *Pretrial Release Data*: one row per arraigned case, arraignment years 2021–2023 (about 250k–325k cases per year, 131 fields). Public download: https://www.nycourts.gov/division-technology-court-research/pretrial-release-data

**Plan.** `docs/项目方案_v1.md` (team working document, Chinese).

## Repository structure

```
ny-pretrial-detention/
├── data/
│   ├── raw/          # NYS for Web <year>.csv (not tracked; download from OCA)
│   ├── processed/    # analysis files (not tracked)
│   └── external/     # county-level context, if any (not tracked)
├── docs/             # plan, OCA data dictionary and documentation
├── notebooks/        # numbered analysis notebooks
├── src/              # config, sample, features, models, evaluate, fairness, explain
├── reports/          # aggregate tables and figures (tracked)
├── models/           # fitted models (not tracked)
└── slides/
```

## Reproducing

1. `pip install -r requirements.txt`
2. Download `NYS for Web 2021.csv`, `2022.csv`, `2023.csv` into `data/raw/`.
3. `python -m src.build_dataset` (to be written) → `data/processed/analytic.parquet`
4. Run notebooks in numeric order.

## Status

2026-11-06: folder created; plan v1; quick profiling of 2022 (`notebooks/00_quick_profile*.py`). Sample and feature code next.
