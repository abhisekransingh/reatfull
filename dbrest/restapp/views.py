from django.shortcuts import render
from django.http import JsonResponse
from .models.models import Employee
from .serializers.serializers import EmployeeSerializers,UserSerializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from rest_framework import status
# Create your views here.
@csrf_exempt
def getData(request):
    if request.method=='GET':
        data=Employee.objects.all()
        serializerdata=EmployeeSerializers(data,many=True)
        return JsonResponse(serializerdata.data,safe=False)
    elif request.method=='POST':
        jsondata=JSONParser().parse(request)
        print(jsondata)
        serialzerdict=EmployeeSerializers(data=jsondata,many=True)
        if serialzerdict.is_valid():
            serialzerdict.save()
            return JsonResponse(serialzerdict.data,safe=False)
        else:
            return JsonResponse(serialzerdict.errors,safe=False)
@csrf_exempt
def getsingledata(request,pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist():
        return HttpResponse(status=404)
    if request.method=="DELETE":
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif request.method=="GET":
        serializer=EmployeeSerializers(employee,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="PUT":
        jsondata=JSONParser().parse(request)
        jsonserializer=EmployeeSerializers(employee,data=jsondata)
        if jsonserializer.is_valid():
            jsonserializer.save()
            return JsonResponse(jsonserializer.data,safe=False)
        else:
            return JsonResponse(status=jsonserializer.errors,safe=False)

        



def getUsersList(request):
    data1=User.objects.all()
    serializersData=UserSerializers(data1,many=True)
    return JsonResponse(serializersData.data,safe=False)
    
    
