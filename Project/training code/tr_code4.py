class TaskManager:
    def __init__(self,):
        self.tasks = []
        
    def add_task(self, task: str):
        self.tasks.append(task)
        
    def remove_task(self, task: str):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print(f"Задача {task} не найдена в списке.")
        
    def get_tasks(self):
        if not self.tasks:
            return "Список задач пуст."
        else:
            return "\n".join(self.tasks)



task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task("Сделать домашку")
task_manager.add_task("Написать код")

# Показываем все задачи
print(task_manager.get_tasks())  # Сделать домашку\nНаписать код

# Удаляем одну задачу
task_manager.remove_task("Сделать домашку")

# Показываем оставшиеся задачи
print(task_manager.get_tasks())  # Написать код