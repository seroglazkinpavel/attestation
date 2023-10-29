from .models import *

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Новости", 'url_name': 'news'},
    {'title': "Отзывы", 'url_name': 'reviews'},
    {'title': "Контакты", 'url_name': 'contacts'},
    {'title': "Статьи", 'url_name': 'articles'}
]


class DataMixin:
    """Создание контекста для шаблона по умолчанию"""
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context