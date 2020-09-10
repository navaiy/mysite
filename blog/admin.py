from django.contrib import admin
from .models import *

# Rename the title
admin.site.site_header = 'مدیریت وبلاگ'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_cover', 'category_title', 'author', 'jcreated_at', 'status']
    search_fields = ['title', 'content']

    def category_title(self, obj):
        return ' , '.join([category.title for category in obj.category.all()])

    category_title.short_description = "دسته بندی"


admin.site.register(Article, ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)
