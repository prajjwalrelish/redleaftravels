from __future__ import absolute_import,unicode_literals

import os
from celery import Celery, app
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE','RedLeafTravels.settings')
app = Celery('RedLeafTravels')
app.conf.enable_utc = False

app.conf.update(timezone ='Asia/Kolkata' )

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# celry beat settings
# app.conf.beat_schedule = {
#     'task_name' : {
#         'task' : 'home.tasks.email_send',
#         'schedule' : crontab(hour=11,minute=8),
#         # 'args': (2,2),
#     },
# }

@app.task(bind = True)
def debug_task(self):
    print(f'Request: {self.request!r}')
