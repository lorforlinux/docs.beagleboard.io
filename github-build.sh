#!/bin/bash -xe

function do_build() {
    echo "**** Building docs: $1 ****"

    cat << EOF > PAGES
PAGES_URL =  $PAGES_URL
GITHUB_USER = $GITHUB_USER
PROJECT_BRANCH = $PROJECT_BRANCH
GITHUB_HOST = $GITHUB_HOST
PROJECT_REPO = $PROJECT_REPO
EOF

    echo "**** make librobotcontrol xml ****"
    if [ -e projects/librobotcontrol/docs ] ; then
        cd projects/librobotcontrol/docs
        doxygen
        cd ../../..
    fi

    if [ "x$1" == "xhtml" ]; then
        mkdir -p public/html
        echo "**** make html ****"
        make html BUILDDIR=public
    fi

    if [ "x$1" == "xpdf" ]; then
        echo "**** make latexpdf ****"
        make latexpdf BUILDDIR=public

        echo "**** cleanup ****"
        mkdir -p public/pdf
        mv public/latex/*.pdf public/pdf
        rm -rf public/doctrees
        rm -rf public/latex
    fi

    if [ "x$1" == "xpublish" ]; then
        echo "**** publishing ****"
        mkdir -p public
        mv public/html/* public/
        mv public/pdf/*.pdf public/

        if [ "$GITHUB_REF_TYPE" == "tag" ]; then
            echo "**** deploying to remote server (optional) ****"
            if [ -n "$PRIVATE_KEY" ]; then
                mkdir -p ~/.ssh
                eval "$(ssh-agent -s)"
                echo "$PRIVATE_KEY" | base64 -d > ~/.ssh/id_rsa
                chmod 600 ~/.ssh/id_rsa
                ssh-add ~/.ssh/id_rsa
                rsync -e 'ssh -p 45 -o "StrictHostKeyChecking=no"' -avP --delete public/. docs@beagleboard.org:/var/www/docs
            fi
        fi
    fi
}

# Detect environment
GITHUB_REF_NAME="${GITHUB_REF##*/}"
GITHUB_USER="${GITHUB_REPOSITORY%/*}"
PROJECT_REPO="${GITHUB_REPOSITORY#*/}"
GITHUB_HOST="github.com"

if [ "$GITHUB_REF_TYPE" == "branch" ]; then
    export PAGES_URL="https://$GITHUB_USER.github.io/$PROJECT_REPO/"
    export PROJECT_BRANCH="$GITHUB_REF_NAME"
    do_build "$1"
elif [ "$GITHUB_REF_TYPE" == "tag" ]; then
    export PAGES_URL="https://docs.beagleboard.org"
    export PROJECT_BRANCH="$(git branch -a --contains tags/$GITHUB_REF_NAME | grep origin | tr -d '* ' | sed 's/.*origin\///' | head -n 1)"
    export SPHINXOPTS="-D todo_include_todos=0"
    do_build "$1"
else
    echo "***** Not on a branch or tag *****"
fi

echo "**** env ****"
env
