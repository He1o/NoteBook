import redis
import time
from contextlib import contextmanager

class RedisRegionController:
    def __init__(self, redis_host='localhost', redis_port=6379, redis_db=0):
        # 初始化 Redis 连接
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

    @contextmanager
    def acquire_lock(self, lock_name, timeout=3600):
        # 尝试获取锁
        lock = self.redis_client.lock(lock_name, timeout=timeout)
        if lock.acquire(blocking=True):
            print("获取锁")
            try:
                yield
            finally:
                lock.release()
        else:
            print("没拿到")
            raise Exception("Could not acquire lock")

    def start_region(self, region_name):
        key = f"region:{region_name}:running"
        lock_name = f"lock:{region_name}"

        print("开始") 
        with self.acquire_lock(lock_name):
            
            time.sleep(10)
            # 尝试设置键，如果键已存在则返回 False
            if self.redis_client.set(key, "1", nx=True):
                print(f"{region_name} is now running.")
                return True
            else:
                print(f"{region_name} is already running.")
                return False

    def stop_region(self, region_name):
        key = f"region:{region_name}:running"
        lock_name = f"lock:{region_name}"

        with self.acquire_lock(lock_name):
            # 删除键以停止区域
            if self.redis_client.delete(key):
                print(f"{region_name} has stopped running.")
                return True
            else:
                print(f"{region_name} was not running.")
                return False

    def is_region_running(self, region_name):
        key = f"region:{region_name}:running"
        return self.redis_client.exists(key)

# 示例用法
if __name__ == "__main__":
    controller = RedisRegionController()

    # 启动广州区域
    controller.start_region('guangzhou')

    # 启动北京区域
    controller.start_region('beijing')

    # 检查广州区域是否在运行
    print(controller.is_region_running('guangzhou'))  # True

    # 停止广州区域
    controller.stop_region('guangzhou')

    # 检查广州区域是否在运行
    print(controller.is_region_running('guangzhou'))  # False
