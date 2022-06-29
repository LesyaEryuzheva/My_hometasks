from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from rest_framework import generics

from .models import Task
from .serializers import TaskSerializer


class ListTask(generics.ListAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        user = self.request.user
        date = timezone.localdate()
        return super().get_queryset().filter(user=user, date__gte=date)


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)


class CreateTask(generics.CreateAPIView):
    serializer_class = TaskSerializer
