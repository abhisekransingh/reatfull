from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Restrurant(models.Model):
    rname=models.CharField(max_length=100)
    place=models.OneToOneField(Place,on_delete=models.CASCADE,primary_key=True)

