from rest_framework import serializers
from restapp.models.models import Employee


class EmployeeSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField(max_length=50)
    phone=serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self, employee, validated_data):
        employee.name=validated_data.get("name")
        employee.email=validated_data.get("email")
        employee.phone=validated_data.get("phone")
        employee.save()
        return employee

class UserSerializers(serializers.Serializer):
    first_name =serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    username=serializers.CharField(max_length=100)


    