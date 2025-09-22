import requests
import time
import os

# توکن ربات (بعداً داخل لیارا به صورت Environment Variable قرار می‌دهیم)
BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN")

API_URL = f'https://botapi.rubika.ir/v3/{BOT_TOKEN}'

def get_updates(offset=None):
    url = f'{API_URL}/getUpdates'
    params = {'offset': offset} if offset else {}
    response = requests.get(url, params=params)
    return response.json()

def send_message(chat_id, text):
    url = f'{API_URL}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    return response.json()

def main():
    offset = None
    while True:
        updates = get_updates(offset)
        for update in updates.get('result', []):
            message = update.get('message', {})
            text = message.get('text', '')
            chat_id = message.get('chat_id', '')
            if 'سلام' in text:
                send_message(chat_id, 'علیک سلام')
            offset = update.get('update_id', 0) + 1
        time.sleep(1)

if name == 'main':
    main()