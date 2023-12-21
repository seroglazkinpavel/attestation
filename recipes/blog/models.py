from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=225, verbose_name='Имя категории')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})


class Recipe(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=225, verbose_name='Название рецепта')
    slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    preparation_steps = models.TextField(verbose_name='Шаги проиготовления', null=True, blank=True)
    cooking_time = models.CharField(max_length=225, verbose_name='Время приготовления')
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    ingredients = models.TextField(verbose_name='Инградиенты', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def get_absolute_url(self):
        return reverse('recipe', kwargs={"rec_slug": self.slug})
