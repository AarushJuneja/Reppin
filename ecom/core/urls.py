from ecom import settings
from django.urls import path

from .views import (
    homepage_view,
    category_view,
    category_gender_view,
    category_gender_subcategory_view,
    brand_view,
)

from core.models import (
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


urlpatterns = [
    path(
        '',
        homepage_view,
        name='homepage_view',
    ),

    path(
        'A/<str:category>',
        category_view,
        name='category_view',
    ),

    path(
        'B/<str:brand>',
        brand_view,
        name='brand_view',
    ),

    path(
        'C/<str:category>/<str:gender>',
        category_gender_view,
        name='category_gender_view',
    ),

    path(
        'D/<str:category>/<str:gender>/<str:subcategory>',
        category_gender_subcategory_view,
        name='category_gender_subcategory_view',
    )
]


