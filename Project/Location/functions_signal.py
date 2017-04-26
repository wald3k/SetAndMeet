# -*- coding: utf-8 -*-
from .models import Location
from geopy.geocoders import Nominatim
# Create your views here.
def fill_location_fields(location_instance):
    geolocator = Nominatim(scheme='http') #had to add (scheme='http) in constructor as there was a problem with an SSL 
    print location_instance.position
    location = geolocator.reverse(str(location_instance.position))
    l_address = location.address# Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
    location_instance.name = l_address