# Lab 2 - Work locally, push, and review (60 minutes)

**Goal:** the daily loop on your own machine - branch, edit, stage, commit, push - then a review with a **suggested change**.

**Where:** your clone of the shared repo from Lab 0 (`~/github-workshop/ccc-data-team-lab`) in a Git Bash terminal.

## 1. Get the latest `main`

```bash
cd ~/github-workshop/ccc-data-team-lab
git switch main
git pull
git log --oneline -5
```

You should see your team page commit from Lab 1.

## 2. Create a branch

```bash
git switch -c <your-handle>/by-type-and-county
git branch
```

## 3. Add a report query

Create `sql/reports/<your-handle>_by_type_and_county.sql` in VS Code:

```sql
-- Purpose: Active licenses by type and county.
SELECT
    license_type,
    county,
    COUNT(*) AS active_count
FROM rpt.active_licenses
GROUP BY license_type, county
ORDER BY license_type, county;
```

## 4. Stage and commit (the two-stage commit)

```bash
git status                      # the file is untracked
git add sql/reports/<your-handle>_by_type_and_county.sql
git status                      # staged, ready to commit
git diff --staged               # exactly what will be committed
git commit -m "Add active licenses by type and county report"
```

Optional, if you have Python: `python scripts/check_sql.py`

## 5. Make a second small commit

Open your team page `docs/team/<your-handle>.md` and add a line:

```markdown
- My first local commit: Add active licenses by type and county report
```

```bash
git add docs/team/<your-handle>.md
git commit -m "Note my first local commit on my team page"
git log --oneline -3
```

## 6. Push and open a pull request

```bash
git push -u origin <your-handle>/by-type-and-county
```

Git prints a link - open it (or use **Compare & pull request** on GitHub). Request your neighbor as reviewer and create the PR.

## 7. Review with a suggested change

As the **reviewer** on your neighbor's PR:

1. **Files changed** > hover the `ORDER BY` line > blue **+**.
2. Click the **Add a suggestion** icon (the +/- document icon) and change the line to:
   `ORDER BY active_count DESC, license_type, county;`
3. **Start a review** > **Finish your review** > **Comment**.

As the **author**:

1. On your PR, find the suggestion > **Commit suggestion** > **Commit changes**.
2. Pull that commit down to your machine:

   ```bash
   git pull
   git log --oneline -3
   ```

3. Ask your reviewer to **Approve**, then **Merge pull request** and **Delete branch**.

## 8. Clean up locally

```bash
git switch main
git pull
git branch -d <your-handle>/by-type-and-county
git fetch --prune
```

## 9. Make history easy to read (aliases)

```bash
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.st "status -sb"
git lg -15
git st
```

## Done when

- [ ] Your report query is on `main` through a reviewed PR
- [ ] You committed a reviewer's suggestion and pulled it locally
- [ ] Your local branch is deleted and `git lg` shows the merge
