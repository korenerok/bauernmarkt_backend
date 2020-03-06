from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Vendor, Market, Product, Item

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Vendor
        fields= '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields= '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Market
        fields='__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user=User(
            email= validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

    def update(self,instance,validated_data):
        user=instance
        user.email= validated_data['email']
        user.username=validated_data['username']
        user.set_password(validated_data['password'])
        user.save()
        return user

