from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^location_new/$', views.location_new, name='add_new_location'),
]
