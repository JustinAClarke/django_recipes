from django.core.management.base import BaseCommand

from recipes.models import Category, Recipe, Ingredient


class Command(BaseCommand):
    help = 'Deletes all Recipes, Categories and Ingredients'
    def handle(self, *args, **options):
    
        categories = Category.objects.all()
        for cat in categories:
            cat.delete()
        
        recipes = Recipe.objects.all()
        for recipe in recipes:
            recipe.delete()
        
        ingredients = Ingredient.objects.all()
        for ing in ingredients:
            ing.delete()
