import requests
from concurrent.futures import ThreadPoolExecutor


# 发送GET请求

post_dict = {
    "data": 2,
    "last": 4,
    "region": "guangzhou"
}

def quest(post_dict):
    response = requests.post('http://127.0.0.1:8001/leviathan/gen', json=post_dict)
    print(response)


_THREAD_POOL = ThreadPoolExecutor(max_workers=20)
for i in range(4):
    post_dict = {
    "data": 2,
    "last": 4,
    "region": "guangzhou"
    }

    post_dict["version"] = i
    _THREAD_POOL.submit(quest, post_dict)
