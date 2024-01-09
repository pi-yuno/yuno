#!/usr/bin/env bash

#!/bin/bash

# Set your commit message
commit_message="<commit_message>"

# Set your branch name
branch_name="<branch_name>"

# Set your GitHub token
github_token="<your_github_token>"

# Configure Git
git config user.email "your.email@example.com"
git config user.name "Your Name"

# Add changes to the staging area
git add .

# Commit changes
git commit -m "$commit_message"

# Push changes to the specified branch
git push origin "$branch_name"
