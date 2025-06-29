#!/bin/bash -xe

function do_build() {
    echo "**** Building docs: $1 ****"

    mkdir -p public

    echo "**** make librobotcontrol xml ****"
    if [ -e projects/librobotcontrol/docs ]; then
        cd projects/librobotcontrol/docs
        doxygen || true
        cd ../../..
    fi

    if [ "x$1" == "xhtml" ]; then
        echo "**** make html ****"
        make html
        mkdir -p public/html
        cp -r _build/html/* public/html/
    fi

    if [ "x$1" == "xpdf" ]; then
        echo "**** make latexpdf ****"
        make latexpdf
        mkdir -p public/pdf
        cp _build/latex/*.pdf public/pdf/
        rm -rf _build/doctrees _build/latex
    fi

    if [ "x$1" == "xpublish" ]; then
        echo "**** publishing ****"
        mkdir -p public
        mv public/html/* public/ || true
        mv public/pdf/*.pdf public/ || true
    fi
}

# GitHub Actions environment fallback
GITHUB_REF_NAME="${GITHUB_REF##*/}"
GITHUB_USER="${GITHUB_REPOSITORY%/*}"
PROJECT_REPO="${GITHUB_REPOSITORY#*/}"
GITHUB_HOST="github.com"

if [ "$GITHUB_REF_TYPE" == "branch" ]; then
    export PAGES_URL="https://${GITHUB_USER}.github.io/${PROJECT_REPO}/"
    export PROJECT_BRANCH="${GITHUB_REF_NAME}"
    do_build "$1"
elif [ "$GITHUB_REF_TYPE" == "tag" ]; then
    export PAGES_URL="https://docs.beagleboard.org"
    export PROJECT_BRANCH="$(git branch -a --contains tags/${GITHUB_REF_NAME} | grep origin | tr -d '* ' | sed 's/.*origin\///' | head -n 1)"
    export SPHINXOPTS="-D todo_include_todos=0"
    do_build "$1"
else
    echo "***** Not on a branch or tag *****"
fi
