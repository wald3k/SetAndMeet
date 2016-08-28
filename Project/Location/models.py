from __future__ import unicode_literals

from django.db import models
#My imports
from geoposition.fields import GeopositionField

# Create your models here.
class Location(models.Model):
     street = models.CharField(max_length = 30, blank=True)
     street_number = models.PositiveIntegerField(blank=True)
     postal_code = models.CharField(max_length = 6,blank=True)
     building_number = models.PositiveIntegerField(blank=True)
     city = models.CharField(max_length = 30,blank=True)
     address = models.CharField(max_length = 128)
     COUNTRY_CHOICES = (('1', 'POLAND'),('2', 'USA'),('3', 'GERMANY'),('4', 'FRANCE'))
     country = models.CharField(max_length=9, choices=COUNTRY_CHOICES, default='POLAND')
     position = GeopositionField() #holds latitude & longitude + adds admin widget
