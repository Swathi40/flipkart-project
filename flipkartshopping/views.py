from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def clothing(request):
    return HttpResponse('<h1>Clothing items are here</h1>')

def winterwear(request):
    return HttpResponse('<i>winter wear is here</i>')
