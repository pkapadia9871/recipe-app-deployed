from django.test import TestCase

# Create your tests here.

from .models import Recipe                   #to access Recipe model

class RecipeModelTest(TestCase):

    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='bob', ingredients='bob, bill', cooking_time=5)

    def test_recipe_name(self):
       # Get a book object to test
       recipe = Recipe.objects.get(id=1)

       # Get the metadata for the 'name' field and use it to query its data
       field_label = recipe._meta.get_field('name').verbose_name

       # Compare the value to the expected result
       self.assertEqual(field_label, 'name')

    def test_get_absolute_url(self):
       book = Recipe.objects.get(id=1)
       #get_absolute_url() should take you to the detail page of book #1
       #and load the URL /books/list/1
       self.assertEqual(book.get_absolute_url(), '/list/1')

class RecipeFormTest(TestCase):

    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='bob', ingredients='bob, bill', cooking_time=5)