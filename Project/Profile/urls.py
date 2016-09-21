from django.conf.urls import url
from . import views

#My imports
from django.contrib.auth import views as contrib_views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^profile/(?P<profile_pk>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^profile_list/$', views.ProfileListView.as_view(), name='profile-list'),
    #url(r'^$', views.IndexView.as_view()),
    url(r'^$', views.home_page),
    url(r'^auth/$', views.auth_view),
    url(r'^wyloguj/$', views.wyloguj),
    url(r'^user_created/$', views.user_created),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
]
