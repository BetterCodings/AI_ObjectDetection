from django.db import models

class Account(models.Model):
    name= models.CharField(max_length=30)
    ID =models.CharField(max_length=30,primary_key=True)
    passwd=models.CharField(max_length=30)