from django.shortcuts import get_object_or_404, render

from .models import Category, Recipe


def all_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'fresher/home.html', {'recipes': recipes})


def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    recipes = Recipe.objects.filter(category=category)
    return render(request, "fresher/recipe/category.html", {"recipes": recipes})


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'fresher/recipe/single.html', {'recipe': recipe})
