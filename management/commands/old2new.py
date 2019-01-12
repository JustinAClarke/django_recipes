from django.core.management.base import BaseCommand

from recipes.olddb import db as Database

from recipes.models import Category, Recipe, Ingredient


class Command(BaseCommand):
    help='migrates from olddb to new scheme'
    def handle(self, *args, **options):
    
    #    django.setup()
        
        '''
          `id` int(11) NOT NULL AUTO_INCREMENT,
          `Board` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
          `Title` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
          `Requirements` varchar(2048) COLLATE utf8_unicode_ci DEFAULT NULL,
          `Content` varchar(2048) COLLATE utf8_unicode_ci DEFAULT NULL,
          `Notes` varchar(2048) COLLATE utf8_unicode_ci DEFAULT NULL,
          `Image` varchar(1024) COLLATE utf8_unicode_ci DEFAULT NULL,

        '''
        '''
            Title = models.CharField(max_length=250)
            Category = models.ForeignKey(Category)
            Prep_Time_hour = models.FloatField(default=0)
            Prep_Time_min = models.FloatField(default=0)
            Cook_Time_hour = models.FloatField(default=0)
            Cook_Time_min = models.FloatField(default=0)
            Serves = models.FloatField(default=0)
            #Ingredients = models.ManyToManyField(Ingredient)
            Method = models.TextField()
            Notes = models.TextField(null=True)
            Image = models.CharField(max_length=250,null=True)
            Deleted = models.NullBooleanField()
        '''

        old_db = ''

        new_db = ''

        '''
        get all from old_db;
        for each row in old_db:
            category_id=check new_db categories
            insert into new_db(id,title,category_id,method,ingredients+notes)
            commit
            continue
        '''

        '''
        #################
        Django method
        '''



        db = Database()

        all_old = db.getAll_notice_board_notices()
        for notice in all_old:
            cat_obj, created = Category.objects.get_or_create(Title=notice['Board'])
            recipe = Recipe()
            recipe.id = notice['id']
            recipe.Title = notice['Title']
            recipe.Category = cat_obj
            recipe.Ingredients = notice['Requirements']
            recipe.Method = notice['Content']
#            recipe.Notes = "{}<br>\n{}".format(notice['Requirements'],notice['Notes'])
            recipe.Notes = notice['Notes']
            recipe.save()
        #recipe = RecipeForm(request.POST,form_ingredients=False) # A form bound to the POST data
        #if recipe.is_valid(): # All validation rules pass
            #new_recipe = recipe.save()
