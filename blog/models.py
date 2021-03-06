from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from django.db import models
from django.urls import reverse
from account.models import User
from extensions.utils import jalali_convert_dt, jalali_convert_d
from django.utils.html import format_html


class Article(models.Model):
    CHOICES_STATUS = (
        ('م', 'منتشر شده'),
        ('پ', 'پیش نویس'),
        ('د', 'در صف انتشار'),
        ('ب', 'برگشت داده شده'),
    )
    title = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name='عنوان')
    cover = models.ImageField(upload_to='media/article_cover/', null=False, blank=False, verbose_name='عکس مقاله')
    content = RichTextUploadingField(blank=False, null=False, verbose_name='متن مقاله')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    category = models.ManyToManyField('Category', blank=False, verbose_name='دسته بندی', related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='انتشار دهنده', null=False, blank=False)
    number_views = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    status = models.CharField(max_length=1, choices=CHOICES_STATUS, verbose_name='وضعیت', null=False, blank=False,default='پ')
    comments = GenericRelation(Comment, related_query_name="article")
    preview=models.TextField(verbose_name="پیش نمایش",blank=False,null=False)

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def jcreated_at(self):
        return jalali_convert_dt(self.created_at)

    def jcreated_d(self):
        return jalali_convert_d(self.created_at)

    def get_absolute_url(self):
        return reverse('account:account')

    # ِDisplay cover in panel
    def display_cover(self):
        return format_html(
            "<img style='width: 100px;height: 60px;  border-radius: 10px;  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'  src='{}'>".format(
                self.cover.url))

    # ِDisplay category in admin LTE
    def category_title(self, ):
        return ' , '.join([category.title for category in self.category.all()])

    # Column name
    display_cover.short_description = 'عکس'
    jcreated_at.short_description = 'زمان انتشار'


class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='دسته بندی ها')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
