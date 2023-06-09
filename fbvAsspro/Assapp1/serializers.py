from rest_framework import serializers
from .models import Course


class CourseSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    price=serializers.FloatField()
    discount=serializers.IntegerField()
    duration=serializers.DurationField()

    def create(self, validated_data):
        return Course.objects.create(**validated_data)
    
    def update(self, cource, validated_data):
        cource.name=validated_data.get("name")
        cource.price=validated_data.get("price")
        cource.discount=validated_data.get("discount")
        cource.duration=validated_data.get("duration")
        cource.save()
        return cource