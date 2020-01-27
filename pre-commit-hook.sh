#!/bin/bash
autopep8 --in-place ./**/*.py
pylint ./**/*.py
exit $?