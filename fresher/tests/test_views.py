from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from fresher.models import Category, Recipe
from fresher.views import all_recipes


@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_exmaple(self):
        pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='vegan chilli', slug='vegan-chilli-barney-desmazery')
        Recipe.objects.create(category_id=1, title='vegan chilli', created_by_id=1,
                              slug='vegan-chilli-barney-desmazery', price='2.99', image='recipe')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_url(self):
        """
        Test category response status
        """
        response = self.c.get(
            reverse('fresher:category_list', args=['recipe']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Example: code validation, search HTML for text
        """
        request = HttpRequest()
        response = all_recipes(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Fresher</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        """
        Example: Using request factory
        """
        request = self.factory.get('/single/recipe-recipe')
        response = all_recipes(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Fresher</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
