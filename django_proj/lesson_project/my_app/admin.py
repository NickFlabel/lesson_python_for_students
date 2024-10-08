from django.contrib import admin
from .models import BBoard

# Register your models here.

class BBoardAdmin(admin.ModelAdmin):
    search_fields = ("title", "content")
    list_display = ("title", "content", "price", "published")

admin.site.register(BBoard, BBoardAdmin)
