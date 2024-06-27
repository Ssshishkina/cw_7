import unittest
from unittest.mock import patch
from config.settings import TELEGRAM_TOKEN
from habits.services import send_tg_message


class TestTelegramBot(unittest.TestCase):
    @patch('habits.services.requests.post')
    def test_send_tg_message(self, mock_post):
        # Подготовка мокового ответа
        mock_post.return_value.json.return_value = {'ok': True}

        # Вызов функции send_telegram_message
        telegram_id = '932235308'
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
