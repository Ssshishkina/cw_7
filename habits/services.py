import requests
from config import settings


def send_tg_message(chart_id, message):
    params = {
        'text': message,
        'chat_id': chart_id,
    }
    response = requests.post(f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage', params=params)
    return response.json()
