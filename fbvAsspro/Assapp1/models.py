from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    discount=models.IntegerField()
    duration=models.DurationField()
    def __str__(self):
        return self.name
