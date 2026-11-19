# Lab 0 - Setup check (15 minutes)

**Goal:** everyone can sign in to GitHub, run Git, and use VS Code before we start.

> Work in **Git Bash** for every lab. In VS Code: `Terminal > New Terminal`, then pick **Git Bash** from the drop-down next to the `+`.
> To make it the default: `Ctrl+Shift+P` > *Terminal: Select Default Profile* > **Git Bash**.

## 1. Check the tools

```bash
git --version
code --version
```

Both should print a version number. If `code` is not found, open VS Code and run *Shell Command: Install 'code' command in PATH* (`Ctrl+Shift+P`).

Optional (used in some checks): `python --version`. You can do every lab without Python.

## 2. Tell Git who you are

Use the **same email** that is on your GitHub account (or your GitHub no-reply address).

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --global pull.rebase false
git config --global --list
```

## 3. Sign in to GitHub

1. In the browser, sign in at <https://github.com> with the account you will use today.
2. Open the workshop repository your instructor shares: `https://github.com/<training-org>/ccc-data-team-lab`.
   If you get a 404, you have not accepted the invitation yet - check your email or <https://github.com/notifications>.

## 4. Clone the workshop repository

```bash
cd ~
mkdir -p github-workshop && cd github-workshop
git clone https://github.com/<training-org>/ccc-data-team-lab.git
cd ccc-data-team-lab
git status
```

The first time you push or clone a private repo, **Git Credential Manager** opens a browser window. Choose *Sign in with your browser* and approve.

If your network uses a proxy, your instructor will give you the value for:

```bash
git config --global http.proxy http://PROXY_SERVER:PORT
```

## 5. Open the repo in VS Code

```bash
code .
```

## Done when

- [ ] `git config --global --list` shows your name and email
- [ ] `git clone` worked and `git status` says *On branch main*
- [ ] The repo is open in VS Code with a Git Bash terminal
