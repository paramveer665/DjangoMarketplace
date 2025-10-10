#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

# Navigate to your project directory
cd /home/ubuntu/DjangoMarketplace

# Pull the latest changes from the main branch
git fetch origin
git reset --hard origin/main

# Activate virtual environment
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python3 manage.py migrate

# Collect static files
# This is a critical step for production
python3 manage.py collectstatic --noinput

# Deactivate the virtual environment
deactivate

# Restart the Gunicorn service to apply changes
sudo systemctl restart gunicorn

echo "Deployment finished successfully!"