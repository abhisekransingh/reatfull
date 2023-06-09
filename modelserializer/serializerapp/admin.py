from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmon(admin.ModelAdmin):
    list_display=["name","email","phone"]
admin.site.register(Employee,EmployeeAdmon)
