from django.http import HttpResponse
from django.shortcuts import render
from .models import Horse

# Create your views here.

def index(requests):
    horse = Horse.objects.all()
    context = {
        'horse' : horse
    }
    return render(requests, "base.html", context)

def pegasus(requests):
    horse = Horse.objects.all()
    return render(requests, "horse/at.html")