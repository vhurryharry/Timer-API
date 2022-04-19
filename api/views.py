from django.http import Http404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TimerSerializer
from .models import Timer


class TimerViewSet(viewsets.ModelViewSet):
    queryset = Timer.objects.all()

    def get_timer(self, pk):
        try:
            return Timer.objects.get(pk=pk)
        except Timer.DoesNotExist:
            raise Http404({'message': 'Timer does not exist'})

    def create(self, request):
        timer = Timer.objects.create(**request.data)
        return Response(timer.id)

    def retrieve(self, request, pk=None):
        timer = self.get_timer(pk)
        return Response(TimerSerializer(timer).data)

    @action(detail=True, methods=['put'])
    def pause(self, request, pk=None):
        timer = self.get_timer(pk)
        timer.pause()
        return Response(TimerSerializer(timer).data)

    @action(detail=True, methods=['put'])
    def resume(self, request, pk=None):
        timer = self.get_timer(pk)
        timer.resume()
        return Response(TimerSerializer(timer).data)
