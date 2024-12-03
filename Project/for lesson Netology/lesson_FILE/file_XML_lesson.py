"""
XML
-Сериализация обьектов любой сложности
-Применяется в API клиент-сервер
-Является стандартом обьена данными и сообщениями большинства информационных систем
-Применяется для хранения файлов конфигурации
-Большинство сложных форматов хранятся в XML

"""
# ET - аляс(короткое имя длинной строки)
import xml.etree.ElementTree as ET

# Создаем парсер и читаем файл в дерево XML
parser = ET.XMLParser(encoding="utf-8") # Нужная кодировка
tree = ET.parse(r"lesson_FILE/newsafr.xml", parser) # Вместо open 
print(tree)

root = tree.getroot()
# print(root)
# print(root.text)

news_list = root.findall("channel/item")
print(len(news_list))

for row in news_list:
    print(row.find("title").text)

 