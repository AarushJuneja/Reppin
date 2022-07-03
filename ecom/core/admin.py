from django.contrib import admin

# Register your models here.

from .models import (
    Header,
    FeaturedSection,
    SubGroup,
    GroupItem,
    Carousel,
    FeaturedBanner,
    FeaturedBrands
)
admin.site.register(FeaturedSection)
admin.site.register(Header)
admin.site.register(SubGroup)
admin.site.register(GroupItem)
admin.site.register(Carousel)
admin.site.register(FeaturedBanner)
admin.site.register(FeaturedBrands)
