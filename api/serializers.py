# serializers.py

from rest_framework import serializers
from .models import Timer


class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = ('id', 'webhook_url', 'duration', 'start_time', 'status')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'webhook_url': data['webhook_url'],
            'status': data['status'],
            'remaining': instance.get_remaining()
        }
