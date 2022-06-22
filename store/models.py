from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.CharField(max_length=1000)



class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password= models.CharField(max_length=200)
