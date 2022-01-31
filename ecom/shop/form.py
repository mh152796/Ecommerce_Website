from django.db import models
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Products, Profile

class ProjectForm(ModelForm):
    class Meta:
        model = Products
        fields = ['title','price','discount_price','category','description','image']
        
    def __init__(self, *args, **kwargs):
         super(ProjectForm, self).__init__(*args, **kwargs)
         
         for name, field in self.fields.items():
             field.widget.attrs.update({'class':'input'})
             
             
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'name'
        }
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
            
        for name, field in self.fields.items():
                field.widget.attrs.update({'class':'input'}) 
            
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username',
                  'location','short_intro']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})