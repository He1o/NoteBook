
"""FLASK HTTP"""
import time
from celery import Celery


from .redis_client import RedisRegionController


app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def write_region(region):
    print("start")
    con = RedisRegionController()
    con.start_region(region)
    time.sleep(5)
    print("stop")
