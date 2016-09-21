from __future__ import unicode_literals

from django.db import models

#my imports
#from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from Event.models import Event
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'static/avatars/user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key = True)
     przezwisko = models.CharField(max_length = 30)
     events = models.ManyToManyField(Event, null=True, blank=True)
     avatar = models.ImageField(upload_to=user_directory_path)


     def __unicode__(self):
         return "%s" % (self.user.username)

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = Profile.objects.get_or_create(user = instance)
