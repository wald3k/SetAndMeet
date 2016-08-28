#ten plik odpowiada za uzupelnienei danych lokalizacji gdy nowa lokalizacja jest tworzona
#Wszelkie informacje w signals.py musza byc zarejestrowane w app.py oraz musi byc podana sciezka do app.py
#w pliku __init__
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Location
from .functions_signal import fill_location_fields

@receiver(pre_save, sender=Location)
def create_location_handler(sender, instance, *args, **kwargs):
    #instance.street = str(instance.position.latitude)  + " Taka tam ulica:-)"
    fill_location_fields(instance)
