from django import forms
from django.utils import timezone
from django.forms import ModelForm

from .models import Ride

user = 'U' 
driver = 'D'
USER_CHOICES = [(user, 'User'), (driver, 'Driver')] 

class Login(forms.Form):
    user_name = forms.CharField(label='Username', max_length = 200)
    email = forms.EmailField(label = 'Email', max_length = 250)
    password = forms.CharField(max_length = 200)
    user_type = forms.ChoiceField(label = 'User Type', choices=USER_CHOICES)

class Register(forms.Form):
    user_name = forms.CharField(label='Username', max_length = 200)
    email = forms.EmailField(label = 'Email', max_length = 250) 
    password = forms.CharField(max_length = 200)
    re_passwd = forms.CharField(label = 'Repeat Password', max_length = 200)
    user_type = forms.ChoiceField(label = 'User Type', choices=USER_CHOICES)

VEHICLE_TYPE = (
        ('s', 'Small'),
        ('l', 'Large'),
)

class RequestRide(forms.Form):
    vehicle = forms.ChoiceField(choices=VEHICLE_TYPE)
    arrival = forms.DateTimeField()
    num_passengers = forms.IntegerField(min_value=1, max_value=6)
    destination = forms.CharField(max_length=200, help_text='What is your destination?')
    shareable = forms.BooleanField()    


'''
class RequestRideForm(ModelForm):
    vehicle = forms.ChoiceField(choices=VEHICLE_TYPE)
    arrival = forms.DateTimeField()
    num_passengers = forms.IntegerField(min_value=1, max_value=6)
    destination = forms.CharField(max_length=200, help_text='What is your destination?')
    shareable = forms.BooleanField()    

    def clean_arrival_time(self):
        date_time = self.cleaned_data['arrival']
        
        if data_time < timezone.now:
            raise ValidationError('Invalid date - trip in past')

        return date_time

    class Meta:
        model = Ride
        fields = ['arrival', 'destination', 'num_passengers', 'vehicle', 'shareable']
'''
