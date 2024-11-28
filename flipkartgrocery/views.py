from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def items(request):
    return HttpResponse('<h1>Any food items are available here</h1>')

def fooditems(request):
    return HttpResponse('<i>Any solid foods or liquids are available here</i>')



