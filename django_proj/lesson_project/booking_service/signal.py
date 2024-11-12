from django.db.models.signals import post_save
from django.dispatch import receiver
from booking_service.models import Room
from django.contrib.auth.models import User
from django.dispatch import Signal
from .tasks import send_activation_mail

@receiver(post_save, sender=Room)
def created(sender, instance, created: bool, **kwargs):
    if created:
        print(f"instance {instance} of model {sender} was created")
    else:
        print(f"instance {instance} of model {sender} was updated")

@receiver(post_save, sender=User)
def created(sender, instance, created: bool, **kwargs):
    if created and not (instance.is_staff or instance.is_superuser):
        instance.is_active = False
        instance.save()
        send_activation_mail.delay(instance.pk)
        

# Room(name="room")

# post_save.connect(created)

my_signal = Signal()

def my_signal_subscriber(sender, **kwargs):
    print("my signal was sent")

my_signal.connect(my_signal_subscriber)
