from django.urls import path, re_path
from my_app.views import index, get_bboard, bboard_create

urlpatterns = [
    re_path(r"^index/.+$", index), # index/qwerty
    path("bboards/<int:bboard_id>/", get_bboard, name="get_bboard"),  # bboard/1/
    path("bboards_create/", bboard_create),
    re_path(r"^.+$", index),
]
