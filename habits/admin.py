from django.contrib import admin
from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    '''Отображение списка привычек'''
    list_display = ('pk', 'owner', 'action', 'time', 'location', 'award', 'is_public',)
    search_fields = ('action',)
    list_filter = ('owner',)
