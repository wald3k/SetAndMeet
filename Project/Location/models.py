# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#My imports
#Copyright © 2016 Philipp Bosch, http://pb.io/
from geoposition import Geoposition
from geoposition.fields import GeopositionField


# Create your models here.
class Location(models.Model):
    name = models.CharField(null=True,max_length = 225, blank=True)
    #  street = models.CharField(null=True,max_length = 30, blank=True)
    #  street_number = models.PositiveIntegerField(null=True,blank=True)
    #  postal_code = models.CharField(null=True,max_length = 6,blank=True)
    #  building_number = models.PositiveIntegerField(null=True,blank=True)
    #  city = models.CharField(null=True,max_length = 30,blank=True)
    #  COUNTRY_CHOICES = (('1', 'POLAND'),('2', 'USA'),('3', 'GERMANY'),('4', 'FRANCE'))
    #  country = models.CharField(max_length=9, choices=COUNTRY_CHOICES, default='POLAND')
    position = GeopositionField(default='52.229,21.011')#holds latitude & longitude + adds admin widget

    def __unicode__(self):
        return '%s' % (self.name[:40] + '...')#first X letters fro left
