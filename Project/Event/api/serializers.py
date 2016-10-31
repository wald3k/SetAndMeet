from rest_framework.serializers import ModelSerializer
from Event.models import Event
class EventSerializer(ModelSerializer):
	class Meta:
		model = Event
		fields = [
			'name',
		]
