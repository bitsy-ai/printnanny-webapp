#!/usr/bin/env bash

git config --global user.email "releases@bitsy.ai"
git config --global user.name "Release Automation"
bump2version --current-version "$1"--new-version "$2"

make python-client
git add clients/
git commit -m "🐍 $1 -> $2 python openapi client codegen"
make python-client-release

make rust-client
git add clients/
git commit -m "🦀 $1 -> $2 typescript openapi client codegen"
make rust-client-release

git push origin "$3"