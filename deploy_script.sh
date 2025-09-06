#!/bin/bash
cd DjangoMarketplace
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
pkill -f "manage.py runserver"
nohup python3 manage.py runserver 0.0.0.0:8000 &