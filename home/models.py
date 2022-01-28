from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    rent = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="house/")
    location = models.CharField(max_length=200)
    house_type = models.CharField(max_length=250)
    area = models.CharField(max_length=50)
    beds = models.CharField(max_length=20)
    baths = models.CharField(max_length=20)
    garage = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Slider(models.Model):
    image = models.ImageField(upload_to="slider/")
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.house.name
    