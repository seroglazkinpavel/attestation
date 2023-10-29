from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    #list_display = ('id', 'title', 'slug', 'image', 'description')
    #list_display_links = ('id', 'title')

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url} width="50">')
        return '_'

    get_photo.short_description = 'Фото'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
