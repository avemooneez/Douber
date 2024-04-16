from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F

router = Router()

@router.message(F.text == "О боте")
async def cmd_help(message: Message):
    await message.reply(
    """
Это — бот-помощник от компании <b><a href="https://t.me/tivehive">TiveHive</a></b>.
Автор: @mnz_pr
Исходный код: https://github.com/avemooneez/Douber

Доступные команды можно посмотреть в /help.
""", parse_mode="html", disable_web_page_preview=True)
