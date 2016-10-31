from rest_framework.generics import ListAPIView
from .serializers import EventSerializer
from Event.models import Event

from rest_framework.decorators import api_view
from rest_framework.response import Response

class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# @api_view(['GET', 'PUT', 'DELETE'])
# def event_list(request):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     event = Event.objects.all()
#     serializer = EventSerializer(event)
#     return Response(serializer.data)
