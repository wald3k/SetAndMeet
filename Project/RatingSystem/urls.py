from django.conf.urls import url
from . import views

#My imports
from django.contrib.auth import views as contrib_views

urlpatterns = [
    url(r'^add_event_review/(?P<event_pk>\d+)/(?P<author_pk>\d+)/(?P<rating>\d+)/$', views.add_event_review, name='add_event_review'),
]
