from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from filters.chat_type import ChatTypeFilter

router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
    """/start — перезапуск бота.
/help — вывод доступных команд.
/about — вывод информации о боте.
/crypto — вывод последней цены покупки выбранных криптовалют.
/settings — настроить некоторые другие команды. """
)
