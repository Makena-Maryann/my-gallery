from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
 url(r'^$',views.all_images,name='allImages'),
 url(r'^photo/(\d+)',views.image_by_id,name='photo'),
 url(r'^location/(\d+)/$',views.images_by_location_taken,name = 'photoLocation' ),
 url(r'^search/',views.search_results,name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#(?P<place>[A-Za-z])