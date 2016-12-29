from django.shortcuts import render
from Event.models import Event
from .models import EventRatingManager, ProfileRatingManager
from Profile.models import Profile
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
#http://stackoverflow.com/questions/32323683/why-ajax-success-not-called-when-json-passed-through-django
@login_required
def add_event_review(request, event_pk,author_pk, rating):
	print "This is adding event review view!!!!!"
	print "Event_pk: %s author: %s rating: %s" % (event_pk,author_pk, rating)
	e  = Event.objects.get(pk=event_pk) #get reference to event with id passed to function as an argument
	p = Profile.objects.get(pk = author_pk)
	erm = EventRatingManager()
	success = erm.add_event_rating(e,p,int(rating))
	response = {'message': success}
	print response
	return HttpResponse(json.dumps(response), content_type='application/json')#return JSON to AJAX query