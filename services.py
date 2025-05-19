import requests


def set_telegram_webhook(token, webhook_url):
    request_url = f"https://api.telegram.org/bot{token}/setWebhook?url={webhook_url}"
    print(request_url)

    response = requests.post(url=request_url)
    return response.content


print(set_telegram_webhook("7052116826:AAFa11oJnr0k7mCq8_2rKDiSDOgWGHEaJSk",
                           'https://70c4-195-245-96-132.ngrok-free.app/getUpdates'))
