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
	#print "This is adding event review view!!!!!"
	#print "Event_pk: %s author: %s rating: %s" % (event_pk,author_pk, rating)
	e  = Event.objects.get(pk=event_pk) #get reference to event with id passed to function as an argument
	p = Profile.objects.get(pk = author_pk)
	erm = EventRatingManager()
	success = erm.add_event_rating(e,p,int(rating))
	response = {'message': success}
	#print response
	return HttpResponse(json.dumps(response), content_type='application/json')#return JSON to AJAX query

"""Returns HttpResponse with dict telling if target Profile has already been rated by given author Profile for a given Event. """
@login_required
def has_been_rated(request):
	if(request.method == 'POST'):
		#Gathering information from AJAX query
		event_pk  =   request.POST['event_pk']
		author_pk =  request.POST['author_pk']
		target_pk =  request.POST['target_pk']
		rating    =  request.POST['rating']
		#Get reference to objects
		event_reference = Event.objects.get(pk=event_pk)
		author_reference = Profile.objects.get(pk = author_pk)
		target_profile_reference = Profile.objects.get(pk = target_pk)
		#Create ProfileRatingManager
		prm = ProfileRatingManager()
		already_rated = prm.check_if_already_rated(event_reference, author_reference, target_profile_reference)
		response = {'profile_was_rated': already_rated}
	else:
		response = {'error':'not a post request!'}
	return HttpResponse(json.dumps(response), content_type='application/json')#return JSON to AJAX query


def rate_target_profile(request):
	if(request.method == 'POST'):
		#Gathering information from AJAX query
		event_pk  =   request.POST['event_pk']
		author_pk =  request.POST['author_pk']
		target_pk =  request.POST['target_pk']
		rating    =  int(request.POST['rating'])
		#Get reference to objects
		event_reference = Event.objects.get(pk=event_pk)
		author_reference = Profile.objects.get(pk = author_pk)
		target_profile_reference = Profile.objects.get(pk = target_pk)
		#Create ProfileRatingManager
		prm = ProfileRatingManager()
		adding_successfull = prm.add_profile_rating(event_reference, author_reference, target_profile_reference, rating)
		response = {'rating_added': adding_successfull}
	else:
		response = {'error':'not a post request!'}
	return HttpResponse(json.dumps(response), content_type='application/json')#return JSON to AJAX query