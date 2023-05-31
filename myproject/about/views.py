from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def aboutFun(request):
    return render(request,'about.html')
