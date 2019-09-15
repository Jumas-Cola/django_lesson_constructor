# Generated by Django 2.2.4 on 2019-09-15 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogarticle',
            options={'ordering': ['-created'], 'verbose_name': 'Статья блога', 'verbose_name_plural': 'Статьи блога'},
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_modified', models.BooleanField(default=False)),
                ('text', models.TextField(max_length=5000, verbose_name='Текст комментария')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogArticle')),
            ],
            options={
                'verbose_name': 'Комментарий блога',
                'verbose_name_plural': 'Комментарии блога',
                'ordering': ['created'],
            },
        ),
    ]
