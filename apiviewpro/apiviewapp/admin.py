from django.contrib import admin
from .models import Employee
# Register your models here.

class Adminmodel(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(Employee,Adminmodel)
