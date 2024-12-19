from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

class MainKeyboard:
    def __init__(self):
        # Создаем кнопки
        self.start_button = KeyboardButton(text="Приветствие")
        self.help_button = KeyboardButton(text="Помощь")
        self.info_button = KeyboardButton(text="Информация")

        # Создаем клавиатуру с кнопками
        self.keyboard = ReplyKeyboardMarkup(
            keyboard=[[self.start_button, 
                       self.help_button, 
                       self.info_button]], 
            resize_keyboard=True
        )

    def get_keyboard(self):
        return self.keyboard
    
