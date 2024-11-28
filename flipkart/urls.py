from django.contrib import admin
from django.urls import path,include
from flipkartcustomer.views import *
from flipkartgrocery.views import*
import flipkartsale,flipkartshopping

urlpatterns = [

    path('customer/',customer,name='customer'),
    path('customercare/',customercare,name='customercare'),
    path('items/',items,name='items'),
    path('fooditems/',fooditems,name='fooditems'),
    path('flipkartsale/',include('flipkartsale.urls')),
    path('flipkartshopping/',include('flipkartshopping.urls')),
]