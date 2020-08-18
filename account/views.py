from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from blog.models import *
from .mixins import *


class ArticleList(LoginRequiredMixin, ListView):
    template_name = 'registration/account.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all().order_by('-created_at')
        else:
            return Article.objects.filter(author__user=self.request.user).order_by('-created_at')


class ArticleCreate(LoginRequiredMixin, FieldMixin, FormValidMixin, CreateView):
    template_name = 'registration/article_create.html'
    model = Article
