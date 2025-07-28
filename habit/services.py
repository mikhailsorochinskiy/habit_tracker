import requests
from config import settings

def send_message_tg(text, chat_id):
    params = {
        'text': text,
        'chat_id': chat_id,
    }
    requests.get(f'https://api.telegram.org/bot{settings.TG_BOT_TOKEN}/sendMessage', params=params)
