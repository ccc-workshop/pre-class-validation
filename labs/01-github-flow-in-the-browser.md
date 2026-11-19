# Lab 1 - GitHub Flow in the browser (45 minutes)

**Goal:** take one small change all the way through GitHub Flow without leaving the browser:
issue > branch > commit > pull request > review > merge.

**Where:** the shared repo `https://github.com/<training-org>/ccc-data-team-lab`.
**Who reviews you:** your neighbor in the attendee list (the instructor will pair you).

## 1. Open an issue

1. Go to the **Issues** tab > **New issue**.
2. Title: `Add team page for <your-handle>`
3. Description: one sentence about what you do on the team.
4. On the right, add the label **documentation** and assign yourself.
5. **Create** the issue. Note its number, for example `#7`.

## 2. Create a branch from the issue

1. In the issue, under **Development** on the right, click **Create a branch**.
2. Keep the suggested name (it starts with the issue number) and choose **Create branch**.

## 3. Add your file on the branch

1. Go to the **Code** tab and use the branch drop-down to switch to your new branch.
2. Open the `docs/team` folder > **Add file** > **Create new file**.
3. Name it `<your-handle>.md` and paste:

   ```markdown
   # <Your Name>

   - Role: <your role>
   - I mostly work with: <SQL / Python / reports / Dynamics / ...>
   - One thing I want from this workshop: <...>
   ```

4. **Commit changes...** > keep *Commit directly to the `<branch>` branch* > **Commit changes**.

## 4. Open a pull request

1. Click **Compare & pull request** (or **Pull requests** > **New pull request**, base `main`, compare `<your branch>`).
2. Title: `Add team page for <your-handle>`
3. In the description write `Closes #<issue-number>` - this links the PR and closes the issue when it merges.
4. Under **Reviewers**, request your neighbor.
5. **Create pull request**. Notice the **checks** section - the automated data checks run here too (Day 2 covers them).

## 5. Review your neighbor's pull request

1. Open **Pull requests** and find your neighbor's PR.
2. **Files changed** tab: hover a line, click the blue **+**, and leave a friendly comment.
3. **Review changes** > **Approve** > **Submit review**.

## 6. Merge your own pull request

1. Back on your PR, once approved and the checks are green, click **Merge pull request** > **Confirm merge**.
2. Click **Delete branch**.
3. Open your issue - it is now **Closed** and linked to the PR.

## Done when

- [ ] Your issue is closed by your merged PR
- [ ] `docs/team/<your-handle>.md` is on `main`
- [ ] You left one review on a teammate's PR
