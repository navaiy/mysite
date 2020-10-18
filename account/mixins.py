from builtins import print

from django.contrib.auth.mixins import AccessMixin
from django.db.models import Q

from account.models import User
from comment.models import Comment
from blog.models import Article
from django.shortcuts import get_object_or_404, Http404


class LoginMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or request.user.is_author:
            return self.handle_no_permission()
        else:
            return super().dispatch(request, *args, **kwargs)


class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['title', 'cover', 'content', 'category', 'author', 'status']
        else:
            self.fields = ['title', 'cover', 'content', 'category', 'status']
        return super().dispatch(request, *args, **kwargs)


class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            if not form.instance.status == 'م':
                form.instance.status = 'پ'
            form.instance.author = self.request.user

        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.author == request.user and article.status in ['پ', 'ب'] or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دیدن این صفحه ندارید")


class SuperUserMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دیدن این صفحه ندارید")


class QuerySetList():
    def get_queryset(self):

        table_search = self.request.GET.get('table_search')
        # table_switch = self.request.GET.get('table_switch')
        # print(table_switch)

        if table_search != None:
            return Article.objects.filter(Q(title__contains=table_search)).order_by('-created_at')

        elif self.request.user.is_superuser:
            # print( self.request.POST.get('switch'))
            return Article.objects.all().order_by('-created_at')
        else:
            return Article.objects.filter(author=self.request.user).order_by('-created_at')


class QuerySetComment():
    def get_queryset(self):

        if self.request.user.is_superuser:
            return Comment.objects.all()

        else:
            return Comment.objects.filter(article__author=self.request.user)
