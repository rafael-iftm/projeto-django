from django.urls import path

from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),  # / (Home) # recipes:home
    path("recipes/<int:id>/", views.recipe, name="recipe"),  # /recipes/<int:id>/ (Recipes) # recipes:recipe
    path("recipes/category/<int:category_id>/", views.category, name="category"),  # recipes/category/<int:category_id>/ (Category) # recipes:category
]
