# Lab 7 - Fix everyday mistakes: amend, reset, reflog, cherry-pick, stash (60 minutes)

**Goal:** practice the "oops" moments in a throwaway repo where nothing can go wrong.

> Rule of thumb: rewrite history (**amend**, **reset**, **rebase**) only on commits you have **not pushed**. For pushed commits, use **revert** (Lab 6).

## 0. Make a scratch repo

```bash
cd ~/github-workshop
mkdir mistakes-lab && cd mistakes-lab
git init
echo "-- Purpose: Licenses by status." > by_status.sql
git add by_status.sql
git commit -m "Add by status qeury"
```

## 1. Typo in the last commit message - amend

```bash
git commit --amend -m "Add by status query"
git log --oneline
```

## 2. Forgot a file in the last commit - amend again

```bash
echo "# Notes" > notes.md
git add notes.md
git commit --amend --no-edit
git show --stat HEAD           # both files are in the one commit
```

## 3. Forgot to create a branch

You made two commits on `main` that should have been on a feature branch.

```bash
printf 'SELECT status, COUNT(*) AS n\n' >> by_status.sql
git commit -am "Start status query"
printf 'FROM stg.licenses\nGROUP BY status;\n' >> by_status.sql
git commit -am "Finish status query"
git lg
```

Move them:

```bash
git branch feature/status-report   # a branch label on your work
git reset --hard HEAD~2            # move main back two commits
git lg                             # main is back; the feature branch has the work
git switch feature/status-report
```

## 4. Reset: soft, mixed, hard

```bash
git reset --soft HEAD~1    # undo the last commit, keep changes STAGED
git status
git commit -m "Finish status query"

git reset HEAD~1           # --mixed (default): undo, keep changes UNSTAGED
git status
git add -A
git commit -m "Finish status query"

git reset --hard HEAD~1    # undo AND throw the changes away - careful!
git log --oneline
cat by_status.sql          # the FROM / GROUP BY lines are gone
```

## 5. Rescue it with the reflog

The reflog is your local "undo history" of where `HEAD` has been.

```bash
git reflog -6
git reset --hard HEAD@{1}  # jump back to before the hard reset
cat by_status.sql          # the lines are back
git log --oneline
```

## 6. Copy one commit to another branch - cherry-pick

```bash
git log --oneline feature/status-report   # copy the sha of "Start status query"
git switch main
echo "Owner: data team" >> notes.md
git commit -am "Add owner to notes"      # main has moved on since the branch was made
git cherry-pick <sha-of-start-status-query>
git lg                                    # same change, new commit (new sha) on main
```

## 7. Park unfinished work - stash

```bash
echo "-- work in progress" >> notes.md
git status
git stash                  # working tree is clean again
git status
git stash list
git stash pop              # bring the change back
git status
git restore notes.md       # throw this scratch change away
```

## Bonus - Clean up commits before a PR with interactive rebase

```bash
git switch feature/status-report
git rebase -i HEAD~2
```

VS Code opens the todo list. Change the second line's `pick` to `squash` (or `s`), save and close. Then edit the combined message, save and close.

```bash
git log --oneline          # two commits squashed into one
```

If anything goes wrong: `git rebase --abort`.

## Done when

- [ ] You amended a message and a forgotten file
- [ ] You moved commits from `main` to a branch
- [ ] You lost a commit with `reset --hard` and got it back with the reflog
- [ ] You cherry-picked and stashed
