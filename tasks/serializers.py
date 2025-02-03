from rest_framework import serializers

from tasks.models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    """ Serializer для модели Tag. """

    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    """ Serializer для модели Task. """
    tags = TagSerializer(many=True)  # Возвращаем теги с именами

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'is_completed', 'created_at', 'tags']

    def create(self, validated_data):
        """ Позволяет создавать новые теги при создании задачи """
        tags_data = validated_data.pop('tags', [])
        task = Task.objects.create(**validated_data)
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_data['name'])
            task.tags.add(tag)
        return task
