#!/usr/bin/env bash

#!/bin/bash

# Set your commit message
commit_message="schedule ai update"

# Set your branch name
branch_name="master"

# Set your GitHub token
github_token="$GH_TOKEN"

# Configure Git
git config user.email "hakurei@asia.com"
git config user.name "hakureii"

# Add changes to the staging area
git add myai.json

# Commit changes
git commit -am "$commit_message"

# Push changes to the specified branch
git push "https://$github_token@github.com/pi-yuno/yuno" "$branch_name"
