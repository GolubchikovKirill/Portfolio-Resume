from aiogram import Bot, Dispatcher, types
import asyncio
from config import TOKEN_bot
from handlers import BotHandlers

TOKEN = TOKEN_bot

bot = Bot(token=TOKEN)
dp = Dispatcher()

handlers = BotHandlers(dp)

async def main():
    print("Запуск бота!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
