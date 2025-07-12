"""Main for gunicorn."""
from flask import Flask
from gen_blueprint import gen_blue

print("test")


app = Flask(__name__)
app.register_blueprint(gen_blue)
if __name__ == "__main__":
  app.run(port=8001)
