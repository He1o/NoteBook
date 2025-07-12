from flask import Flask
app = Flask(__name__)
import time
from threading import Thread
import time
print("start")

def run():
    for i in range(5):
        print(i + 100)
        time.sleep(5)


@app.route('/', methods=["POST"])
def hello_world():
    for _ in range(5):
        t1 = Thread(target=run)
        t1.start()
    print("stop")
    return 'Hello World'

if __name__ == '__main__':
    app.run(port=8001)

