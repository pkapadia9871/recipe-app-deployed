from django.urls import path
from .views import RecipeListView, RecipeDetailView, recipes_home, records

app_name = 'recipes'

urlpatterns = [
   path('', recipes_home),
   path('list/', RecipeListView.as_view(), name='list'),
   path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('records', records, name='records'),
]