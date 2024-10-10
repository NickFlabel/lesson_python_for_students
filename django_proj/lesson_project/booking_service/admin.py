from django.contrib import admin
from booking_service.models import Category, Room, Booking, Amenity

# Register your models here.

admin.site.register(Category)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Amenity)
