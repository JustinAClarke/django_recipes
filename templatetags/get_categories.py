from django import template
from recipes.models import Category
from django.shortcuts import render


register = template.Library()

@register.inclusion_tag('recipes/categories_div.html', takes_context=True)
#@register.tag
def get_categories(context):
    categories = Category.objects.all().order_by('Title')
    context = {'categories': categories}
 #   return render(request, 'recipes/categories_div.html', context)
    return context
    
