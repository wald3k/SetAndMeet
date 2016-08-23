from django.contrib import admin

#My imports
from .models import Message
# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model = Message
#Registering Classes in admin panel
admin.site.register(Message, MessageAdmin)
