from django.db import models

# Create your models here.

class Gas(models.Model):
    device_id = models.CharField('Device Id', max_length=10)    #GAS00001
    co = models.CharField('CO', max_length=10)
    nox = models.CharField('NOx', max_length=10)
    temp = models.CharField('Temperature', max_length=10)
    hum = models.CharField('Humidity', max_length=10)
    
    def __str__(self):
        return self.device_id + '  ' + self.co + '  ' + self.nox
    
    
    
class User(models.Model):
    first_name = models.CharField('First Name', max_length=20)
    second_name = models.CharField('Second Name', max_length=20)
    email = models.EmailField('Email')
    address = models.CharField("Address", max_length=200)
    phone_number = models.CharField("Phone Number", max_length=15)
    gas = models.ForeignKey(Gas, on_delete=models.CASCADE) #firstname+secondname+device
    
    def __str__(self):
        return self.first_name + ' ' + self.second_name + ' ' + self.email
    