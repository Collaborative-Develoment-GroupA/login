from django.db import models


class admin_login(models.Model):
    username = models.CharField(max_length=100, default="admin")
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
    def __str__(self):
        return self.email

class Officer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    citizenship= models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    post = models.CharField(max_length=50)

class Accident(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    fault_vehicle_number = models.CharField(max_length=100)
    fault_driver_name = models.CharField(max_length=100)
    fault_driver_email = models.EmailField()
    fault_driver_phone = models.CharField(max_length=100)
    fault_driver_address = models.TextField()
    victim_vehicle_number = models.CharField(max_length=100)
    victim_name = models.CharField(max_length=100)
    victim_email = models.EmailField()
    victim_phone = models.CharField(max_length=100)
    victim_address = models.TextField()
    injuries = models.TextField()
    description = models.TextField()

class User(models.Model):
    fullName = models.CharField(max_length=100)
    licenseno = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=20)

class Ticket(models.Model):
    ticket_type = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact_number= models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    district=models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()


    
