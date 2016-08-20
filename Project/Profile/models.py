from __future__ import unicode_literals

from django.db import models

#my imports
#from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key = True)
     przezwisko = models.CharField(max_length = 30)

     def __unicode__(self):
         return "%s" % (self.przezwisko)

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = Profile.objects.get_or_create(user = instance)
