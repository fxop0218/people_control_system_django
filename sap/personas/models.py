from django.db import models


# Create your models here.
class Persona(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    # Change the visualization of the object in django admin
    def __str__(self):
        return f"Person {self.id}: Name: {self.name} {self.surname} {self.email}"
