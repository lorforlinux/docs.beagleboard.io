#!/bin/bash

env

if [ "$CI_COMMIT_BRANCH" == "$CI_DEFAULT_BRANCH" ]; then

rm -rf public
sphinx-build -b html . public/latest/
sphinx-build -M latexpdf . public/latest/
mv public/latest/latex/beagleboard-docs.pdf public/latest/
rm -rf public/latest/latex
cat <<HERE > public/index.html
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url='latest/'" />
  </head>
  <body>
    <p>Please follow <a href="latest/">this link</a>.</p>
  </body>
</html>
HERE

elif [ "$CI_COMMIT_BRANCH" != "" ]; then

sphinx-build -b html . public/$CI_COMMIT_BRANCH/
sphinx-build -M latexpdf . public/$CI_COMMIT_BRANCH/
mv public/$CI_COMMIT_BRANCH/latex/beagleboard-docs.pdf public/$CI_COMMIT_BRANCH/
rm -rf public/$CI_COMMIT_BRANCH/latex

elif [ "$CI_COMMIT_TAG" != "" ]; then

export GIT_BRANCH=$(git branch -a --contains tags/$CI_COMMIT_TAG | grep origin | sed 's/.*origin\///')
sphinx-build -b html . public/$GIT_BRANCH/
sphinx-build -M latexpdf . public/$GIT_BRANCH/
mv public/$GIT_BRANCH/latex/beagleboard-docs.pdf public/$GIT_BRANCH/beagleboard-docs-$CI_COMMIT_TAG.pdf
ln -s public/$GIT_BRANCH/latex/beagleboard-docs-$CI_COMMIT_TAG.pdf public/$GIT_BRANCH/beagleboard-docs.pdf
rm -rf public/$GIT_BRANCH/latex

fi

