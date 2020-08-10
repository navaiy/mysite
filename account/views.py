from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import *


class ArticleList(LoginRequiredMixin,ListView):
    template_name = 'registration/account.html'
    queryset = Article.objects.all()
