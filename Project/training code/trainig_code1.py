import asyncio

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    async def run_task(self):
        print(f"Задача {self.name} принята в работу.")
        await asyncio.sleep(self.duration)
        print(f"Задача {self.name} - выполнена")
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"Задача {task.name} - добавлена в список.")

    async def run_all(self):
        print("Запуск всех задач.")
        await asyncio.gather(*(task.run_task() for task in self.tasks))
        print("Все задачи завершены.")

async def main():
    task1 = Task("Задача 1", 5)
    task2 = Task("Задача 2", 2)

    manager = TaskManager()
    manager.add_task(task1)
    manager.add_task(task2)

    await manager.run_all()

asyncio.run(main())



