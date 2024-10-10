from operator import ge
from django.shortcuts import render, redirect
from booking_service.models import Room
from booking_service.forms import RoomForm
from django.shortcuts import get_object_or_404

# Create your views here.

def room_list(request):
    all_rooms = Room.objects.all()
    context = {
        "rooms": all_rooms
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
    return render(request, "booking_service/create_room.html", {"form": form})
