#!/usr/bin/env bash

bump2version --current-version "$1"--new-version "$2"
git add -A
git config --global user.email "releases@bitsy.ai"
git config --global user.name "Release Automation"
git push origin "$3"