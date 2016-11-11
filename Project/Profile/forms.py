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
            user.save()

        p = Profile.objects.get(pk = user.pk)
        p.przezwisko = "Default nickname"
        p.avatar = self.cleaned_data['avatar']
        p.save()

        return user
