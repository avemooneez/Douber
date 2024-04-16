from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

router = Router()

@router.message(F.text == "Помощь")
async def cmd_start(message: Message):
    await message.reply("Остались какие-то вопросы? Вышла какая-то ошибка?\nСмело пиши @mnz_pr, и ты сможешь получить ответ на свой вопрос!")
