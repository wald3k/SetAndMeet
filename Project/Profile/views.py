#from django.shortcuts import render
#from django.http import HttpResponse #dla prostego html
from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.utils import timezone

from django.views.generic import TemplateView
from django.contrib.auth import logout

# Create your views here.

from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# def login_user(request):
#     username = password = ''
#     if request.POST:
#         username = request.POST.get('username',False)
#         password = request.POST.get('password',False)
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#     #return render_to_response('base.html', context_instance=RequestContext(request))
#     return render(request, 'base.html', RequestContext(request))
#     # print "Tu jestem!"
#     # context_dict = {}


from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password = password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




@login_required
def test(request):
    current_user = request.user
    p = Profile.objects.get(user = current_user)
    context = {'profile':p}
    template = 'Profile/base.html'
    return render(request,template,context)

@login_required
def profile_detail(request,profile_pk):
    p  = Profile.objects.get(pk=profile_pk)
    context = {'profile':p}
    template = 'Profile/base.html'
    return render(request,template,context)


class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class IndexView(TemplateView):
    #template_name = 'index.html'
    template_name = 'base.html'

def wyloguj(request):
    logout(request)
    return redirect('/')
