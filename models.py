from django.db import models

# Create your models here.


class Category(models.Model):
    Title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.Title

    
class Ingredient(models.Model):
    Title = models.CharField(max_length=250)
    Unit = models.CharField(max_length=250)
#    Recipe = models.ForeignKey(Recipe)
    Quantity = models.FloatField()
    
    def __str__(self):
        return self.Title


class Recipe(models.Model):
    Title = models.CharField(max_length=250)
    Category = models.ForeignKey(Category)
    Prep_Time_hour = models.FloatField(default=0)
    Prep_Time_min = models.FloatField(default=0)
    Cook_Time_hour = models.FloatField(default=0)
    Cook_Time_min = models.FloatField(default=0)
    Serves = models.FloatField(default=0)
    Ingredients = models.ManyToManyField(Ingredient)
    Method = models.TextField()
    Notes = models.TextField(null=True)
    Image = models.CharField(max_length=250,null=True)
    Deleted = models.NullBooleanField()
    
    
    def __str__(self):
        return self.Title
