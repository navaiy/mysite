from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'avatar', 'description','is_author', 'number_points')
UserAdmin.list_display += ('number_points', 'avatar','is_author')
admin.site.register(User, UserAdmin)
