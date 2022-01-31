from email.mime import image
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, default="default.jpg")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
# Create your models here.


    
# class Order(models.Model):
#     items = models.CharField(max_length=1000)
#     name = models.CharField(max_length=100)
#     email = models.CharField(max_length=100)
#     address = models.CharField(max_length=1000)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)
#     total = models.CharField(max_length=100)

#     def __str__(self):
#         return self.items

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)
    