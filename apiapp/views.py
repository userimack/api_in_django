from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'apiapp/home.html',{})

def api(request):
    return render(request,'apiapp/api.html',{})


