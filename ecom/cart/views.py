from http.client import ImproperConnectionState
from django.shortcuts import render, redirect
from numpy import product
from . models import Cart
from products.models import Product
from user.models import User

def cart_view(request):
    total = 0
    data = {}
    data['count'] = Cart.objects.filter(User__Id=1).count()
    data['products'] = []
    carts = Cart.objects.filter(User__Id=1)
    for cart in carts:
        data['products'].append({
            'id' : cart.Product.Id,
            'name': cart.Product.Name,
            'price': cart.Product.Price,
            'image': cart.Product.Image1,
            'quantity': cart.Quantity,
            'subtotal': cart.Quantity * cart.Product.Price
        })
        total += (cart.Product.Price * cart.Quantity)
    data['total'] = total
    return render(request, 'core/cart.html', data)

def AddToCart(request, id):
    if(Cart.objects.filter(User__Id=1, Product__Id=id)):
        cart = Cart.objects.get(User__Id=1, Product__Id=id)
        cart.Quantity += 1
        cart.save()
        print(cart)
        print(cart.Quantity)

    else:
        user = User.objects.get(Id=1)
        product = Product.objects.get(Id=id)
        Cart.objects.create(User=user, Product=product, Quantity=1)

    return redirect('/cart')

def RemoveFromCart(request, id):
    if(Cart.objects.filter(User__Id=1, Product__Id=id)):
        cart = Cart.objects.get(User__Id=1, Product__Id=id)
        if(cart.Quantity > 1):
            cart.Quantity -= 1
            cart.save()
        elif(cart.Quantity == 1):
            Cart.objects.filter(User__Id=1, Product__Id=id).delete()
    else:
        return redirect('/cart')
    return redirect('/cart')

def Checkout(request):
    return render(request, 'core/checkout.html')