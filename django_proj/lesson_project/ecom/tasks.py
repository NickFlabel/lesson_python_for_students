from celery import shared_task
import time

@shared_task
def long_task():
    time.sleep(10)
    print("long task has been performed")
