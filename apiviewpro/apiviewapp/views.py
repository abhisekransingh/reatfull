from django.shortcuts import render
from .models.models import Employee
from .serializers.serializers import EmployeeSerializers,UserSerializers
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import mixins,generics


# Create your views here.
@api_view(["GET","POST"])
def getData(request):
    if request.method=='GET':
        data=Employee.objects.all()
        serializerdata=EmployeeSerializers(data,many=True)
        return Response(serializerdata.data)
    elif request.method=='POST':
        serialzerdict=EmployeeSerializers(data=request.data,many=True)
        if serialzerdict.is_valid():
            serialzerdict.save()
            return Response(serialzerdict.data)
        else:
            return Response(serialzerdict.errors)
@api_view(["DELETE","PUT","GET"])
def getsingledata(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist():
        return HttpResponse(status=404)
    if request.method=="DELETE":
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif request.method=="GET":
        serializer=EmployeeSerializers(employee)
        return Response(serializer.data)
    elif request.method=="PUT":
        jsonserializer=EmployeeSerializers(employee,data=request.data)
        if jsonserializer.is_valid():
            jsonserializer.save()
            return Response(jsonserializer.data)
        else:
            return Response(status=jsonserializer.errors)

        


@api_view(["GET","POST"])
def getUsersList(request):
    if request.method=="GET":
        # data1=User.objects.all()
        data1= User.objects.values()
        print(data1)
        print('RANSINGH',str(data1.query))
        serializersData=UserSerializers(data1,many=True)
        return Response(serializersData.data)
    


    a=list(lambda x:x*x for i in range(10))
    print(a)

    
    
