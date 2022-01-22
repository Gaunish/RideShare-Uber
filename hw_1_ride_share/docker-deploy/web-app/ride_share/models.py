from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#User class
class User(models.Model):
    user_name = models.CharField(max_length = 200, unique = True)
    email = models.CharField(max_length = 250, unique = True)
    password = models.CharField(max_length = 200)

'''
# Create your models here.
class Car(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    make = models.CharField(max_length=200, help_text='Enter year, model, and make of vehicle')
    color = models.CharField(max_length=20)
<<<<<<< HEAD
    capacity = models.PositiveIntegerField()
=======
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('vehicle-detail', args=[str(self.id)])

    def __str__(self):
        return self.owner + "'s" + self.license_plate
'''
>>>>>>> a41ebba53a327951db31c11a38767d86123b3942
