from ast import Or
from django.urls import path
from .views import (
    ProfileViewSet,
    CategoryViewSet,
    ProductViewSet,
    OrderViewSet,
    ReadOnlyProfileViewSet,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet, basename="products"),
router.register(r"orders", OrderViewSet),
router.register(r"profiles-protected", ReadOnlyProfileViewSet, basename="read-only-profiles")

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls
