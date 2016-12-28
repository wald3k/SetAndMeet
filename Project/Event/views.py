from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, Category
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

#Imports used in event_create and dealing with forms
from .forms import EventForm, LocationForm
from Location.models import Location
from geoposition.fields import GeopositionField
from geoposition import Geoposition
from datetime import datetime
from Profile.models import Profile #import Profile object


"""
Returns view for a specified Event
"""
#@login_required #Not required. Everyone can see, even guests.
def event_detail(request,event_pk):
    e  = Event.objects.get(pk=event_pk) #get reference to event with id passed to function as an argument
    context = {'user':request.user,'event':e}   #create context dictionary(that will be passed to render class)
    if request.user.is_authenticated():
        p = Profile.objects.get(user = request.user) #get reference to Profile that is bound to this user
        if request.user.is_active and e.is_on_list(p):
            template = 'Event/event_detail.html'
        else:
            template = 'Event/event_description.html' #If user is not a participant then he cannot see event details
    else:
        template = 'Event/event_description.html'
    return render(request,template,context) #No matter what if. Return render shortcut class





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
    context = {'user':user,'event':e}                                       #adding user to the context dictinary
    if (e.profiles.filter(user_id=user.id).exists()):                       #filters profile from profiles by user_id field
        e.cur_capacity = e.cur_capacity - 1
        e.profiles.remove(request.user.profile)                             #remove from manyToMany refrecence
        e.save()
        return HttpResponseRedirect('/event_list')
    else:
        print "User was not registered for the event!"
        return HttpResponseRedirect('/')



"""
Create new Event
"""
def event_create(request):
    if request.method == 'POST': #If form was sent via POST method:
        context = {}
        form1 = EventForm( request.POST,prefix="form1")
        form2 = LocationForm( request.POST,prefix="form2")
        pos =  form2['position'].value()                                                #get list of coordinates
        lat = pos[0]                                                                    #get latitude from the list
        lng = pos[1]                                                                    #get longitude from the list
        geo = Geoposition(lat, lng)                                                     #Create a Geoposition object from the coordinates that are passed as arguments to constructor
        location = Location.objects.create(name="test", position=geo)
        name = form1['name'].value()
        cat = form1['category'].value()                                                 #category is given as an integer i.e: 1,2,3....
        category = Category.objects.get(pk=cat)                                         #get Category by pk and not by name
        d_start = form1['date_start'].value()                                           #get Date string in format 2016-12-24
        print d_start
        date_start = datetime.strptime(d_start, '%Y/%m/%d %H:%M')    #create a datetime object
        print date_start
        d_end = form1['date_end'].value()
        date_end = datetime.strptime(d_end, '%Y/%m/%d %H:%M')          #create a datetime object
        description = form1['description'].value()
        person_limit = form1['person_limit'].value()
        fee = form1['fee'].value()
        public = form1['public'].value()
        participant = request.user.profile                                              #reference to Logged Profile object
        #Create an Event object
        newly_created_event = Event.objects.create(name=name,category=category,date_start=date_start, date_end=date_end,description=description,person_limit=person_limit,fee=fee,public=public,host=participant,where=location)
        newly_created_event.add_participant(participant)                                #Adds profile to profiles list in Event model and saves changes to database.
    else:   #If entered to this URL by GET request:
        #Create a context  dictionary and pass both forms with different prefixes
        context = {
            'event_form': EventForm(prefix='form1'),
            'location_form': LocationForm(prefix='form2'),
        }
    template = 'Event/event_create.html'                                                #Destination template browswer will redirect to.
    return render(request,template, context)
