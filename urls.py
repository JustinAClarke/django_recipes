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
    
]
