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

from Event.models import Event, EventImage
from RatingSystem.models import ProfileRatingManager
import json
from django.core import serializers
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

from django.db.models import Q #for seach users
"""User logs to the application."""
def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = auth.authenticate(username=username, password = password)
    if user is not None:
        if  request.POST.get('remember_me', None):
            request.session.set_expiry(0)   #overwritting django session cookie age in seconds (0 means remember as long as browswer is opened)
        auth.login(request, user)
        #return HttpResponseRedirect('/')
        try:
            next = request.session['next']
            if (next != ""):
                print next
                print request.path
                return HttpResponseRedirect(next) #testowo
        except:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER','')) #after login go to last loaction
    else:
        return HttpResponseRedirect('/')

from django.contrib.auth.forms import UserCreationForm
from .forms import MyRegistrationForm

"""
Creating a new Profile by users.
"""
def register_profile(request):
    context = {}                                                                #create a context dictionary
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = MyRegistrationForm(data=request.POST, files=request.FILES)
            if form.is_valid():                  #validation of the form
                newly_created_user = form.save() #reference to created User object. It fires post_save function.
                print "New User object created."
                return HttpResponseRedirect('/profile_list')
            print form.errors
        else:                                                               #Entered here from method GET i.e. by typing address. It means that new form will be created.
            form = MyRegistrationForm()                                     #creating new empty form
        context.update(csrf(request))
        context['form'] = form
        return render(request, 'register_profile.html', context)

def login_secondary(request):
    next =  request.GET.get('next', '')
    context = {'next':next}
    request.session['next'] = next
    return render(request, 'login.html', context)

def user_created(request):
    return render_to_response('user_created.html')

@login_required
def test(request):
    current_user = request.user
    p = Profile.objects.get(user = current_user)
    context = {'user':request.user,'profile':p}
    template = 'Profile/base.html'
    return render(request,template,context)
"""
Returns view for a specified Profile
"""
#@login_required #Not required. Everyone can see, even guests.
def profile_detail(request,profile_pk):
    p  = Profile.objects.get(pk=profile_pk)
    #take last x events of this user
    events  = Event.objects.filter(host=p)[:10]
    #Calculating profile rating
    prm  = ProfileRatingManager()
    profile_rating = prm.calculate_rating(p)
    total_number_of_ratings = prm.get_number_of_ratings(p)
    #Getting list of all images uploaded by profile
    imgs = EventImage.objects.filter(author = p)
    number_of_pictures = len(imgs) #for javascript gallery
    pic_descriptions = []
    for desc in imgs:
        pic_descriptions.append(desc.img_desc.encode('utf8'))
    pic_descriptions = json.dumps(list(pic_descriptions))
    context = {'user':request.user,'profile':p,'hosted_events': events,'profile_rating':profile_rating,'ratings_qty':total_number_of_ratings, 'uploaded_imgs':imgs, 'number_of_pictures':number_of_pictures,'pic_descriptions':pic_descriptions}
    template = 'Profile/profile_detail.html'
    return render(request,template,context)

"""
Returns a list of all profiles
"""
class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        if(self.request.user.is_authenticated()): #if user is logged then it has his profile. Otherwise user is annonymous and doesn't have a profile.
            p  = Profile.objects.get(pk=self.request.user.id)
            context['profile']  = p
        # print "W context data"
        # context['user'] = self.request.user #no need to add user to context as in settings.py in context_processors is 'django.core.context_processors.request'
        return context

class IndexView(TemplateView):
    #template_name = 'index.html'
    template_name = 'base.html'

"""
View used to logout currently logged user
"""
def wyloguj(request):
    logout(request)
    return redirect('/')

"""
View for home page
"""
def home_page(request):
    if not request.user.is_authenticated():
        context = {}
    else:
        current_user = request.user
        p = Profile.objects.get(user = current_user)
        context = {}
        context = {'user':request.user,'profile':p}
    template = 'index.html'
    return render(request,template,context)

"""
View for finding all user Profiles that contains given part of the user.username field.
"""
class ProfileSearchView(ListView):
    model = Profile
    #select_related = ['user']
    template_name = 'profile_list.html'
    #context_object_name = 'profiles'

    def get_queryset(self):
        query = self.request.GET.get("q")
        return self.model.objects.filter(Q(user__username__icontains=query) | Q(user__email__icontains=query))
        #return self.model.objects.filter(user__username__icontains=query, user__email__icontains=query)

@login_required
def add_friend(request,profile_pk):
    logged_user = Profile.objects.get(user=request.user)                       #get currently logged user
    friend_user = Profile.objects.get(pk=profile_pk) #get user that we want to invite to friends
    print logged_user
    print friend_user
    if(logged_user == friend_user):
        print "Can't be friend with himself."
    else:
        logged_user.friends.add(friend_user)             #added a new friend
        print "Friend added"
    #return redirect(request.META['HTTP_REFERER']) #redirect to previous url.
    return redirect ('/profile/' + profile_pk)

def remove_friend(request,profile_pk):
    logged_user = Profile.objects.get(user=request.user)                       #get currently logged user
    friend_user = Profile.objects.get(pk=profile_pk) #get user that we want to invite to friends
    print logged_user
    print friend_user
    if(friend_user in logged_user.friends.all()):
        logged_user.friends.remove(friend_user)
        friend_user.friends.remove(logged_user)
        print "friend removed"
    return redirect(request.META['HTTP_REFERER']) #redirect to previous url.
