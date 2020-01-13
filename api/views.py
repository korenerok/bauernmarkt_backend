from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor,MarketEvent
from django.core import serializers
# Create your views here.

def index(request):
    return HttpResponse('Testing API')

def vendors(request):
    vendors= serializers.serialize('json', Vendor.objects.all(),fields=('name'))
    return HttpResponse(vendors)

def market_events(request):
    market_events= serializers.serialize('json', MarketEvent.objects.all(),use_natural_foreign_keys=True)
    return HttpResponse(market_events)