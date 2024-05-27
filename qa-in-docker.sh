#!/usr/bin/env bash

docker build -t adminlte3 .

docker run --rm -v `pwd`:/apps/app -u 1000 adminlte3 bash -c '
echo "
# Generate pui stubs"
# stubgen -o adminlte3/ adminlte3/*.py
# stubgen -o adminlte3/ adminlte3/templatetags/*.py
# stubgen -o adminlte3/admin/ adminlte3/admin/*.py

echo "
# Code formatter"
black .

echo "
# Lint"
ruff .
flake8 --benchmark --doctests  --tee .

echo "
# Static type check"
mypy --warn-unused-configs --python-version 3.9 --show-error-context --show-column-numbers --show-error-end --show-error-codes --pretty --html-report artifacts/statictypecheck --cobertura-xml-report artifacts/statictypecheck --explicit-package-bases adminlte3*

echo "
# PyDoc - Disabled"
# pdoc3 --html -o artifacts/pydocs --config show_source_code=False --force adminlte3*
'
