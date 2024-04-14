from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

router = Router()

@router.message(Command("support"))
async def cmd_start(message: Message):
    await message.answer("Остались какие-то вопросы? Вышла какая-то ошибка? Смело пиши @mnz_pr, и ты сможешь получить ответ на свой вопрос!")
