from aiogram import Router, types
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я асинхронный Telegram-бот, развернутый из шаблона Benua.")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Доступные команды: /start — начать, /help — помощь.")
