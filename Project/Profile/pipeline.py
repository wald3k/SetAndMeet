from django.contrib.auth import get_user_model
from .models import Profile

from django.conf import settings#for user
import os #for deleting imagefield




"""
This method saves avatar of a facebook profile as an absolute path to an image i.e. http://...
"""
# def get_avatar(backend, strategy, details, response,
#         user=None, *args, **kwargs):
#     try:
#         from django.contrib.auth import get_user_model
#     except ImportError: # django < 1.5
#         from django.contrib.auth.models import User
#     else:
#         User = get_user_model()
#     url = None
#     if backend.name == 'facebook':
#         #url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
#         # if you need a square picture from fb, this line help you
#         url = "http://graph.facebook.com/%s/picture?width=150&height=150"%response['id']
#     if url:
#         u = User.objects.get(email = details['email'])
#         profile = Profile.objects.get(user = u)
#         profile.avatar = url
#         profile.save()



from io import BytesIO
from urllib2 import urlopen
from django.core.files import File
"""
This method saves avatar from facebook on a local drive.
"""
def get_avatar(backend, strategy, details, response,
        user=None, *args, **kwargs):
    try:
        from django.contrib.auth import get_user_model
    except ImportError: # django < 1.5
        from django.contrib.auth.models import User
    else:
        User = get_user_model()
    url = None
    if backend.name == 'facebook':
        #url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
        # if you need a square picture from fb, this line help you
        url = "http://graph.facebook.com/%s/picture?width=150&height=150"%response['id']
        u = User.objects.get(email = details['email'])
        profile = Profile.objects.get(user = u)
        response = urlopen(url)
        io = BytesIO(response.read())
        if(profile.avatar != None):#some avatar exists
            print "deleting " + profile.avatar.name
            os.remove(profile.avatar.name)#delete old avatar before saving a new one! os.remove by filepath
        profile.avatar.save("user_{}".format(u.id), File(io))
