#!/bin/bash
if [ -z ${GOOGLEMAPS_API_KEY+x} ]; then echo "GOOGLEMAPS_API_KEY is unset" && exit 1; fi
pip install -r requirements.txt
python app/app.py

