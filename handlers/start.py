from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from keyboards.main import main_kb
from db import Database

router = Router()
db = Database("./database.db")

@router.message(Command("start"))
@router.message(F.text == "Закрыть")
async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.get_db()
    await message.answer(
"""Добро пожаловать в Douber — бот-помощник от компании <b><a href="https://t.me/tivehive">TiveHive</a></b>.
Воспользуйся кнопками ниже для управления ботом""",
                         reply_markup=main_kb(),
                         parse_mode="html",
                         disable_web_page_preview=True)
