import os
from datetime import datetime, timedelta

from celery import Celery
from celery.schedules import crontab
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from accounting.models import Transaction
from accounting_api import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "accounting_api.settings")

app = Celery("accounting_api")
app.config_from_object("django.conf:settings", namespace="CELERY")


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes every day at 7 a.m.
    sender.add_periodic_task(
        crontab(hour=7),
        send_statistics.s(),
    )


@app.task(bind=True)
def send_statistics():
    users = get_user_model().objects.all()
    for user in users:
        # Select transactions from last day
        transactions = Transaction.objects.filter(
            user__iexact=user, created__gte=datetime.now() - timedelta(days=1)
        )
        transactions_total = 0
        for transaction in transactions:
            transactions_total += transaction.sum

        mail_subject = f"Statistics for {user.username}"
        message = (
            f"Your balance: {user.balance} \n Last day expenses: {transactions_total}"
        )
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
