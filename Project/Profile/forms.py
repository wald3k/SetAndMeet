from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings #settings.AUTH_USER_MODEL
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    avatar = forms.ImageField(required = False)
    class Meta:
        model = User
        fields = {'username', 'password1', 'password2', 'email'}

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=True)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        if user.email and User.objects.filter(email=user.email).exclude(username=user.username).count():    #Check if email address is unique, otherwise raise exception
            raise forms.ValidationError(u'Email addresses must be unique.')
        if commit:
            user.save() #When User is saved then automatically Profile is created(also User post_save is called here).
            #since profile is created I can get reference to it:
            p = Profile.objects.get(pk = user.pk)
            #If form had some additional fields they could be here
            #i.e. change avatar (it will override one created in post_save create_profile fun. in models/signals.py)
            #so do it only if self.cleaned_data['avatar'] is != None
            if(self.cleaned_data['avatar'] != None):#user has chosen some avatar
                print "User chose some avatar"
                p.avatar = self.cleaned_data['avatar'] #avatar set and is no longer default img.
            p.save()#save profile to DB
        return user
