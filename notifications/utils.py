def send_telegram_notification(user_telegram_id, message):
    import requests
    bot_token = "ВАШ_TELEGRAM_BOT_TOKEN"
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {"chat_id": user_telegram_id, "text": message}
    response = requests.post(url, data=data)
    return response.json()
