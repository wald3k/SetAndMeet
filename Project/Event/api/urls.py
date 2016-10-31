from django.conf.urls import url
from . import views

#My imports
from django.contrib.auth import views as contrib_views

urlpatterns = [
    url(r'^$', views.EventListAPIView.as_view(), name='event_list_api'),
    # url(r'^$', views.event_list, name='event_list_api'),
]
