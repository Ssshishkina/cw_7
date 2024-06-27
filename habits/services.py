import requests
from config import settings


def send_tg_message(telegram_id, message):
    params = {
        'text': message,
        'chat_id': telegram_id,
    }
    response = requests.post(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
    return response.json()

    response_data = response.json()
    if not response_data.get('ok'):
        print(f"Ошибка отправки: {response_data}")
    return response_data
