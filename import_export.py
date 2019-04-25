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

"""

TODO:
build system to allow importing and exporting recipes.

export (array, images=false)

get recipes from array, compress them into a csv
if not images download file to user.
if images create tmp folder, place csv and images of recipes array into tmp folder
    compress folder
    download to user.
    
import (file post, overwrite{initial creation/migration}

if file is zip,
    open into tmp folder, copy all images to stadard directory

if overwrite
    extract each line from csv to db keeping ID's.

extract each line from csv to db, creating new id's



"""
import os
import zipfile
import csv
import tempfile

from .models import Recipe

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('tmp/', zipf)
    zipf.close()



def export(recipe_id_array, export_file):
    
    with open(export_file, 'w', newline='') as csvfile:
        fieldnames = ['id','Title','Prep_Time_hour','Prep_Time_min','Cook_Time_hour','Cook_Time_min','Serves','Category','Ingredients','Method','Notes','Image','Deleted']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for recipe_id in recipe_id_array:
            recipe = Recipe.objects.get(pk=recipe_id)
            writer.writerow({
            'id':recipe.id,
            'Title':recipe.Title,
            'Prep_Time_hour':recipe.Prep_Time_hour,
            'Prep_Time_min':recipe.Prep_Time_min,
            'Cook_Time_hour':recipe.Cook_Time_hour,
            'Cook_Time_min':recipe.Cook_Time_min,
            'Serves':recipe.Serves,
            'Category':recipe.Category,
            'Ingredients':recipe.Ingredients,
            'Method':recipe.Method,
            'Notes':recipe.Notes,
            'Image':recipe.Image,
            'Deleted':recipe.Deleted
            })
        
    

