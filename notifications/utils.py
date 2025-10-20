from dotenv import load_dotenv

load_dotenv()

def send_telegram_notification(user_telegram_id, message):
    import requests
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": user_telegram_id, "text": message}
    response = requests.post(url, data=data)
    return response.json()
