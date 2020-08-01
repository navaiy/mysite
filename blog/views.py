from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DateDetailView


# Display page home
class Index(ListView):
    queryset = Article.objects.all().order_by('-created_at')
    paginate_by = 1
    template_name = 'blog/index.html'


# Display a article
class DetailArticle(DateDetailView):
    template_name = 'blog/detail_article.html'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Article, id=id)


# Display articles in a category
class ACategory(ListView):
    paginate_by = 2
    template_name = 'blog/category.html'

    def get_queryset(self):
        title = self.kwargs.get('title')
        category = get_object_or_404(Category, title=title)
        return category.article.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs.get('title')
        return context
