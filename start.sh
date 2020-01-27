#!/bin/bash
cd /app
#/usr/local/bin/gunicorn -b :5000 --access-logfile - --error-logfile - wsgi:app
gunicorn -c /etc/gunicorn.conf.py wsgi:app