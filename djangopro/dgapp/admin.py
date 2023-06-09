from django.contrib import admin
from .models import Place,Restrurant
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display=["name"]
admin.site.register(Place,PlaceAdmin)

class RestrurantAdmin(admin.ModelAdmin):
    list_display=["rname"]
admin.site.register(Restrurant,RestrurantAdmin)



