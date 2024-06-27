from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from habits.services import send_tg_message


# тестовая задача проверки celery
# @shared_task
# def send_tg_habits_reminder():
#     today = timezone.now().today().date
#     print(today)


@shared_task
def send_tg_habits_reminder():
    '''ТГ-рассылка напоминаний о том, в какое время и какие
    привычки необходимо выполнять, если дата выполнения - сегодня.'''
    today = timezone.now().date()     # .today().date отобразится в формате даты
    habits = Habit.objects.all()     # фильтруем привычки
    # telegram_id_list = []     # выводим список привычек

    for habit in habits:
        # Проверяем, что у пользователя есть telegram_id и время выполнения привычки соответствует сегодняшнему дню
        if habit.owner.telegram_id and habit.time.date() == today:
            # Формируем сообщение для текущей привычки
            message = f'Привет! Выполни {habit.action} {habit.time}, место - {habit.location}'
            send_tg_message(habit.owner.telegram_id, message)
        # telegram_id_list.append(habit.owner.telegram_id)

        # Обновление времени выполнения привычки в зависимости от periodicity
        if habit.periodicity == '1':
            habit.time += timedelta(days=1)
        elif habit.periodicity == '2':
            habit.time += timedelta(days=2)
        elif habit.periodicity == '3':
            habit.time += timedelta(days=3)
        elif habit.periodicity == '4':
            habit.time += timedelta(days=4)
        elif habit.periodicity == '5':
            habit.time += timedelta(days=5)
        elif habit.periodicity == '6':
            habit.time += timedelta(days=6)
        elif habit.periodicity == 'weekly':
            habit.time += timedelta(days=7)
        habit.save()
