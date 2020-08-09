from django.db import models
from django.contrib.auth.models import User
from extensions.utils import jalali_convert_dt, jalali_convert_d
from django.utils.html import format_html


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    avatar = models.ImageField(upload_to='media/user_avatar/', null=False, blank=False, verbose_name='عکس کاربر')
    description = models.CharField(max_length=500, blank=False, null=False, verbose_name='توضیحات و رزمه')

    class Meta:
        verbose_name = 'انتشار دهنده'
        verbose_name_plural = 'انتشار دهنده ها'

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name='عنوان')
    cover = models.ImageField(upload_to='media/article_cover/', null=False, blank=False, verbose_name='عکس مقاله')
    content = models.TextField(blank=False, null=False, verbose_name='متن مقاله')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    category = models.ManyToManyField('Category', blank=False, verbose_name='دسته بندی', related_name='article')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='انتشار دهنده')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    # Change the Gregorian time to the solar
    def jcreated_at(self):
        return jalali_convert_dt(self.created_at)

    def jcreated_d(self):
        return jalali_convert_d(self.created_at)

    # ِDisplay cover in panel
    def display_cover(self):
        return format_html(
            "<img style='width: 100px;height: 60px;  border-radius: 10px;  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);'  src='{}'>".format(
                self.cover.url))

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
