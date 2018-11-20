import time
from celery_app import app


@app.task
def multipl(x, y):
    time.sleep(6)
    return x * y