from rest_framework import permissions
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
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet, basename="products"),
router.register(r"orders", OrderViewSet),
router.register(r"profiles-protected", ReadOnlyProfileViewSet, basename="read-only-profiles")

schema_view = get_schema_view(
    openapi.Info(
        title="ecom app",
        default_version="v1",
        description="Учебный проект",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc-ui"),
]

urlpatterns += router.urls
