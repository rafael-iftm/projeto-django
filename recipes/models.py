from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    """
    Represents a recipe in the application.

    Attributes:
        title (str): The title of the recipe.
        description (str): A brief description of the recipe.
        slug (str): The URL-friendly slug for the recipe.
        preparation_time (int): The preparation time for the recipe.
        preparation_time_unit (str): The unit of measurement for the preparation time.
        servings (int): The number of servings the recipe yields.
        servings_unit (str): The unit of measurement for the servings.
        preparation_steps (str): The detailed steps to prepare the recipe.
        preparation_steps_is_html (bool): Indicates if the preparation steps contain HTML.
        created_at (datetime): The date and time when the recipe was created.
        updated_at (datetime): The date and time when the recipe was last updated.
        is_published (bool): Indicates if the recipe is published.
        cover (ImageField): The image representing the recipe.
        category (Category): The category to which the recipe belongs.
        author (User): The user who created the recipe.
    """

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title