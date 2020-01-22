from django.shortcuts import render
from django.http import HttpResponse
from http.client import HTTPResponse

# Create your views here.
def index(request):
    return HTTPResponse("Rango says hey there partner!")