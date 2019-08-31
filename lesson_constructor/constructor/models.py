from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class TeachingMethod(models.Model):
    title = models.CharField(
        max_length=1000,
        help_text="Название педагогического приёма"
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(
        help_text="Описание педагогического приёма"
    )

    lesson_part = models.ForeignKey('LessonPart', on_delete=models.SET_NULL, null=True)

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
        help_text="Название фрагмента урока"
    )

    description = models.TextField(
        help_text="Описание педагогического приёма"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фрагмент урока'
        verbose_name_plural = 'Фрагменты урока'
