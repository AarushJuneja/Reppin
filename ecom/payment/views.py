from django.shortcuts import render
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

from cart.models import Cart


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
	auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))


# def paymentpage(request):
# 	currency = 'INR'
# 	amount = 100 # Rs. 1

# 	# Create a Razorpay Order
# 	razorpay_order = razorpay_client.order.create(dict(amount=amount,
# 													currency=currency,
# 													payment_capture='0'))

# 	# order id of newly created order.
# 	razorpay_order_id = razorpay_order['id']
# 	callback_url = 'http://127.0.0.1:8000/checkout/paymenthandler/'
    

# 	# we need to pass these details to frontend.
# 	context = {}
# 	context['razorpay_order_id'] = razorpay_order_id
# 	context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
# 	context['razorpay_amount'] = amount
# 	context['currency'] = currency
# 	context['callback_url'] = callback_url

# 	return render(request, 'core/payment.html', context=context)


# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):

    total = 0

    carts = Cart.objects.filter(User__Id=1)

    for cart in carts:
        total += (cart.Product.Price * cart.Quantity)

	# only accept POST request.
    if request.method == "POST":
        try:
			# get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

			# verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is None:
                amount = total * 100 # Rs. 1
                try:

                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)

                    Cart.objects.filter(User__Id=1).delete()

                    # render success page on successful caputre of payment
                    return render(request, 'core/paymentsuccess.html')
                except:

                    # if there is an error while capturing payment.
                    return render(request, 'core/paymentfail.html')
            else:

                # if signature verification fails.
                return render(request, 'core/paymentfail.html')
        except:

            # if we don't find the required parameters in POST data
            return render(request, 'core/paymentfail.html')
    else:
    # if other than POST request is made.
        return render(request, 'core/paymentfail.html')


