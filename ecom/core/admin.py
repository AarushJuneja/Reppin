from django.contrib import admin

# Register your models here.

from .models import (
    Header,
    FeaturedSection,
    SubGroup,
    GroupItem,
    Carousel
)
admin.site.register(FeaturedSection)
admin.site.register(Header)
admin.site.register(SubGroup)
admin.site.register(GroupItem)
admin.site.register(Carousel)
