from django.db import models

# Create your models here.


class ContactNumber(models.Model):
    country_code=models.IntegerField()
    number=models.IntegerField()

class Vehicle(models.Model):
    vehicle_model=models.CharField(max_length=255)

class Owner(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    mobile_no=models.OneToOneField(ContactNumber,on_delete=models.PROTECT)
    vehicle=models.ForeignKey(Vehicle,on_delete=models.PROTECT)
    