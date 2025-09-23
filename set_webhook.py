import requests

BOT_TOKEN = "CCDBE0LFKZCPFRIVTEQMMPAQHFIZANGDNQYLWSBEFXXGXOGGOAYBTNPGUQJRWRWV"
WEBHOOK_URL = "https://epic-dirac-epmedhnbm.liara.run/webhook"

response = requests.post(
    f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/setWebhook",
    json={"url": WEBHOOK_URL}
)

print(response.json())