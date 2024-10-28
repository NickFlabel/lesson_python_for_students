from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_id.username


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"Category: {self.name}, pk: {self.pk}"
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    stock = models.IntegerField()

    def __str__(self) -> str:
        return f"Product: {self.name}, pk: {self.pk}"
    

class Order(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=(
        ('pending', 'Pending'), ("completed", "Completed"), ("canceled", "Canceled")
    ))

    def __str__(self):
        return f"Order {self.pk} by {self.profile_id.user_id.username}"

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.quantity} x {self.product_id.name} for {self.order_id.pk}'
