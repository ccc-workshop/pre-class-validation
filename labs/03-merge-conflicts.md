# Lab 3 - Merge conflicts (45 minutes)

**Goal:** see why conflicts happen and resolve them two ways - in the browser and in VS Code.

## Part A - A planned conflict on GitHub (everyone together)

Everyone changes **the same line** of `docs/refresh-schedule.md`. The first PR to merge wins; everyone else resolves a conflict.

1. In the shared repo on GitHub, open `docs/refresh-schedule.md` > pencil icon (**Edit**).
2. Change the line `Nightly refresh time: 02:00 ET` to a different time, for example `Nightly refresh time: 03:15 ET`.
3. **Commit changes...** > choose **Create a new branch** named `<your-handle>/refresh-time` > **Propose changes** > **Create pull request**.
4. Wait for the instructor to merge one PR.
5. Your PR now says **This branch has conflicts that must be resolved**. Click **Resolve conflicts**.
6. In the editor you see the conflict markers:

   ```text
   <<<<<<< <your-handle>/refresh-time
   Nightly refresh time: 03:15 ET
   =======
   Nightly refresh time: 04:00 ET
   >>>>>>> main
   ```

7. Keep the line the team agrees on, delete the three marker lines, click **Mark as resolved** > **Commit merge**.
8. Close your PR with a comment that `main` already has the agreed time. (In real work you would merge it if your version is the one to keep.)

## Part B - Resolve a conflict locally in VS Code

The repo has a branch called `practice/merge-conflict` that changed the `status` row of the data dictionary differently from `main`.

```bash
cd ~/github-workshop/ccc-data-team-lab
git switch main
git pull
git switch -c <your-handle>/conflict-practice origin/practice/merge-conflict
git merge main
```

Git stops with:

```text
CONFLICT (content): Merge conflict in docs/data-dictionary.md
Automatic merge failed; fix conflicts and then commit the result.
```

1. `git status` - the file is listed under *Unmerged paths*.
2. Open `docs/data-dictionary.md` in VS Code. Above the conflict choose **Accept Current**, **Accept Incoming**, **Accept Both**, or edit by hand. A good resolution combines both:

   `| status | VARCHAR(20) | Active, Pending, Suspended or Expired; trimmed and uppercased before reporting |`

3. Make sure no `<<<<<<<`, `=======` or `>>>>>>>` lines are left.
4. Finish the merge and push your branch:

   ```bash
   git add docs/data-dictionary.md
   git commit --no-edit
   git lg -8
   git push -u origin <your-handle>/conflict-practice
   ```

**Tip:** if a merge goes wrong, `git merge --abort` puts everything back the way it was before `git merge`.

## Done when

- [ ] You resolved a conflict in the browser (Part A)
- [ ] You resolved a conflict locally and pushed your branch (Part B)
