from django.contrib import admin
#my imports
from .models import Event, Category
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    class Meta:
        model = Event

class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category

#Registering Classes in admin panel
admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
