from django.contrib import admin
<<<<<<< HEAD
#from .models import Vehicle

# Register your models here.
#admin.site.register(Vehicle)
=======
from .models import User

# Register your models here.
#admin.site.register(Vehicle)
admin.site.register(User)
>>>>>>> a41ebba53a327951db31c11a38767d86123b3942
'''class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type', 'color', 'capacity', 'owner')

class VehicleAdmin(admin.ModelAdmin):
    fields = ['capacity', 'color']

admin.site.register(Vehicle, VehicleAdmin)'''
