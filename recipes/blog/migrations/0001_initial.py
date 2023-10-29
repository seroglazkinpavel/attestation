# Generated by Django 4.2.6 on 2023-10-13 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Имя категории')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='Url')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225, verbose_name='Название рецепта')),
                ('slug', models.SlugField(max_length=225, unique=True, verbose_name='Url')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('preparation_steps', models.TextField(blank=True, null=True, verbose_name='Шаги проиготовления')),
                ('cooking_time', models.CharField(max_length=225, verbose_name='Время приготовления')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('ingredients', models.TextField(blank=True, null=True, verbose_name='Инградиенты')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
    ]
