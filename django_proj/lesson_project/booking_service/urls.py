from django.urls import path, re_path
from booking_service.views import room_list, room_detail

urlpatterns = [
    path("rooms/", room_list, name="room_list"),
    path("rooms/<int:room_id>", room_detail, name="room_detail"),
]
