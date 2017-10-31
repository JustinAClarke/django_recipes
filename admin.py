from django.contrib import admin

# Register your models here.

from .models import Category, Recipe, Ingredent

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredent)
