from django.urls import path
from .views import RideListView, RideDetailView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logout, name = 'logout'),
    path('user/', views.user_home, name = 'user_home'),
    #path('rides/', views.rides, name='rides'),
    path('rides/', RideListView.as_view(), name='rides'),
    path('rides/<pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('vehicle/', views.myVehicle, name='vehicle'),
    path('open_rides/', views.open_rides, name='open_rides'),
    path('request_ride/', views.request_ride, name='request_ride'),
    #path('rides/new/', RideCreateView.as_view(), name='ride-create'),
    #path('vehicle/new/', VehicleCreateView.as_view(), name='vehicle-create'),
]
