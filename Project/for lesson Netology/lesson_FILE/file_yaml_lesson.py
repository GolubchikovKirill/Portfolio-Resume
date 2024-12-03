"""
YAML
-Нужен для создания файлов настроек
-Самый компактный язык разметки
-Используется для описания классов,ресурсов и манифестов в API
-Может хранить несколько обьектов в одном файле (в отличии от json)

swagger - для создания API(openAPI)

Десериализация:
Из файла: yaml.load(file), yaml.load_all(file)
Из строки: yaml.loads(str)

Сериализация:
В файл: yaml.dump
В строку: yaml.dumps

Печать не-ascii символов, отступы:
allow_unicode=True,default_flow_style=False
"""

import yaml # Библиотека для работы с ямл "pyyaml"