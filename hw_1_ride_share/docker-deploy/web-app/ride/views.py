from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import User, Vehicle, Ride, Rider
from .forms import Login, Register, RequestRideForm, Register_driver, RequestRideShare
from datetime import datetime
from django.utils import timezone
from django.views.generic import UpdateView, DetailView
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    user = login_required(request)
    if user == True:
        if check_user(request) == True:
            return redirect('user_home')
        else:
            return redirect('driver_home')
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

            if check_user(request) == True:
                return redirect('user_home')
            else:
                return redirect('driver_home')
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
            info = form.cleaned_data['special_info']
            driver = User.objects.get(id = request.session['id'])

            #sql query to register user in table user
            try:
                vehicle = Vehicle(vehicle_type = veh_type, license_plate = plate, capacity = cap, owner = driver, special_info = info)
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

# Route for user home
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

#Route for driver home
def driver_home(request):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is driver
    if check_user(request) == True:
        return redirect('login')

    #sql query to get user
    user = User.objects.get(id = request.session['id'])
    
    return render(request, 'driver/home.html', {'name' : user.user_name})


#Route to update ride status to finished
def finish_ride(request, ride):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is driver
    if check_user(request) == True:
        return redirect('login')

    #sql query to update ride to status = finished
    try:
        this_ride = Ride.objects.get(id = ride)
        this_ride.status = 'c'
        this_ride.save()
    except:
        return redirect('conf_rides_detail', ride)

    return redirect('view_rides')

    
#Route to view detail of particular ride, to finish it(Driver end)
def conf_rides_detail(request, ride):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is driver
    if check_user(request) == True:
        return redirect('login')

    #sql query to get user
    driver = User.objects.get(id = request.session['id'])

    #get details of ride
    try:
        ride = Ride.objects.get(id = ride)
    except:
        return redirect('view_rides')

    #get details of owner, sharers
    try:
        owner = Rider.objects.get(ride = ride, is_sharer = False)
        sharers = list(Rider.objects.filter(ride = ride, is_sharer = True))

    except:
        return redirect('view_rides')

    
    context = {
        'ride': ride,
        'owner': owner,
        'sharers': sharers
    }

    return render(request, 'driver/ride_detail.html', context)
    

#Route to view confirmed rides, update to finished (Driver end)
def view_rides(request):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is driver
    if check_user(request) == True:
        return redirect('login')

    #sql query to get user
    driver = User.objects.get(id = request.session['id'])

    #sql query to get confirmed rides
    try:
        #FOR TESTING : CHANGE C TO F
        rides = list(Ride.objects.filter(driver = driver, status = 'f'))
    except:
        return redirect('driver_home')

    return render(request, 'driver/conf_rides.html', {'rides':rides})
    
#Route to change status from open to confirmed (Driver end)
def confirm_ride(request, ride):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is driver
    if check_user(request) == True:
        return redirect('login')

    #get ride and update its fields
    try:
        this_ride = Ride.objects.get(id = ride)
        driver = User.objects.get(id = request.session['id'])
        this_ride.driver = driver
        this_ride.status = 'f'
        this_ride.save()
        
    except:
        return redirect('rides')

    subject = 'Ride-Share ride #' + str(ride) + ' is confirmed'
    message = ' Hello!\n Your ride #' + str(ride) + ' is confirmed.\n Thanks,\n Ride-share'

    recipient = [driver.email]

    #get list of riders
    try:
        riders = list(Rider.objects.filter(ride = this_ride))
        for rider in riders:
            recipient.append(rider.rider.email)
    except:
        return redirect('rides')

    #send emails
    send_mail(subject, message, settings.EMAIL_HOST_USER, recipient)
    
    
    return redirect('view_rides')
    
    
#Route to search for open rides (Driver end)
def search_ride(request): 
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type is driver
    if check_user(request) == True:
        return redirect('login')

    #get driver, vehicle field. Then, get matching rides
    try:
        driver = User.objects.get(id = request.session['id'])
        veh_d = Vehicle.objects.get(owner = driver)
    
    except:
        return redirect('driver_home')

    try:
        #get matching rides
        if not veh_d.special_info:
            ride = list(Ride.objects.filter(vehicle = veh_d.vehicle_type, num_passengers__lte = veh_d.capacity, special_request = veh_d.special_info, status = 'o'))
        else:
            ride = list(Ride.objects.filter(vehicle = veh_d.vehicle_type, num_passengers__lte = veh_d.capacity, status = 'o'))
    except:
        ride = None

    if len(ride) == 0:    
        ride = None
        
    return render(request, 'driver/rides.html', {'rides':ride})

   

class RideDetailView(DetailView):
    model = Ride
    template_name = 'user/ride_detail.html'
    context_object_name = 'this_ride'

class RideUpdateView(UpdateView):
    model = Ride
    template_name = 'user/ride_form.html'
    fields = ['arrival', 'destination', 'num_passengers', 'vehicle', 'shareable', 'special_request']

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        view_name = 'rides'
        return reverse(view_name)

class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ['vehicle_type', 'capacity', 'license_plate', 'special_info']

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        view_name = 'vehicle'
        return reverse(view_name)
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
    user = User.objects.get(id = request.session['id'])
    context = {
        'all_rides': Ride.objects.filter(owner = user, status__in = ['o', 'f'])
    }
    return render(request,'user/rides.html', context)

#route to select open rides
def add_ride(request, ride, num):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')
    #check user type is user
    if check_user(request) == False:
        return redirect('login')


    try:
        this_user = User.objects.get(id = request.session['id'])
        this_ride = Ride.objects.get(id = ride)
        this_rider = Rider(ride = this_ride, rider = this_user, num = num, name = this_user.user_name,  is_sharer = True)
        this_rider.save()
        this_ride.capacity_remaining = this_ride.capacity_remaining - num
        this_ride.num_passengers = this_ride.num_passengers + num
        this_ride.save()
    except:
        return redirect('open_rides')
    
    return redirect('rides')
    
#route to search for rides to share
def open_rides(request):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')
    #check user type is user
    if check_user(request) == False:
        return redirect('login')

    
    if request.method == 'POST':
        form = RequestRideShare(request.POST)
        if form.is_valid():

            #get user data
            dest = form.cleaned_data['dest']
            start_arr = form.cleaned_data['start_arr']
            end_arr = form.cleaned_data['end_arr']
            num = form.cleaned_data['num_passengers']

            #verify input data
            if end_arr < start_arr:
                return redirect('open_rides')
            if num < 1:
                return redirect('open_rides')

            #sql query to search for ride
            try:
                search = list(Ride.objects.filter(destination = dest, arrival__gte = start_arr, arrival__lte = end_arr, status = 'o', capacity_remaining__gte = num, shareable = True))
            except:
                search = None

            context ={
                'rides' : search,
                'num' : num
            }
            return render(request, 'user/join_ride.html', context)

    # Get view
    else:
        form = RequestRideShare()

    context = {
        'form' : form
    }
        
    return render(request,'user/open_rides.html', context)

#route to request a ride
def request_ride(request):
    #check if user is logged in
    user = login_required(request)
    if user == False:
        return redirect('login')

    #check user type
    if check_user(request) == False:
        return redirect('login')

    user = User.objects.get(id = request.session['id'])

    if request.method == 'POST':
        form = RequestRideForm(request.POST)

        if form.is_valid():
            #get user data
            arrival = form.cleaned_data['arrival']
            destination = form.cleaned_data['destination']
            num_passengers = form.cleaned_data['num_passengers']
            shareable = form.cleaned_data['shareable']
            vehicle = form.cleaned_data['vehicle']
            request = form.cleaned_data['special_request']

            #get capacity of vehicle
            if vehicle == 's':
                capacity = 4
            else:
                capacity = 6

            #sql query to put ride into table
            try:
                this_ride = Ride(owner = user, vehicle = vehicle, arrival = arrival, num_passengers = num_passengers, capacity_remaining = capacity - num_passengers, destination = destination, shareable = shareable, special_request = request)
                this_ride.save()        
            except:
                redirect('request_ride')

            try:
                this_ride = Ride.objects.get(owner = user, vehicle = vehicle, arrival = arrival)
                this_rider = Rider(ride = this_ride, rider = user, num = num_passengers, name = user.user_name, is_sharer = False)
                this_rider.save()
            except:
                redirect('request_ride')
                
        return redirect('rides')
        
    else:
        #thirty_mins = timezone.now() + datetime.timedelta(minutes=30)
        #form = RequestRideForm(initial={'arrival': thirty_mins})
        form = RequestRideForm()

    context = {
        "form": form
    }

    return render(request,'user/request_ride.html', context)


def myVehicle(request):
    user = User.objects.get(id = request.session['id'])
    context = {
        'my_vehicle': Vehicle.objects.filter(owner = user)
    }
    return render(request,'ride/vehicle.html', context)

