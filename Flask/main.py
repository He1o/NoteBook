"""Main for gunicorn."""
from common import thread_pool
from flask import Flask
from generator import Generator
from gen_blueprint import gen_blue
from Flask.common.host_env import get_host_env

app = Flask(__name__)
run_mode = get_host_env()
thread_pool.init()
Generator.init_context(run_mode=run_mode)
Generator.init_logging()
app.register_blueprint(gen_blue)
if __name__ == "__main__":
  run_mode = get_host_env()
  thread_pool.init()
  Generator.init_context(run_mode=run_mode)
  Generator.init_logging()
  app.run()
