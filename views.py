"""    
    Django Recipes Justin Fuhrmeister-Clarke, a web-based Recipe book.
    Copyright (C) 2017  Justin Fuhrmeiser-Clarke <justin@fuhrmeister-clarke.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    """
# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404, JsonResponse

from django.urls import reverse
from django.forms import formset_factory

from django.conf import settings

from django.template import loader

from .models import Category, Recipe, Ingredient
from .forms import *

def index(request):
    categories = Category.objects.all().order_by('Title')
    context = {'categories': categories,'title':getTitle()}
    return render(request, 'recipes/index.html', context)

def all(request):
    categories = Category.objects.all().order_by('Title')
    context = {'categories': categories,'title':getTitle()}
    return render(request, 'recipes/all.html', context)


def category(request, category):
    category = get_object_or_404(Category, pk=category)
    context = {'category': category,'title':getTitle()}
    return render(request, 'recipes/category.html', context)

def recipe(request, category, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)
    if( recipe.Deleted ):
        return render(request, 'recipes/index.html', {'error_message': "Unable to find Recipe.",})
        
    ingredients=recipe.ingredient_set.all()
    context = {'recipe': recipe,'ingredients':ingredients,'title':getTitle(recipe.Title)}
    return render(request, 'recipes/recipe.html', context)

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
            
    context = {'search':request.GET,'recipes':recipes,'title':getTitle("Search")}
    return render(request, 'recipes/search.html', context)


def addRecipe(request,category=-1):
    if request.method == "POST":
        recipe = RecipeForm(request.POST,form_ingredients=False) # A form bound to the POST data
        if recipe.is_valid(): # All validation rules pass
            new_recipe = recipe.save()
            return HttpResponseRedirect(reverse('recipes:single', args=(new_recipe.Category_id,new_recipe.id)))
    else:
        recipe = False
        recipe = RecipeForm(form_ingredients=False)
        if category != -1:
            #recipe = False
            #RecipeFormSet = formset_factory(RecipeForm, extra=2)
            #recipe = RecipeFormSet(initial=[{'category':category}])
            #recipe = recipe.form
            recipe_init = Recipe()
            recipe_init.Category = Category.objects.get(pk=category)
            recipe = RecipeForm(instance=recipe_init,ingredients=False)
        #recipe.Category = category
    context = {'request':request,'form':recipe,'category':category,'title':getTitle("Add New")}
    return render(request, 'recipes/add_edit_recipe.html',context)

def editRecipe(request, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)
    title=getTitle("Edit '" + recipe.Title +"'")
    #get ingredients:
    ingredients = get_ingredients(request,recipe)
    if request.method == "POST":
        recipe = RecipeForm(request.POST,instance=recipe, form_ingredients=ingredients) # A form bound to the POST data
        if recipe.is_valid(): # All validation rules pass
            new_recipe = recipe.save()
            #
            return HttpResponseRedirect(reverse('recipes:single', args=(new_recipe.Category_id,new_recipe.id)))
    else:
        recipe = RecipeForm(instance=recipe,form_ingredients=ingredients)
    context = {'recipe': recipe,'form':recipe,'title':title,'form_ingredients_test':ingredients}
    return render(request, 'recipes/add_edit_recipe.html', context )


def import_csv(request):
    context = {}
    if request.method == "POST":
        context['imported'] = "import POST"
        file = request.files['file']
        
    else:
        context['imported' ]= "not yet ;)"
    return render(request, 'recipes/import_csv.html', context )
    

def get_import_example(request):
    return render(request, 'recipes/import_example.html')
    
def export_csv(request):
    pass
    
def get_ingredients(request,recipe):
    #recipe = get_object_or_404(Recipe, pk=recipe)
    
    ingredients=recipe.ingredient_set.values()
    return ingredients
    
def test(request, recipe):
    recipe = get_object_or_404(Recipe, pk=recipe)

    return HttpResponseRedirect(reverse('recipes:single', args=(recipe.Category_id,recipe.id)))
    
def getTitle(title=""):
    
    #string = "Recipes"
    string = ""
    try:
        string = settings.SITE_TITLE
    except:
        string = "Recipe Title"
    if(title):
        string += " - " + title
    return string
    
def ingredient_add(request):
    ingredient = IngredientForm()
    context = {'ingredient': ingredient,'form':ingredient,'title':'Ingredient Add'}
    return render(request, 'recipes/ingredients.html', context )

def category_add(request):
    category = CategoryForm()
    context = {'category': category,'form':category,'title':'Category Add'}
    return render(request, 'recipes/category_add.html', context )
    
def ingredients(request,ing_id,action):
    ingredient = get_object_or_404(Ingredient, pk=ing_id)
    title=getTitle("Edit '" + recipe.Title +"'")
    if request.method == "POST":
        ingredient = IngredientForm(request.POST,instance=recipe) # A form bound to the POST data
        if ingredient.is_valid(): # All validation rules pass
            new_ingredient = ingredient.save()
    else:
        ingredient = IngredientForm(instance=ingredient)
    context = {'ingredient': ingredient,'form':ingredient,'title':'Ingredient Edit'}
    return render(request, 'recipes/ingredients.html', context )


def categories(request,cat_id,action):
    cat = get_object_or_404(Category, pk=ing_id)
    title=getTitle("Edit '" + cat.Title +"'")
    if request.method == "POST":
        cat = IngredientForm(request.POST,instance=recipe) # A form bound to the POST data
        if cat.is_valid(): # All validation rules pass
            new_cat = cat.save()
    else:
        cat = IngredientForm(instance=recipe)
    context = {'recipe': cat,'form':cat,'title':title}
    return render(request, 'recipes/category.html', context )


#API's

def get_ing(request,recipe=-1):
    recipe = get_object_or_404(Recipe, pk=recipe)
    count=recipe.ingredient_set.count()
    error=0
    if( recipe.Deleted ):
        error=1
        data={
            'error':'Deleted'
        }
    if( not count ):
        error=1
        data={
            'error':'No Ingredients'
        }
        ingredients=recipe.ingredient_set.all()
    if( not error ):
        data={
            'ingredients':recipe.ingredient_set.all().values_list()
            }
    return JsonResponse(data)
    

def add_ing(request):
    pass

def add_cat(request):
    if request.method == "POST":
        new_cat = Category()
        new_cat.Title = request.POST.get('new_cat','')
        new_cat.save()
        data={'cat_id':new_cat.id, 'cat_title':new_cat.Title}
        return JsonResponse(data)
