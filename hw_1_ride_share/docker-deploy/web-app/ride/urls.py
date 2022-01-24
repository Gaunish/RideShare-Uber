from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('rides/', views.rides, name='rides'),
    path('vehicle/', views.myVehicle, name='vehicle'),
    path('open_rides/', views.open_rides, name='open_rides'),
    path('request_ride/', views.request_ride, name='request_ride'),
]
