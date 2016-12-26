from __future__ import unicode_literals

from django.db import models

#my imports
from django.contrib.auth.models import User
from django.utils import timezone
from Profile.models import Profile
from Location.models import Location
from Profile.models import Profile
from django.core.validators import MaxValueValidator, MinValueValidator #for integerfield validators

from django.db.models.signals import post_init #for adding host to participants
# Create your models here.
"""
Model to represent a category for an Event.
:name: Name of the category
"""
class Category(models.Model):
	name = models.CharField(unique = True, null = False, max_length = 30)
	description = models.TextField(blank=True)
	"""
	Meta class that contains additional info ie. verbose_name_plural.
	"""
	class Meta:
		verbose_name_plural = "Categories" #Changes plural name in admin-panel
	"""
	Displays Category in admin panel.
	Returns:
		String: name of the category
	"""
	def __unicode__(self):
		return '%s' % (self.name)



"""
 Model to contain information about an event.
 :title: Title of an event
 :category: Category of an event
 :event_start: When an event starts
 :event_end (optional): Wnen an event ends
 :description: Description of an event
 :spots: Total number of spots for the event
 :cur_capacity: Number of people currently signed to the event
"""
class Event(models.Model):
	name = models.CharField(unique=True,null=True,max_length=30)
	category = models.ForeignKey(Category, unique=False)
	created     = models.DateTimeField(editable=False)
	modified    = models.DateTimeField(editable=False)
	date_start = models.DateTimeField(blank = False,null = False)
	date_end = models.DateTimeField(blank = True, null = True)
	description = models.TextField()
	person_limit = models.PositiveIntegerField(null=True, default = 0)
	cur_capacity = models.PositiveIntegerField(editable=False, default = 0)
	fee = models.PositiveIntegerField(default = 0)
	#profiles = models.ForeignKey(Profile, on_delete=models.CASCADE)
	profiles = models.ManyToManyField(Profile, blank=True) #profile_set.get(name='name of a profile') to access elements via m2m relation or profiles.all
	host = models.ForeignKey(Profile, blank = False, null = False, related_name="hosted_events") #related name is what can be accessed from inside Profile model
	where = models.ForeignKey(Location, blank = False, null = False, related_name="location") #related name is what can be accessed from inside Profile model
	public = models.BooleanField(blank=False, null = False, default = True)					#if event is public it should be visible for everyone
	#rating = models.DecimalField(default=0, max_digits=9, decimal_places=2)					#average rating of this eventuser = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key = True)
	def __unicode__(self):
		"""
		Displays Event in admin panel.
		Returns:
			string: title of the event
		"""
		return '%s' %(self.name)


	def save(self, *args, **kwargs):
		""" On save, update timestamps """
		if not self.id:
			self.created = timezone.now()
			self.modified = self.created
		self.modified = timezone.now()
		return super(Event, self).save(*args, **kwargs)

	"""
	Adds a Profile reference to profiles list in the Event model and then saves changes to the database.
	"""
	def add_participant(self,profile):
		if isinstance(profile, Profile):
			if(not profile in self.profiles.all() and self.cur_capacity < self.person_limit):#if profile is not already on the list and there are free spots left
				self.profiles.add(profile)
				self.cur_capacity = self.cur_capacity + 1
				self.save()									#save changes to the DB
				return True									#successfully added a new profile
		return False										#Couldn't add profile to list of participants
	def add_event_rating(self, author, rating):
		print timezone.now()
		print self.date_end
		print author
		print rating
		#Check if user already rated this event:
		already_rated = EventRating.objects.filter(event = self, author = author).exists()
		if(already_rated == True):
			print "User has already rated this event!"
			return 						#exit function 
		if(rating < 1 or rating > 5):
			print "Rating out of range!"
			return
		if(self.date_end < timezone.now()): #Event is finished so participants can rate an event
			print "Go ahead rate this event"
			if(author in self.profiles.all()):#check if author of a new rating was taking part in an event
				print "This user was on the list :)"
				event_rating = EventRating.objects.create(event = self, author = author, rating = rating)
				print "Successfully saved rating!"
			else:
				print "This user was not on the list! Cannot save this rating!"
		else:								#Event has not been finished yet!
			print "Too early to rate this event!"
	"""
	Calculates average rating
	"""
	def calculate_rating(self):
		all_ratings = EventRating.objects.filter(event = self)
		result = 0
		i = 0
		if(len(all_ratings) > 0):
			for e_rating in all_ratings:
				result = result + e_rating.rating
				i = i + 1
			result = result / (i)					#If wants floating point number use this:result = result / (i * 1.0)
		print "Overal rating for event with id: " + str(self.id) + " is: " + str(result)
		return result
		

"""
Class representing raing of an event.
"""
class EventRating(models.Model):
	event  =models.ForeignKey(Event) #on_delete=models.CASCADE: when deleting Event, EventRating will also be deleted.
	author = models.ForeignKey(Profile)
	pub_date = models.DateTimeField(auto_now_add='true')
	rating = models.IntegerField(blank=False, null=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])


	#Rather than here make it in the forms
	# def save(self):
	# 	try:
	# 		eventRating = EventRating.objects.get(event = self.event, author = self.author)
	# 		print "Object exists, raising exception!"
	# 		raise Exception('This user already rated this event!. Not saving to the database!')
	# 	except EventRating.DoesNotExist:
	# 		print "Object doesn't exist." #object doesnt exists so pass it to save!