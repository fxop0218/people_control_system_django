from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    return HttpResponse("Welcome 😁")


def goodbye(request):
    return HttpResponse("Goodbye 🤨")
