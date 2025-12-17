#!/url/bin/env bash
set -o errexit

pip install -r reqirements.txt
python manage.py collectstatic --no-input
python manage.py migrate