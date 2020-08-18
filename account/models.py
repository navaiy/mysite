from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    number_points = models.IntegerField(default=0, null=True,blank=True, verbose_name="نعداد امتیاز")

    def __str__(self):
        return self.get_full_name()
