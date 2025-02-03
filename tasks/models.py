from django.db import models


NULLABLE = {"blank": True, "null": True}


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Тег")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['pk']


class Task(models.Model):
    """ Model for tasks """

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    due_date = models.DateTimeField(**NULLABLE, verbose_name="Срок")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    tags = models.ManyToManyField(Tag, **NULLABLE, verbose_name="Теги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['pk']