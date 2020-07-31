from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from django.core.paginator import Paginator


# Display page home
class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all().order_by('-created_at')
        # Paginator
        paginator = Paginator(objects, 2)
        page_number = request.GET.get('page')
        article_all = paginator.get_page(page_number)

        article_data = []
        for article in article_all:
            article_data.append({
                'id': article.id,
                'title': article.title,
                'cover': article.cover.url,
                'contact': article.content[100:],
                'category': ' , '.join([category.title for category in article.category.all()]),
                'created_at': article.jcreated_at(),
            })

        context = {
            'article_data': article_data,
            'paginator': article_all,
        }
        return render(request, 'blog/index.html', context)


# Display a article
class DetailArticle(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        context = {
            'article': get_object_or_404(Article, id=kwargs.get('id'))
        }
        return render(request, 'blog/detail_article.html', context)


# Display articles in a category
class ACategory(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        article_all = get_object_or_404(Category, title=kwargs.get('title'))
        article_data = []
        for article in article_all.article.all():
            article_data.append({
                'id': article.id,
                'title': article.title,
                'cover': article.cover.url,
                'contact': article.content[100:],
                'category': ' , '.join([category.title for category in article.category.all()]),
                'created_at': article.jcreated_at()
            })

        context = {
            'article_data': article_data
        }
        return render(request, 'blog/category.html', context)
