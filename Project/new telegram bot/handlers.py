from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import MainKeyboard

class BotHandlers:
    def __init__(self, dp: Dispatcher):
        self.dp = dp
        self.keyboard = MainKeyboard() 
        self.register_handlers()

    def register_handlers(self):
        self.dp.message.register(self.start_handler, Command("start"))
        self.dp.message.register(self.help_handler, Command("help"))
        self.dp.message.register(self.info_handler, Command("info"))

    async def start_handler(self, message: Message):      
        bot_start = "Привет! Я твой бот. Нажми 'Помощь' для получения списка функций."
        await message.answer(bot_start, reply_markup=self.keyboard.get_keyboard())

    async def help_handler(self, message: Message):
        help_text = (
            "/start - Приветственное сообщение\n"
            "/help - Список команд\n"
            "/info - Информация о боте"
        )
        await message.answer(help_text, reply_markup=self.keyboard.get_keyboard())

    async def info_handler(self, message: Message):
        bot_info = "Я бот на aiogram 3.14. Моя версия: 1.0"
        await message.answer(bot_info, reply_markup=self.keyboard.get_keyboard())

    
