import requests
import time
import threading
from flask import Flask

# ⚡ توکن ربات را اینجا قرار بده
BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
API_URL = f'https://botapi.rubika.ir/v3/{BOT_TOKEN}'

app = Flask(__name__)  # name صحیح است

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

def run_bot():
    offset = None
    while True:
        try:
            updates = get_updates(offset)
            for update in updates.get('result', []):
                message = update.get('message', {})
                text = message.get('text', '')
                chat_id = message.get('chat_id', '')
                if 'سلام' in text:
                    send_message(chat_id, 'علیک سلام')
                offset = update.get('update_id', 0) + 1
        except Exception as e:
            print("Error:", e)
        time.sleep(1)

# یک مسیر ساده برای تست وب
@app.route("/")
def home():
    return "Rubika bot is running!"

if __name__ == "__main__":
    # اجرای ربات در یک Thread جدا
    threading.Thread(target=run_bot, daemon=True).start()

    # پورت لیارا
    port = 80
    app.run(host="0.0.0.0", port=port)