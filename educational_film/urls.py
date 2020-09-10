from django.urls import path

from .views import *

app_name = 'educational_film'
urlpatterns = [
    path('', ArticleList.as_view(), name='ArticleList'),
]