from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendor,Market, Product, Item

# Create your views here.

def index(request):
    return HttpResponse('Testing API')