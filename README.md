# Data Team Lab Repository

A practice repository for the **GitHub for Developers** workshop.
Everything in here is fictional sample data. No real license, business or person data belongs in this repo.

## What's in here

| Folder | What it holds |
| --- | --- |
| `sql/` | Table definitions, views and report queries |
| `python/` | A small Python helper that cleans the license extract, plus its tests |
| `data/sample/` | A tiny fictional CSV used by the tests |
| `docs/` | Data dictionary, refresh schedule and team pages |
| `scripts/` | Checks that run locally and in GitHub Actions |
| `labs/` | Step-by-step lab guides for the workshop |
| `.github/workflows/` | The automated checks that run on every pull request |

## How we work

1. Open or pick an **issue** for the change.
2. Create a **branch** from `main`.
3. Make small, focused **commits**.
4. Open a **pull request**, ask a teammate to review, and wait for the checks to pass.
5. **Merge**, then delete the branch.

## Run the checks yourself

```bash
python scripts/check_sql.py
python -m unittest discover -s python/tests -v
```

Both checks also run automatically in GitHub Actions on every pull request.
