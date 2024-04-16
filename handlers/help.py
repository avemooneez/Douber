from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from keyboards import all_commands

router = Router()

@router.message(F.text == "Все команды")
async def cmd_help(message: Message):
    await message.reply(
    "В клавиатуре ниже предоставлены все команды", reply_markup=all_commands.kb()
)
