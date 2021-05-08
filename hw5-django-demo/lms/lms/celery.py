import os
from celery import Celery

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')

app = Celery('lms')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def update_token():
    for user in User.objects.all():
        token = Token.objects.filter(user=user)
        new_key = token[0].generate_key()
        token.update(key=new_key)
