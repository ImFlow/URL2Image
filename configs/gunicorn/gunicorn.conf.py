"""
Configuration for gunicorn when running in docker container
"""
# coding=utf-8
# Reference: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py
import os
import multiprocessing

# pylint: disable=invalid-name
_ROOT = "/app"
_VAR = os.path.join(_ROOT, 'var')
_ETC = os.path.join(_ROOT, 'etc')

loglevel = 'info'
errorlog = "-"
accesslog = "-"

bind = '0.0.0.0:5000'

workers = multiprocessing.cpu_count() * 2 + 1

timeout = 3 * 60  # 3 minutes
keepalive = 24 * 60 * 60  # 1 day

capture_output = True
# pylint: enable=invalid-name
