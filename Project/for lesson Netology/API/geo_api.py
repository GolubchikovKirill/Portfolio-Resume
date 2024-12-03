"""
Условие задачи
Альберт Эйнштейн, возвращаясь из своей очередной научной конференции, решил разыграть свою жену. Он ей рассказал, что посетил большое количество европейских городов, но больше всего ему понравился город из Великобритании. И пообещал ей, если она сможет найти по координатам этот город, то свозит её туда в ближайший отпуск. Целую неделю Эльза работала с картами, чтобы найти нужный город. А как мы были решили эту задачу, имея API и интернет?

Напишите функцию, которая принимает на вход список из координат (кортеж из широты и долготы) и возращает английский город. Список городов Великобритании ограничен 8 самыми популярными городами: Leeds, London, Liverpool, Manchester, Oxford, Edinburgh, Norwich, York. Гарантируется, что в списке есть как минимум 1 британский город. Для нахождения города по координатам рекомендуется использовать API geocode.
"""

import requests

UK_CITIES = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']


def find_uk_city(coordinates):
    for lat, lon in coordinates:
        response = requests.get(f'https://geocode.maps.co/reverse?lat={lat}&lon={lon}')
        data = response.json()
        city = data['address']['city']
        if city in UK_CITIES:
            return city

    print(city)
if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'