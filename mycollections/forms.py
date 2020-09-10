from django import forms

from educational_film.models import Article, Video
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


class CollectionTitleForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ()


CollectionTitleFormSet = inlineformset_factory(
    Article, Video, form=CollectionTitleForm,
    extra=1, fields=['video', 'description'], can_delete=True
)


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CollectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('title'),
                Field('cover'),
                Field('content'),
                Field('author'),
                Field('status'),
                Fieldset('اضافه کردن فیلم',
                         Formset('titles')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
            )
        )
