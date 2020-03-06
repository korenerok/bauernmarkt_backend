from django.urls import path
from . import views
from .apiviews import ProductViewSet, MarketViewSet, ItemViewSet, UserViewSet, VendorViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as views_auth


router=DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('markets',MarketViewSet,basename='markets')
router.register('items',ItemViewSet,basename='items')
router.register('users',UserViewSet,basename='users')
router.register('vendors',VendorViewSet,basename='vendors')



urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views_auth.obtain_auth_token,name='login'),
]

urlpatterns += router.urls