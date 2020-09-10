from django.contrib import admin

from educational_film.models import Article, Video


class VideoAdmin(admin.StackedInline):
    model = Video


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [VideoAdmin]


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
