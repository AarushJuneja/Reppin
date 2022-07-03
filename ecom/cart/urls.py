from ecom import settings
from django.urls import path

from .views import (
    AddToCart,
    UserCart,
    Checkout
)

urlpatterns = [
    path(
        '',
        UserCart,
        name='cart',
    ),

    path(
        'checkout',
        Checkout,
        name='checkout',
    ),

    
    
]


