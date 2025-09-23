import requests
import time

BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
API_URL = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}"

offset = 0  # برای دنبال کردن آخرین پیام دریافت شده

def get_updates(offset):
    try:
        response = requests.get(f"{API_URL}/getUpdates", params={"offset": offset})
        data = response.json()
        if data.get("status") == "ok":
            return data.get("result", [])
        else:
            print("Error in get_updates:", data)
            return []
    except Exception as e:
        print("Exception in get_updates:", e)
        return []

def send_message(chat_id, text):
    try:
        response = requests.post(f"{API_URL}/sendMessage", data={"chat_id": chat_id, "text": text})
        return response.json()
    except Exception as e:
        print("Exception in send_message:", e)

print("Bot is running...")

while True:
    updates = get_updates(offset)
    for update in updates:
        message = update.get("message", {})
        text = message.get("text", "")
        chat_id = message.get("chat_id")
        print(f"Received from {chat_id}: {text}")

        # پاسخ ساده
        if "سلام" in text:
            send_message(chat_id, "علیک سلام")

        # بروزرسانی offset
        offset = max(offset, update.get("update_id", 0) + 1)

    time.sleep(1)  # هر ثانیه پیام‌های جدید را بررسی می‌کند