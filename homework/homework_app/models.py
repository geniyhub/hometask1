from django.db import models
from django.db import models

class Games(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    creator = models.TextField()
    genre = models.CharField(max_length=255)
    year = models.IntegerField()

class Payment(models.Model):
    username = models.CharField(max_length=255)
    amount_money = models.IntegerField()
    comment = models.TextField(max_length=500)

class User(models.Model):
    username = models.TextField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.TextField()
    password = models.TextField()

# Create your models here.
