#!/usr/bin/env bash

set -eu

bump2version --current-version $(cat version.txt) --new-version "$1" patch

make python-client
git add clients/
git commit --amend -m "🐍 $1 python openapi client codegen"
make python-client-release

make rust-client
git add clients/
git commit --amend -m "🦀 $1 typescript openapi client codegen"
make rust-client-release

git push
git push --tags