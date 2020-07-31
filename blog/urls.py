from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', Index.as_view(), name='Index'),
    path('DetailArticle/<int:id>', DetailArticle.as_view(), name='DetailArticle'),
    path('Category/<str:title>', ACategory.as_view(), name='Category'),
]
