from django.db.models.signals import post_save
from django.dispatch import receiver
from booking_service.models import Room, Booking
from django.dispatch import Signal

@receiver(post_save, sender=Room)
def created(sender, instance, created: bool, **kwargs):
    if created:
        print(f"instance {instance} of model {sender} was created")
    else:
        print(f"instance {instance} of model {sender} was updated")

# Room(name="room")

my_signal = Signal()

def my_signal_subscriber(sender, **kwargs):
    print("my signal was sent")

my_signal.connect(my_signal_subscriber)
