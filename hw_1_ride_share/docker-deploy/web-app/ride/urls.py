from django.urls import path
from .views import RideUpdateView, RideDetailView, VehicleUpdateView, UserUpdateView
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('reg_vehicle/',views.reg_vehicle, name = 'reg_vehicle'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('profile_user/', views.profile_user, name = 'profile_user'),
    path('user/', views.user_home, name = 'user_home'),
    path('driver/', views.driver_home, name = 'driver_home'),
    path('search_ride/', views.search_ride, name = 'search_ride'),
    path('confirm_ride/<int:ride>/', views.confirm_ride, name = 'confirm_ride'),
    path('rides/', views.rides, name='rides'),
    path('confirmed_rides/', views.view_rides, name = 'view_rides'),
    path('conf_rides_detail/<int:ride>/', views.conf_rides_detail, name = 'conf_rides_detail'),
    path('finish_ride/<int:ride>/', views.finish_ride, name = 'finish_ride'),
    path('add_ride/<int:ride>/<int:num>/', views.add_ride, name='add_ride'),
    path('leave_ride/<int:ride>/', views.leave_ride, name='leave_ride'),
    path('vehicle/', views.myVehicle, name='vehicle'),
    path('open_rides/', views.open_rides, name='open_rides'),
    path('join_ride/', views.open_rides, name='join_ride'),
    path('request_ride/', views.request_ride, name='request_ride'),
    path('rides/<pk>/update/', RideUpdateView.as_view(), name='ride-update'),
    path('vehicle/<pk>/update/', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('user/<pk>/update/', UserUpdateView.as_view(), name='user-update'),
]
