from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    '''Класс Пользователя.'''
    username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='Email', help_text='Укажите почту')
    telegram_id = models.CharField(max_length=50, verbose_name='Телеграм', help_text='Укажите id Телеграм',
                                   **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
