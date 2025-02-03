from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from tasks.filters import TaskFilter


from tasks.models import Task, Tag
from tasks.serializers import TaskSerializer, TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """ ViewSet для модели Task. """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = TaskFilter
    ordering_fields = ['due_date', 'created_at', 'title']
    search_fields = ['title', 'description']

    @action(detail=True, methods=['patch'])
    def complete(self, request, pk=None):
        """ Метод для перевода задачи в выполненные. """

        task = self.get_object()
        task.is_completed = True
        task.save()
        return Response({'status': 'Задача отмечена как выполненная'})


class TagViewSet(viewsets.ModelViewSet):
    """ ViewSet для модели Tag. """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
