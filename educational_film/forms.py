from django import forms
from django.forms.models import inlineformset_factory, ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

from educational_film.models import Video, Article


class VideoForms(ModelForm):
    class Meta:
        model = Video
        exclude = ()


VideoFormsSet = inlineformset_factory(
    Article, Video, VideoForms, extra=1,can_delete=True)


class ArticleForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'cover', 'content', 'author', 'status']

    def __init__(self, *args, **kwargs):
        super(ArticleForms, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('subject'),
                Field('owner'),
                Fieldset('Add titles',
                         Formset('titles')),
                Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
            )
        )
