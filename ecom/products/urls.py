from django.conf.urls.static import static
from ecom import settings
from django.urls import path

from .views import (
    product_detail,
)

urlpatterns = [

    

    path(
        '<int:id>',
        product_detail,
        name='product_detail',
    )
]

