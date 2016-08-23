from __future__ import unicode_literals

from django.db import models

#My imports
from Profile.models import Profile

# Create your models here.

class Message(models.Model):
    receiver = models.ForeignKey(Profile, related_name='received_messages')
    sender = models.ForeignKey(Profile, related_name='sent_messages')
    subject = models.CharField(max_length = 30)
    body = models.TextField()
    date_sent = models.DateTimeField()

    def __unicode__(self):
        return '%s' % (self.subject)
