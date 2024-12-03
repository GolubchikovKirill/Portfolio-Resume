"""
API - application Programming Interface

HTTP(HTTPS) - протокол прикладного взаимодействия:
* Клиент-сервер
* Основной обьект манипуляции - ресурс. Ресурс облажает URI (URL)
* HTTP не хранит свое состояние. Ответы часто кэшируются
* Для поддержки авторизации используется куки
* Протокол HTTP определяет структуру сообщений

Что нужно знать, чтобы задать запрос:
1) Адрес ресурса (URL,URI)
2) Метод, который используем
3) Данные и их формат

Методы:
- GET - получение данных с сервера
- POST - передача данных на сервер
- PUT - создание или изменение ресурсов
- DELETE - удаление данных на сервере

Данные и их формат:
- query string
- заголовках запросов
- тело запросов (чаще всего используются форматы JSON, XML, FORM-DATA)

APi - контракт клента и сервера
"""

import requests
import json

from pprint import pprint

# # Получаем страницу сайта
# url = 'https://ru.wikipedia.org/wiki/HTTP'
# response = requests.get(url)
# # pprint(response.status_code)
# # pprint(response.headers)
# # pprint(response.text)
# # pprint(response.content)

# # Заполнить анкету

# url = 'https://functions.yandexcloud.net/d4e8qsrmeednndemfsus'
# payload = {
#     "name": "Rawdf",
#     "surname": "Ardfa",
#     "patronymic": "+7(234)432-52-43",
#     "birthdate": "2345-05-23",
#     "passport": "1234 12345678"
# }
# headers = {
#     'Content-Type': 'application/json'
# }

# # response = requests.post(url, 
# #                         headers=headers, 
# #                         data=json.dumps(payload)) # Ошибка, мы приложили словарь вместо json если не пишем dumps

# response = requests.post(url, 
#                         json=payload) # Облегченная версия 

# # pprint(response.status_code)
# # pprint(response.headers)
# # pprint(type(response.json()))

nasa_url = 'https://api.nasa.gov/planetary/apod'
params = {
    'api_key': 'xCDgnTn7REyaZIl9z8d02ZSL2hieQ8vOcHWkZ5AP'
}

response = requests.get(nasa_url, params=params) # Добавляем к URL апи ключ
# pprint(response.json()) # выводим в json формате файл 

image_url = response.json()['url']
filename = image_url.split('/')[-1] # Для получения разных картинок в разных файлах, а не обновления старой
pprint(image_url)

response = requests.get(image_url)

with open('image.jpg', 'wb') as f:
    f.write(response.content)

yadi_url = 'https://cloud-api.yandex.net/v1/disk/resources?path=image'
headers = {
    'Authorization': 'OAuth y0_AgAAAABL4gDdAADLWwAAAAEY4Xf-AAC1zpG9sNdFWbBHbRV7T36pYKt39Q'
}
params = {
    'path': 'image'
}

response = requests.put(yadi_url, headers=headers, params=params)

print(response.status_code)
print(response.json)


