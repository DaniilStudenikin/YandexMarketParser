import requests
import json


payload = {
    'params': [
        '2825'
    ],
    'path': '/?no-pda-redir=1'
}

url = 'https://market.yandex.ru/api/resolve/?r=suggest:addRequestToSuggestHistory'

print(payload)
payload = json.dumps(payload)
print(payload)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'market.yandex.ru',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
}


resp = requests.post(url=url, data=payload, headers=headers)
print(resp)
print(resp.headers)
