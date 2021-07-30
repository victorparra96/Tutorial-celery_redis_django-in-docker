from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'sum_random_for_5_seconds': {
        'task': 'sum_random',
        'schedule': timedelta(seconds=5),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}

""" @app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request)) """