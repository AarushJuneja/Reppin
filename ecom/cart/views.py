from django.shortcuts import render
from . models import Cart
from products.models import Product

def UserCart(request):
    cart = Cart.objects.get(User__Id=1)
    products = cart.Products.all()

    data = {}
    data['products'] = []

    for product in products:
        data['products'].append({
            'name' : product.Name,
            'image' : product.Image1,
            'price' : product.Price,
        }) 
    return render(request, 'core/cart.html', data)

def AddToCart(request, id):
    if(Cart.objects.get(User__Id=1)):
        cart = Cart.objects.get(User__Id=1)
    else:
        Cart.objects.create(User__Id=1)

    if(cart.Products.through.objects.filter(product_id=id)):
        incart = True
    else: 
        cart.Products.add(Product.objects.get(Id=id))

    return UserCart(request)

def RemoveFromCart(request, id):
    cart = Cart.objects.get(User__Id=1)

    if(cart.Products.through.objects.filter(product_id=id)):
        cart.Products.remove(Product.objects.get(Id=id))
    else: 
        pass

    return UserCart(request)

def Checkout(request):
    return render(request, 'core/checkout.html')