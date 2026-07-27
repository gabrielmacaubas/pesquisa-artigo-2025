#!/bin/bash

echo "BUILD START" 
python3.9 -m ensurepip 
python3.9 -m pip install -r requirements.txt 
echo "BUILD END"

python3.9 manage.py migrate

echo "Collect Static..."
python3.9 manage.py collectstatic