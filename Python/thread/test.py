from threading import Thread
import time


def run():
    for i in range(5):
        print(i)
        time.sleep(1)

def main():
    for _ in range(5):
        t1 = Thread(target=run)
        t1.start()
    print("end")

main()