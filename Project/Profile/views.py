#from django.shortcuts import render
#from django.http import HttpResponse #dla prostego html
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.
@login_required
def test(request):
    current_user = request.user
    p = Profile.objects.get(user = current_user)
    context = {'profile':p}
    template = 'Profile/base.html'
    return render(request,template,context)

@login_required
def profile_detail(request,profile_id):
    p  = Profile.objects.get(id=profile_id)
    context = {'profile':p}
    template = 'Profile/base.html'
    return render(request,template,context)


class IndexView(TemplateView):
    template_name = 'index.html'

def wyloguj(request):
    logout(request)
    return redirect('/')
