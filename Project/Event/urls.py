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
    url(r'^event_review/(?P<event_pk>\d+)/$', views.event_review, name='event_review'),
    url(r'^past_event_list/$', views.past_event_list, name='past_event_list'),
    url(r'^historical_event_list/$', views.historical_event_list, name='historical_event_list'),
    url(r'^upcoming_event_list/$', views.UpcomingEventListView.as_view(), name='upcoming_event_list'),
    url(r'^event_rate/(?P<event_pk>\d+)/$', views.event_rate, name='event_rate'),
    url(r'^add_event_image/$', views.add_event_image, name='add_event_image'),
]
