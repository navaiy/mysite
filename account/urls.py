from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', ArticleList.as_view(), name='account'),
    path('ArticleCreate/Create/', ArticleCreate.as_view(), name='ArticleCreate'),
    path('ArticleUpdate/Update/<int:pk>/', ArticleUpdate.as_view(), name='ArticleUpdate'),
    path('ArticleDelete/Delete/<int:pk>/', ArticleDelete.as_view(), name='ArticleDelete'),
    path('Profile/', Profile.as_view(), name='Profile'),

]

