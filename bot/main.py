import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from handlers import taskshandler

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN", "ВАШ_TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

taskshandler.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
