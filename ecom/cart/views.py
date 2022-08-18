from contextlib import redirect_stderr
from http.client import ImproperConnectionState
from django.shortcuts import render, redirect
from numpy import product
from . models import Cart
from products.models import Product
from user.models import User
import razorpay
from django.conf import settings






def cart_view(request):
    total = 0
    data = {}
    
    carts = Cart.objects.filter(User__Id=1)
    count = 0
    for cart in carts:
        count += cart.Quantity
    data['count'] = count

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

def totalcalc(id):
    carts = Cart.objects.filter(User__Id=id)
    total = 0
    for cart in carts:
        total += (cart.Product.Price * cart.Quantity)

    return total

def Checkout(request):

    amount=totalcalc(1) * 100

    razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
    currency = 'INR'

	# Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
													currency=currency,
													payment_capture='0'))

	# order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/checkout/paymenthandler/'
    

	# we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = 123
    context['currency'] = currency
    context['callback_url'] = callback_url


    total = 0

    carts = Cart.objects.filter(User__Id=1)
    count = 0
    for cart in carts:
        count += cart.Quantity
    context['count'] = count

    context['products'] = []
    carts = Cart.objects.filter(User__Id=1)
    for cart in carts:
        context['products'].append({
            'id' : cart.Product.Id,
            'name': cart.Product.Name,
            'price': cart.Product.Price,
            'image': cart.Product.Image1,
            'quantity': cart.Quantity,
            'subtotal': cart.Quantity * cart.Product.Price
        })
        total += (cart.Product.Price * cart.Quantity)
    context['total'] = total

   

    return render(request, 'core/checkout.html', context)