from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram import Router
from utils.urlshort import short_url
from db import Database

router = Router()
db = Database("./database.db")

@router.message(Command("url"))
async def cmd_urlshort(message: Message, command: CommandObject):
    link = command.args
    if link == None:
        await message.reply(
            "Неверное использование: /url <ссылка>"
        )
        return
    url = short_url(url=link)
    if url != "Please enter a valid URL.":
        await message.reply(url)
    else:
        await message.reply("К сожалению, ссылка не валидна. Попробуйте ещё раз")
