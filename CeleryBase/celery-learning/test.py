from celery_app import task1, task2


task1.add.delay(23, 7)
task2.multipl.delay(6, 6)
print("End......")