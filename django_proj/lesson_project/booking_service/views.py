from tkinter import image_names
from django.shortcuts import render, redirect, get_object_or_404
from booking_service.models import Room
from booking_service.forms import RoomForm, ConfirmDeleteForm, AvailabilityForm, UserRegistrationForm
from django.db.models import Count, Avg
from django.contrib.auth import login
from booking_service.utils import get_available_rooms
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views import View

# Create your views here.


# def mock_user_required(request, view):
#     if request.user:
#         return view(request)

# Авторизация во view-функциях:
# @login_required - проверяет, что пользователь вошел в сеть
# @permission_required - проверяет, что пользователь обладает правами, переданными в качестве аргумента в декоратор
# @user_passes_test(func: Callable) - проверяет пользователя, прокидывая его в качестве первого аргумента в Callable-объект, передаваемый в декоратор


class RoomListView(View):
    # dispatch() - берет метод запроса и ищет соответствующий метод в классе-контроллере
    # setup()
    # as_view()
    def get(self, request):
        all_rooms = Room.objects.annotate(booking_count=Count("booking"))
        average_price = Room.objects.aggregate(Avg("price"))
        context = {
            "rooms": all_rooms,
            "avg_price": average_price["price__avg"]
        }
        return render(request, "booking_service/room_list.html", context)


@user_passes_test(lambda user: user.is_superuser)
def room_list(request):
    print(request.user)
    print(request.user.get_all_permissions())
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
        form = RoomForm(initial={"price": 100})
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
                                                # curl -X POST http://example.com -d "param1=value1& /<id>/"

    if form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        available_rooms = get_available_rooms(start_date, end_date)
    
    return render(request, "booking_service/check_availability.html", {"form": form, "available_rooms": available_rooms})


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("room_list")
    else:
        form = UserRegistrationForm()
    return render(request, "booking_service/register.html", {"form": form})
