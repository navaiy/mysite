# Generated by Django 3.0.8 on 2020-09-10 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='عنوان')),
                ('cover', models.ImageField(upload_to='media/article_cover/', verbose_name='عکس مقاله')),
                ('content', models.TextField(verbose_name='متن مقاله')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')),
                ('status', models.CharField(choices=[('م', 'منتشر شده'), ('پ', 'پیش نویس'), ('د', 'در صف انتشار'), ('ب', 'برگشت داده شده')], default='پ', max_length=1, verbose_name='وضعیت')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='انتشار دهنده')),
                ('category', models.ManyToManyField(related_name='article', to='blog.Category', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
