#!/bin/bash
export VER_LATEST_MAJOR=1
export VER_LATEST_MINOR=0
export VER_LATEST_EXTRA=wip
export PATCHLEVEL=$(date +%Y%m%d)
export VERSION_TWEAK=$(( $(date "+10#%H * 60 + 10#%M") ))

function do_build() {
	cat << EOF > PAGES
PAGES_URL =  $PAGES_URL
PAGES_SLUG = $PAGES_SLUG
GITLAB_USER = $GITLAB_USER
PROJECT_BRANCH = $PROJECT_BRANCH
GITLAB_HOST = $GITLAB_HOST
PROJECT_REPO = $PROJECT_REPO
EOF

	cat << EOF > VERSION
VERSION_MAJOR = $VERSION_MAJOR
VERSION_MINOR = $VERSION_MINOR
PATCHLEVEL = $PATCHLEVEL
VERSION_TWEAK = $VERSION_TWEAK
EXTRAVERSION = $EXTRAVERSION
EOF

	mkdir -p public
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

	echo "**** Updating $PAGES_URL/$VER_DIR ****"

	echo "**** env ****"
	env

	echo "**** make clean ****"
	# Clean build directory
	make clean BUILDDIR=public/$VER_DIR

	echo "**** make html ****"
	# Build and serve HTML
	make html BUILDDIR=public/$VER_DIR
	mv public/$VER_DIR/html/* public/$VER_DIR/

	echo "**** make latexpdf ****"
	# Build, optimize, and serve PDF
	make latexpdf BUILDDIR=public/$VER_DIR

	echo "**** pdfcpu ****"
	if [ "x${CI_RUNNER_EXECUTABLE_ARCH}" == "xlinux/arm64" ] ; then
		echo "**** check and install pdfcpu ****"
		if [ ! -f /usr/local/bin/pdfcpu ] ; then
			wget https://github.com/pdfcpu/pdfcpu/releases/download/v0.4.0/pdfcpu_0.4.0_Linux_arm64.tar.xz
			tar xf pdfcpu_0.4.0_Linux_arm64.tar.xz
			mv -v pdfcpu_0.4.0_Linux_arm64/pdfcpu /usr/local/bin/
		fi
		/usr/local/bin/pdfcpu version
		du -sh public/$VER_DIR/latex/beagleboard-docs.pdf
		/usr/local/bin/pdfcpu optimize public/$VER_DIR/latex/beagleboard-docs.pdf
		du -sh public/$VER_DIR/latex/beagleboard-docs.pdf
	else
		pdfcpu version
		pdfcpu optimize public/$VER_DIR/latex/beagleboard-docs.pdf
	fi
	mv public/$VER_DIR/latex/beagleboard-docs.pdf public/$VER_DIR/

	echo "**** cleanup ****"
	# Cleanup
	rm -rf public/$VER_DIR/doctrees
	rm -rf public/$VER_DIR/latex

	# Update docs.beagleboard.org
	if [ "$CI_COMMIT_TAG" != "" ]; then
		if [ "$VER_DIR" = "latest" ]; then
			cp public/index.html /var/www/docs
		fi
		rsync -v -a --delete public/$VER_DIR/. /var/www/docs/$VER_DIR
	fi
}

if [ "$CI_COMMIT_BRANCH" == "$CI_DEFAULT_BRANCH" ]; then
	export VER_DIR=latest
	export PAGES_URL=$CI_PAGES_URL
	export PAGES_SLUG=$CI_COMMIT_BRANCH
	export GITLAB_USER=$CI_PROJECT_NAMESPACE
	export GITLAB_HOST=$CI_SERVER_HOST
	export PROJECT_BRANCH=$CI_COMMIT_BRANCH
	export PROJECT_REPO=$CI_PROJECT_NAME
	export VERSION_MAJOR=$VER_LATEST_MAJOR
	export VERSION_MINOR=$VER_LATEST_MINOR
	export EXTRAVERSION=$VER_LATEST_EXTRA
	do_build
elif [ "$CI_COMMIT_BRANCH" != "" ]; then
	export VER_DIR=$CI_COMMIT_BRANCH
	export PAGES_URL=$CI_PAGES_URL
	export PAGES_SLUG=$CI_COMMIT_BRANCH
	export GITLAB_USER=$CI_PROJECT_NAMESPACE
	export GITLAB_HOST=$CI_SERVER_HOST
	export PROJECT_BRANCH=$CI_COMMIT_BRANCH
	export PROJECT_REPO=$CI_PROJECT_NAME
	export BRANCH_VER=($(echo $CI_COMMIT_BRANCH | tr "." "\n"))
	export VERSION_MAJOR=${BRANCH_VER[0]}
	export VERSION_MINOR=${BRANCH_VER[1]}
	export EXTRAVERSION=wip
	do_build
elif [ "$CI_COMMIT_TAG" != "" ]; then
	export TAG_SPLIT=($(echo $CI_COMMIT_TAG | tr "-" "\n"))
	export TAG_VER=($(echo ${TAG_SPLIT[0]} | tr "." "\n"))
	export VERSION_MAJOR=${TAG_VER[0]}
	export VERSION_MINOR=${TAG_VER[1]}
	export EXTRAVERSION=${TAG_SPLIT[1]}
	export PAGES_URL=https://docs.beagleboard.org
	export GITLAB_USER=docs
	export GITLAB_HOST=$CI_SERVER_HOST
	export PROJECT_REPO=docs.beagleboard.io
	export GIT_BRANCH=$(git branch -a --contains tags/$CI_COMMIT_TAG | grep origin | tr -d '* ' | sed 's/.*origin\///' | head -n 1)
	export PROJECT_BRANCH=$GIT_BRANCH
	if [ "$GIT_BRANCH" == "$CI_DEFAULT_BRANCH" ]; then
		export VER_DIR=latest
		export PAGES_SLUG=latest
	else
		export VER_DIR=$GIT_BRANCH
		export PAGES_SLUG=$GIT_BRANCH
	fi
	do_build
else
	echo "***** Not on a branch or tag *****"
fi

env

