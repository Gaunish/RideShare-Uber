from django import forms
from django.utils import timezone
from django.forms import ModelForm
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from .models import Ride, Vehicle

#Choices for uaer type
user = 'U' 
driver = 'D'
USER_CHOICES = [(user, 'User'), (driver, 'Driver')] 

#Form for user login
class Login(forms.Form):
    user_name = forms.CharField(label='Username', max_length = 200)
    password = forms.CharField(max_length = 200)

#Form for user register
class Register(forms.Form):
    user_name = forms.CharField(label='Username', max_length = 200)
    email = forms.EmailField(label = 'Email', max_length = 250) 
    password = forms.CharField(max_length = 200)
    re_passwd = forms.CharField(label = 'Repeat Password', max_length = 200)
    user_type = forms.ChoiceField(label = 'User Type', choices=USER_CHOICES)

    
#VEHICLE_TYPE = (
 #       ('s', 'Small'),
  #      ('l', 'Large'),
#)

class Register_driver(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'license_plate', 'special_info'] 

    
class RequestRideForm(ModelForm):
    #vehicle = forms.ChoiceField(choices=VEHICLE_TYPE)
    #arrival = forms.DateTimeField()
    #num_passengers = forms.IntegerField(min_value=1, max_value=6)
    #destination = forms.CharField(max_length=200, help_text='What is your destination?')
    #shareable = forms.BooleanField()    

    '''def clean_arrival_time(self):
        date_time = self.cleaned_data['arrival']
        
        if data_time < timezone.now:
            raise ValidationError('Invalid date - trip in past')

        return date_time'''

    class Meta:
        model = Ride
        fields = ['arrival', 'destination', 'num_passengers', 'vehicle', 'shareable', 'special_request']


class RequestRideShare(forms.Form):
    dest = forms.CharField(label='Destination', max_length = 200)
    start_arr = forms.DateTimeField(initial = datetime.now, label = 'Earliest Arrival', input_formats=['%d/%m/%Y %H:%M'],
       widget = forms.DateTimeInput(format ='%d/%m/%Y %H:%M'))
    end_arr = forms.DateTimeField(initial = datetime.now, label = 'Latest Arrival', input_formats=['%d/%m/%Y %H:%M'],
       widget = forms.DateTimeInput(format ='%d/%m/%Y %H:%M'))
    num_passengers = forms.IntegerField(initial = 1, label = 'Num of Passengers')
