from django.db.models import Q
from booking_service.models import Room, Booking

def get_available_rooms(start_date, end_date):
    conflicting_bookings = Booking.objects.filter(Q(start_time__lte=end_date) & Q(end_time__gte=start_date))

    available_rooms = Room.objects.exclude(id__in=conflicting_bookings.values("room_id"))

    return available_rooms
