from django.db import models

# Create your models here.

class admin1(models.Model):
    fname=models.CharField(max_length=15)
    lname=models.CharField(max_length=15)
    email=models.CharField(max_length=30, unique=True)    # Only one email per register
    password=models.CharField(max_length=15)

class book(models.Model):
    bname=models.CharField(max_length=50)
    aname=models.CharField(max_length=25)
    price=models.BigIntegerField()

