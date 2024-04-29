from aiogram.types import Message
from aiogram import Router, F
from utils import crypto
from middlewares.antiflood import AntiFloodMiddleware
from aiogram.fsm.storage.redis import RedisStorage


storage = RedisStorage.from_url("redis://localhost:6379/0")
router_crypto = Router()
router_crypto.message.middleware(middleware=AntiFloodMiddleware(storage=storage, limit=5))

@router_crypto.message(F.text == "Крипта")
async def edit_kb(message: Message):
    await message.reply(crypto.get_message(message.from_user.id))
