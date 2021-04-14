#!/bin/bash

set -ex

test_id=$(uuidgen)
directory_name="fastapi-cookiecutter-test_$test_id"
current_path="$(pwd)"

(cd /tmp && cookiecutter --no-input "$current_path" app_name="FastAPI+Cookiecutter test $test_id" directory_name="$directory_name" project_slug="fastapi_cookiecutter_test")

set +ex
(cd "/tmp/$directory_name" && pytest -sv .)
test_exit_code=$?

set -x
rm -r "/tmp/$directory_name"
exit $test_exit_code
