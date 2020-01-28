from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor,MarketEvent, Product, Catalog
from django.core import serializers
# Create your views here.

def index(request):
    return HttpResponse('Testing API')

def vendors(request,id=None):
    if(id):
        vendors=Vendor.objects.filter(pk=id)
    else:
        vendors=Vendor.objects.all()
    return HttpResponse(serializers.serialize('json',vendors))

def market_events(request,id=None):
    if(id):
        market_events= MarketEvent.objects.filter(pk=id)
    else:
        market_events= MarketEvent.objects.all()
    return HttpResponse(serializers.serialize('json',market_events,use_natural_foreign_keys=True))

def products(request,id=None):
    if (id):
        products= Product.objects.filter(pk=id)
    else:
        products= Product.objects.all()
    return HttpResponse(serializers.serialize('json', products))

def catalogs(request, market=None):
    if (market):
        catalog=Catalog.objects.filter(market=market)
    else:
        catalog=Catalog.objects.all()
    return HttpResponse(serializers.serialize('json',catalog ,use_natural_foreign_keys=True))
