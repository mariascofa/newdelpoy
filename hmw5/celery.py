import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hmw5.settings')

app = Celery('Django', include=[])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def task_test(self):
    return 2 + 2

