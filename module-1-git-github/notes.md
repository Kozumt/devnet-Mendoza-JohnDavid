# Module 1 — Git & GitHub

**Student:** John David Mendoza
**Date:** September 27,2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Git is a tool that tracks changes in your code and provides commands. GitHub, on the hand is an online platform where you can store, share and collaborate on Git projects.

---

## Key vocabulary (in your own words)

- repository:Repository is a folder or a project where your code and its history are kept and managed with Git. I think of it as a locker for my work.

- commit:Commit is a saved checkpoint that records the changes you made to your project. When I make a commit I know what I added.

- branch: Branch is a separate version of a project where you can work on changes without affecting the main version. I use branches to test ideas.
- push / pull: Push is when you send your local changes to GitHub while pull is when you get the latest changes from GitHub to your computer. I always push before I pull to keep everything in sync.

- pull request: Pull request is a request to add your changes from one branch into another branch for someone to review first. I submit a pull request so my teammates can check my work.

- merge conflict: Merge conflict is a problem that happens when Git finds changes, to the same part of a file and does not know which one to keep. I solve merge conflicts by choosing the version.


---

## Walking through what I did

First I created a branch called `notes`. Then I opened the file `nites.md` inside the folder `module-1-git-github` made the edits I needed and ran `git status` to see what had changed. I committed the changes using the message `git commit -m "Key Vocab"`. Next I pushed the branch to GitHub with `git push -u origin notes`. Finally on GitHub I created a Pull Request, from the `functions` branch to the `main` branch so the changes could be reviewed before merging.


```
# paste your actual commands here
git branch notes
git switch notes
git add .
git commit -m "Key Vocab
git push -u origin notes
```

---

## A mistake I made (or one I want to avoid)

The mistake I made is by pushing to the main branch affecting the original one. That's what I want to avoid too.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
