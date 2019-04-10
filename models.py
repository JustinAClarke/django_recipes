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
from django.db import models

# Create your models here.


class Category(models.Model):
    Title = models.CharField(max_length=250,unique=True)
    
    def __str__(self):
        return self.Title

class Recipe(models.Model):
    Title = models.CharField(max_length=250)
    Category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    Prep_Time_hour = models.IntegerField(default=0)
    Prep_Time_min = models.IntegerField(default=0)
    Cook_Time_hour = models.IntegerField(default=0)
    Cook_Time_min = models.IntegerField(default=0)
    Serves = models.FloatField(default=0)
    Ingredients = models.TextField(null=True)
    #Ingredients = models.ManyToManyField(Ingredient)
    Method = models.TextField()
    Notes = models.TextField(null=True)
    Image = models.ImageField(upload_to='photo_files/thumbnails',null=True)
    Deleted = models.NullBooleanField()
    
    
    def __str__(self):
        if(self.Deleted):
            return "Deleted - " + self.Title
        else:
            return self.Title

class Ingredient(models.Model):
    Title = models.CharField(max_length=250)
    Unit = models.CharField(max_length=250)
#    Recipe = models.ForeignKey(Recipe)
    Quantity = models.FloatField()
    
    def __str__(self):
        return "{quantity} {unit} {title}".format(quantity=self.Quantity,unit=self.Unit,title=self.Title)
