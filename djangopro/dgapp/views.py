from django.shortcuts import render
from .models import Place,Restrurant
from django.http import HttpResponse

# Create your views here.


def getdata(request):
    data=Restrurant.objects.all()
    for i in data:
        print(i.rname,i.place)
    return HttpResponse(list(data))


a={'abhiSek':1,'ranSingh':2}
#{"abhi_sek":1,"ran_singh":2}
b={}
for i in a.keys():
    c=''
    for j in i:
        if j.isupper():
            c=c+'_'+j.lower()
        else:
            c=c+j
    
    b[c]=a[i]
print(b)

a = (1,2,[3,4])
print(a)
    

    
