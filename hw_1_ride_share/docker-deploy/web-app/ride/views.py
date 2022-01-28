from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Vehicle, Ride
from .forms import Login, Register, RequestRideForm
import datetime
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

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
            try:
                user = User.objects.get(user_name = name, email = email, user_type = user_type)
            except:
                return redirect('login')
            
            return redirect('rides')
    #GET METHOD
    else:
        form = Login()

    return render(request, 'auth/login.html', {'form':form})
        
def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():        
            #get data entered by user
            name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']


            #sql query
            user = User(user_name = name, email = email, password = password, user_type = user_type)
            user.save()
            
            return redirect('login')
    else:
        form = Register()
    return render(request, 'auth/reg.html', {'form':form})    


class RideListView(ListView):
    model = Ride
    template_name = 'ride/rides.html'
    context_object_name = 'all_rides'
    ordering = ['-arrival']

class RideDetailView(DetailView):
    model = Ride
    context_object_name = 'this_ride'

class RideCreateView(CreateView):
    model = Ride
    #context_object_name = 'new_ride'
    fields = ['arrival', 'destination', 'num_passengers', 'vehicle', 'shareable']
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

#overrided by RideListView - same functionality
'''def rides(request):
    context = {
        'all_rides': Ride.objects.all()
    }
    return render(request,'ride/rides.html', context)'''

def open_rides(request):
    if request.method == 'GET':
        context = {
            'open_rides': Ride.objects.filter(shareable = True, status = 'o')
        }
    else:
        context = None  
    return render(request,'ride/open_rides.html', context)

def request_ride(request):
    if request.method == 'POST':
        form = RequestRideForm(request.POST)
    else:
        #thirty_mins = timezone.now() + datetime.timedelta(minutes=30)
        #form = RequestRideForm(initial={'arrival': thirty_mins})
        form = RequestRideForm()

    context = {
        'form': form,
    }

    return render(request,'ride/request_ride.html', context)

def myVehicle(request):
    context = {
        'my_vehicle': Vehicle.objects.all()
    }
    return render(request,'ride/vehicle.html', context)
