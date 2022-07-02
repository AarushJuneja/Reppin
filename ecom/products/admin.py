from django.contrib import admin

# Register your models here.
from .models import (
    Category,
    Subcategory,
    Brand,
    Size,
    Product,
    Gender,
    
)

admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Product)