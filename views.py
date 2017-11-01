# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from django.urls import reverse

from django.template import loader

from .models import Category, Recipe, Ingredient
from .forms import *


def index(request):
    categories = Category.objects.all().order_by('Title')
    context = {'categories': categories}
    return render(request, 'recipes/index.html', context)


def category(request, category):
    category = get_object_or_404(Category, pk=category)
    return render(request, 'recipes/category.html', {'category': category})

def recipe(request, category, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)
    if( recipe.Deleted ):
        return render(request, 'recipes/index.html', {'error_message': "Unable to find Recipe.",})
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
            recipes = recipes.union(Recipe.objects.filter(Ingredient__Title__icontains=request.GET['q']),recipes)
            
    context = {'search':request.GET,'recipes':recipes}
    return render(request, 'recipes/search.html', context)


def addRecipe(request,category=-1):
    if request.method == "POST":
        recipe = RecipeForm(request.POST) # A form bound to the POST data
        if recipe.is_valid(): # All validation rules pass
            new_recipe = recipe.save()
            return HttpResponseRedirect(reverse('recipes:single', args=(new_recipe.Category_id,new_recipe.id)))
    else:
        recipe = RecipeForm()

    return render(request, 'recipes/add_edit_recipe.html',{'request':request,'form':recipe,'category':category})

def editRecipe(request, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)
    if request.method == "POST":
        recipe = RecipeForm(request.POST,instance=recipe) # A form bound to the POST data
        if recipe.is_valid(): # All validation rules pass
            new_recipe = recipe.save()
            return HttpResponseRedirect(reverse('recipes:single', args=(new_recipe.Category_id,new_recipe.id)))
    else:
        recipe = RecipeForm(instance=recipe)
    return render(request, 'recipes/add_edit_recipe.html', {'recipe': recipe,'form':recipe})




def test(request, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)

    return HttpResponseRedirect(reverse('recipes:single', args=(recipe.Category_id,recipe.id)))
    
