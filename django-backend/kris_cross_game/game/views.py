from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def game(req):
    return HttpResponse("HELLO WORLD")