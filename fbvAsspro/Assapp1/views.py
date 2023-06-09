from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
# Create your views here.


@csrf_exempt
def gettAlldata(request):
    if request.method=="GET":
        coursedata=Course.objects.all()
        courseserializer=CourseSerializers(coursedata,many=True)
        return JsonResponse(courseserializer.data,safe=False)
    elif request.method == "POST":
        print("Abhisek")
        jsondata=JSONParser().parse(request)
        print("21",type(jsondata))
        serializerdata=CourseSerializers(data=jsondata)
        print("23",serializerdata)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse(serializerdata.data,safe=False)
        else:
            return JsonResponse(serializerdata.errors,safe=False)

@csrf_exempt
def updatedata(request,pk):
    try:
        cource=Course.objects.get(pk=pk)
    except Course.DoesNotExist("Required cource is not exit"):
        return HttpResponse("Data does not exit",status=status.HTTP_400_BAD_REQUEST)
    if(request.method=="DELETE"):
        cource.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif(request.method=="GET"):
        serializedata=CourseSerializers(cource)
        return JsonResponse(serializedata.data,safe=False)
    elif(request.method=="PUT"):
        parsedata=JSONParser().parse(request)
        serializerdata=CourseSerializers(cource,data=parsedata)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse(serializerdata.data)
    
