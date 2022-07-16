#!/bin/bash
set -e

# collect static file
python manage.py collectstatic -c --noinput

# migrate database
python manage.py migrate