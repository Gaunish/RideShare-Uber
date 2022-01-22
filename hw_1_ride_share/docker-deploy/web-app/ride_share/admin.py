from django.contrib import admin
from .models import User

# Register your models here.
#admin.site.register(Vehicle)
admin.site.register(User)
'''class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'color', 'capacity', 'owner')
'''
