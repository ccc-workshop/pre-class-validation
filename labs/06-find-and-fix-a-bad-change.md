# Lab 6 - Find and fix a bad change: diff, bisect, blame, revert (45 minutes)

**Scenario:** the dashboard team says the *active licenses* view started including **pending** licenses some time in the last two weeks. Twelve commits landed on the `bisect-practice` branch in that time. Which one broke it, who made it, and how do we undo it safely?

**Where:** your own copy (`~/github-workshop/my-lab`), Git Bash.

## 1. Confirm the problem

```bash
cd ~/github-workshop/my-lab
git switch bisect-practice
sh scripts/check_active_view.sh
git log --oneline main..bisect-practice
```

The check prints `BAD`. On `main` it is fine:

```bash
git switch main
sh scripts/check_active_view.sh
git switch bisect-practice
```

## 2. Look at what changed (diff)

```bash
git diff main...bisect-practice --stat
git diff main...bisect-practice -- sql/views/active_licenses.sql
```

(Three dots = only what changed on `bisect-practice` since it branched off `main`.)

You can see the bad line - but not *which* commit added it or *why*. With hundreds of commits, reading diffs does not scale. Enter `git bisect`.

## 3. Bisect by hand

```bash
git bisect start
git bisect bad                 # the current commit is bad
git bisect good main           # main is known good
```

Git checks out a commit halfway between. Test it and tell Git the answer:

```bash
sh scripts/check_active_view.sh
git bisect good                # if it printed GOOD
# or
git bisect bad                 # if it printed BAD
```

Repeat until Git prints **`<sha> is the first bad commit`** (about 4 rounds for 12 commits). Note the sha, author and message.

```bash
git bisect reset               # go back to where you started
```

## 4. Bisect automatically

Let Git run the check for you:

```bash
git bisect start bisect-practice main
git bisect run sh scripts/check_active_view.sh
git bisect reset
```

Same answer, no typing. Any script that exits `0` for good and `1` for bad works - a unit test, a SQL check, a row count.

## 5. Who changed that line, and why (blame)

```bash
git blame sql/views/active_licenses.sql
git blame -L '/WHERE/,+2' sql/views/active_licenses.sql
git show <sha>
```

The commit message says *Tidy active licenses view formatting* - but it changed behavior. That is why small, honest commits and reviews matter.

In VS Code you can also see blame inline: open the file and hover the line, or use the **Timeline** view in the Explorer.

## 6. Undo it safely (revert)

`git revert` adds a **new** commit that undoes the bad one. History is not rewritten, so it is safe on shared branches.

```bash
git revert <sha> --no-edit
sh scripts/check_active_view.sh   # GOOD again
git lg -5
```

## 7. Ship the fix through a pull request

```bash
git push -u origin bisect-practice
```

Open a pull request from `bisect-practice` into `main`. The checks run, and when they are green, **Merge pull request**.

## Done when

- [ ] You found the first bad commit by hand and with `git bisect run`
- [ ] You used `git blame` to find who changed the line
- [ ] You reverted the commit and merged the fix through a PR
