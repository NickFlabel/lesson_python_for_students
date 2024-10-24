from django.urls import path
from booking_service.views import (
    check_availability, register, RoomListView, RoomDetailView, RoomCreateView, RoomDeleteView, RoomUpdateView, get_json_rooms
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("rooms/", RoomListView.as_view(), name="room_list"),
    path("rooms/<int:room_id>", RoomDetailView.as_view(), name="room_detail"),
    path("room_create/", RoomCreateView.as_view(), name="room_create"),
    path("room_update/<int:room_id>", RoomUpdateView.as_view(), name="room_update"),
    path("room_delete/<int:room_id>", RoomDeleteView.as_view(), name="room_delete"),
    path("check_availability/", check_availability, name="check_availablity"),
    path("register/", register, name="registration"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("rooms_json/", get_json_rooms)
]
