#ten plik odpowiada za tworzenie profilu gdy uzytkownik jest tworzony
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from . import models

# Signals below won't work unless hooked up in init.py & apps.py
# http://stackoverflow.com/questions/34948102/django-pre-delete-signal-gets-ignored

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_handler(sender, instance, created, **kwargs):
	print "In create_profile_handler in signals.py file" 
    if not created:
        return
        # Create the profile object, only if it is newly created
        profile = models.Profile(user=instance)
        profile.save()


