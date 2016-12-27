from __future__ import unicode_literals
from django.db import models
from Event.models import Event
from Profile.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator #for integerfield validators
from django.utils import timezone
#Create your models here.
"""
Class representing raing of an event.
"""
class EventRating(models.Model):
	event  =models.ForeignKey(Event) #on_delete=models.CASCADE: when deleting Event, EventRating will also be deleted.
	author = models.ForeignKey(Profile)
	pub_date = models.DateTimeField(auto_now_add='true')
	rating = models.IntegerField(blank=False, null=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

	def __unicode__(self):
		return "%s with rating of %s stars." % (self.event.name, self.rating)

		"""
Class representing raing of an event.
"""
class ProfileRating(models.Model):
	event  =models.ForeignKey(Event) #on_delete=models.CASCADE: when deleting Event, EventRating will also be deleted.
	author = models.ForeignKey(Profile, related_name = 'author')
	rated_profile = models.ForeignKey(Profile, related_name = 'rated_profile')
	pub_date = models.DateTimeField(auto_now_add='true')
	rating = models.IntegerField(blank=False, null=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

	def __unicode__(self):
		return "Event: %s. RATING: %s stars. AUTHOR: %s." % (self.event.name, self.rating, self.author.user.username)


class EventRatingManager:
	"""Constructor. Takes event id and queries database for an event with this ID."""
	def __init__(self, event_id):
		self.event = Event.objects.get(pk = event_id)
	"""Adding rating to an event"""
	def add_event_rating(self, author, rating):
		print timezone.now()
		print self.event.date_end
		print author
		print rating
		#Check if user already rated this event:
		already_rated = EventRating.objects.filter(event = self.event, author = author).exists()
		if(already_rated == True):
			print "User has already rated this event!"
			return 						#exit function 
		if(rating < 1 or rating > 5):
			print "Rating out of range!"
			return
		if(self.event.date_end < timezone.now()): #Event is finished so participants can rate an event
			print "Go ahead rate this event"
			if(author in self.event.profiles.all()):#check if author of a new rating was taking part in an event
				print "This user was on the list :)"
				event_rating = EventRating.objects.create(event = self.event, author = author, rating = rating)
				print "Successfully saved rating!"
			else:
				print "This user was not on the list! Cannot save this rating!"
		else:								#Event has not been finished yet!
			print "Too early to rate this event!"
	"""
	Calculates average rating
	"""
	def calculate_rating(self):
		all_ratings = EventRating.objects.filter(event = self.event)
		result = 0
		i = 0
		if(len(all_ratings) > 0):
			for e_rating in all_ratings:
				result = result + e_rating.rating
				i = i + 1
			result = result / (i)					#If wants floating point number use this:result = result / (i * 1.0)
		print "Overal rating for event with id: " + str(self.event.id) + " is: " + str(result)
		return result