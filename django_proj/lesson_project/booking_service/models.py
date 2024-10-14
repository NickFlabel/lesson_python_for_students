from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Категория комнат
# Комнаты
# Бронирование
# Удобства


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField() # DecimalField(max_digits=5, decimal_places=2) - число с двумя позициями после точки
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Room: {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Category: {self.name}"


class Booking(models.Model): 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Бронирование {self.room_id.name} пользователя {self.user_id.username}"


class Amenity(models.Model):
    name = models.CharField(max_length=100)
    rooms = models.ManyToManyField(Room, related_name="amenities") # От Amenity к Room -> amenity.rooms.all() / от Room к Amenity -> room.amenities.all() by_default = "<название модели>_set"

    def __str__(self) -> str:
        return f"Amenity: {self.name}"


# В моделях django в objects есть метод под название filter, который функционально соответствует использованию WHERE в SQL-запросах

# 1)     all_rooms = Room.objects.filter(price=150) - по значению какого-либо поля модели
# 2)     all_rooms = Room.objects.filter(price=150, name="room") - по значеним нескольких полей
# 3)     all_rooms = Room.objects.filter(name__icontains="room") - проверка на наличие подстроки
# 4)     all_rooms = Room.objects.filter(price__gt=150) - сравнение - > gt, < lt, >= gte, <= lte
# 5)     all_rooms = Room.objects.filter(price__range=(100, 149)) - range значений для какого-то конкретного поля
# 6)     all_rooms = Room.objects.filter(name__startwith="A") - начало строки

# Объект Q (сложные запросы)
# 1)     all_rooms = Room.objects.filter(Q(name="my_room") | Q(name="office")) - два условия с опрератором ИЛИ
# 2)     all_rooms = Room.objects.filter(Q(name="my_room") & ~Q(price__gt=100)) - два условия с оператором И и НЕ (~)


# rooms = Room.objects.raw("SELECT * FROM booking_service_room;") - голый SQL-запрос
# room = Room.objects.select_related("category_id").first() - select_relate - способ создавать запросы с JOIN в Django ORM
