"""
URL configuration for lesson_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# http://127.0.0.1/admin/ -> 'admin/' 
# http://127.0.0.1/my_app/index/ -> my_app/index/ -> index/

urlpatterns = [
    path('admin/', admin.site.urls),
    path("my_app/", include("my_app.urls")),
    path("", include("booking_service.urls")), # urlpatterns += booking_service.urs.urlpatters
    path("api/", include("ecom.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
