from flipkartshopping.views import*
from django.urls import path
urlpatterns=[

    path('clothing/',clothing,name='clothing'),
    path('winterwear/',winterwear,name='winterwear'),
   
]