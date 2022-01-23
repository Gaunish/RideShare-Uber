from django.db import models

class User(models.Model):
    user = 'U'
    driver = 'D'
    USER_CHOICES = [(user, 'User'), (driver, 'Driver')]
    
    user_name = models.CharField(max_length = 200, unique = True)
    email = models.EmailField(max_length = 250, unique = True)
    password = models.CharField(max_length = 200)
    user_type = models.CharField(max_length = 1, choices=USER_CHOICES) 

class Vehicle(models.Model):
    make = models.CharField(max_length=200, help_text='Enter year, make, model of vehicle')
    color = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        """String for representing the Model object."""
        return self.make
