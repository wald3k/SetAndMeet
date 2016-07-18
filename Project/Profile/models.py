from __future__ import unicode_literals

from django.db import models

#my imports
from django.conf import settings
# Create your models here.

class Profile(models.Model):
     user = models.OneToOneField(settings.AUTH_USER_MODEL)
     przezwisko = models.CharField(max_length = 30)

     def __unicode__(self):
         return "%s" % (self.przezwisko)
