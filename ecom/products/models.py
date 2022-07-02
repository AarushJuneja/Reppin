from ast import Sub
from hashlib import new
from http.client import PROXY_AUTHENTICATION_REQUIRED
from multiprocessing import parent_process
from tokenize import Name, blank_re
from turtle import up
from django.db import models
from matplotlib import category
from matplotlib.axis import XAxis
from traitlets import default
import pathlib

class Gender(models.Model):
    Gender = models.CharField(max_length=10, default="")
    def __str__(self):
        return self.Gender
    class Meta: 
        verbose_name = "Gender"

class Category(models.Model):
    Name = models.CharField(max_length=255, blank=False)

    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.Name


class Subcategory(models.Model):
    Name = models.CharField(max_length=255, blank=False)
    ParentCategory = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    Gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.SET_NULL)
   
    class Meta: 
        verbose_name = "Sub Category"
        verbose_name_plural = "Sub Categories"

    def __str__(self):
        return self.ParentCategory.Name + " - " + self.Name + " - " + self.Gender.Gender

class Brand(models.Model):
    Name = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.Name
    class Meta: 
        verbose_name = "Brand"


class Size(models.Model):
    Size = models.CharField(max_length=255, blank=False)
    def __str__(self):
        return self.Size
    class Meta: 
        verbose_name = "Size"

def product_image_handle(self, filename):
    file_path = pathlib.Path(filename)
    category = self.Category.Name
    gender = self.Gender.Gender
    subcategory = self.Subcategory.Name
    name = self.Name
    return f"products/{category}/{gender}/{subcategory}/{name}/{file_path}"


class Product(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255, blank=False)
    Description = models.CharField(max_length=255, blank=True)
    Size = models.ForeignKey(Size, null=True, blank=True, on_delete=models.SET_NULL)
    Category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    Gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.SET_NULL)
    Subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.SET_NULL)
    Brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL)
    Price = models.IntegerField()
    Featured = models.BooleanField(default=False)
    Latest = models.BooleanField(default=False)

    

    Image1 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)
    Image2 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)
    Image3 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)
    Image4 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)
    Image5 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)
    Image6 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)
    Image7 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)
    Image8 = models.ImageField(upload_to=product_image_handle, null=True, blank=True)

    def __str__(self):
        return self.Name
    class Meta: 
        verbose_name = "Product"

