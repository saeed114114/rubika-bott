from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Rubika bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print("Received data:", data)  # پیام‌ها در لاگ لیارا نمایش داده می‌شوند

        # مثال پاسخ خودکار: اگر پیام شامل "سلام" بود جواب بده
        message = data.get("message", {})
        text = message.get("text", "")
        chat_id = message.get("chat_id", "")
        if "سلام" in text and chat_id:
            send_message(chat_id, "علیک سلام")  # تابع send_message را زیر تعریف کن

    except Exception as e:
        print("Error processing webhook:", e)
    return jsonify({"status": "ok"})

# تابع ارسال پیام به روبیکا
import requests
BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
API_URL = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}"

def send_message(chat_id, text):
    url = f"{API_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    try:
        r = requests.post(url, data=payload)
        print("Send message response:", r.text)
    except Exception as e:
        print("Error sending message:", e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)