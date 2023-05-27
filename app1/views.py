from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def geetha(request):
    return HttpResponse('<marquee><h1>Geetha is a Naughty girl</h1></marquee>')
