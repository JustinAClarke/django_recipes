# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.urls import reverse

from django.template import loader

from .models import Category, Recipe, Ingredent


def index(request):
    categories = Category.objects.all().order_by('Title')
    context = {'categories': categories}
    return render(request, 'recipes/index.html', context)


def category(request, category):
    category = get_object_or_404(Category, pk=category)
    return render(request, 'recipes/category.html', {'category': category})

def recipe(request, category, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)
    return render(request, 'recipes/recipe.html', {'recipe': recipe})

def search(request):
    recipes=Recipe.objects.none()
    
    if(request.GET.get('q',default=None)):
        if(request.GET.get('title',default=None)):
            recipes = recipes.union(Recipe.objects.filter(Title__icontains=request.GET['q']))
        if(request.GET.get('method',default=None)):
            recipes = recipes.union(Recipe.objects.filter(Method__icontains=request.GET['q']),recipes)
        if(request.GET.get('notes',default=None)):
            recipes = recipes.union(Recipe.objects.filter(Notes__icontains=request.GET['q']),recipes)
        if(request.GET.get('ingredients',default=None)):
            recipes = recipes.union(Recipe.objects.filter(ingredent__Title__icontains=request.GET['q']),recipes)
            
    context = {'search':request.GET,'recipes':recipes}
    return render(request, 'recipes/search.html', context)

