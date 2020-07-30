from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import *


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        article_all = Article.objects.all().order_by('-created_at')
        article_data = []
        for article in article_all:
            article_data.append({
                'id': article.id,
                'title': article.title,
                'cover': article.cover.url,
                'contact': article.content[100:],
                'category': article.category.title,
                'created_at': article.jcreated_at()
            })

        context = {
            'article_data': article_data
        }
        return render(request, 'blog/index.html', context)


class DetailArticle(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        context = {
            'article': get_object_or_404(Article, id=kwargs.get('id'))
        }
        return render(request, 'blog/detail_article.html', context)
