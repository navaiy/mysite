from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', ArticleList.as_view(), name='ArticleList'),
    path('DetailArticle/<str:title>/', DetailArticle.as_view(), name='DetailArticle'),
    path('Category/<str:title>/', ArticleListCategory.as_view(), name='ArticleListCategory'),
    path('About/', About.as_view(), name='About'),
]
