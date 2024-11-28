from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def offer(request):
    return HttpResponse('<h1>Discount 10%</h1>')

def dhamaka(request):
    return HttpResponse('<h1>Special offers</h1>')
