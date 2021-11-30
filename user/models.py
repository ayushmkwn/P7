from django.db import models

class Post(models.Model):
    postusername = models.CharField(max_length=20)
    postname = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class UserProfile(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    birthdate = models.CharField(max_length=10)
    mobileno = models.CharField(max_length=10)
    gender = models.CharField(max_length=6)
    city = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    profile = models.ImageField(upload_to = "images/")
    document = models.FileField(upload_to= "docs/")