from django.shortcuts import render
from django.http import HttpResponse     

# Create your views here.

def customer(request):
    return HttpResponse('<h1>queries are cleared here</h1>')


def customercare(request):
    return HttpResponse('<i>Any product damaged?? call me</i>')

