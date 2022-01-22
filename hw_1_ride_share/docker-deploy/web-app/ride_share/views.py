from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#from .models import Vehicle

# Create your views here.

#dummy data
all_rides = [
    {
        'driver': 'Owen',
        'passenger': 'Gaunish',
        'party_size': '4',
        'vehicle': '2020 Mazda CX-5',
        'destination': '1234 Memory Lane',
        'status': 'confirmed',
    },
    {
        'driver': 'Owen',
        'passenger': 'Grady',
        'party_size': '2',
        'vehicle': '2020 Mazda CX-5',
        'destination': '321 Main Street',
        'status': 'open',
    }
]

def index(request):
    return render(request,'index.html')

def rides(request):
    context = {
        'all_rides': all_rides
    }
    return render(request,'ride_share/rides.html', context)

'''def vehicles(request):
    context = {
        'all_vehicles': Vehicle.objects.all()
    }
    return render(request,'ride_share/vehicle.html', context)
'''
