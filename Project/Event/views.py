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

"""
Registers logged user for the event(if there are still spots for the event).
"""
def event_join(request,event_pk):
        e  = Event.objects.get(pk=event_pk)                                     #get reference to an event user wants to join
        user = request.user
        context = {'user':user,'event':e}                               #adding user to the context dictinary
        if user.is_anonymous():
            #In future after successfull login it should redirect to the last location
            return HttpResponseRedirect('/login_secondary/')
        if(e.cur_capacity < e.person_limit):
            if (not e.profiles.filter(user_id=user.id).exists()):               #filters profile from profiles by user_id field
                e.cur_capacity = e.cur_capacity + 1
                e.profiles.add(request.user.profile) #see models.py for name of profile set
                e.save()
                template = 'Event/event_detail.html'
                return render(request,template,context)
            else:
                print "User already logged in!"
        else:
            print "No spots left!"
        return HttpResponseRedirect('/event_list')
        # template = 'Event/event_list.html'
        # return render(request,template,context)


"""
Unregisters user from the event
"""
def event_leave(request,event_pk):
    e  = Event.objects.get(pk=event_pk)                                     #get reference to an event user wants to join
    user = request.user
    context = {'user':user,'event':e}                               #adding user to the context dictinary
    if (e.profiles.filter(user_id=user.id).exists()):               #filters profile from profiles by user_id field
        e.cur_capacity = e.cur_capacity - 1
        e.profiles.remove(request.user.profile)                     #remove from manyToMany refrecence
        e.save()
        return HttpResponseRedirect('/event_list')
    else:
        print "User was not registered for the event!"
        return HttpResponseRedirect('/')
