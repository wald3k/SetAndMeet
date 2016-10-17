from .models import EventRating
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
