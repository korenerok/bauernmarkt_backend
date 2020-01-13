from django.contrib import admin
from .models import Vendor, MarketEvent

# Register your models here.

admin.site.register(Vendor)
admin.site.register(MarketEvent)

