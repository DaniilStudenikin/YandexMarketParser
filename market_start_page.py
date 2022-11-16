import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

url = "https://market.yandex.ru/catalog--smartfony/16814639/list?hid=91491&glfilter=16816262:16816264&onstock=1"

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

response = requests.request("GET", url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

test = soup.find('form')

url_captcha = urlparse(test.get("action"))
payload = url_captcha.query

headers2 = {
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
    'content-type': 'application/x-www-form-urlencoded'
}
resp2 = requests.get('https://market.yandex.ru', data=payload, headers=headers2)

print(resp2.headers)
print(resp2.cookies)
print(resp2)
print(resp2.text)

with open('text2.html', 'w', encoding='utf-8') as file1:
    file1.write(resp2.text)
