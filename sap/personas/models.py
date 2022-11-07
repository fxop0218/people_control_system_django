from django.db import models


# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=255)
    street_no = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"Address {self.id}: Street: {self.street} {self.street_no} country: {self.country}"


class Persona(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    # Change the visualization of the object in django admin
    def __str__(self):
        return f"Person {self.id}: Name: {self.name} {self.surname} {self.email}"
