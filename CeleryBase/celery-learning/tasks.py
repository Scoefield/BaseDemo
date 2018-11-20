from celery import Celery
import time


broker = "redis://root:123456@192.168.1.100:6379/1"
backend = "redis://root:123456@192.168.1.100:6379/2"
app = Celery("my_task", broker=broker, backend=backend)

@app.task
def add(x, y):
    print("Enter fun...")
    time.sleep(4)
    return x + y