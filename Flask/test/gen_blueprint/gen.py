
"""FLASK HTTP"""
import json
import time
from celery import Celery
from flask import request

from . import gen_blue

import multiprocessing


from celery_app.celery_app import write_region


@gen_blue.route("/gen", methods=["POST"])
def generate_process():
  """The entrance of the request."""
  start = time.time()
  params = json.loads(request.get_data())
  print(params)
  write_region.delay(params["region"])
  end = time.time()
  return {'cost': str(start) + '_' + str(end)}
