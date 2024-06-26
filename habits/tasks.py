from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from habits.services import send_tg_message


# тестовая задача проверки celery
# @shared_task
# def add():
#     print('Hello, world!')


@shared_task
def send_tg_habits_reminder():
    '''ТГ-рассылка напоминаний о том, в какое время и какие
    привычки необходимо выполнять, если дата выполнения - сегодня.'''
    today = timezone.now()       # .today().date отобразится в формате даты
    print('today')
    habits = Habit.objects.all()     # фильтруем привычки
    #telegram_id_list = []     # выводим список привычек

    for habit in habits:
        chat_id = habit.user.telegram_id
        print('chat_id')
        if habit.time >= today:
            message = f'Привет! Выполни {habit.action} {habit.time}, место - {habit.location}'
            send_tg_message(chat_id, message)
        #telegram_id_list.append(habit.owner.telegram_id)
        if habit.periodicity == '1':
            habit.time = today + timedelta(days=1)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=2)
        elif habit.periodicity == '3':
            habit.time = today + timedelta(days=3)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=4)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=5)
        elif habit.periodicity == '2':
            habit.time = today + timedelta(days=6)
        else:
            habit.time = today + timedelta(days=7)
        habit.save()
        