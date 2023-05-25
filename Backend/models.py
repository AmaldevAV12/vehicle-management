from django.db import models

# Create your models here.
class Vehicle_Category(models.Model):
    Cname = models.CharField(max_length=50, null=True, blank=True)
    # Brand = models.CharField(max_length=50,null=True, blank=True)
    Comments = models.CharField(max_length=500, null=True, blank=True)
    Image = models.ImageField(upload_to="profile")

class VehicleDB(models.Model):
   Cname = models.CharField(max_length=50, null=True, blank=True)
   Vname = models.CharField(max_length=50, null=True, blank=True)
   Colour = models.CharField(max_length=50, null=True, blank=True)
   Price = models.IntegerField(null=True, blank=True)
   Comments = models.CharField(max_length=500, null=True, blank=True)
   Image = models.ImageField(upload_to="profile")

class Admindb(models.Model):
    Name = models.CharField(max_length=50,null=True,blank=True)
    MobileNumber = models.IntegerField(null=True,blank=True)
    EmailID = models.EmailField(null=True,blank=True)
    Image = models.ImageField(upload_to="profile")
    Review = models.CharField(max_length=50,null=True,blank=True)
    # Password = models.CharField(max_length=50,null=True,blank=True)
    # ConfirmPassword = models.CharField(max_length=50,null=True,blank=True)

class Contactdatab(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    EmailID = models.EmailField(null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Message = models.CharField(max_length=50, null=True, blank=True)