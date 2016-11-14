from django.conf.urls import url
from . import views

#My imports
from django.contrib.auth import views as contrib_views

urlpatterns = [
    url(r'^event/(?P<event_pk>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^event_join/(?P<event_pk>\d+)/$', views.event_join, name='event_join'),
    url(r'^event_leave/(?P<event_pk>\d+)/$', views.event_leave, name='event_leave'),
    url(r'^event_list/$', views.EventListView.as_view(), name='event_list'),
    url(r'^event_create/$', views.event_create, name='event_create'),
]
