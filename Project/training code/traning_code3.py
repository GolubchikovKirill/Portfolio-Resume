
class UserProfile:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.is_active = True
    
    def deactivate(self):
        self.is_active = False
        
    def activate(self):
        self.is_active = True
    
    def get_info(self):
        status = "Активен" if self.is_active else "Не активен"
        return f"Пользователь - {self.username}, email: {self.email}, Статус: {status}"
        
user = UserProfile("johndoe", "john@example.com")
print(user.get_info())  # Пользователь: johndoe, Email: john@example.com, Статус: Активен

user.deactivate()
print(user.get_info())  # Пользователь: johndoe, Email: john@example.com, Статус: Неактивен

user.activate()
print(user.get_info())  # Пользователь: johndoe, Email: john@example.com, Статус: Активен


