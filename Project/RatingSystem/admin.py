from django.contrib import admin
from .models import EventRating, ProfileRating
# Register your models here.

class EventRatingAdmin(admin.ModelAdmin):
    # readonly_fields=('created','modified',) #show these fields in admin panel even though they are (editable=false) im models.py
    class Meta:
        model = EventRating


class ProfileRatingAdmin(admin.ModelAdmin):
    class Meta:
        model = ProfileRating


#Registering Classes in admin panel
admin.site.register(EventRating, EventRatingAdmin)
admin.site.register(ProfileRating, ProfileRatingAdmin)
