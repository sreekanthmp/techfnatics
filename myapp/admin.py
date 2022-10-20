from django.contrib import admin

# Register your models here.
from . models import Contact
from . models import Products
from . models import Image
from . models import Text

from . models import Socialmedia



admin.site.register(Contact)
admin.site.register(Products)
admin.site.register(Image)
admin.site.register(Text)

admin.site.register(Socialmedia)



