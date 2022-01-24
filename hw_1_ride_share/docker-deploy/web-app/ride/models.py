from django.db import models
from datetime import datetime
from django.utils import timezone

class User(models.Model):
    user = 'U'
    driver = 'D'
    USER_CHOICES = [(user, 'User'), (driver, 'Driver')]
    
    user_name = models.CharField(max_length = 200, unique = True)
    email = models.EmailField(max_length = 250, unique = True)
    password = models.CharField(max_length = 200)
    user_type = models.CharField(max_length = 1, choices=USER_CHOICES) 

    def __str__(self):
        """String for representing the Model object."""
        return self.user_name

VEHICLE_TYPE = (
        ('s', 'Small'),
        ('l', 'Large'),
)

class Vehicle(models.Model):
    #make = models.CharField(max_length=200, help_text='Enter year, make, model of vehicle')
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE, default='s')
    license_plate = models.CharField(max_length=7, unique = True)
    capacity = models.PositiveIntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None) #, choices=User.objects.filter(user_type='D'))

    def __str__(self):
        """String for representing the Model object."""
        return self.license_plate

# COMMENTED TO MAKE SURE WE WANT A RIDE CLASS BEFORE MAKE MIGRATIONS
class Ride(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='ride_owner')
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, related_name='ride_driver', null=True, blank=True)
    #vehicle_type = models.CharField(,blank=True)
    vehicle = models.CharField(max_length=20, choices=VEHICLE_TYPE, default='s')
    arrival = models.DateTimeField(default=timezone.now)
    num_passengers = models.PositiveIntegerField(default=1)
    destination = models.CharField(max_length=200, help_text='What is your destination?')
    shareable = models.BooleanField(default=False)
    sharer = models.ManyToManyField(User, default=None, blank=True, related_name='ride_sharer')
    #special_request = models.CharField(blank=True)

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

    class Meta:
        ordering = ['arrival']

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.owner}'s Trip to {self.destination}"
        
    #@property
    #def driver(self):
    #    return self.vehicle.getattr(owner)


