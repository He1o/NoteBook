import time
from contextlib import contextmanager


# print (t)                       #原始时间数据
# print (int(t))                  #秒级时间戳
# print (int(round(t * 1000)))    #毫秒级时间戳
# print (int(round(t * 1000000))) #微秒级时间戳
@contextmanager
def timer(name):
    
    start = int(round(time.time() * 1000))
    print(start)
    yield
    end = int(round(time.time() * 1000))
    print(end)
    print('{} COST:{}'.format(name, end - start))