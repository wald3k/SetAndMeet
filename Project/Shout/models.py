from __future__ import unicode_literals

from django.db import models
#My inports
from Profile.models import Profile
from Event.models import Event
from django.utils import timezone
# Create your models here.


class Shout(models.Model):
    author = models.ForeignKey(Profile)
    event = models.ForeignKey(Event)
    date_created = models.DateTimeField(editable=False)
    text = models.TextField()
    def __unicode__(self):
    	"""
    	Displays Shout in admin panel.
    	Returns:
    		string: Author + text
    	"""
    	return '%s: %s' %(self.author.user.username,self.text)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        return super(Shout, self).save(*args, **kwargs)
