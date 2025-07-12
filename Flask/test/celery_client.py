from celery import Celery

# 创建 Celery 实例
app = Celery('tasks', broker='redis://localhost:6379/0')

# 可选：加载配置
app.conf.update(
    result_backend='redis://localhost:6379/0',
)