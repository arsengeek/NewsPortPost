import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.broker_connection_retry_on_startup = True

app.conf.beat_shedules = {
    'action_every' : {
        'task': 'signals',
        'schedule' : crontab(day_of_week='monday', hour='8', minute='0'),
        'args' : (),
    }
}
app.autodiscover_tasks() 

