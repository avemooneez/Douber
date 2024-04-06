from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from db import Database
from filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))
db = Database("./database.db")

@router.message(Command("start"))
async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.get_db()
    await message.answer("Привет! Напиши /about чтобы узнать больше о этом боте.")
