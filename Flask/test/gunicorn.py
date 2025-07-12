#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The gunicorn config."""
import os

log_dir = '/Users/didi/Code/NoteBook/Flask/log'
if not os.path.exists(log_dir):
  os.mkdir(log_dir)

debug = True
loglevel = 'debug'
bind = '0.0.0.0:8001'
pidfile = f'{log_dir}/gunicorn.pid'
logfile = f'{log_dir}/debug.log'
errorlog = f'{log_dir}/error.log'
accesslog = f'{log_dir}/access.log'

# 启动的进程数
workers = 5
worker_connections = 1

x_forwarded_for_header = 'X-FORWARDED-FOR'