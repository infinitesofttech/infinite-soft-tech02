#!/usr/bin/env bash
set -o errexit

cd infinity

echo "Installing Python dependencies..."
python -m pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput --verbosity 2

echo "Running database migrations..."
python manage.py migrate

echo "Build completed successfully!"
