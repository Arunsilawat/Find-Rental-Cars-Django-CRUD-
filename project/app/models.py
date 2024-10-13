from django.db import models

# Create your models here.

class Userdata(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=25)


class Book_data(models.Model):
    fname=models.CharField(max_length=(50))
    lname=models.CharField(max_length=(50))
    email=models.EmailField()
    carnm=models.CharField(max_length=(50))
    amount=models.IntegerField()
    address=models.TextField()
    pick=models.CharField(max_length=(50))
    drop=models.CharField(max_length=(50))
    feedback=models.TextField()