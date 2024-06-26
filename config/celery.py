import os
from celery import Celery
import eventlet

# eventlet.monkey_patch()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Автообнаружение задач в различных Джанго приложениях.
app.autodiscover_tasks()
