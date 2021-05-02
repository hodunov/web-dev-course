import time
from lms.celery import app
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


@app.task
def send_contact_us_email(name, message, email):
    time.sleep(5)
    send_mail(
        f'{name} leave message for you!',
        f"{message}\n email: {email}",
        settings.SUPPORT_EMAIL_FROM,
        [settings.ADMIN_EMAIL],
        fail_silently=False,
    )


@app.task
def delete_old_logs():
    """
    Delete all logs (Logger model) older than 7 days with frequency of once a day (created)
    """
    from core.models import Logger
    Logger.objects.filter(created__lte=timezone.timedelta(days=7)).delete()
