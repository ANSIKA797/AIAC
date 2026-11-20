#!/usr/bin/env bash
set -e
REPO=$(mktemp -d)
cd "$REPO"
git init -b main
git config user.name "Adagiri Ansika"
git config user.email "ansika@sru.edu"

echo 'print("Initial v1")' > app.py
git add app.py
git commit -m "chore: initial app setup"

git checkout -b feature/ai-enhancements
echo 'print("Enhanced v2 with validation")' > app.py
git add app.py
git commit -m "feat: add AI-assisted input validation"

git checkout main
git merge --no-ff feature/ai-enhancements -m "merge: integrate feature/ai-enhancements"
git log --oneline --graph --all
rm -rf "$REPO"
