from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''class Vehicle(models.Model):
    license_plate = models.OneToOneField(Vehicle, max_length=7, help_text='Enter license plate', on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=200, help_text='Enter year, model, and make of car')
    max_passengers = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    color = models.CharField(max_length=20)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.license_plate
    '''
