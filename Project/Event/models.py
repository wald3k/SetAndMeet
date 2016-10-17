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
	profiles = models.ManyToManyField(Profile, blank=True) #profile_set.get(name='name of a profile') to access elements via m2m relation
	host = models.ForeignKey(Profile, blank = False, null = False, related_name="hosted_events") #related name is what can be accessed from inside Profile model
	where = models.ForeignKey(Location, blank = False, null = False, related_name="location") #related name is what can be accessed from inside Profile model
	public = models.BooleanField(blank=False, null = False, default = True)					#if event is public it should be visible for everyone
	rating = models.DecimalField(default=0, max_digits=9, decimal_places=2)					#average rating of this event
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

class EventRating(models.Model):
	event = models.ForeignKey(Event)
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
