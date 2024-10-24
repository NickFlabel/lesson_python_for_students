from rest_framework import generics
from .models import Product, Profile, Order
from .serializers import (
    ProductInSerializer,
    ProductOutSerializer, 
    ProfileSerializer, 
    OrderCreateSerializer, 
    OrderOutSerializer
)

# Create your views here.


class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # lookup_url_kwarg = "pk" - наименование url-параметра


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProductInSerializer
        return ProductOutSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return ProductInSerializer
        return ProductOutSerializer
    

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OrderCreateSerializer
        return OrderOutSerializer


class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return OrderCreateSerializer
        return OrderOutSerializer
