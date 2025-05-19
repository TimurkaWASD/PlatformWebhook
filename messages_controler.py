import requests

def message(data):
    if data['message']['text'] == "/start":
        tg_user_id = str(data["message"]["from"]["id"])
        params = {'username': data["message"]["from"]["username"], 'tg_user_id': tg_user_id}  #данные для проверки
        response = requests.post(url="http://127.0.0.1:8000/user/create_user", params=params)

        user_data = response.json() #конвертируется в формат JSON с помощью метода .json(). После этого мы получаем данные, которые вернул сервер
        text = user_data["info"]
        send_message(tg_user_id, text)

        print(response.text)
        print(params)

token = "7052116826:AAFa11oJnr0k7mCq8_2rKDiSDOgWGHEaJSk"

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)
