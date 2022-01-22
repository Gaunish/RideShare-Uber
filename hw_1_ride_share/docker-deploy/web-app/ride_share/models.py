from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    make = models.CharField(max_length=200, help_text='Enter year, model, and make of vehicle')
    color = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()
