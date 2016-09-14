from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^profile/(?P<profile_pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile_list/$', views.ProfileListView.as_view(), name='profile-list'),
    url(r'^$', views.IndexView.as_view()),
    url(r'^wyloguj/$', views.wyloguj),
]
