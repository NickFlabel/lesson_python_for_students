from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from my_app.models import BBoard
from my_app.forms import BBoardForm

from datetime import datetime
from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.


def cached_view(request):
    cached_data = cache.get("current_time")
    if cached_data:
        return JsonResponse({"time": cached_data, "cached": True})
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cache.set("current_time", current_time, timeout=30)
    return JsonResponse({"time": current_time, "cached": False})


def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("index.html")
    ads = BBoard.objects.all()
    context = {"ads": ads}
    return HttpResponse(template.render(context, request))


def get_bboard(request: HttpRequest, bboard_id: int) -> HttpResponse:
    bboard = get_object_or_404(BBoard, id=bboard_id)
    return render(request, "get_bboard.html", {"bboard": bboard})

def bboard_create(request: HttpRequest) -> HttpResponse: # HTTP methods - GET, POST, PUT, DELETE, PATCH
    if request.method == "POST":
        form = BBoardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("New bboard has been saved")
    else:
        form = BBoardForm()
    return render(request, "bboard_create.html", {"form": form})

