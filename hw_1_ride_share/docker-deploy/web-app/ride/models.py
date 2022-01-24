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
    license_plate = models.CharField(max_length=7, unique = True)
    capacity = models.PositiveIntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        """String for representing the Model object."""
        return self.make

''' COMMENTED TO MAKE SURE WE WANT A RIDE CLASS BEFORE MAKE MIGRATIONS
class Ride(models.Model):
    owner = models.OneToOneField(User, default=None)
    driver = models.OneToOneField(User, default=None)
    num_passengers = models.PositiveIntegerField(default=1)
    shareable = models.BooleanField(default=False)
    destination = models.CharField(max_length=200, help_text='What is your destination?')

    RIDE_STATUS = (
        ('o', 'Open'),
        ('c', 'Complete'),
        ('f', 'Confirmed'),
    )
    
    status = models.CharField(
        max_length=1,
        choices=RIDE_STATUS,
        default='o',
        help_text='Ride Status',
    )
'''
