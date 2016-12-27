from django.contrib import admin
#my imports
from .models import Event, Category
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    readonly_fields=('created','modified',) #show these fields in admin panel even though they are (editable=false) im models.py
    class Meta:
        model = Event


class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category


#Registering Classes in admin panel
admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
