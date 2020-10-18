from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm, UserCreationForm
from django.utils.html import format_html
from django.utils.translation import gettext, gettext_lazy as _

from account.models import User
from blog.models import Article


class ProFileForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProFileForms, self).__init__(*args, **kwargs)
        if not user.is_superuser:
            self.fields['username'].disabled = True
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar', 'description']


class PasswordChangeForms(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = format_html(
            "<ul>"
            "<li>رمز عبور شما نمی تواند شبیه سایر اطلاعات شما باشد.</li>"
            "<li>رمز عبور شما می&zwnj;بایست حداقل از 8 حرف تشکیل شده باشد.</li>"
            "<li>رمز عبور شما نمی تواند از عبارات معروف باشد.</li>"
            "<li>رمز عبور شما نمی تواند کاملا عدد باشد.</li></ul>")


class ArticleCreateForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'cover', 'content', 'category', 'author', 'status']


class CustomUserCreationForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _('دو قسمت رمز عبور با هم مطابقت ندارند.'),
    }
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')