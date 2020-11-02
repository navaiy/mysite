from django.contrib.admin.options import get_content_type_for_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import get_user_model
from blog.models import *
from account.models import *
from .mixins import *
from .forms import *
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy


class ArticleList(LoginMixin, QuerySetList, ListView):
    template_name = 'registration/account.html'


class ArticleCreate(LoginMixin, FieldMixin, FormValidMixin, CreateView):
    template_name = 'registration/article_create.html'
    # model = Article
    form_class = ArticleCreateForms


class ArticleUpdate(AuthorAccessMixin, FieldMixin, FormValidMixin, UpdateView):
    template_name = 'registration/article_create.html'
    model = Article


class ArticleDelete(AuthorAccessMixin, DeleteView):
    template_name = 'registration/article_delete.html'
    model = Article
    success_url = reverse_lazy('account:account')


class Profile(LoginMixin, UpdateView):
    template_name = 'registration/profile.html'
    form_class = ProFileForms
    success_url = reverse_lazy('account:Profile')

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
    form_class = PasswordChangeForms


class CommentaAccont(LoginMixin, QuerySetComment, ListView):
    template_name = 'registration/comment.html'
    model = Comment


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('blog:ArticleList')
