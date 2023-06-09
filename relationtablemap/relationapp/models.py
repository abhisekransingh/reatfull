from django.db import models

# Create your models here.


class Department(models.Model):
    dname=models.CharField(max_length=100)
    did=models.IntegerField()


class Student(models.Model):
    sname=models.CharField(max_length=100)
    sid=models.IntegerField()
    #department=models.OneToOneField(Department,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='student')

def m1(a):
    print(a)


if __name__ == "__main__":
    m1(10)