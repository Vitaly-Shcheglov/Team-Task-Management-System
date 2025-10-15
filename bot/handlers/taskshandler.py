from aiogram import types
from aiogram.dispatcher import Dispatcher

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(task_list_handler, commands=['tasks'])
    dp.register_message_handler(task_complete_handler, commands=['complete'])

async def start_handler(message: types.Message):
    await message.reply("Добро пожаловать в Task Manager бот! Введите /tasks для просмотра задач.")

async def task_list_handler(message: types.Message):
    tasks = "Список ваших задач."
    await message.reply(tasks)

async def task_complete_handler(message: types.Message):
    parts = message.text.split()
    if len(parts) < 2:
        await message.reply("Укажите ID задачи для завершения.")
    else:
        task_id = parts[1]
        await message.reply(f"Задача {task_id} отмечена как выполненная.")
