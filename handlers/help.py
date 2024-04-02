from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

router = Router()

@router.message(Command("help"))
async def cmd_help(message: Message):
    if message.chat.type == 'private':
        await message.answer(
    """/start - команда для перезапуска бота, также при несуществовании юзера в БД команда служит регистратором.

/help - команда для вывода этого текста.

/crypto - команда для вывода последней цены покупки выбранных криптовалют.
Выбрать криптовалюты - /settings -> Crypto.

/settings - команда для настройки некоторых других команд. 
/settings -> Crypto - настроить отображение криптовалют по команде /crypto."""
    )
