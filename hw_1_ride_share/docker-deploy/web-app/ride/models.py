from django.db import models

class Vehicle(models.Model):
    make = models.CharField(max_length=200, help_text='Enter year, make, model of vehicle')
    color = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.make
