from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    '''Отображение списка пользователей'''
    list_display = ('pk', 'email', 'telegram_id',)
    search_fields = ('email',)
