from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from utils import crypto

router = Router()
router.message.filter(F.chat.type.in_({"private"}))

@router.message(Command("crypto"))
async def cmd_crypto(message: Message):
    await message.answer(crypto.get_message(message.from_user.id))
