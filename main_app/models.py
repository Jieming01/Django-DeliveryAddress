from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
