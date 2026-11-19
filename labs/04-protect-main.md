# Lab 4 - Your own copy, and protecting `main` (45 minutes)

**Goal:** make your own copy of the lab repo, then set rules so nobody (including you) can push straight to `main` or merge broken work.

From today you work in **your own copy**, so you are the admin and can change settings.

## 1. Create your copy from the template

1. Open the shared repo `https://github.com/<training-org>/ccc-data-team-lab`.
2. Click **Use this template** > **Create a new repository**.
3. Tick **Include all branches** (you need the practice branches later).
4. Owner: **your own account**. Name: `ccc-data-team-lab`. Visibility: **Public** (sample data only).
   > Rules on *private* repos need a paid GitHub plan. Public keeps the labs working on a free account.
5. **Create repository**.

## 2. Clone your copy

```bash
cd ~/github-workshop
git clone https://github.com/<your-handle>/ccc-data-team-lab.git my-lab
cd my-lab
git branch -a
```

You should see `remotes/origin/bisect-practice` and `remotes/origin/practice/merge-conflict`.

## 3. Run the checks once

1. In your copy on GitHub, open the **Actions** tab. If asked, click **I understand my workflows, go ahead and enable them**.
2. Select **Data checks** > **Run workflow** > branch `main` > **Run workflow**.
3. Wait for the green tick. (This registers the check name `sql-and-python-checks` so you can require it.)

## 4. Add a ruleset for `main`

1. **Settings** > **Rules** > **Rulesets** > **New ruleset** > **New branch ruleset**.
2. Name: `protect-main`. Enforcement status: **Active**.
3. **Target branches** > **Add target** > **Include default branch**.
4. Tick:
   - **Restrict deletions**
   - **Require a pull request before merging** - required approvals: `0` (use `1` if you have a review partner who is a collaborator)
   - **Require status checks to pass** > **Add checks** > type `sql-and-python-checks` and select it
   - **Block force pushes**
5. **Create**.

> Classic alternative: **Settings** > **Branches** > **Add classic branch protection rule** for `main` with the same options.

## 5. Prove it works - try to push to `main`

```bash
git switch main
echo "" >> README.md
echo "Maintained by <Your Name>." >> README.md
git commit -am "Add maintainer line"
git push
```

The push is **rejected** - the rules require a pull request. Move the commit to a branch instead:

```bash
git switch -c <your-handle>/maintainer-line   # the commit comes with you
git switch main
git reset --hard origin/main                   # put main back where GitHub has it
git switch <your-handle>/maintainer-line
git push -u origin <your-handle>/maintainer-line
```

Do not open the PR yet - we use this branch with CODEOWNERS next.

## 6. Add CODEOWNERS

```bash
mkdir -p .github
git mv CODEOWNERS.example .github/CODEOWNERS
code .github/CODEOWNERS
```

Replace `@your-handle` with your GitHub handle (and `@teammate-handle` with a partner's, or delete it). Save, then:

```bash
git add .github/CODEOWNERS
git commit -m "Add CODEOWNERS"
git push
```

Open a pull request for `<your-handle>/maintainer-line`. On the PR you can see the code owners and the required check. When it is green, **Merge pull request** and **Delete branch**.

> With a partner you could also tick **Require review from Code Owners** in the ruleset. Leave it off when you work alone - you cannot approve your own PR.

## Done when

- [ ] Your own public copy exists with all branches
- [ ] A direct push to `main` is rejected
- [ ] `.github/CODEOWNERS` is on `main` through a PR with a green check
