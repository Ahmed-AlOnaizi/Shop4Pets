

from django import template
from pets.models import Category
from django.template.loader import render_to_string

register = template.Library()




@register.inclusion_tag('pets/categories.html')
def get_category_list():
    categories = Category.objects.all()
    return {'categories': categories}



