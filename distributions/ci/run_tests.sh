#!/bin/bash

# This script is meant to be called by the "script" step defined in
# .travis.yml. See http://docs.travis-ci.com/ for more details.
# The behavior of the script is controlled by environment variables defined
# in the .travis.yml in the top level folder of the project.

echo "============================"
echo "============================"
echo "Testing Environment:"
python --version
echo "============================"
echo "============================"

if [[ "$COVERAGE" == "true" ]]; then
    nosetests -v --with-coverage --cover-inclusive --cover-branches sources
else
    nosetests -v sources
fi
