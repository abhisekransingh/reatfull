from django.db import models
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.IntegerField()
    