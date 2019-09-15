from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class BlogArticle(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_modified = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(
        max_length=10000,
        verbose_name='Текст статьи'
    )

    def __str__(self):
        return self.title

    def preview(self):
        preview_len = 200
        if len(self.text) > preview_len:
            preview_string = self.text[:preview_len] + '...'
        else:
            preview_string = self.text
        return preview_string

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])

    class Meta:
        ordering = ['-created']
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Статьи блога'


class BlogComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    method = models.ForeignKey(BlogArticle, on_delete=models.CASCADE)
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
        verbose_name = 'Комментарий блога'
        verbose_name_plural = 'Комментарии блога'
