from django.db import models
from blog.models import *
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    number_points = models.IntegerField(default=0, null=True, blank=True, verbose_name="نعداد امتیاز")
    avatar = models.ImageField(upload_to='media/user_avatar/', null=True, blank=False, verbose_name='عکس کاربر')
    description = models.CharField(max_length=500, null=True, blank=False, verbose_name='توضیحات و رزمه')
    is_author = models.BooleanField(default=0, null=True, blank=False, verbose_name='نویسندگی')

    def __str__(self):
        if self.get_full_name():
            return self.get_full_name()
        else:
            return self.username
