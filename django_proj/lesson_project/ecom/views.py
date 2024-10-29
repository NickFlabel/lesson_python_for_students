from rest_framework import generics
from rest_framework.response import Response
from .models import Category, Product, Profile, Order
from .serializers import (
    CategorySerializer,
    ProductInSerializer,
    ProductOutSerializer,
    ProductPriceFilterSerializer, 
    ProfileSerializer, 
    OrderCreateSerializer, 
    OrderOutSerializer,
)
from rest_framework import viewsets
from rest_framework.decorators import action
from .paginators import CustomPageNumberPagination

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ReadOnlyProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=["get"])
    def get_products(self, request, pk):
        products = Product.objects.filter(category_id=pk)
        serializer = ProductOutSerializer(products, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH", "POST"]:
            return OrderCreateSerializer
        return OrderOutSerializer


class ProductViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH", "POST"]:
            return ProductInSerializer
        return ProductOutSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        if self.request.method in ["PUT", "PATCH", "POST", "DELETE"]:
            return queryset
        serializer = ProductPriceFilterSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)

        min_price = serializer.validated_data.get("min_price")
        max_price = serializer.validated_data.get("max_price")

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)
        return queryset

# Методы внутри ViewSet
# 1) list - метод, исполняемый при GET /products/
# 2) retrieve - метод, исполняемый при GET /products/<pk>/
# 3) create - метод, исполняемы при POST /products/
# 4) update - метод, исполняемый при PUT /products/<pk>/
# 5) partial_update - метод, исполняемый PATCH /products/<pk>/
# 6) destroy - метод, исполняемый при DELETE /products/<pk>/



# class ProfileListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer


# class ProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
    # lookup_url_kwarg = "pk" - наименование url-параметра
    # serializer(data=request.data) -> create()
    # serializer(instance: Model, data=request.data) -> update()



# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     pagination_class = CustomPageNumberPagination

#     def get_serializer_class(self):
#         if self.request.method == "POST":
#             return ProductInSerializer
#         return ProductOutSerializer

#     def get_queryset(self):
#         queryset = Product.objects.all()
#         serializer = ProductPriceFilterSerializer(data=self.request.query_params)
#         serializer.is_valid(raise_exception=True)

#         min_price = serializer.validated_data.get("min_price")
#         max_price = serializer.validated_data.get("max_price")

#         if min_price is not None:
#             queryset = queryset.filter(price__gte=min_price)
#         if max_price is not None:
#             queryset = queryset.filter(price__lte=max_price)
#         return queryset


# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()

#     def get_serializer_class(self):
#         if self.request.method in ["PUT", "PATCH"]:
#             return ProductInSerializer
#         return ProductOutSerializer






# class OrderListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Order.objects.all()

#     def get_serializer_class(self):
#         if self.request.method in ["PUT", "PATCH", "POST"]:
#             return OrderCreateSerializer
#         return OrderOutSerializer


# class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
    
#     def get_serializer_class(self):
#         if self.request.method in ["PUT", "PATCH"]:
#             return OrderCreateSerializer
#         return OrderOutSerializer
