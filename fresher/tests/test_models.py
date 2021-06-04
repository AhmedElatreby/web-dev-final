from django.test import TestCase
from django.urls import reverse

from fresher.models import Category, Recipe


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='recipe', slug='recipe')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'recipe')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(
            reverse('store:category_list', args=[data.slug]))
        self.assertEqual(response.status_code, 200)


class TestRecipeModel(TestCase):
    def setUp(self):
        Category.objects.create(name='vegan', slug='vegan-chilli-barney-desmazery')
        self.data1 = Recipe.objects.create(recip_id=1, title='vegan chilli', created_by_id=1,
                                           slug='vegan-chilli-barney-desmazery', price='2.99', image='recipe')
        self.data2 = Recipe.recipes.create(category_id=1, title='vegan chilli', created_by_id=1,
                                           slug='vegan-chilli-barney-desmazery', price='2.99', image='recipe')

    def test_recipe_model_entry(self):
        """
        Test recipe model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Recipe))
        self.assertNotEqual(str(data), 'vegan-chilli-barney-desmazery')
