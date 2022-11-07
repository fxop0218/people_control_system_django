from django.forms import ModelForm, EmailInput, TextInput

from personas.models import Persona, Address


# other way to do a form
class PersonForm(ModelForm):
    class Meta:
        model = Persona
        fields = "__all__"
        widgets = {'email': EmailInput(attrs={"type": "email"})}

# Address form added
class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
        widgets = {"street_no": TextInput(attrs={"type": "number"})}
