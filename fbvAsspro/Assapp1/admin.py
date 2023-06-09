from django.contrib import admin
from .models import Course
# Register your models here.

class AdminCource(admin.ModelAdmin):
    list_display=["name","price","discount","duration"]

admin.site.register(Course,AdminCource)


