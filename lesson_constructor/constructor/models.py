from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid


class TeachingMethod(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Уникальное ID для данного метода'
    )

    title = models.CharField(
        max_length=1000,
        help_text='Название педагогического приёма',
        verbose_name='Заголовок'
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(
        help_text='Описание педагогического приёма',
        verbose_name='Описание'
    )

    lesson_part = models.ForeignKey(
        'LessonPart',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Фрагмент урока'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('teaching-method-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Метод обучения'
        verbose_name_plural = 'Методы обучения'


class LessonPart(models.Model):
    name = models.CharField(
        max_length=1000,
        help_text='Название фрагмента урока'
    )

    description = models.TextField(
        help_text='Описание педагогического приёма'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фрагмент урока'
        verbose_name_plural = 'Фрагменты урока'


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    method = models.ForeignKey(TeachingMethod, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_modified = models.BooleanField(default=False)
    text = models.TextField(
        max_length=5000,
        verbose_name='Текст комментария'
    )

    def __str__(self):
        len_title = 75
        if len(self.description) > len_title:
            titlestring = self.description[:len_title] + '...'
        else:
            titlestring = self.description
        return titlestring

    class Meta:
        ordering = ['created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
