import requests
from flask import Flask, request, jsonify

# توکن ربات روبیکا
BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
API_URL = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}"

# آدرس وب‌هوک
WEBHOOK_URL = "https://epic-dirac-epmedhnbm.liara.run/webhook"

app = Flask(__name__)

def send_message(chat_id, text):
    """
    ارسال پیام به کاربر
    """
    try:
        url = f"{API_URL}/sendMessage"
        payload = {'chat_id': chat_id, 'text': text}
        response = requests.post(url, data=payload)
        print("Send message response:", response.text)
        return response.json()
    except Exception as e:
        print("Error sending message:", e)
        return None

@app.route("/")
def home():
    return "Rubika bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    """
    دریافت پیام از وب‌هوک
    """
    try:
        data = request.json
        print("Incoming data:", data)  # لاگ کامل پیام دریافتی
        message = data.get('message', {})
        text = message.get('text', '')
        chat_id = message.get('chat_id', '')

        if text and chat_id:
            # پاسخ ساده به پیام‌ها
            if 'سلام' in text:
                send_message(chat_id, 'علیک سلام')
            else:
                send_message(chat_id, f"پیغام شما: {text}")
    except Exception as e:
        print("Error processing webhook:", e)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)