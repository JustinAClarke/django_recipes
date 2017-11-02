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


