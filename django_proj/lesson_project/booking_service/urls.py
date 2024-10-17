from django.urls import path
from booking_service.views import (
    room_list, room_detail, create_room, 
    update_room, delete_room, check_availability, register
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("rooms/", room_list, name="room_list"),
    path("rooms/<int:room_id>", room_detail, name="room_detail"),
    path("room_create/", create_room, name="room_create"),
    path("room_update/<int:room_id>", update_room, name="room_update"),
    path("room_delete/<int:room_id>", delete_room, name="room_delete"),
    path("check_availability/", check_availability, name="check_availablity"),
    path("register/", register, name="registration"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
