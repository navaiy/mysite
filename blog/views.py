from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DateDetailView


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
class DetailArticle(DateDetailView):
    template_name = 'blog/datail_article.html'

    def get_object(self, queryset=None):
        title = self.kwargs.get('title')
        if self.request.user.is_authenticated:
            return get_object_or_404(Article, title=title)
        else:
            return get_object_or_404(Article, title=title, status='م')

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
        context['box_list'] = Article.objects.filter(status='م').order_by('-created_at')[:3]
        return context
