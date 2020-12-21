#!/bin/bash

set -x

change_file () {
  sed -i -e "s|.*VERSION=.*|VERSION=\"$_version\"|g" codecov
  rm codecov-e
}

update_branch () {
  # Checkout maater
  git checkout master
  # Update master
  git pull
}

tag_and_push () {
  # Tag the version change 
  git tag $RELEASE_TAG
  # Push tag
  git push origin $RELEASE_TAG
}

clear_branch () {
  # Clear changes
  git stash
}




cd codecov-bash

clear_branch
update_branch
short_git=$(git rev-parse --short HEAD)
date=`date +%Y%m%d`
RELEASE_TAG="$date-$short_git"
change_file
tag_and_push
