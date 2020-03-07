from rest_framework import viewsets,generics, permissions
from rest_framework.views import APIView, Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from .models import Product,Market,Item,Vendor
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import ProductSerializer, MarketSerializer, ItemSerializer,UserSerializer, VendorSerializer
from .permissions import IsOwner, IsAdmin, ProductPermissions, UserPermissions, ItemPermissions, MarketPermissions

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class= ProductSerializer
    permission_classes=[ProductPermissions]

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class= ItemSerializer
    permission_classes=[ItemPermissions]

class MarketViewSet(viewsets.ModelViewSet):
    queryset=Market.objects.all()
    serializer_class= MarketSerializer
    permission_classes=[MarketPermissions]

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class= UserSerializer
    permission_classes=[UserPermissions]

class VendorViewSet(viewsets.ModelViewSet):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer
    permission_classes=[IsAdmin]

#class ItemByFilter(generics.ListAPIView):
#    queryset=Item.objects.all()
#    serializer_class=ItemSerializer
#
#    def list(self,request,keyword,pk):
#        filter_to_apply={'{}'.format(keyword):pk}
#        queryset=Item.objects.filter(**filter_to_apply)
#        serializer=ItemSerializer(queryset,many=True)
#        return Response(serializer.data)

class ItemByProduct(generics.ListAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

    def list(self,request,pk):
        queryset=Item.objects.filter(product=pk)
        serializer=ItemSerializer(queryset,many=True)
        return Response(serializer.data)

class ItemByMarket(generics.ListAPIView):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

    def list(self,request,pk):
        queryset=Item.objects.filter(market=pk)
        serializer=ItemSerializer(queryset,many=True)
        return Response(serializer.data)
