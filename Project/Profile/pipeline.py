from django.contrib.auth import get_user_model
from .models import Profile

from django.conf import settings#for user




# User details pipeline
#Ta metoda zawiera jakies bledy!
def save_profile(strategy, details, response, user=None, *args, **kwargs):
    """Update user details using data from provider."""
    if user:
        # ...
        # Just created the user?
        if kwargs['is_new']:
            attrs = {'user': user}
            # I am using also Twitter backend, so I am checking if It's FB
            # or Twitter. Might be a better way of doing this
            if strategy.backend.__class__.__name__ == 'FacebookOAuth2':
                # We should check values before this, but for the example
                # is fine
                fb_data = {
                'przezwisko': response['gender'],
                }
                attrs = dict(attrs.items() + fb_data.items())
                Profile.objects.create(
                **attrs
                )



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
    if url:
        print "DRUKUJE:**********************************************"
        print url
        print backend
        print strategy
        u = User.objects.get(email = details['email'])
        profile = Profile.objects.get(user = u)
        profile.avatar = url
        profile.save()
