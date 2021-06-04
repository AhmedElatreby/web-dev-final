from django.urls import path

from . import views

app_name = 'fresher'

urlpatterns = [
    path('', views.all_recipes, name='all_recipes'),
    path('item/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
