from django.urls import path
from . import views

urlpatterns=[
    path('vendors/',views.vendors,name='vendors'),
    path('markets/',views.market_events,name='market_events'),
    path('',views.index,name='index')
]