from django.contrib.auth import views
from django.urls import path
from .views import *

app_name = 'account'

urlpatterns = [
    path('', ArticleList.as_view(), name='account'),
    path('ArticleCreate/Create/', ArticleCreate.as_view(), name='ArticleCreate'),
    path('ArticleUpdate/Update/<int:pk>/', ArticleUpdate.as_view(), name='ArticleUpdate'),
    path('ArticleDelete/Delete/<int:pk>/', ArticleDelete.as_view(), name='ArticleDelete'),

]

urlpatterns += [
    path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    #
    # path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
