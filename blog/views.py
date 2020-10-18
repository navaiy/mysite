from django.shortcuts import render, get_object_or_404
from .models import *

from django.views.generic import ListView, DetailView


# Display page home
class ArticleList(ListView):
    queryset = Article.objects.filter(status='م').order_by('-created_at')
    paginate_by = 2
    template_name = 'blog/article_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleList, self).get_context_data(**kwargs)
        context['box_list'] = Article.objects.filter(status='م').order_by('-created_at')[:3]
        context['box_comment'] = Comment.objects.all().order_by('-posted')[:3]
        return context


# Display a article
class DetailArticle(DetailView):
    template_name = 'blog/datail_article.html'

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')

        # Define access to the preview page
        if self.request.user.is_authenticated:
            obj = get_object_or_404(Article, title=title)
            obj.number_views += 1  # number_views
            obj.save()
            return obj

        else:
            obj = get_object_or_404(Article, title=title, status='م')
            obj.number_views += 1  # number_views
            obj.save()
            return obj

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DetailArticle, self).get_context_data(**kwargs)
        context['box_comment'] = Comment.objects.all().order_by('-posted')[:3]
        context['box_list'] = Article.objects.filter(status='م').order_by('-created_at')[:3]
        return context


# Display articles in a category
class ArticleListCategory(ListView):
    paginate_by = 2
    template_name = 'blog/article_list.html'

    def get_queryset(self):
        title = self.kwargs.get('title')
        category = get_object_or_404(Category, title=title)
        return category.article.filter(status='م')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListCategory, self).get_context_data(**kwargs)
        context['title'] = self.kwargs.get('title')
        # sidebar
        context['box_list'] = Article.objects.filter(status='م').order_by('-created_at')[:3]
        context['box_comment'] = Comment.objects.all().order_by('-posted')[:3]
        return context


class About(ListView):
    template_name = 'blog/about.html'
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs.get('title')
        # sidebar
        context['box_list'] = Article.objects.filter(status='م').order_by('-created_at')[:3]
        context['box_comment'] = Comment.objects.all().order_by('-posted')[:3]
        return context
