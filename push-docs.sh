#!/bin/bash

git add docs/

# mkdocs build
# git add site/

git commit -m "updated docs" docs/ 
# git commit -m "updated site" site/ 

git push
