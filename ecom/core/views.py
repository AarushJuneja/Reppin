from re import sub
from tokenize import Name
from django.shortcuts import render
from django.http import HttpResponse
from numpy import product
from core.models import (
    FeaturedSection,
    Header, 
    SubGroup,
    GroupItem,
    Carousel
)

from products.models import (
    Category,
    Subcategory,
    Brand,
    Size,
    Product,
    Gender,   
)

header = Header.objects.first()
headings = header.Headings.all()
carousel = Carousel.objects.first()
featured = header.Featured
latest = header.Latest
discount = header.Discount  

data = {
    'Groups' : [],
    'latest': latest,
    'discount': discount,
    'carousel': carousel,
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



def homepage_view(request):
    return render(request,'core/homepage.html', data)


def category_view(request, category):
    data['products'] = []
    products = Product.objects.filter(Category__Name=category)
    for product in products:
        data['products'].append({
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
        })
    return render(request,'core/shop-left-sidebar.html', data)

def category_gender_view(request, category, gender):
    data['products'] = []
    products = Product.objects.filter(Category__Name=category, Gender__Gender=gender)
    for product in products:
        data['products'].append({
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
        })
    return render(request,'core/shop-left-sidebar.html', data)

def category_gender_subcategory_view(request, category, gender, subcategory):
    data['products'] = []
    products = Product.objects.filter(Category__Name=category, Gender__Gender=gender, Subcategory__Name=subcategory)
    for product in products:
        data['products'].append({
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
        })
        print(data['products'][0]['name'])
    return render(request,'core/shop-left-sidebar.html', data)