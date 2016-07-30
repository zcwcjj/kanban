from celery import task

import time

@task()
def add(x, y):
    time.sleep(10)
    print("----------------start!")
    return x + y
