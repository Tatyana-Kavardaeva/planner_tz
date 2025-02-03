import django_filters
from tasks.models import Task

class TaskFilter(django_filters.FilterSet):
    tags = django_filters.BaseInFilter(field_name='tags__id', lookup_expr='in')

    class Meta:
        model = Task
        fields = ['is_completed', 'tags']
