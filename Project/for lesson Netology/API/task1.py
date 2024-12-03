import requests

def get_weather(city: str) -> str:
    """
    Получает текущую погоду для указанного города с использованием OpenWeatherMap API.
    """
    api_key = "df12010e5ee8b0762641c005b92b91e7"
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,       # Название города
        "appid": api_key,  # Ключ API
        "units": "metric",  # Единицы измерения температуры (метрические)
        "lang": "ru"      # Язык ответа
    }

    try:
        response = requests.get(url, params=params)
        
        # Отладочные сообщения
        # print(f"Отправленный запрос: {response.url}")
        # print(f"Код ответа: {response.status_code}")
        # print(f"Ответ сервера: {response.text}")
        
        if response.status_code != 200:
            return f"Ошибка: {response.status_code}. Не удалось получить данные для города {city}."
        
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        return f"В городе {city} сейчас {temp}°C, {description}. Скорость ветра: {wind_speed} м/с."
    except requests.exceptions.RequestException as e:
        return f"Ошибка сети: {e}"


if __name__ == '__main__':
    city_name = input("Введите название города: ")
    print(get_weather(city_name))