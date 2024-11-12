from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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
from .permissions import IsOwnerOrAdmin
import logging
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .tasks import long_task

logger = logging.getLogger("ecom")

# Create your views here.

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated] # Требует чтобы пользователь прислал свой валидный токен


class ReadOnlyProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Требует токена только на POST, PUT, PATCH, DELETE

    def list(self, request, *args, **kwargs):
        logger.info(f"Request with method GET was made by user {request.user}")
        long_task.delay() # Отправка задачи через брокер сообщений в celery
        subject = "Тема письма"
        from_email = "admin@admin.com"
        to = "my_mail@mail.com"
        text = "Текст"
        html_content = render_to_string("email_template.html", {"content": text})

        msg = EmailMultiAlternatives(subject, text, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        logger.debug("DEBUG MESSAGE")
        return super().list(request, *args, **kwargs)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=["get"], url_path='comments/<int:comment_id>/')
    @swagger_auto_schema(
        operation_description="Отдает все товары какой-либо категории",
        responses={200: ProductOutSerializer(many=True)}
    )
    def get_products(self, request, pk, comment_id):
        products = Product.objects.filter(category_id=pk)
        serializer = ProductOutSerializer(products, many=True)
        return Response(serializer.data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsOwnerOrAdmin]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH", "POST"]:
            return OrderCreateSerializer
        return OrderOutSerializer


class ProductViewSet(viewsets.ModelViewSet):
    pagination_class = CustomPageNumberPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter("max_price", openapi.IN_QUERY, description="Максимальная цена", type=openapi.TYPE_INTEGER),
            openapi.Parameter("min_price", openapi.IN_QUERY, description="Максимальная цена", type=openapi.TYPE_INTEGER)
        ],
        operation_description="Отдает все товары",
        responses={200: ProductOutSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=ProductInSerializer,
        responses={201: ProductOutSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

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
