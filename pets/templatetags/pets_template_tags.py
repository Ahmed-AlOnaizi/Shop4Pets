"""from django import template
from pets.models import Category

register = template.Library()
@register.inclusion_tag('pets/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.all(), 'current_category': current_category}"""

from django import template
from pets.models import Category
from django.template.loader import render_to_string

register = template.Library()




@register.inclusion_tag('pets/categories.html')
def get_category_list():
    categories = Category.objects.all()
    return {'categories': categories}



