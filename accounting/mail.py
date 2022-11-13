from django.core.mail import send_mail
from accounting_api.settings import EMAIL_HOST_USER


def send_statistics(subject, message, receivers):
    send_mail(subject, message, EMAIL_HOST_USER, [receivers], fail_silently=False)
