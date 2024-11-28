from flipkartsale.views import*
from django.urls import path
urlpatterns=[

    path('offer/',offer,name='offer'),
    path('dhamaka/',dhamaka,name='dhamaka'),

]