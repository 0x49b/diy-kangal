#!/bin/bash

git add docs/

mkdocs build
git add site/

git commit -m "updated docs" docs/ site/

git push
