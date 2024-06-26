from rest_framework import serializers
from habits.models import Habit
from habits.validators import RelatedHabitAwardValidator, TimeValidator, RelatedHabitIsNiceValidator, IsNiceValidator, \
    PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):
    '''Описываем сериализатор Привычки.'''
    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            RelatedHabitAwardValidator(field1='related_habit', field2='award'),
            TimeValidator(field='duration'),
            RelatedHabitIsNiceValidator(field1='related_habit', field2='is_nice'),
            IsNiceValidator(field1='related_habit', field2='is_nice', field3='award'),
            PeriodicityValidator(field='periodicity')
        ]
