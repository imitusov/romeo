from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    return HttpResponse("What's up, man?")