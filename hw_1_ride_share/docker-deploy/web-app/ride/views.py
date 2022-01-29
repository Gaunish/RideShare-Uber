from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Vehicle, Ride
from .forms import Login, Register, RequestRideForm, Register_driver
import datetime
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView


def index(request):
    user = login_required(request)
    if user == True:
        return redirect('user_home')
    
    return render(request,'index.html')

#function to check whether user is logged in
def login_required(request):
   user = request.session.get('id', "None")

   if user == "None":
       return False
   
   return True

#function to check whether user type is correct
def check_user(request):
    user = User.objects.get(id = request.session['id'])
    if user.user_type != 'U':
        return False
    return True

#route for common login 
def login(request):
    #POST METHOD
    if request.method == 'POST':
        #Put the post data into form 
        form = Login(request.POST)

        #if valid data
        if form.is_valid():
            #get data entered by user
            name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            #sql query to verify records
            try:
                user = User.objects.get(user_name = name)
            except:
                return redirect('login')

            #check password
            if password != user.password:
               return redirect('login')

            request.session['id'] = user.id;
            return redirect('user_home')
    #GET METHOD
    else:
        form = Login()

    return render(request, 'auth/login.html', {'form':form})


#route for logout 
def logout(request):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #clear the session
    del request.session['id']
    return redirect('login')


#Route to register the user
def register(request):
    #Post method
    if request.method == 'POST':
        #check validity of data
        form = Register(request.POST)
        if form.is_valid():
            
            #get cleansed data entered by user
            name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            re_password = form.cleaned_data['re_passwd']
            user_type = form.cleaned_data['user_type']

            #check if password match
            if password != re_password:
                redirect('register')

            #sql query to register user in table user
            try:
                user = User(user_name = name, email = email, password = password, user_type = user_type)
                user.save()
            except:
                #To implement : error message to be shown, password hash
                redirect('register')

            #if driver, register vehicle
            if user_type == 'D':
                user = User.objects.get(user_name = name)
                request.session['id'] = user.id;
                return redirect('reg_vehicle')
            
            return redirect('login')
    #Get method
    else:
        form = Register()
    
    context = {
        'form' : form,
    }
    return render(request, 'auth/reg.html', context)    

#Route for registering vehicle
def reg_vehicle(request):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is driver
    if check_user(request) == True:
        return redirect('login')

    if request.method == 'POST':
        form = Register_driver(request.POST)
        if form.is_valid():
            
            #get cleansed data entered by user
            veh_type = form.cleaned_data['vehicle_type']
            plate = form.cleaned_data['license_plate']
            cap = form.cleaned_data['capacity']
            driver = User.objects.get(id = request.session['id'])

            #sql query to register user in table user
            try:
                vehicle = Vehicle(vehicle_type = veh_type, license_plate = plate, capacity = cap, owner = driver)
                vehicle.save()
            except:
                #delete record from user
                driver.delete()
                
                #To implement : error message to be shown
                redirect('register')
            
            return redirect('login')
    #Get method
    else:
        form = Register_driver()
    
    context = {
        'form' : form,
    }
    return render(request, 'ride/vehicle_form.html', context)    

#Route for user home
def user_home(request):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is user
    if check_user(request) == False:
        return redirect('login')

    #sql query to get user
    user = User.objects.get(id = request.session['id'])
    
    return render(request, 'user/home.html', {'name' : user.user_name})


class RideListView(ListView):
    model = Ride
    template_name = 'user/rides.html'
    context_object_name = 'all_rides'
    ordering = ['-arrival']

class RideDetailView(DetailView):
    model = Ride
    template_name = 'user/ride_detail.html'
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
    return render(request,'user/rides.html', context)

def open_rides(request):
    if request.method == 'GET':
        context = {
            'open_rides': Ride.objects.filter(shareable = True, status = 'o')
        }
    else:
        user = User.objects.get(id = request.session['id'])
        this_ride = request.POST.copy()
        this_ride['sharer'] = user
        request.POST = this_ride
        
        context = None  
    return render(request,'user/open_rides.html', context)


def request_ride(request):
<<<<<<< HEAD
#<<<<<<< HEAD
#<<<<<<< HEAD
#=======
#>>>>>>> b23f1160da5254b1dcd709ec3b7025f2469abe88
=======
>>>>>>> a7f1e3992eb06b64914470619cb89538f09e9b0a
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type
    if check_user(request) == False:
        return redirect('login')

    #user = User.objects.get(id = request.session['id'])
    
    user = "None"
    user_row = request.session.get('id', "None")
    if user_row != "None":
        user_r = User.objects.get(id = request.session['id'])
        user = user_r.user_name
<<<<<<< HEAD
#<<<<<<< HEAD
#=======
    user = User.objects.get(id = request.session['id'])
#>>>>>>> 6d860299601862bd2c9b0f3c71d3d00e56bd0d74
#=======
    user = User.objects.get(id = request.session['id'])
#>>>>>>> b23f1160da5254b1dcd709ec3b7025f2469abe88
=======
    user = User.objects.get(id = request.session['id'])
>>>>>>> a7f1e3992eb06b64914470619cb89538f09e9b0a

    if request.method == 'POST':
        form = RequestRideForm(request.POST)

        if form.is_valid():
            arrival = form.cleaned_data['arrival']
            destination = form.cleaned_data['destination']
            num_passengers = form.cleaned_data['num_passengers']
            shareable = form.cleaned_data['shareable']
            vehicle = form.cleaned_data['vehicle']

            #sql query
            try:
                this_ride = Ride(owner = user, vehicle = vehicle, arrival = arrival, num_passengers = num_passengers, destination = destination, shareable = shareable)
                this_ride.save()
            except:
                redirect('request_ride')
        return redirect('rides')
        
    else:
        #thirty_mins = timezone.now() + datetime.timedelta(minutes=30)
        #form = RequestRideForm(initial={'arrival': thirty_mins})
        form = RequestRideForm()

    context = {
        "form": form,
        "name": user,
    }

    return render(request,'user/request_ride.html', context)


def myVehicle(request):
    context = {
        'my_vehicle': Vehicle.objects.all()
    }
    return render(request,'ride/vehicle.html', context)

