#!/usr/bin/env bash

set -eu

bump2version --current-version $(cat version.txt) --new-version "$1" patch

make ts-client
git add clients/
git commit --amend --no-edit

make python-client
git add clients/
git commit --amend --no-edit

make rust-client
git add clients/
git commit --amend --no-edit

make js-client-release
make python-client-release
make rust-client-release

git push
git push --tags