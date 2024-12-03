class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)
        
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                print("Контакт был удален.")
                return
        print(f"Контакт с именем {name} не найден")
        
    def find_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                return f"{contact['name']}: {contact['phone']}, {contact['email']}"
        return f"Контакт с именем {name} не найден."
    
    def get_all_contacts(self):
        if not self.contacts:  # Проверяем, пуст ли список
            return "Список контактов пуст."
        return "\n".join(
            f"{contact['name']}: {contact['phone']}, {contact['email']}" for contact in self.contacts
        )  # Форматируем каждый контакт
            
book = ContactBook()

# Добавляем контакты
book.add_contact("Иван Иванов", "123456", "ivan@example.com")
book.add_contact("Мария Петрова", "654321", "maria@example.com")

# Получаем список всех контактов
print(book.get_all_contacts())
# Иван Иванов: 123456, ivan@example.com
# Мария Петрова: 654321, maria@example.com

# Ищем контакт
print(book.find_contact("Мария Петрова"))  
# Мария Петрова: 654321, maria@example.com

# Удаляем контакт
book.remove_contact("Иван Иванов")

# Проверяем оставшиеся контакты
print(book.get_all_contacts())
# Мария Петрова: 654321, maria@example.com
        
        
        