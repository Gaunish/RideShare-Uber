from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,'ride/rides.html', context)

#dummy data
my_vehicle = [
    {
        'make': '2020 Mazda CX-5',
        'color': 'Blue',
        'capacity': '4',
    }
]

def myVehicle(request):
    context = {
        'my_vehicle': my_vehicle
    }
    return render(request,'ride/vehicle.html', context)
