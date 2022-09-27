#!/bin/bash

env

cat << EOF > PAGES
PAGES_URL =  $CI_PAGES_URL
PAGES_SLUG = $CI_COMMIT_BRANCH
GITLAB_USER = $CI_PROJECT_NAMESPACE
PROJECT_BRANCH = $CI_COMMIT_BRANCH
GITLAB_HOST = $CI_SERVER_HOST
PROJECT_REPO = $CI_PROJECT_NAME
EOF

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
# This is just a temporary to test
rsync -a --delete public/latest/. /var/www/docs/latest
cp public/index.html /var/www/docs

elif [ "$CI_COMMIT_BRANCH" != "" ]; then

sphinx-build -b html . public/$CI_COMMIT_BRANCH/
sphinx-build -M latexpdf . public/$CI_COMMIT_BRANCH/
mv public/$CI_COMMIT_BRANCH/latex/beagleboard-docs.pdf public/$CI_COMMIT_BRANCH/
rm -rf public/$CI_COMMIT_BRANCH/latex

elif [ "$CI_COMMIT_TAG" != "" ]; then

# Find which branch has the tag commit
export GIT_BRANCH=$(git branch -a --contains tags/$CI_COMMIT_TAG | grep origin | sed 's/.*origin\///')
cat << EOF > PAGES
PAGES_URL =  $CI_PAGES_URL
PAGES_SLUG = $GIT_BRANCH
GITLAB_USER = $CI_PROJECT_NAMESPACE
PROJECT_BRANCH = $GIT_BRANCH
GITLAB_HOST = $CI_SERVER_HOST
PROJECT_REPO = $CI_PROJECT_NAME
EOF
if [ "$GIT_BRANCH" == "$CI_DEFAULT_BRANCH" ]; then
export GIT_BRANCH=latest
rm -rf public
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
cp public/index.html /var/www/docs
fi
sphinx-build -b html . public/$GIT_BRANCH/
sphinx-build -M latexpdf . public/$GIT_BRANCH/
cp public/$GIT_BRANCH/latex/beagleboard-docs.pdf public/$GIT_BRANCH/beagleboard-docs-$CI_COMMIT_TAG.pdf
cp public/$GIT_BRANCH/latex/beagleboard-docs.pdf public/$GIT_BRANCH/beagleboard-docs.pdf
rm -rf public/$GIT_BRANCH/latex
rsync -a --delete public/$GIT_BRANCH/. /var/www/docs/$GIT_BRANCH

fi
