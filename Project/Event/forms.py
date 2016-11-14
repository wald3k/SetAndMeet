from django.forms import ModelForm
from django import forms
from .models import Event
from geoposition.fields import GeopositionField
from Location.models import Location
from django.contrib.admin import widgets
import datetime
#Unused imports
# from django.forms.extras.widgets import SelectDateWidget  #alternative to Admin Widgets
# from selectTimeWidget import SelectTimeWidget
# Create the form class.
"""
Class represents an Event form to be shown to end-user via HTML.
"""
class EventForm(ModelForm):
    #Adding my own fields to match some of the excluded fields. These will be processed in a view.
    # date_start = forms.DateField(widget=widgets.AdminDateWidget(), initial=datetime.date.today)
    # time_start = forms.DateField(widget=widgets.AdminTimeWidget())
    # date_end = forms.DateField(widget=widgets.AdminDateWidget(), initial=datetime.date.today)
    # time_end = forms.DateField(widget=widgets.AdminTimeWidget())
    date_start = forms.DateField()
    date_end = forms.DateField()

    class Meta:
        model = Event
        #exclude = ('rating','where','host','date_start','date_end','profiles') #Excluding fields from original model
        fields=['date_start','date_end','name','category','description','person_limit','fee','public']

"""
Class represents Location form that will be shown to end-user via HTML.
"""
class LocationForm(ModelForm):
    #geo_position_field = GeopositionField()
    class Meta:
        model = Location
        fields = ('position',)
