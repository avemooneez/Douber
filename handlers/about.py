from aiogram.types import Message
from aiogram import Router, F
from keyboards import all_commands


router = Router()

@router.message(F.text == "О боте")
async def cmd_help(message: Message):
    await message.reply(
        text="""
Это — бот-помощник от компании <b><a href="https://t.me/tivehive">TiveHive</a></b>.
Автор: @mnz_pr
Исходный код: https://github.com/avemooneez/Douber

Невошедшие команды в основную клавиатуру вы видите ниже.
Также ещё не в глобальном использовании команды /url, /download""",
    parse_mode="html",
    disable_web_page_preview=True,
    reply_markup=all_commands.kb()
    )
