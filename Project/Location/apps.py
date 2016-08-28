#Klasa wspolpracuje z __init__ i z signals.py
from __future__ import unicode_literals
from django.apps import AppConfig

class LocationConfig(AppConfig):
    name = 'Location'
    def ready(self):
        # import signal handlers
        import Location.signals
