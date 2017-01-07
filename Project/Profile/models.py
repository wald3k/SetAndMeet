from __future__ import unicode_literals
from django.db import models
#my imports
#from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

import os
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    # return 'static/users/user_%s/%s' % (instance.user.user.username, filename)
    return 'static/users/user_{0}/{1}'.format(instance.user.id, filename)
    

class Profile(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key = True)
     przezwisko = models.CharField(max_length = 30)
     #events = models.ManyToManyField(Event, null=True, blank=True)
     avatar = models.ImageField(upload_to=user_directory_path, default='static/defaults/!default_user_avatar/user.png')# #default didn't quite work. When deleted profile the default img was also deleted
     friends = models.ManyToManyField("self",symmetrical=True, blank = True) #friends_set is a reference to friends list

     def __unicode__(self):
         return "%s" % (self.user.username)

"""When User object is created it sends signal to receivers that listen 
to post_save method and User sender"""
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    print "in create_profile in models.py file."
    """Create a Profile when a new User account is created"""
    if created:
        profile, new = Profile.objects.get_or_create(user = instance)
        print "Przezwisko to: " + profile.przezwisko
        profile.przezwisko = instance.username
        print "Ustawione Przezwisko to: " + profile.przezwisko
        #print "avatar to: " + profile.avatar
        profile.save()#saving Profile to DB
        print "New Profile saved"

# @receiver(pre_delete, sender = Profile)
# def delete_profile(sender, instance, using, **kwargs):
#     print "Pre_delete function.."
#     instance.avatar = None

"""Function that creates a folder for a user in static files"""
def create_user_folder(user):
    print "In create_folder function"
    directory = 'static/users/user_{0}'.format(user.id)
    print directory
    if not os.path.exists(directory):
        os.makedirs(directory)
        print "dir created !"