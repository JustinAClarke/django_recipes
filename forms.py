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
from django.forms import CharField
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
        exclude = ['Deleted']
        
    #ingredients:
    #(id,title,quantity,unit)
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('form_ingredients')
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['ingredient_count'] = 0
        if extra != 0:
            for ingredient in extra:
                self.fields['ingredient_title_{id}'.format(id=ingredient['id'])] = CharField(label="Title",initial=ingredient['Title'])
                #self.fields['ingredient_title_{id}'] = CharField(label="Title",initial=ingredient['id'])
                self.fields['ingredient_quantity_{id}'.format(id=ingredient['id'])] = CharField(label="Quantity",initial=ingredient['Quantity'])
                self.fields['ingredient_unit_{id}'.format(id=ingredient['id'])] = CharField(label="Unit",initial=ingredient['Unit'])
                self.fields['ingredient_count'] += 1
            


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [ 'Title' ]
        #field_classes = {'Title':'cat_form'}
        


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = [ 'Title', 'Unit', 'Quantity',]


