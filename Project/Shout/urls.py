from django.conf.urls import url
from . import views

#My importsviews
from django.contrib.auth import views as contrib_views

urlpatterns = [
    url(r'^shout_add/$', views.shout_add, name='shout_add'),
    url(r'^shout_list/$', views.shout_list, name='shout_list'),
]
