from django.http import HttpResponse
from django.shortcuts import render
from .models import Orangecap,Purplecap
# Create your views here.

def index(request):
    return render(request, 'index.html')

def orangecap(request):
    orangecaps = Orangecap.objects.all()
    return render(request, 'orangecap.html',{'orangecaps':orangecaps})  

def purplecap(request):
    purplecaps = Purplecap.objects.all()
    return render(request, 'purplecap.html',{'purplecaps':purplecaps})

