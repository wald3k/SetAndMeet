from django.shortcuts import render

#My imports
from django.http import HttpResponse
from .models import Shout
from django.utils import timezone
from Event.models import Event
from Profile.models import Profile

import json


from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def shout_add(request):
    print "Drukuje id eventu: "
    print request.POST.get('event_id')
    shout_text = request.POST.get('text')   #Take shout 'text' that is passed from ajax
    event = Event.objects.get(pk=request.POST.get('event_id')) #Take event_id value that is passed from AJAX
    user = request.user                         #Take the user that posted this request
    author = Profile.objects.get(user = user)
    avatar = request.POST.get('avatar')
    #print shout_text
    shout = Shout.objects.create(author = author, event = event, date_created = timezone.now(),text = shout_text)
    event_shouts = Shout.objects.filter(event = event) #event_shouts is a list []
    #response = serializers.serialize("json", event_shouts)
    # temp_list= []
    # for s in event_shouts:
    #     t = []
    #     t.append(s)
    #     t.append(s.author)
    #     temp_list.append(t)
    # all_objects = list(list(temp_list))
    response = {}
    response = serializers.serialize('json', event_shouts) #if you want to send all shouts
    print "\n\n"
    print response
    response['avatar'] = str(avatar) #jak dodac avatar do respnsa?

    return HttpResponse(response, content_type='application/json')
@login_required
def shout_list(request):
    print "Zwracam wszystkie shouty!"
    event = Event.objects.get(pk=request.POST.get('event_id')) #Take event_id value that is passed from AJAX
    user = request.user                         #Take the user that posted this request
    author = Profile.objects.get(user = user)
    event_shouts = Shout.objects.filter(event = event) #event_shouts is a list []
    response = serializers.serialize('json', event_shouts) #if you want to send all shouts
    return HttpResponse(response, content_type='application/json')
