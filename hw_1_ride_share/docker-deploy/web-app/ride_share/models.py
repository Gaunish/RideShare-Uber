from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Vehicle(models.Model):
    #license_plate = models.OneToOneField(User, max_length=7, help_text='Enter license plate', on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=200, help_text='Enter year, model, and make of car')
    capacity = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('vehicle-detail', args=[str(self.id)])

    def __str__(self):
        return self.owner + "'s" + self.license_plate
