import requests
from .models import TeleSettings

def SendTelegram(name,phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)

        if text.find('{name}')!=-1 and text.find('{phone}')!=-1:
            text = text.replace('{name}', name)
            text = text.replace('{phone}', phone)
            api='https://api.telegram.org/bot'
            method = api + token + '/sendMessage'
        else:
            text = 'В исходном тексте не найдены {name} и/или {phone}'

        try:
            api = 'https://api.telegram.org/bot'
            method = api + token + '/sendMessage'
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text
            })
        except:
            print ('Ошибка в Боте Телеграм')
    else:
        pass