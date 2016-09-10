from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
    url(r'^profile/(?P<profile_id>\d+)/$', views.profile_detail, name='profile_detail'),
    url(r'^$', views.IndexView.as_view()),
    url(r'^wyloguj/$', views.wyloguj),
]
