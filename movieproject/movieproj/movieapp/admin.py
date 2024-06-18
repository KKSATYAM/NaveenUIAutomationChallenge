from django.contrib import admin
from movieapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=['name','rollno','dob']

admin.site.register(Student,StudentAdmin)

