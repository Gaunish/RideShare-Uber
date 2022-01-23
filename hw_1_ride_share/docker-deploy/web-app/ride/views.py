from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Login

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

def login(request):
    #POST METHOD
    if request.method == 'POST':
        #Put the post data into form 
        form = Login(request.POST)
        #if valid data
        if form.is_valid():
            #get data entered by user
            name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']

            #sql query
            user = Login.objects.get(user_name = name, email = email, user_type = user_type)
            #if user.password != hash(password):
                #return render(request, 'error.html')

            #return render(request, 'success.html')

            #NOT WORKING
            return redirect(reverse(rides))
    #GET METHOD
    else:
        form = Login()

    return render(request, 'auth/login.html', {'form':form})
        

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
