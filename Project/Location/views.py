from django.shortcuts import render
#My imports
from .forms import LocationForm

# Create your views here.
def location_new(request):
    form = LocationForm()
    return render(request, 'Location/location_form.html', {'form': form})
