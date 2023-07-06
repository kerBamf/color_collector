#!/usr/bin/env bash
set -o errexit

pip3 install -r build.sh

python manage.py collectstatic --no-input
python manage.py migrate