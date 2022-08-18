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
    Carousel,
    FeaturedBanner,
    FeaturedBrands
)

from products.models import (
    Category,
    Subcategory,
    Brand,
    Size,
    Product,
    Gender,   
)

from cart.models import Cart

header = Header.objects.first()
headings = header.Headings.all()
banners = FeaturedBanner.objects.all()
carousel = Carousel.objects.first()
featured = header.Featured
latest = header.Latest
discount = header.Discount  
brands = FeaturedBrands.objects.all()


data = {
    'Groups' : [],
    'brands' : [],
    'latest': latest,
    'featured': featured,
    'discount': discount,
    'carousel': carousel,
}


data['banner1'] = {

        'brand': banners[0].Brand,
        'brandimage': banners[0].BrandImage,

        'product1': banners[0].Product1,
        'product1image': banners[0].Product1.Image1,
        'product1id': banners[0].Product1.Id,
        'product1brand': banners[0].Product1.Brand,
        'product1price': banners[0].Product1.Price,

        'product2': banners[0].Product2,
        'product2image': banners[0].Product2.Image1,
        'product2id': banners[0].Product2.Id,
        'product2brand': banners[0].Product2.Brand,
        'product2price': banners[0].Product2.Price,

        'product3': banners[0].Product3,
        'product3image': banners[0].Product3.Image1,
        'product3id': banners[0].Product3.Id,
        'product3brand': banners[0].Product3.Brand,
        'product3price': banners[0].Product3.Price,

        'product4': banners[0].Product4,
        'product4image': banners[0].Product4.Image1,
        'product4id': banners[0].Product4.Id,
        'product4brand': banners[0].Product4.Brand,
        'product4price': banners[0].Product4.Price,
    }


data['banner2'] = {

        'brand': banners[1].Brand,
        'brandimage': banners[1].BrandImage,

        'product1': banners[1].Product1,
        'product1image': banners[1].Product1.Image1,
        'product1id': banners[1].Product1.Id,
        'product1brand': banners[1].Product1.Brand,
        'product1price': banners[1].Product1.Price,

        'product2': banners[1].Product2,
        'product2image': banners[1].Product2.Image1,
        'product2id': banners[1].Product2.Id,
        'product2brand': banners[1].Product2.Brand,
        'product2price': banners[1].Product2.Price,

        'product3': banners[1].Product3,
        'product3image': banners[1].Product3.Image1,
        'product3id': banners[1].Product3.Id,
        'product3brand': banners[1].Product3.Brand,
        'product3price': banners[1].Product3.Price,

        'product4': banners[1].Product4,
        'product4image': banners[1].Product4.Image1,
        'product4id': banners[1].Product4.Id,
        'product4brand': banners[1].Product4.Brand,
        'product4price': banners[1].Product4.Price,
    }


for brand in brands[:3]:
    data['brands'].append({
        'name': brand.Brand,
        'image': brand.BrandImage
    })


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

    carts = Cart.objects.filter(User__Id=1)
    count = 0
    for cart in carts:
        count += cart.Quantity
    data['count'] = count    

    return render(request,'core/homepage.html', data)


def category_view(request, category):
    data['products'] = []

    carts = Cart.objects.filter(User__Id=1)
    count = 0
    for cart in carts:
        count += cart.Quantity
    data['count'] = count

    products = Product.objects.filter(Category__Name=category)
    data['totalProducts'] = products.count()
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

    carts = Cart.objects.filter(User__Id=1)
    count = 0
    for cart in carts:
        count += cart.Quantity
    data['count'] = count

    products = Product.objects.filter(Category__Name=category, Gender__Gender=gender)
    data['totalProducts'] = products.count()
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

    carts = Cart.objects.filter(User__Id=1)
    count = 0
    for cart in carts:
        count += cart.Quantity
    data['count'] = count

    products = Product.objects.filter(Category__Name=category, Gender__Gender=gender, Subcategory__Name=subcategory)
    data['totalProducts'] = products.count()
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


def brand_view(request, brand):
    data['products'] = []

    carts = Cart.objects.filter(User__Id=1)
    count = 0
    for cart in carts:
        count += cart.Quantity
    data['count'] = count
    
    products = Product.objects.filter(Brand__Name=brand)
    data['totalProducts'] = products.count()
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

