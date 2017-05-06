"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from Profile.views import IndexView
from django.views.generic import TemplateView #To go straight to a template view i.e. about/contact pages

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', admin.site.urls),
    url(r'', include('Profile.urls', namespace='Profile')),#namespaces are used in templates i.e   <a href="{% url 'Profile:profile_detail' user.userprofile.id %}">
    url(r'', include('Location.urls', namespace='Location')),
    url(r'', include('Event.urls', namespace='Event')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html')),     #Go straight to the URL
    url(r'', include('Shout.urls', namespace='Shout')),
    url(r'^api/event/',include('Event.api.urls', namespace='event-api')),
    url(r'', include('RatingSystem.urls', namespace='RankingSystem')),
    url(r'^', include('Email_sender.urls')),
]
