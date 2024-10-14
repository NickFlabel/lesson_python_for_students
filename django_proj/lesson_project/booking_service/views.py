from operator import ge
from tkinter import N
from django.shortcuts import render, redirect, get_object_or_404
from booking_service.models import Room
from booking_service.forms import RoomForm, ConfirmDeleteForm, AvailabilityForm
from django.db.models import Q, Count, Avg
from booking_service.utils import get_available_rooms

# Create your views here.

def room_list(request):
    all_rooms = Room.objects.annotate(booking_count=Count("booking"))
    average_price = Room.objects.aggregate(Avg("price"))
    context = {
        "rooms": all_rooms,
        "avg_price": average_price["price__avg"]
    }
    return render(request, "booking_service/room_list.html", context)

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, "booking_service/room_detail.html", {"room": room})

def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm()
    return render(request, "booking_service/room_form.html", {"form": form})


def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm(instance=room)
    return render(request, "booking_service/room_form.html", {"form": form})


def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == "POST":
        form = ConfirmDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data["confirm"]:
            room.delete()
            return redirect("room_list")
    else:
        form = ConfirmDeleteForm()
    return render(request, "booking_service/room_form.html", {"form": form})

# 1) Найти все комнаты, которые свободны от бронирования в определенный период
# 2) Посчитать количество бронирований для каждой комнаты
# 3) Если комната забронирована, она меняет статус


def check_availability(request):
    available_rooms = None
    form = AvailabilityForm(request.GET or None) # http://mysite/my_urs?my_var=1 -> my_var - GET-параметр

    if form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        available_rooms = get_available_rooms(start_date, end_date)
    
    return render(request, "booking_service/check_availability.html", {"form": form, "available_rooms": available_rooms})
