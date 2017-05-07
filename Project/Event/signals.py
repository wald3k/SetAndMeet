from .models import EventRating, Event
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

@receiver(pre_save, sender = EventRating)
def can_add_rating(sender, instance, *args, **kwargs):
    try:
    	eventRating = EventRating.objects.get(event = instance.event, author = instance.author)
        print "Object exists, raising exception!"
        raise Exception('This user already rated this event!. Not saving to the database!')
	except model.DoesNotExist:
        print "Object doesn't exist." #object doesnt exists so pass it to save!

@receiver(post_save, sender = Event)
def set_participants(sender, instance, *args, **kwargs):
	"""This receiver is launched on post_save method for Event object. It sets the amount of participants
	participants for an event, if event was created from administrator panel."""
	try:
		event = Event.objects.get(pk = instance.pk)
		#setting cur_capacity if profiles were assigned in administrator panel
		event.cur_capacity = len(self.profiles.all())
		event.save()#save changed event to the db
	except model.DoesNotExist:
		raise Exception ('This event does not exist!)