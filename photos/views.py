from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image

# Create your views here.
def all_images(request):
    photos = Image.get_images()
    return render(request,'photos/all-photos.html', {"photos":photos})

def images_by_location_taken(request,location_id):
    photos = Image.filter_images_by_location(location_id)
    return render(request, 'photos/photo-location.html',{"photos":photos}) 