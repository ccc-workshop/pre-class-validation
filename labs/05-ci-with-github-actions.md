# Lab 5 - Automatic checks with GitHub Actions (45 minutes)

**Goal:** see a workflow stop a bad change before it reaches `main`, then fix it.

**Where:** your own copy (`~/github-workshop/my-lab`).

## 1. Read the workflow

Open `.github/workflows/checks.yml` in VS Code and find:

- **on:** - when it runs (every pull request, pushes to `main`, and manually)
- **jobs > checks > runs-on:** - a fresh Ubuntu machine from GitHub
- **steps:** - check out the code, set up Python, run the SQL house rules, run the Python tests

Open `scripts/check_sql.py` and read the three house rules at the top.

## 2. Break a rule on purpose

```bash
cd ~/github-workshop/my-lab
git switch main
git pull
git switch -c <your-handle>/top-counties
```

Create `sql/reports/top_counties.sql`:

```sql
SELECT *
FROM rpt.active_licenses
```

```bash
git add sql/reports/top_counties.sql
git commit -m "Add top counties report"
git push -u origin <your-handle>/top-counties
```

Open a pull request into `main`.

## 3. Watch it fail

1. On the PR, the check **Data checks / sql-and-python-checks** turns **red**.
2. **Details** > open the step **SQL house rules**. The log lists three problems: no `-- Purpose:` line, `SELECT *`, and no semicolon.
3. The **Merge** button is blocked because your ruleset requires the check.

## 4. Fix it

Replace the file contents with:

```sql
-- Purpose: Counties with the most active licenses.
SELECT
    county,
    COUNT(*) AS active_count
FROM rpt.active_licenses
GROUP BY county
ORDER BY active_count DESC;
```

```bash
git commit -am "Follow SQL house rules in top counties report"
git push
```

The check runs again and turns **green**. **Merge pull request** > **Delete branch**.

## 5. Optional - run the same checks locally (needs Python)

```bash
python scripts/check_sql.py
python -m unittest discover -s python/tests -v
```

## 6. Optional - add a status badge

Add this line near the top of `README.md` on a new branch and open a PR:

```markdown
![Data checks](https://github.com/<your-handle>/ccc-data-team-lab/actions/workflows/checks.yml/badge.svg)
```

## Done when

- [ ] You saw a red check block a merge
- [ ] You fixed it and merged with a green check
