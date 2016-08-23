from __future__ import unicode_literals

from django.db import models
#My imports
from Profile.models import Profile
from Event.models import Event
# Create your models here.
class AbstractComment(models.Model):
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile)
    body = models.TextField(blank=True)
    like = models.PositiveIntegerField(default = 0, null=True, blank=True)
    dislike = models.PositiveIntegerField(default = 0, null=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '%s' % (self.body)

class PrimaryComment(AbstractComment):
    event_id = models.ForeignKey(Event)
    answers = models.ManyToManyField('SecondaryComment', blank=True)# name in single quote, otherwise name not defined error


class SecondaryComment(AbstractComment):
    parent_comment = models.ForeignKey('PrimaryComment', blank=True)
    def __unicode__(self):
        return '%s' % (self.body)
