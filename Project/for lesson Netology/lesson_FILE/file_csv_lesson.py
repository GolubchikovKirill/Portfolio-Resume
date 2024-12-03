"""
Форматы данных CSV, JSON, YAML, XML
Сериализация - процесс преобразования обьекта в поток байтов для сохранения или перерачи в память, базу данных или файл
Десериализация - читаете файл из памяти
"""

"""
CSV - Значения, разделенные запятыми
- Основное применение - выгрузка данных
- Не подходит для иерархических данных
- Удобно хранить данные и хорошо используется архивами
- Нет ограничений на размер файла для обработки
- Файл можно открывать в Exel
- Поддерживает дозапись данных
"""
import csv # библиотека для csv

# Кодировки: utf-8, cp1251 
# Чтение файла CSV
with open(r"newsafr.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) 
        # print(row[-1]) - для title, но само слово title будет учитываться

# Чтение файла построчно
with open(r"newsafr.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    count = 0
    for row in reader: # для подсчета именно заголовков текста
        if count > 0:
            print(row[-1])
            count += 1
#print(f"В этом файле {count-1} новостей") 

#Чтение файла целиком
with open(r"newsafr.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    new_list = list(reader) # Оборачиваем reader в список

header = new_list.pop(0) # Заключаем заголовок title в переменную header для вывода без title

for row in new_list: # Выводим все строки из списка для чтения по очереди
    print(row[-1])

#print(f"В этом файле {len(new_list)} новостей") 

"""
Десериализация:
reader = csv.reader(file)
data - list(reader)

Десериализация в словарь:
reader = csv.DictReader(file)

Настройка форматирования:
csv.register_dialect()

Сериализация из списка:
writer = csv.writer(file)

Сериализация из словаря:
writer = csv.DictWriter(file, fieldnames=reader.fieldnames)

Запись заголовка (только словарь):
writer.writeheader()

Запись данных (список, словарь):
writer.writerows(data)
writer.writerow(data)

"""
