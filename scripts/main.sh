#!/usr/bin/env bash

# env
BRANCH="train-ai"
ORIGIN="https://$GH_TOKEN@github.com/pi-yuno/yuno.git"


# deps
git config --global "user.email" "hakurei@asia.com"
git config --global "user.email" "hakureii"

pip install -r requirements.txt



function github_update() {
	git pull origin master --rebase false
	git add --all
	git commit -am "schedule ai"
	git push $ORIGIN $BRANCH
}

while [ -f TRUE ]
do
	github_update
	python3 bot.py
done

