from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def location_taken(request,place):
#Do error handling
#Filter the photos using the {place} param
    pass