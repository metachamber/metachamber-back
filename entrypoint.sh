#!/bin/bash
set -e

gunicorn metachamber_back.wsgi:application --bind 0.0.0.0:8000