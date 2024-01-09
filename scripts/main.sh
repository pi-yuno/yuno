#!/usr/bin/env bash

# env
BRANCH="master"
ORIGIN="https://$GH_TOKEN@github.com/pi-yuno/yuno.git"

pip install -r requirements.txt



function github_update() {
	git pull --rebase true
	git add --all
	git commit -am "schedule ai"
	git push $ORIGIN $BRANCH
}

while [ -f TRUE ]
do
	github_update
	python3 bot.py
done

