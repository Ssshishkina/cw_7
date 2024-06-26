from django.conf import settings
from django.db import models
from users.models import NULLABLE


class Habit(models.Model):
    '''Класс привычки:
    Поле related_habit указывается только для полезной привычки;
    Поле is_nice - признак приятной привычки, можно привязать к полезной;
    Поле award указывается только для полезной привычки, если нет привязки к приятной
    '''

    ACTION_CHOICES = [
        ('cycling', 'велопрогулка'),
        ('water', 'пить_воду'),
        ('reading', 'чтение'),
        ('fitness', 'фитнес'),
    ]

    PERIOD_CHOICES = [
        ('1', 'Ежедневно'),
        ('2', 'Каждые 2 дня'),
        ('3', 'Каждые 3 дня'),
        ('4', 'Каждые 4 дня'),
        ('5', 'Каждые 5 дней'),
        ('6', 'Каждые 6 дней'),
        ('weekly', 'Еженедельно'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки',
                              related_name='owner', help_text='Укажите создателя привычки', **NULLABLE)
    location = models.TextField(verbose_name='Место выполнения',
                                help_text='Укажите место выполнения привычки', **NULLABLE)
    time = models.TimeField(verbose_name='Когда выполнить', help_text='Укажите время выполнения привычки',
                            **NULLABLE)
    action = models.CharField(max_length=200, choices=ACTION_CHOICES, verbose_name='Что выполнить',
                              help_text='Укажите действие привычки')
    is_nice = models.BooleanField(default=False, verbose_name='Приятная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка',
                                      related_name='good_habit', **NULLABLE)
    periodicity = models.CharField(max_length=50, verbose_name='Периодичность выполнения', choices=PERIOD_CHOICES,
                                   default='daily', help_text='Укажите периодичность выполнения')
    award = models.TextField(verbose_name='Вознаграждение', help_text='Укажите вознаграждение', **NULLABLE)
    duration = models.DurationField(verbose_name='Время на выполнение', help_text='Укажите длительность выполнения',
                                    **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Публичная привычка')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'{self.owner} будет {self.action} в {self.time} в {self.location}'
