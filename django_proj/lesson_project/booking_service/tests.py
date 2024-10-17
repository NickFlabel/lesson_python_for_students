from django.urls import reverse
from django.test import TestCase
from booking_service.models import Room, Category

# Create your tests here.

class RoomViewsTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test_category")
        self.room1 = Room.objects.create(name="Room 1", price=100, description="test", category_id=self.category)
        self.room2 = Room.objects.create(name="Room 2", price=150, description="test", category_id=self.category)

    def test_room_list_view(self):
        # Подготовка - Arrange

        # Действие  - Act
        # with self.assertRaises(ValueError): контекстный менеджер для проверки exception'ов
        response = self.client.get(reverse("room_list"))

        # Оценка результата - Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking_service/room_list.html")
        self.assertContains(response, self.room1.name)
        self.assertContains(response, self.room2.name)

    def test_room_detail_view(self):

        response = self.client.get(reverse("room_detail", args=[self.room1.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "booking_service/room_detail.html")
        self.assertContains(response, self.room1.name)

    def test_create_room(self):
        data = {"name": "new_room", "price": 200, "description": "test", "category_id": self.category.id, "availability": True}

        response = self.client.post(reverse("room_create"), data)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Room.objects.filter(name="new_room").exists())

    def test_update_room_view(self):
        data = {"name": "new_room", "price": 200, "description": "test", "category_id": self.category.id, "availability": True}

        response = self.client.post(reverse("room_update", args=[self.room1.id]), data)
        
        self.assertEqual(response.status_code, 302)
        updated_room = Room.objects.get(id=self.room1.id)
        self.assertEqual(updated_room.name, "new_room")

    def test_delete_room_view(self):
        response = self.client.post(reverse("room_delete", args=[self.room1.id]), {"confirm": True})

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Room.objects.filter(id=self.room1.id).exists())
