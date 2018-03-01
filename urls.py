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
from django.conf.urls import url

from . import views

app_name = 'recipes'

urlpatterns = [
    # ex: /recipe/
    url(r'^$', views.index, name='index'),
    
    # ex: /recipe/category/
    url(r'^(?P<category>[0-9]+)/$', views.category, name='category'),
    # ex: /recipe/<category>+w/<recipe>+w/
    url(r'^(?P<category>[0-9]+)/(?P<recipe>[0-9]+)/$', views.recipe, name='single'),
    
    # ex: /recipe/<query>
    url(r'^search/$', views.search, name='search'),
    
    # ex: /recipe/all
    url(r'^all/$', views.all, name='all'),
    
    # ex: /recipe/add
    url(r'^add/(?P<category>[0-9]+)/$', views.addRecipe, name='addRecipeCat'),
    url(r'^add/$', views.addRecipe, name='addRecipe'),
    
    # ex: /recipe/edit/<recipe>
    url(r'^edit/(?P<recipe>[0-9]+)/$', views.editRecipe, name='editRecipe'),
    
    # ex: /recipe/import
    url(r'^import/$', views.import_csv, name='import_csv'),
    
    # ex: /recipe/get_import_example
    url(r'^get_import_example/$', views.get_import_example, name='get_import_example'),
    
    # ex: /recipe/export
    url(r'^export/$', views.export_csv, name='export_csv'),
    
    
    url(r'^test/(?P<recipe>[0-9]+)/$', views.test, name='test'),
    
]
