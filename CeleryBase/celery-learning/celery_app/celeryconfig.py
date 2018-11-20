from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = "redis://root:123456@10.214.21.135:6379/1"
CELERY_RESULT_BACKEND = "redis://root:123456@10.214.21.135:6379/2"

# UTC
CELERY_TIMEZONE = "Asia/Shanghai"

# 导入指定的模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)


# 定时任务
CELERYBEAT_SCHEDULE = {
    'task1': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (4, 5)
    },
    'task2': {
        'task': 'celery_app.task2.multipl',
        'schedule': crontab(hour=15, minute=11),
        'args': (9, 9)
    }
}
