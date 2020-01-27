#!/bin/bash
export GLOBIGNORE="*docu*"
autopep8 --in-place ./**/*.py
pylint ./**/*.py
unset GLOBIGNORE
exit $?