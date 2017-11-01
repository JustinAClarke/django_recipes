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
    
    url(r'^test/(?P<recipe>[0-9]+)/$', views.test, name='test'),
    
]
