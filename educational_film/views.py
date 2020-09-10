from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic import CreateView

from educational_film.forms import VideoForms, VideoFormsSet, ArticleForms
from educational_film.models import Article


class ArticleList(CreateView):
    model = Article
    template_name = 'educational_film/list.html'
    form_class = ArticleForms
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(ArticleList, self).get_context_data(**kwargs)
        # if self.request.method == "POST":
        #     data['titles'] = VideoFormsSet(self.request.POST)
        # else:
        data['titles'] = VideoFormsSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(ArticleList, self).form_valid(form)
