from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Event
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.utils import timezone

from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect



"""
Returns view for a specified Event
"""
#@login_required #Not required. Everyone can see, even guests.
def event_detail(request,event_pk):
    e  = Event.objects.get(pk=event_pk)
    context = {'user':request.user,'event':e}
    if request.user.is_authenticated():
        if request.user.is_active:
            template = 'Event/event_detail.html'
            return render(request,template,context)
    else:
        template = 'Event/event_description.html'
        return render(request,template,context)





"""
Returns a list of all Events
"""
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs) #in template reference by {{ object. }}
        return context


def event_join(request,event_pk):
        e  = Event.objects.get(pk=event_pk)
        context = {'user':request.user,'event':e}
        if(e.cur_capacity < e.person_limit):
            e.cur_capacity = e.cur_capacity + 1
            e.profiles.add(request.user.profile) #see models.py for name of profile set
            e.save()
        template = 'Event/event_list.html'
        return render(request,template,context)
