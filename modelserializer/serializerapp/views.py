from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["GET","POST"])
def getORCreate(request):
    if request.method=="GET":
        empdata=Employee.objects.all()
        serializerdata=EmployeeSerializer(empdata,many=True)
        return Response(serializerdata.data)
    elif(request.method=="POST"):
        serializerdata=EmployeeSerializer(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data)
