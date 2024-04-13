from aiogram.types import CallbackQuery
from aiogram import Router, F
from utils import crypto
from keyboards.back import back
from middlewares.antiflood import AntiFloodMiddleware
from aiogram.fsm.storage.redis import RedisStorage

storage = RedisStorage.from_url("redis://localhost:6379/0")
router = Router()
router.message.filter(F.chat.type.in_({"private"}))
router.message.middleware(middleware=AntiFloodMiddleware(storage=storage, limit=3))

@router.callback_query(F.data == "crypto")
async def edit_kb(callback: CallbackQuery):
    await callback.message.edit_text(crypto.get_message(callback.from_user.id), reply_markup=back())
