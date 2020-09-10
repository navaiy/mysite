from django.db import models
from django.utils.html import format_html

from account.models import User
from extensions.utils import jalali_convert_dt, jalali_convert_d


class Article(models.Model):
    CHOICES = (
        ('م', 'منتشر شده'),
        ('پ', 'پیش نویس'),
        ('د', 'در صف انتشار'),
        ('ب', 'برگشت داده شده'),
    )
    title = models.CharField(max_length=200, blank=False, null=False, unique=True, verbose_name='عنوان')
    cover = models.ImageField(upload_to='media/article_cover/', null=False, blank=False, verbose_name='عکس مقاله')
    content = models.TextField(blank=False, null=False, verbose_name='متن مقاله')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    # category = models.ManyToManyField('Category', blank=False, verbose_name='دسته بندی', related_name='article')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author' ,verbose_name='انتشار دهنده', null=False, blank=False)
    status = models.CharField(max_length=1, choices=CHOICES, verbose_name='وضعیت', null=False, blank=False, default='پ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'توضیحات فیلم آموزشی'
        verbose_name_plural = ' توضیحات فیلم های آموزشی'

    def jcreated_at(self):
        return jalali_convert_dt(self.created_at)

    def jcreated_d(self):
        return jalali_convert_d(self.created_at)

    def display_cover(self):
        return format_html(
            "<img style='width: 100px;height: 60px;  border-radius: 10px;  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'  src='{}'>".format(
                self.cover.url))

    display_cover.short_description = 'عکس'
    jcreated_at.short_description = 'زمان انتشار'


class Video(models.Model):
    video = models.FileField(upload_to='media/video/', blank=False, null=False, verbose_name='فیلم')
    description = models.CharField(max_length=400, blank=False, null=False, verbose_name='توضیحات')
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='has_titles')

    def __str__(self):
        return self.description[:50]

    class Meta:
        verbose_name = 'فیلم '
        verbose_name_plural = 'فیلم ها'
