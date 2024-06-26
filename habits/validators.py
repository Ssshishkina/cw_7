from rest_framework.serializers import ValidationError


class RelatedHabitAwardValidator:
    '''Класс исключения одновременного выбора
    связанной привычки и указания вознаграждения.'''
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        rel_hab = dict(value).get(self.field1)
        award = dict(value).get(self.field2)
        if rel_hab and award:
            raise ValidationError('Нельзя одновременно заполнить и поле вознаграждения, и поле связанной привычки.')


class TimeValidator:
    '''Класс время выполнения.'''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        time = dict(value).get(self.field)
        if time is not None and int(time) > 120:
            raise ValidationError('Время выполнения должно быть не больше 120 секун.')


class RelatedHabitIsNiceValidator:
    '''Класс связанные привычки
    с признаком приятной привычки.'''
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        related_habit = dict(value).get(self.field1)
        is_nice = dict(value).get(self.field2)
        if related_habit and is_nice is True:
            raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class IsNiceValidator:
    '''Класс приятной привычки.'''
    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, value):
        rel_hab = dict(value).get(self.field1)
        is_nice = dict(value).get(self.field2)
        award = dict(value).get(self.field3)
        if is_nice is True and (rel_hab is not None and award is not None):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки.')


class PeriodicityValidator:
    '''Класс периодичности
    выполнения привычки.'''
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)
        if periodicity is not None and int(periodicity) > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')
        