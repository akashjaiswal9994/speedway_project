

from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from speed_way.models import  Vehicle,Owner,ContactNumber



class UserVehicle(serializers.Serializer):
     vehicle_model=serializers.CharField(max_length=255)

class Contact(serializers.Serializer):
    country_code=serializers.IntegerField()
    number=serializers.IntegerField()

class UserList(serializers.Serializer):
    #Id=serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    mobile_no=Contact()
    vehicle=UserVehicle()
    
