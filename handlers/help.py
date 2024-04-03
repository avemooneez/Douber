from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router = Router()

@router.message(Command("help"))
async def cmd_help(message: Message):
    if message.chat.type == 'private':
        await message.answer(
    """/start — перезапуск бота.
/help — вывод доступных команд.
/about — вывод информации о боте.
/crypto — вывод последней цены покупки выбранных криптовалют.
/settings — настроить некоторые другие команды. """
    )
