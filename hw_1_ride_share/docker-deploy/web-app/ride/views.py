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

            #sql query to verify records
            try:
                user = User.objects.get(user_name = name, email = email, user_type = user_type)
            except:
                return redirect('login')

            #check password
            if password != user.password:
               return redirect('login')

            request.session['id'] = user.id;
            return redirect('request_ride')
    #GET METHOD
    else:
        form = Login()

    return render(request, 'auth/login.html', {'form':form})

def logout(request):
    del request.session['id']
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            
            #get data entered by user
            name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_passwd']
            user_type = form.cleaned_data['user_type']

            if password != re_password:
                redirect('register')

            #sql query
            try:
                user = User(user_name = name, email = email, password = password, user_type = user_type)
                user.save()
            except:
                redirect('register')
            
            return redirect('login')
    else:
        form = Register()

    name = "None"
    user_row = request.session.get('id', "None")
    if user_row != "None":
        user = User.objects.get(id = request.session['id'])
        name = user.user_name
        
    context = {
        'form' : form,
        'name' : name,
    }
    return render(request, 'auth/reg.html', context)    



class RideListView(ListView):
    model = Ride
    template_name = 'ride/rides.html'
    context_object_name = 'all_rides'
    ordering = ['-arrival']

class RideDetailView(DetailView):
    model = Ride
    context_object_name = 'this_ride'
'''
class RideCreateView(CreateView):
    model = Ride
    #context_object_name = 'new_ride'
    fields = ['arrival', 'destination', 'num_passengers', 'vehicle', 'shareable']

    def form_valid(self, form):
        #form.instance.owner = self.request.user
        user_row = self.request.session.get('id', "None")
        if user_row != "None":
            user = User.objects.get(id = request.session['id'])
        print (user)
        form.instance.owner = user
        return super().form_valid(form)
    def get_initial(self):
        return {
             'owner': self.request.user,
             'destination': datetime.date.today()
        }

class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ['vehicle_type', 'capacity', 'license_plate']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

#overrided by RideListView - same functionality
'''


def rides(request):
    context = {
        'all_rides': Ride.objects.all()
    }
    return render(request,'ride/rides.html', context)

def open_rides(request):
    if request.method == 'GET':
        context = {
            'open_rides': Ride.objects.filter(shareable = True, status = 'o')
        }
    else:
        context = None  
    return render(request,'ride/open_rides.html', context)


def request_ride(request):
    user = "None"
    user_row = request.session.get('id', "None")
    if user_row != "None":
        user_r = User.objects.get(id = request.session['id'])
        user = user_r.user_name

    if request.method == 'POST':
        form = RequestRideForm(request.POST)
        return redirect('rides')
        
    else:
        #thirty_mins = timezone.now() + datetime.timedelta(minutes=30)
        #form = RequestRideForm(initial={'arrival': thirty_mins})
        form = RequestRideForm()

    context = {
        "form": form,
        "name": user,
    }

    return render(request,'ride/request_ride.html', context)


def myVehicle(request):
    context = {
        'my_vehicle': Vehicle.objects.all()
    }
    return render(request,'ride/vehicle.html', context)

