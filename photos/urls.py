from django.conf.urls import url
from . import views

urlpatterns=[
 url(r'^$',views.all_images,name='allImages'),
 url(r'^location/(?P<place>[A-Za-z])/$',views.images_by_location_taken,name = 'photoLocation' ),
]