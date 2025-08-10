#!/bin/sh
source .venv/bin/activate
export $(cat .env | xargs)
python -u -m flask --app main run --debug