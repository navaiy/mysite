from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from account.views import PasswordChange,Register
from mysite import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('Register/', Register.as_view(), name='Register'),
    path('password_change/', PasswordChange.as_view(), name='password_change'),
    path('', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
    path('comment/', include('comment.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('video/', include('educational_film.urls')),
    # path('video1/', include('mycollections.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
