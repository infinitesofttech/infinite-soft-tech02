#!/bin/bash
# Script to collect Django static files

set -e

echo "Collecting static files..."

cd infinity

# Ensure the staticfiles directory exists
mkdir -p staticfiles

# Run Django's collectstatic command
python manage.py collectstatic --noinput --verbosity 2

echo "Static files collected successfully!"
echo "Static files location: $(pwd)/staticfiles"
ls -lah staticfiles/ | head -20
