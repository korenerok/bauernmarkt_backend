from django.contrib import admin
from .models import Vendor, MarketEvent, Product, Catalog

# Register your models here.

admin.site.register(Vendor)
admin.site.register(MarketEvent)
admin.site.register(Product)
admin.site.register(Catalog)

