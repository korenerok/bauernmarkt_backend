from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('vendors/<int:id>',views.vendors,name='vendors'),
    path('vendors/',views.vendors,name='vendors'),
    path('markets/<int:id>',views.market_events,name='market_events'),
    path('markets/',views.market_events,name='market_events'),
    path('products/<int:id>',views.products,name='products'),
    path('products/',views.products,name='products'),
    path('catalog/<int:market>',views.catalogs,name='catalogs'),
    path('catalog/',views.catalogs,name='catalogs'),
]