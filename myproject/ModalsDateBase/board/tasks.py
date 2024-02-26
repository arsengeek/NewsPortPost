from celery import shared_task
import time

@shared_task
def output():
    time.sleep(10)
    print('hello world')