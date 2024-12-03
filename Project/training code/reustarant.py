"""
Условие:
Ваша задача — создать систему управления заказами в ресторане с использованием ООП и asyncio.
	1.	Класс Order:
	•	Атрибуты:
	•	order_id — уникальный идентификатор заказа.
	•	items — список блюд в заказе.
	•	status — статус заказа ("Принят", "Готовится", "Готов").
	•	Метод для изменения статуса заказа.
	2.	Класс Kitchen:
	•	Метод prepare_order(order: Order, duration: int):
	•	Асинхронно готовит заказ, используя asyncio.sleep(duration).
	•	По завершении меняет статус заказа на "Готов".
	3.	Класс OrderManager:
	•	Хранит список всех заказов.
	•	Методы:
	•	add_order(order: Order) — добавляет заказ в список.
	•	process_orders() — запускает приготовление всех заказов параллельно.
	•	display_orders() — выводит текущий список заказов и их статус.
"""

import asyncio

class Order:
    def __init__(self, order_id, items, status):
        self.order_id = order_id
        self.items = items
        self.status = status

    def __str__(self):
        return f"Заказ принят с ID:{self.order_id}, статус заказа - {self.status}"
    
class Kitchen:
    async def prepare_order(self, order: Order, duration: int):
        await asyncio.sleep(duration)
        order.status = "Готов"

class OrderManager:
    def __init__(self):
        self.orders = []  # Список для хранения всех заказов

    def add_order(self, order: Order):
        self.orders.append(order)

    async def process_orders(self):
        if not self.orders:
            print("Нет заказов для обработки.")
            return
        
        print("Начинается обработка заказов...")

        # Создаем список задач для всех заказов
        tasks = [
            Kitchen.prepare_order(order, duration=2)  # Имитация готовки с временем 2 сек.
            for order in self.orders
        ]

        # Запускаем задачи параллельно
        await asyncio.gather(*tasks)

        # Обновляем статусы и выводим результат
        for order in self.orders:
            print(f"Заказ {order.order_id} обработан. Текущий статус: {order.status}")
            

