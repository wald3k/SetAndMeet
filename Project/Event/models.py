from __future__ import unicode_literals

from django.db import models

#my imports
from django.contrib.auth.models import User
from django.utils import timezone
from Profile.models import Profile
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
