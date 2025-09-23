import requests
import time

BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
API_URL = f'https://botapi.rubika.ir/v3/{BOT_TOKEN}'

def get_updates(offset=None):
    params = {'offset': offset} if offset else {}
    response = requests.get(f"{API_URL}/getUpdates", params=params)
    try:
        return response.json()
    except Exception as e:
        print("Error decoding JSON:", e, response.text)
        return {"result": []}  # برگرداندن لیست خالی تا برنامه ادامه دهد

def send_message(chat_id, text):
    try:
        response = requests.post(f"{API_URL}/sendMessage", data={'chat_id': chat_id, 'text': text})
        return response.json()
    except Exception as e:
        print("Error sending message:", e)
        return {}

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

if __name__ == "__main__":
    main()