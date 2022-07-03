from django.db import models

from user.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()

