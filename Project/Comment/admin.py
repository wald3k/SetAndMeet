from django.contrib import admin

#My imports
from .models import PrimaryComment, SecondaryComment
# Register your models here.


class PrimaryCommentAdmin(admin.ModelAdmin):
    class Meta:
        model = PrimaryComment

class SecondaryCommentAdmin(admin.ModelAdmin):
    class Meta:
        model = SecondaryComment
#Registering Classes in admin panel
admin.site.register(PrimaryComment, PrimaryCommentAdmin)
admin.site.register(SecondaryComment, SecondaryCommentAdmin)
