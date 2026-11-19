# Lab 8 - Capstone: issue to release (40 minutes)

**Goal:** put the whole flow together in your own copy - issue, branch, commit, pull request, checks, merge - then tag and publish a release.

**Where:** your own copy (`~/github-workshop/my-lab`).

## 1. Tag the starting point

```bash
cd ~/github-workshop/my-lab
git switch main
git pull
git tag -a v1.0 -m "Workshop baseline"
git push origin v1.0
git tag
```

## 2. Plan the work

1. **Issues** > **New issue**: `Add expiring soon by license type report`, label **enhancement**, assign yourself.
2. Optional: **Projects** tab > **New project** > **Board**, then add the issue and move it to **In Progress**.

## 3. Branch, build, commit

```bash
git switch -c <issue-number>-expiring-by-type
```

Create `sql/reports/expiring_soon_by_type.sql`:

```sql
-- Purpose: Active licenses expiring in the next 60 days, by license type.
SELECT
    license_type,
    COUNT(*) AS expiring_count
FROM rpt.active_licenses
WHERE expires_date < DATEADD(day, 60, CAST(GETDATE() AS DATE))
GROUP BY license_type
ORDER BY expiring_count DESC;
```

```bash
git add sql/reports/expiring_soon_by_type.sql
git commit -m "Add expiring soon by type report"
git push -u origin <issue-number>-expiring-by-type
```

## 4. Pull request, checks, merge

1. Open a pull request. Description: `Closes #<issue-number>`.
2. Wait for the green check. If you have a partner, ask for a review.
3. Use the merge drop-down and choose **Squash and merge** > **Confirm**. Delete the branch.
4. The issue closes automatically (and moves to **Done** on your board).

## 5. Publish a release

1. **Code** tab > **Releases** > **Draft a new release**.
2. **Choose a tag** > type `v1.1` > **Create new tag: v1.1 on publish**. Target: `main`.
3. **Generate release notes** - GitHub lists the PRs merged since `v1.0`.
4. **Publish release**.

```bash
git pull --tags
git tag
git lg -10
```

## Done when

- [ ] `v1.0` and `v1.1` tags exist
- [ ] The v1.1 release lists your merged PRs
- [ ] Your issue is closed by the squash-merged PR
