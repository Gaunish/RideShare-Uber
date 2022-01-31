from django.contrib import admin
from .models import Vehicle, User, Ride, Rider

admin.site.register(User)
admin.site.register(Vehicle)
admin.site.register(Ride)
admin.site.register(Rider)
