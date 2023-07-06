#!/usr/bin/env bash

pip3 install -r build.sh

python manage.py collectstatic --no-input
python manage.py migrate