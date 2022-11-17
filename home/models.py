from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    age = models.CharField(max_length = 200)
    country = models.CharField(max_length=200)
    city  = models.CharField(max_length = 200)
    street = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 20)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length = 200)
    model = models.CharField(max_length = 20)
    brand = models.CharField(max_length=200)

class Ads(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    price_per_km = models.IntegerField(default=100)




    