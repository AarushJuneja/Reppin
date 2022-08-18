from multiprocessing import parent_process
from tkinter import CASCADE
from django.db import models
from psutil import disk_io_counters
import pathlib
from products.models import (
    Category,
    Subcategory,
    Brand, 
    Product
)

def carousel_image_handle(self, filename):
    file_path = pathlib.Path(filename)
    return f"carousel/{file_path}"


class Header(models.Model):
    Latest = models.BooleanField(default=True)
    Featured = models.BooleanField(default=True)
    Discount = models.BooleanField(default=True)
    Headings = models.ManyToManyField(Category)
    def __str__(self):
        return "Header"
    class Meta: 
        verbose_name = "Header"


class FeaturedSection(models.Model):
    Headings = models.ManyToManyField(Category)
    def __str__(self):
        return "Featured Section"
    class Meta: 
        verbose_name = "Featured Section"


class SubGroup(models.Model):
    Title = models.CharField(max_length=255)
    ParentGroup = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subgroups')
    def __str__(self):
        return self.Title + " - " + self.ParentGroup.Name
    class Meta: 
        verbose_name = "Sub Group"
        verbose_name_plural = "Sub Groups"


class GroupItem(models.Model):
    Title = models.CharField(max_length=255)
    # Subgroup = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    ParentGroup = models.ForeignKey(SubGroup, on_delete=models.CASCADE, related_name='groupitems')
    def __str__(self):
        return self.Title + " - " + self.ParentGroup.Title + " - " + self.ParentGroup.ParentGroup.Name
    class Meta: 
        verbose_name = "Group Item"
        verbose_name_plural = "Group Items"


class Carousel(models.Model):
    Image1 = models.ImageField(upload_to=carousel_image_handle, null=True, blank=True)
    Image2 = models.ImageField(upload_to=carousel_image_handle, null=True, blank=True)
    Image3 = models.ImageField(upload_to=carousel_image_handle, null=True, blank=True)
    Image4 = models.ImageField(upload_to=carousel_image_handle, null=True, blank=True)
    Image5 = models.ImageField(upload_to=carousel_image_handle, null=True, blank=True)

    def __str__(self):
        return "Carousel"

    class Meta: 
        verbose_name = "Carousel"

class FeaturedBanner(models.Model):
    Name = models.CharField(max_length=50)
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    BrandImage = models.ImageField(upload_to="brands")
    Product1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products1")
    Product2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products2")
    Product3 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products3")
    Product4 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products4")

    def __str__(self):
        return self.Name

    class Meta: 
        verbose_name = "Featured Banner"

class FeaturedBrands(models.Model):
    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    BrandImage = models.ImageField(upload_to="brands")

    def __str__(self):
        return self.Brand.Name

    class Meta: 
        verbose_name = "Featured Brand"

