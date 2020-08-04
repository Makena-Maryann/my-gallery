from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Image,Location,Category

# Create your views here.
def all_images(request):
    photos = Image.get_images()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request,'photos/all-photos.html', {"photos":photos, "locations":locations, "categories":categories,})

def images_by_location_taken(request,location_id):
    photos = Image.filter_images_by_location(location_id)
    return render(request, 'photos/photo-location.html',{"photos":photos}) 

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        category = request.GET.get("photo")
        searched_images = Image.search_image(category) 
        message =f"{category}"

        return render(request, 'photos/search.html',{"message":message, "photos": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})

def image_by_id(request,image_id):
    try:
        photo = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photos/photo.html", {"photo":photo})                