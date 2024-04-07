from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from db import Database

router = Router()
router.message.filter(F.chat.type.in_({"private"}))
db = Database("./database.db")

@router.message(Command("start"))
async def cmd_start(message: Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
        db.get_db()
    await message.answer("Привет! Напиши /about чтобы узнать больше о этом боте.")
