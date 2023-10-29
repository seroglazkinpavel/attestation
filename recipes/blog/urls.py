from django.urls import path

from .views import *

urlpatterns = [
    path('', RecipeHome.as_view(), name='home'),
    path('office/', Office.as_view(), name='office'),
    path('update/<int:pk>/', NewsUpdateRecipe.as_view(), name='news_update'),
    # path('reviews/', reviews, name='reviews'),
    # path('contacts/', contacts, name='contacts'),
    # path('articles/', articles, name='articles'),
    path('category/<str:slug>', RecipeCategory.as_view(), name='category'),
    path('product/<slug:rec_slug>', ShowProduct.as_view(), name='recipe'),
    path('add-recipe/', AddRecipe.as_view(), name='add_recipe'),
    path('search/', Search.as_view(), name='search'),
]