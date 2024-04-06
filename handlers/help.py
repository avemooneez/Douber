from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

router = Router()
router.message.filter(F.chat.type.in_({"private"}))

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
    """/start — перезапуск бота.
/help — вывод доступных команд.
/about — вывод информации о боте.
/crypto — вывод последней цены покупки выбранных криптовалют.
/settings — настроить некоторые другие команды. """
)
