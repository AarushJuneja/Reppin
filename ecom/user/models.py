from tokenize import Name
from django.db import models

# Create your models here.
class User(models.Model):
    Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=50)