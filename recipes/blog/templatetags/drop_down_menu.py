from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/drop_down.html')
def show_drop_down_menu(drop_down_list='drop_down_menu'):
    categories = Category.objects.all()
    return {"categories": categories, "drop_down_list": drop_down_list}
