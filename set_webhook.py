import requests

BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
WEBHOOK_URL = "https://epic-dirac-epmedhnbm.liara.run/webhook"

# آدرس صحیح
WEBHOOK_API = f"https://botapi.rubika.ir/bot{BOT_TOKEN}/setWebhook"

response = requests.post(WEBHOOK_API, json={"url": WEBHOOK_URL})
print(response.json())