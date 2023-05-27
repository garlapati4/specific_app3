from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def roopa(request):
    return HttpResponse('<center><h1>Roopa is a Lovely girl</h1></center>')
