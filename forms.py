from django.forms import ModelForm
from .models import Category, Recipe, Ingredient


# Create the form class.
class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        """fields = [
                    'Title',
                    'Category',
                    'Prep_Time_hour',
                    'Prep_Time_min',
                    'Cook_Time_hour',
                    'Cook_Time_min',
                    'Serves',
                    'Method',
                    'Notes',
                    'Image',
                ]"""

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [ 'Title' ]


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = [ 'Title', 'Unit', 'Quantity',]


