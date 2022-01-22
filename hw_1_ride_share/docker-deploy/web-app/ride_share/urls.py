from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rides/', views.rides, name='rides'),
#    path('vehicle/', views.vehicles, name='vehicle'),
]
