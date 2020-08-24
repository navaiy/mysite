from builtins import print

from blog.models import UserProfile, Article
from django.shortcuts import get_object_or_404, Http404


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
            form.instance.author = UserProfile.objects.get(user=self.request.user, )
            # form.instance.status = 'پ'
        return super().form_valid(form)


class AuthorAccessMixin():
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        if article.author.user ==request.user  and article.status in ['پ','ب'] or request.user.is_superuser :
            print("hellp")
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دیدن این صفحه ندارید")


class SuperUserMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دیدن این صفحه ندارید")
