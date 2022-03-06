from django.db import models

# Create your models here.
class Member(models.Model):
    email=models.CharField(max_length=100)
    passwd=models.CharField(max_length=100)
    
