from django.db import models

from user.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
    User = models.ForeignKey(User)
    Products = models.ManyToManyField(Product, blank=True, related_name='cart')
