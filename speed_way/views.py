from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView
from .searlization import Contact, UserList, UserVehicle
from speed_way.models import  Vehicle,Owner,ContactNumber
from rest_framework.decorators import api_view 
from rest_framework.response import Response
# Create your views here.
'''class OwnerList(ListCreateAPIView):
    queryset=UserList.objects.all()
    serializer_class=UserList'''

@api_view()
def  ownerDetails(request):
    show=Owner.objects.all()
    serial=UserList(show,many=True)
    return Response(serial.data)