from django.contrib import admin
from .models import Department,Student

# Register your models here.


class Departmentadmin(admin.ModelAdmin):
    list_display=['dname','did']
admin.site.register(Department,Departmentadmin)



class Studentadmin(admin.ModelAdmin):
    list_display=['sname','sid']
admin.site.register(Student,Studentadmin)




