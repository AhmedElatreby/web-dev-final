from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('fresher:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Recipe(models.Model):
    category = models.ForeignKey(Category, related_name='recipe', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def get_absolute_url(self):
        return reverse('fresher:recipe_detail', args=[self.slug])

    def __str__(self):
        return self.title
