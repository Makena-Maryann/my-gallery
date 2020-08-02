from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
 url(r'^$',views.all_images,name='allImages'),
 url(r'^location/(?P<place>[A-Za-z])/$',views.images_by_location_taken,name = 'photoLocation' ),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)