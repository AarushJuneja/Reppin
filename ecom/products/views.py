from django.shortcuts import render
from requests import request

from products.models import Product, Category
from cart.models import Cart
from core.models import Header


header = Header.objects.first()
headings = header.Headings.all()
featured = header.Featured
latest = header.Latest

carts = Cart.objects.filter(User__Id=1)

count = 0
for cart in carts:
    count += cart.Quantity



data = {
    'Groups' : [],
    'count': count,
    'latest': latest,
    'featured': featured,
}

for heading in headings:
    group = Category.objects.get(Name=heading)
    subgroups = group.subgroups.all()

    groupobject = {
        'GroupTitle' : heading.Name,
        'SubGroups' : []
    } 
        
    for subgroup in subgroups:
        groupitems = subgroup.groupitems.all()
        subgroupobject = {
            'SubGroupTitle' : subgroup.Title,
            'GroupItems' : []
        }
        
        for groupitem in groupitems:
            subgroupobject['GroupItems'].append(groupitem.Title)

        groupobject['SubGroups'].append(subgroupobject)
    data['Groups'].append(groupobject)




def product_detail(request, id):

    product = Product.objects.get(Id=id)
    data['productData'] = {
            'id' : product.Id,
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