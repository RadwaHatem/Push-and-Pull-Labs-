from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homeFun(request):
    return render(request,'home.html')
