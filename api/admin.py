from django.contrib import admin
from .models import Vendor, Market, Product, Item

# Register your models here.

admin.site.register(Vendor)
admin.site.register(Market)
admin.site.register(Product)
admin.site.register(Item)

