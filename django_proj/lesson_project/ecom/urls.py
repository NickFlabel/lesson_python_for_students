from django.urls import path
from .views import (
    ProductRetrieveUpdateDestroyAPIView, 
    ProductListCreateAPIView,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
    ProfileViewSet,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)

urlpatterns = [
    path("products/", ProductListCreateAPIView.as_view(), name="product-list-create"),
    path("products/<int:pk>", ProductRetrieveUpdateDestroyAPIView.as_view(), name="product-detail"),

    path("orders/", OrderListCreateAPIView.as_view(), name="order-list-create"),
    path("orders/<int:pk>", OrderRetrieveUpdateDestroyAPIView.as_view(), name="order-detail")
]

urlpatterns += router.urls
