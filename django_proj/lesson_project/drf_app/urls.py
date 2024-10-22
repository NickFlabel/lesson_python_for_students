from django.urls import path
from drf_app.views import profile_list_create, profile_detail

urlpatterns = [
    path("profiles/", profile_list_create),
    path("profiles/<int:pk>/", profile_detail),
]
