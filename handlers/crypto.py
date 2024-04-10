from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from utils import crypto
from middlewares.antiflood import AntiFloodMiddleware
from aiogram.fsm.storage.redis import RedisStorage

storage = RedisStorage.from_url("redis://localhost:6379/0")
router = Router()
router.message.filter(F.chat.type.in_({"private"}))
router.message.middleware(middleware=AntiFloodMiddleware(storage=storage, limit=3))

@router.message(Command("crypto"))
async def cmd_crypto(message: Message):
    await message.answer(crypto.get_message(message.from_user.id))
