#!/usr/bin/env bash

PROJECT_NAME="django-adminlte3"
FULL_IMAGE_NAME="kelsoncm/$PROJECT_NAME"

if [[ $# -ne 1 ]]
  then

  if [[ "$#" == 0 ]]
    then
    echo "ERROR: Chooce a option."
  else
    if [[ "$1" != "-l" && "$1" != "-g" && "$1" != "-p" && "$1" != "-a" ]]
      then
      echo "ERROR: Invalid option: $1."
    elif [[ "$#" == 1 ]]
      then
      echo "ERROR: Set a version number."
    fi
  fi

    echo "
DESCRIPTION
       Create a new release $PROJECT_NAME package.
EXAMPLE
       ./release.sh 3.2.0.001
"
    exit
fi

sed "s/lib_version/$1/g" setup.template.py > setup.py
rm -r adminlte3.egg-info dist
python setup.py sdist

# if [[ "$1" == "-p" || "$1" == "-a" ]]
# then
#   echo ""
#   echo "PyPI Hub: Uploading"
#   echo ""
#   docker login
#   docker run --rm -it -v `pwd`:/src $FULL_IMAGE_NAME:latest twine upload dist/$PROJECT_NAME-$2.tar.gz
# fi

echo ""
echo "Done."
