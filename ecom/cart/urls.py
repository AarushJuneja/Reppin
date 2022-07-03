from ecom import settings
from django.urls import path

from .views import (
    AddToCart,
    cart_view,
    Checkout
)

urlpatterns = [
    path(
        '',
        cart_view,
        name='cart_view',
    ),

    path(
        'checkout',
        Checkout,
        name='checkout',
    ),

    
    
]


