import requests
from flask import Flask, request, jsonify

BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
API_URL = f'https://botapi.rubika.ir/v3/{BOT_TOKEN}'

app = Flask(__name__)

def send_message(chat_id, text):
    url = f'{API_URL}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=payload)
    return response.json()

@app.route("/")
def home():
    return "Rubika bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        message = data.get('message', {})
        text = message.get('text', '')
        chat_id = message.get('chat_id', '')
        if 'سلام' in text:
            send_message(chat_id, 'علیک سلام')
    except Exception as e:
        print("Error processing webhook:", e)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)