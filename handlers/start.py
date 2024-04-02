from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from db import Database

router = Router()
db = Database("./database.db")

@router.message(Command("start"))
async def cmd_start(message: Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
            print(db.get_db())
        await message.answer("Welcome!")