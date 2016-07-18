#from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def test(request):
    #context = locals()
    p  = Profile.objects.get(id=1)
    template = 'home.html'
    html = "<html><body>%s</body></html>" % p.przezwisko
    return HttpResponse(html)
