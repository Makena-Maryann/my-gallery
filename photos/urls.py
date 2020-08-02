from django.conf.urls import url
from . import views

urlpatterns=[
 url(r'^$',views.welcome,name='welcome'),
 url(r'^location/(?P<place>[A-Za-z])/$',views.location_taken,name = 'photoLocation' ),
]