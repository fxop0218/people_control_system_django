from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from personas.forms import PersonForm
from personas.models import Persona


# One way to do a form
# PersonForm = modelform_factory(Persona, exclude=[])


def person_information(request, id):
    # person = Persona.objects.get(pk=id)
    person = get_object_or_404(Persona, pk=id)
    return render(request, "personas/detail.html", {"person": person})


def new_person(request):
    if request.method == "POST":
        person_form = PersonForm(request.POST)
        # Validate form
        if person_form.is_valid():
            person_form.save()
            return redirect("index")
    else:
        person_form = PersonForm()

    return render(request, "personas/new.html", {"personForm": person_form})


def person_edit(request, id):
    person = get_object_or_404(Persona, pk=id)

    if request.method == "POST":
        person_form = PersonForm(request.POST, instance=person)  # Instance = to update the exact object

        if person_form.is_valid():
            person_form.save()
            return redirect("index")
    else:
        person_form = PersonForm(instance=person)

    return render(request, "personas/edit.html", {"personForm": person_form})


def person_delete(request, id):
    person = get_object_or_404(Persona, pk=id)

    if person:
        person.delete()
    return redirect("index")
