from django.shortcuts import render
from requests import request

from products.models import Product
from cart.models import Cart

# Create your views here.
def product_detail(request, id):
    product = Product.objects.get(Id=id)
    data = {
            'id' : product.Id,
            'count' : Cart.objects.filter(User__Id=1).count(),
            'name' : product.Name,
            'description' : product.Description,
            'size' : product.Size,
            'category' : product.Category,
            'gender' : product.Gender,
            'subcategory' : product.Subcategory,
            'brand' : product.Brand,
            'price' : product.Price,
            'featured' : product.Featured,
            'latest' : product.Latest,
            'image1' : product.Image1,
            'image2' : product.Image2,
            'image3' : product.Image3,
            'image4' : product.Image4,
            'image5' : product.Image5,
            'image6' : product.Image6, 
            'image7' : product.Image7, 
            'image8' : product.Image8,
        }
    return render(request, 'core/product.html', data)