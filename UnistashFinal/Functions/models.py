from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models.signals import post_save

from django.db.models.signals import *
import os
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField( default = os.path.join(settings.STATIC_ROOT,'static','abc1.jpg'),
                            )#upload_to='media/')
    #rate=models.IntegerField()
#(max_length=100) #upload_to='media/')


    def create_user_profile(sender, instance, created, **kwargs):
       if created:
        b=instance._photo
        #c=instance._rate
        a=Profile.objects.create(user=instance,photo=b)#,rate=c)

    post_save.connect(create_user_profile ,sender=User)


# Create your models here.
class users(models.Model):
    username = models.CharField(max_length=200)
    #password = models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    college= models.CharField(max_length=200)

    def __str__(self):
        return self.username

   
class contactus(models.Model):
    email = models.EmailField(max_length=200)
    #password = models.CharField(max_length=200)
    name= models.CharField(max_length=300)
    message= models.CharField(max_length=9000)

    def __str__(self):
        return self.email

class students(models.Model):
    name=models.CharField(max_length=200)
    email= models.EmailField(max_length=200)
    course=models.CharField(max_length=200)
    year=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    experience=models.TextField(max_length=11000)
    
    def __str__(self):
        return self.name
