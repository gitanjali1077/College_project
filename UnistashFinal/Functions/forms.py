from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import users ,contactus
from captcha.fields import CaptchaField
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = User
        fields=['username','first_name','email','password']

class UserFormlog(forms.Form):
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()


class ContactForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        #contain info about this outer class
        model = contactus
        fields = ['name','email','message']


