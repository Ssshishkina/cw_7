import unittest
from unittest.mock import patch
from config.settings import TELEGRAM_TOKEN
from habits.services import send_tg_message
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from habits.models import Habit
from users.models import User


class TestTelegramBot(unittest.TestCase):
    @patch('habits.services.requests.post')
    def test_send_tg_message(self, mock_post):
        # Подготовка мокового ответа
        mock_post.return_value.json.return_value = {'ok': True}

        # Вызов функции send_telegram_message
        telegram_id = '1768003537'
        message = 'Тестовое сообщение'
        response = send_tg_message(telegram_id, message)

        # Проверка, что функция отправила запрос на корректный URL
        mock_post.assert_called_once_with(
            'https://api.telegram.org/bot{}/sendMessage'.format(TELEGRAM_TOKEN),
            params={'text': message, 'chat_id': telegram_id}
        )

        # Проверка, что функция вернула корректный ответ
        self.assertEqual(response, {'ok': True})


if __name__ == '__main__':
    unittest.main()


class HabitTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        '''Создание и авторизация пользователя'''

        self.user = User.objects.create(email='admin_admin@sky.pro', password='vfif', is_active=True)
        self.user.set_password("vfif")
        self.user.save()
        self.client.force_authenticate(user=self.user)

        '''Создание полезной привычки'''

        self.habit = Habit.objects.create(owner=self.user, action='cycling',
                                          location='Ижевск', is_nice=True)

    def test_habit_create(self):
        '''Создание новой привычки.'''

        url = reverse('habits:habit_create')
        data = {
            "owner": self.user.pk,
            "action": "cycling",
            "location": "стадион",
            "is_nice": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_retrieve(self):
        '''Просмотр привычки'''

        path = reverse('habits:habit_view', [self.habit.id])
        response = self.client.get(path)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['action'], self.habit.action)

    def test_habit_delete(self):
        '''Удаление привычки'''

        self.client.force_authenticate(user=self.user)
        path = reverse('habits:habit_delete', [self.habit.id])
        response = self.client.delete(path)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())
