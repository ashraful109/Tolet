import email
from unicodedata import name
from accounts.models import User
from email.mime import image
from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class House(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
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
    video = EmbedVideoField(blank=True,null=True)
    date_added = models.DateField(auto_now_add=True)
    is_publish = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
    

class Slider(models.Model):
    image = models.ImageField(upload_to="slider/")
    house = models.ForeignKey(House,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.house.name

class Inquary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    email = models.CharField(max_length=50,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    message = models.TextField(max_length=250,blank=True,null=True)