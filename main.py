import requests
import time

# ======= تنظیمات ربات =======
BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
API_URL = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}"

# شناسه آخرین پیام دریافت شده (برای جلوگیری از پاسخ تکراری)
offset = 0

# ======= تابع گرفتن پیام‌ها =======
def get_updates(offset=None):
    try:
        params = {'offset': offset} if offset else {}
        response = requests.get(f"{API_URL}/getUpdates", params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting updates: {response.status_code}")
    except Exception as e:
        print(f"Exception in get_updates: {e}")
    return {}

# ======= تابع ارسال پیام =======
def send_message(chat_id, text):
    try:
        data = {'chat_id': chat_id, 'text': text}
        response = requests.post(f"{API_URL}/sendMessage", data=data, timeout=10)
        if response.status_code != 200:
            print(f"Error sending message: {response.status_code}")
    except Exception as e:
        print(f"Exception in send_message: {e}")

# ======= حلقه اصلی =======
print("Bot is running...")

while True:
    updates = get_updates(offset)
    if updates and updates.get("result"):
        for update in updates["result"]:
            message = update.get("message")
            if message:
                chat_id = message.get("chat_id")
                text = message.get("text", "")
                
                print(f"Received message: {text} from chat_id: {chat_id}")  # لاگ لیارا
                
                # پاسخ ساده به پیام "سلام"
                if text == "سلام":
                    send_message(chat_id, "علیک سلام")
                
                # به‌روزرسانی offset
                offset = update["update_id"] + 1
    time.sleep(1)  # چک کردن هر ۱ ثانیه