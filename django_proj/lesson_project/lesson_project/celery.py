from celery import Celery
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lesson_project.settings")

app = Celery("my_task_queue")

app.conf.broker_url = "redis://redis:6379/0"
app.conf.result_backend = "redis://redis:6379/1"

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
