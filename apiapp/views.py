from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the home page")

def api(request):
    return HttpResponse("This is my First API")

