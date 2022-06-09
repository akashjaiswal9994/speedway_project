from django.contrib import admin
from .models import Owner,Vehicle,ContactNumber
# Register your models here.
admin.site.register(Owner)
admin.site.register(Vehicle)
admin.site.register(ContactNumber)