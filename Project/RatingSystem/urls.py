from django.conf.urls import url
from . import views

#My imports
from django.contrib.auth import views as contrib_views

urlpatterns = [
    url(r'^add_event_review/(?P<event_pk>\d+)/(?P<author_pk>\d+)/(?P<rating>\d+)/$', views.add_event_review, name='add_event_review'),
	url(r'^has_been_rated/$', views.has_been_rated, name='has_been_rated'),
	url(r'^rate_target_profile/$', views.rate_target_profile, name='rate_target_profile'),
]
