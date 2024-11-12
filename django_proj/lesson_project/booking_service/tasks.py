from django.core.mail import send_mail
from django.core.signing import Signer
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from celery import shared_task

signer = Signer()

@shared_task
def send_activation_mail(user_id):
    from django.contrib.sites.models import Site    
    try:
        user = User.objects.get(pk=user_id)
        domain = Site.objects.get_current().domain
        activation_link = f"htpp://{domain}{reverse("activate", kwargs={"token": signer.sign(user_id)})}"

        subject = "Подтверждение регистрации"
        message = f"{activation_link}"

        send_mail(subject, message, "admin@admin.com", [user.email])
    except User.DoesNotExist:
        pass