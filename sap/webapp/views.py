from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from personas.models import Persona


def welcome(request):
    person_no = Persona.objects.count()  # Get information from the database
    # people = Persona.objects.all()
    people = Persona.objects.order_by("id")
    return render(request, "welcome.html", {'no_persons': person_no, "people": people})  # In templates


def goodbye(request):
    return HttpResponse("Goodbye 🤨")



