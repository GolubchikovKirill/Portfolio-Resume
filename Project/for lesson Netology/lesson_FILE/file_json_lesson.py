"""
JSON 

-Импорт/экспорт данных в базы данных
-Для сохранения вложенных структур данных
-Используется для API
-Самый популярный и простой в использовании формат для Python и Java
-Является подмножеством формата YAML

-Но нельзя читать файл частично, только полностью

Десериализация:
Из файла: json.load(file)
Из строки: json.loads(str)

Сериализация:
В файл: json.dump()
В строку: json.dumps()

Печать не-ascii симоволов, отступы:
ensure_ascii=False,indent=2
(То есть это печать красивого файла на кирилице с отступом 2)

"""

import json
from pprint import pprint

# Открытие файла и чтение
with open(r"lesson_FILE/newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

news_list = json_data["rss"]["channel"]["items"]
# print(news_list)

for row in news_list:
    print(row["title"])
print(f"В этом файле {len(news_list)} новостей")

# pprint(json_data)

with open(r"newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

json_str = json.dumps(json_data, ensure_ascii=False)
print(json_str) 

