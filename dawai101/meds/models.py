from django.db import models

# Create your models here.

class medicines(models.Model):
    med_name= models.CharField(max_length=100)
    manufacturer= models.CharField(max_length=100)
    price=models.IntegerField()

class prescription(models.Model):
    date=models.DateField()
    med_name=models.CharField(max_length=100)
    quantity=models.IntegerField()