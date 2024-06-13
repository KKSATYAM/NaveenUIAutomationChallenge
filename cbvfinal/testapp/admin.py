from django.contrib import admin
from .models import Bear

# Register your models here.

class BearAdmin(admin.ModelAdmin):
    list_display=['name','taste','color','price']

admin.site.register(Bear,BearAdmin)
