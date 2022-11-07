from django.contrib import admin
from personas.models import Persona, Address
# Register your models here.
admin.site.register(Persona) # Import personas to see in django admin
admin.site.register(Address)
