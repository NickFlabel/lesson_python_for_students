from tkinter import image_names
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from booking_service.models import Room
from booking_service.forms import RoomForm, ConfirmDeleteForm, AvailabilityForm, UserRegistrationForm
from django.db.models import Count, Avg
from django.contrib.auth import login
from booking_service.utils import get_available_rooms
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.views import View
from django.db.transaction import atomic
from booking_service.signal import my_signal
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse

# Create your views here.


# def mock_user_required(request, view):
#     if request.user:
#         return view(request)

# Авторизация во view-функциях:
# @login_required - проверяет, что пользователь вошел в сеть
# @permission_required - проверяет, что пользователь обладает правами, переданными в качестве аргумента в декоратор
# @user_passes_test(func: Callable) - проверяет пользователя, прокидывая его в качестве первого аргумента в Callable-объект, передаваемый в декоратор


# class RoomListView(View):
#     # dispatch() - берет метод запроса и ищет соответствующий метод в классе-контроллере
#     # setup()
#     # as_view()
#     def get(self, request):
#         all_rooms = Room.objects.annotate(booking_count=Count("booking"))
#         average_price = Room.objects.aggregate(Avg("price"))
#         context = {
#             "rooms": all_rooms,
#             "avg_price": average_price["price__avg"]
#         }
#         return render(request, "booking_service/room_list.html", context)


# Авторизация в классах:
# LoginRequiredMixin - миксин для того, чтобы проверять, что пользователь, сделавший запрос, вошел в сеть
# PermissionRequiredMixin - миксин для проверки прав пользователя, требует определения параметра permission_required
# UserPassesTestMixin - миксин, котоырй требует определения метода test_func. В случае возвращение True пропускает пользователя и наоборот

class RoomListView(PermissionRequiredMixin, ListView):
    model = Room
    permission_required = "booking_service.view_room"
    # context_object_name = "rooms"
    # template_name: str = "booking_service/room_list.html"

    def get_queryset(self): # запрос в БД. self.model.objects.all()
        my_signal.send("My sender")
        return self.model.objects.annotate(booking_count=Count("booking"))

    def get_context_data(self, **kwargs) -> dict: # формирование контекста
        context = super().get_context_data(**kwargs)
        context["avg_price"] = self.model.objects.aggregate(Avg("price"))["price__avg"]
        return context


class RoomDetailView(DetailView):
    model = Room
    pk_url_kwarg: str = "room_id" # default - "pk"

    # def get_object(self, queryset):
    #     return self.get_queryset().get(pk=self.object_id)


class RoomCreateView(CreateView):
    model = Room
    form_class = RoomForm
    # fields = "__all__"
    success_url = reverse_lazy("room_list")
    template_name: str = "booking_service/room_form.html" # default: room_create.html


class RoomUpdateView(UpdateView):
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy("room_list")
    template_name: str = "booking_service/room_form.html"
    pk_url_kwarg: str = "room_id"


class RoomDeleteView(DeleteView):
    model = Room
    template_name: str = "booking_service/room_form.html"
    success_url = reverse_lazy("room_list")
    pk_url_kwarg: str = "room_id"


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

@atomic
def create_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("room_list")
    else:
        form = RoomForm(initial={"price": 100})
    return render(request, "booking_service/room_form.html", {"form": form})


def update_room(request, room_id): # __call__(request)
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
    # cookies = request.COOKIES
    my_cookie = request.get_signed_cookie("my_cookie")
    print(my_cookie)
    available_rooms = None
    form = AvailabilityForm(request.GET or None) # http://mysite/my_urs?my_var=1 -> my_var - GET-параметр
                                                # curl -X POST http://example.com -d "param1=value1& /<id>/"

    if form.is_valid():
        start_date = form.cleaned_data["start_date"]
        end_date = form.cleaned_data["end_date"]

        available_rooms = get_available_rooms(start_date, end_date)
    
    response = render(request, "booking_service/check_availability.html", {"form": form, "available_rooms": available_rooms})
    # response.set_cookie("my_cookie", "10")
    response.set_signed_cookie("my_cookie", "10")
    return response


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


def get_json_rooms(request):
    objects = Room.objects.all()

    data = [{"id": obj.id, "name": obj.name} for obj in objects]

    return JsonResponse(data, safe=False)
